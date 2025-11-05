import os
import gc
from pathlib import Path
import tensorflow as tf
import pandas as pd

# ===============================
# CONFIGURATION
# ===============================
MODELS_DIR = "/home/amit/code_only/code/new/bellpepper_disease_classifier/models"
TEST_DIR = "/home/amit/code_only/code/new/bellpepper_disease_classifier/data/Test/Other_Images"
CSV_OUTPUT_DIR = "/home/amit/code_only/code/new/bellpepper_disease_classifier/csv"
IMAGE_SIZE = (256, 256)

# ✅ Hardcoded class names
CLASS_NAMES = ['Apple Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy']

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
    """Predict all images in test_dir for each model in models_dir and save per-model CSVs."""
    models_dir = Path(models_dir)
    test_dir = Path(test_dir)
    os.makedirs(CSV_OUTPUT_DIR, exist_ok=True)

    model_counter = 1

    for model_file in sorted(models_dir.glob("*.keras")):
        print(f"\n🔹 Loading model {model_counter}: {model_file.name}")
        model = tf.keras.models.load_model(str(model_file))
        rows = []

        for img_path in sorted(test_dir.rglob("*")):
            if not img_path.is_file():
                continue
            if img_path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
                continue

            actual_label = img_path.parent.name
            pred_idx, conf = predict_image(model, str(img_path), image_size=image_size)
            pred_name = class_names[pred_idx] if pred_idx < len(class_names) else str(pred_idx)

            rows.append({
                "model": model_file.name,
                "filepath": str(img_path),
                "actual": actual_label,
                "predicted": pred_name,
                "predicted_index": pred_idx,
                "confidence_percent": conf
            })

        # Save predictions for this model
        df = pd.DataFrame(rows)
        csv_filename = Path(CSV_OUTPUT_DIR) / f"{model_counter}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"✅ Saved {len(df)} predictions to {csv_filename}")

        # Free up memory
        tf.keras.backend.clear_session()
        del model
        gc.collect()

        model_counter += 1


# ===============================
# MAIN EXECUTION
# ===============================
if __name__ == "__main__":
    print("🚀 Starting batch predictions...\n")
    predict_models_on_folder(
        models_dir=MODELS_DIR,
        test_dir=TEST_DIR,
        class_names=CLASS_NAMES,
        image_size=IMAGE_SIZE
    )
    print("\n🎯 All models processed successfully!")
