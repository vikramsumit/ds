import os
import sys
import gc
from pathlib import Path
import tensorflow as tf
import pandas as pd
from collections import Counter

# ===============================
# CONFIGURATION
# ===============================
PLANT_MODELS_DIR = "../all_data/models"
PLANT_CLASS_NAMES = ['apple', 'bellpepper', 'cherry', 'corn(maize)', 'grape', 'peach', 'potato', 'strawberry', 'tomato']
IMAGE_SIZE = (256, 256)

# Disease models directories mapping
DISEASE_DIRS = {
    'apple': '../apple_disease_classifier/models',
    'bellpepper': '../bellpepper_disease_classifier/models',
    'cherry': '../cherry_disease_classifier/models',
    'corn(maize)': '../corn(maize)_disease_classifier/models',
    'grape': '../grape_disease_classifier/models',
    'peach': '../peach_disease_classifier/models',
    'potato': '../potato_disease_classifier/models',
    'strawberry': '../strawberry_disease_classifier/models',
    'tomato': '../tomato_disease_classifier/models'
}

# Disease class names (assuming similar structure; can be customized per plant if needed)
DISEASE_CLASS_NAMES = {
    'apple': ['Apple Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy'],
    'bellpepper': ['Bacterial Spot', 'Healthy'],  # Placeholder; adjust based on actual classes
    'cherry': ['Healthy', 'Powdery Mildew'],  # Placeholder
    'corn(maize)': ['Blight', 'Common Rust', 'Gray Leaf Spot', 'Healthy'],  # Placeholder
    'grape': ['Black Measles', 'Black Rot', 'Healthy'],  # Placeholder
    'peach': ['Bacterial Spot', 'Healthy'],  # Placeholder
    'potato': ['Early Blight', 'Healthy', 'Late Blight'],  # Placeholder
    'strawberry': ['Healthy', 'Leaf Scorch'],  # Placeholder
    'tomato': ['Bacterial Spot', 'Early Blight', 'Healthy', 'Late Blight', 'Leaf Mold', 'Septoria Leaf Spot', 'Spider Mites', 'Target Spot', 'Tomato Mosaic Virus', 'Tomato Yellow Leaf Curl Virus']  # Placeholder
}

PLANT_CONFIDENCE_THRESHOLD = 50.0  # Minimum confidence for plant prediction

# ===============================
# HELPER FUNCTIONS
# ===============================
def predict_image(model, image_input, image_size=(256, 256), channels=3):
    """Predict a single image using a TensorFlow model."""
    if isinstance(image_input, (str, Path)):
        img_raw = tf.io.read_file(str(image_input))
        img = tf.image.decode_image(img_raw, channels=channels)
    else:
        img = image_input

    img = tf.cast(img, tf.float32)
    img = tf.image.resize(img, image_size)
    img = tf.expand_dims(img, 0)  # batch size = 1

    preds = model.predict(img, verbose=0)
    idx = int(tf.argmax(preds[0]))
    conf = float(tf.reduce_max(preds[0]) * 100.0)
    return idx, conf, preds[0]


def predict_plant(image_path, models_dir, class_names, image_size=(256, 256)):
    """Predict plant type using the best plant model."""
    models_dir = Path(models_dir)
    best_conf = 0.0
    best_pred = None
    best_model_name = None

    if not models_dir.exists():
        print(f"Models directory not found: {models_dir}")
        return "None", 0.0, None

    model_files = list(models_dir.glob("*.keras"))
    if not model_files:
        print(f"No .keras models found in {models_dir}")
        return "None", 0.0, None

    for model_file in sorted(model_files):
        try:
            model = tf.keras.models.load_model(str(model_file))
            pred_idx, conf, preds = predict_image(model, image_path, image_size=image_size)
            if conf > best_conf:
                best_conf = conf
                best_pred = class_names[pred_idx] if pred_idx < len(class_names) else str(pred_idx)
                best_model_name = model_file.name
            tf.keras.backend.clear_session()
            del model
            gc.collect()
        except Exception as e:
            print(f"Error loading model {model_file}: {e}")
            continue

    return best_pred, best_conf, best_model_name


def predict_disease(image_path, plant_name, disease_models_dir, disease_class_names, image_size=(256, 256)):
    """Predict disease using all models for the plant, with ensembling."""
    models_dir = Path(disease_models_dir)
    all_preds = []
    all_confs = []

    for model_file in sorted(models_dir.glob("*.keras")):
        model = tf.keras.models.load_model(str(model_file))
        pred_idx, conf, preds = predict_image(model, image_path, image_size=image_size)
        pred_name = disease_class_names[pred_idx] if pred_idx < len(disease_class_names) else str(pred_idx)
        all_preds.append(pred_name)
        all_confs.append(conf)
        tf.keras.backend.clear_session()
        del model
        gc.collect()

    # Ensembling: Majority vote for prediction, average confidence
    if all_preds:
        most_common_pred = Counter(all_preds).most_common(1)[0][0]
        avg_conf = sum(all_confs) / len(all_confs)
        return most_common_pred, avg_conf
    else:
        return "Unknown", 0.0


def combined_predict(image_path):
    """Combined prediction: First plant, then disease."""
    print(f"🔍 Analyzing image: {image_path}")

    # Step 1: Predict plant
    plant_pred, plant_conf, plant_model = predict_plant(
        image_path=image_path,
        models_dir=PLANT_MODELS_DIR,
        class_names=PLANT_CLASS_NAMES,
        image_size=IMAGE_SIZE
    )

    print(f"🌱 Plant Prediction: {plant_pred} (Confidence: {plant_conf:.2f}%, Model: {plant_model})")

    if plant_conf < PLANT_CONFIDENCE_THRESHOLD:
        print(f"⚠️  Plant prediction confidence too low ({plant_conf:.2f}% < {PLANT_CONFIDENCE_THRESHOLD}%). Not sure about the plant.")
        return {
            "plant": plant_pred,
            "plant_confidence": plant_conf,
            "disease": "Not sure",
            "disease_confidence": 0.0
        }

    # Step 2: Predict disease based on plant
    if plant_pred in DISEASE_DIRS:
        disease_models_dir = DISEASE_DIRS[plant_pred]
        disease_class_names = DISEASE_CLASS_NAMES.get(plant_pred, [])
        disease_pred, disease_conf = predict_disease(
            image_path=image_path,
            plant_name=plant_pred,
            disease_models_dir=disease_models_dir,
            disease_class_names=disease_class_names,
            image_size=IMAGE_SIZE
        )
        print(f"🦠 Disease Prediction: {disease_pred} (Avg Confidence: {disease_conf:.2f}%)")
    else:
        disease_pred = "Data not available in this model"
        disease_conf = 0.0
        print(f"⚠️  Data not available in this model for plant: {plant_pred}")

    return {
        "plant": plant_pred,
        "plant_confidence": plant_conf,
        "disease": disease_pred,
        "disease_confidence": disease_conf
    }


# ===============================
# MAIN EXECUTION
# ===============================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No image path provided")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print(f"Error: Image not found: {image_path}")
        sys.exit(1)

    result = combined_predict(image_path)
    print("Final Result:")
    print(f"Plant: {result['plant']} ({result['plant_confidence']:.2f}%)")
    print(f"Disease: {result['disease']} ({result['disease_confidence']:.2f}%)")
