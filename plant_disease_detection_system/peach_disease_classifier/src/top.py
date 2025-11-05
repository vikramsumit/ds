import os
import gc
from pathlib import Path
import tensorflow as tf
from tqdm import tqdm  # for progress bar

# ===============================
# CONFIGURATION
# ===============================
MODELS_DIR = "/home/amit/code_only/code/new/peach_disease_classifier/models"
TEST_DIR = "/home/amit/code_only/code/new/peach_disease_classifier/data/Test/Other_Images"
IMAGE_SIZE = (256, 256)

# ✅ Hardcoded class names
CLASS_NAMES = ['Bacterial Spot', 'Healthy']


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
    return idx, conf


def predict_models_on_folder(models_dir, test_dir, class_names, image_size=(256, 256)):
    """Predict all images in test_dir for each model in models_dir and print results."""
    models_dir = Path(models_dir)
    test_dir = Path(test_dir)
    model_counter = 1

    for model_file in sorted(models_dir.glob("*.keras")):
        print(f"\n🔹 Loading model {model_counter}: {model_file.name}")
        model = tf.keras.models.load_model(str(model_file))

        # Collect image paths
        image_paths = [p for p in test_dir.rglob("*") if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png"}]

        correct = 0
        total = 0

        # Show predictions in terminal
        for img_path in tqdm(image_paths, desc=f"Predicting ({model_file.name})", unit="img"):
            actual_label = img_path.parent.name
            pred_idx, conf = predict_image(model, str(img_path), image_size=image_size)
            pred_name = class_names[pred_idx] if pred_idx < len(class_names) else str(pred_idx)

            total += 1
            if actual_label.lower() == pred_name.lower().replace(" ", "_"):
                correct += 1

            tqdm.write(f"📸 {img_path.name} | Actual: {actual_label} | Predicted: {pred_name} ({conf:.1f}%)")

        # Show accuracy summary
        acc = (correct / total * 100) if total else 0
        print(f"\n✅ Model {model_counter} ({model_file.name}) finished.")
        print(f"   Total images: {total}")
        print(f"   Correct predictions: {correct}")
        print(f"   Accuracy: {acc:.2f}%")

        # Clear memory
        tf.keras.backend.clear_session()
        del model
        gc.collect()

        model_counter += 1


# ===============================
# MAIN EXECUTION
# ===============================
if __name__ == "__main__":
    print("🚀 Starting predictions...\n")
    predict_models_on_folder(
        models_dir=MODELS_DIR,
        test_dir=TEST_DIR,
        class_names=CLASS_NAMES,
        image_size=IMAGE_SIZE
    )
    print("\n🎯 All models processed successfully!")
