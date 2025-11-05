import argparse
import pathlib
import pandas as pd
import numpy as np
import tensorflow as tf
from datetime import datetime

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif"}

def model_has_rescaling_layer(model: tf.keras.Model) -> bool:
    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.Rescaling):
            return True
    return False

def infer_image_size_from_model(model: tf.keras.Model, default=(256, 256)):
    try:
        shape = model.input_shape  # e.g. (None, H, W, C)
        # handle nested models or multiple inputs
        if isinstance(shape, list):
            shape = shape[0]
        if len(shape) >= 3 and shape[1] and shape[2]:
            return (int(shape[1]), int(shape[2]))
    except Exception:
        pass
    return default

def load_class_names(classes_file: str = None, test_root: str = None):
    if classes_file:
        p = pathlib.Path(classes_file)
        if p.exists():
            return [line.strip() for line in p.read_text().splitlines() if line.strip()]
    if test_root:
        p = pathlib.Path(test_root)
        if p.exists():
            dirs = [d for d in sorted(p.iterdir()) if d.is_dir()]
            if dirs:
                return [d.name for d in dirs]
    return None

def preprocess_image(path: pathlib.Path, image_size=(256,256), channels=3, model_rescales=False):
    raw = tf.io.read_file(str(path))
    img = tf.image.decode_image(raw, channels=channels)
    img = tf.cast(img, tf.float32)
    img = tf.image.resize(img, image_size)
    if not model_rescales:
        img = img / 255.0
    img = tf.expand_dims(img, 0)  # batch dim
    return img

def gather_image_files(folder: str):
    p = pathlib.Path(folder)
    files = [f for f in sorted(p.rglob("*")) if f.is_file() and f.suffix.lower() in IMAGE_EXT and not f.name.startswith(".")]
    return files

def predict_folder_with_model(model_path, input_folder, out_csv=None, classes_file=None, image_size=None, channels=3):
    model_path = pathlib.Path(model_path)
    assert model_path.exists(), f"Model not found: {model_path}"
    print("Loading model:", model_path)
    model = tf.keras.models.load_model(str(model_path))

    # determine preprocessing settings
    model_rescales = model_has_rescaling_layer(model)
    print("Model contains Rescaling layer:", model_rescales)
    inferred_size = infer_image_size_from_model(model)
    if image_size is None:
        image_size = inferred_size
    print("Using image size:", image_size)

    class_names = load_class_names(classes_file, test_root=input_folder)
    if class_names:
        print("Loaded class names, count:", len(class_names))
    else:
        print("No class names provided; predicted indices will be returned instead of names.")

    files = gather_image_files(input_folder)
    print(f"Found {len(files)} images in {input_folder}")

    rows = []
    for fp in files:
        try:
            inp = preprocess_image(fp, image_size=image_size, channels=channels, model_rescales=model_rescales)
            preds = model.predict(inp, verbose=0)
            probs = np.asarray(preds[0], dtype=float)
            idx = int(np.argmax(probs))
            conf = float(np.max(probs) * 100.0)
            pred_name = class_names[idx] if (class_names and idx < len(class_names)) else str(idx)
            rows.append({
                "filename": fp.name,
                "filepath": str(fp),
                "predicted_class": pred_name,
                "predicted_index": idx,
                "confidence_percent": conf
            })
        except Exception as e:
            rows.append({
                "filename": fp.name,
                "filepath": str(fp),
                "predicted_class": "ERROR",
                "predicted_index": -1,
                "confidence_percent": 0.0,
                "error": str(e)
            })

    df = pd.DataFrame(rows)
    if out_csv is None:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_csv = f"predictions_{model_path.stem}_{ts}.csv"
    df.to_csv(out_csv, index=False)
    print(f"Wrote {len(df)} rows to {out_csv}")
    # clean up
    tf.keras.backend.clear_session()
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict images in a folder using a single .keras model")
    parser.add_argument("--model", default="models/1.keras", help="Path to .keras model (default: models/1.keras)")
    parser.add_argument("--input", required=True, help="Folder with images to predict (recursive)")
    parser.add_argument("--out", default=None, help="Output CSV path (defaults to timestamped file)")
    parser.add_argument("--classes", default=None, help="Optional classes.txt (one class per line) or training/test root to infer classes")
    parser.add_argument("--size", default=None, help="Image size HxW (e.g. 256x256). If omitted will try to infer from model input.")
    args = parser.parse_args()

    img_size = None
    if args.size:
        try:
            h, w = args.size.split("x")
            img_size = (int(h), int(w))
        except Exception:
            raise SystemExit("Invalid --size format. Use HxW e.g. 256x256")

    predict_folder_with_model(args.model, args.input, out_csv=args.out, classes_file=args.classes, image_size=img_size)
