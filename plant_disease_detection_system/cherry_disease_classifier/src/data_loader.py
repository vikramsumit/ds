# ...existing code...
import os
import tensorflow as tf
import numpy as np

# Default class order (used if no classes file / inference provided)
DEFAULT_CLASS_NAMES = [
    "Apple Scab",
    "Black Rot",
    "Cedar Apple Rust",
    "Healthy"
]

def load_models(models_dir):
    models = []
    for model_file in os.listdir(models_dir):
        if model_file.endswith('.keras'):
            model_path = os.path.join(models_dir, model_file)
            model = tf.keras.models.load_model(model_path)
            models.append(model)
            print(f"Loaded model from {model_path}")
    return models

def preprocess_image(image_tensor, image_size):
    img = tf.cast(image_tensor, tf.float32)
    img = tf.image.resize(img, image_size)
    img = img / 255.0  # Normalize to [0, 1]
    return img

def predict_with_models(models, image_tensor, image_size):
    processed_image = preprocess_image(image_tensor, image_size)
    processed_image = tf.expand_dims(processed_image, axis=0)  # Add batch dimension

    preds_list = []
    for model in models:
        p = model.predict(processed_image)
        p = np.asarray(p)          # ensure numpy
        p = p.reshape(-1)          # flatten to (num_classes,)
        preds_list.append(p)

    if len(preds_list) == 0:
        raise ValueError("No models loaded")

    preds_arr = np.vstack(preds_list)     # shape (n_models, num_classes)
    mean_preds = np.mean(preds_arr, axis=0)  # shape (num_classes,)
    return mean_preds  # 1D array of probabilities

def format_predictions(predictions, class_names=None):
    """
    predictions: 1D numpy array of class probabilities (num_classes,)
    class_names: list of class names matching training ordering
                 if None, DEFAULT_CLASS_NAMES will be used
    """
    probs = np.asarray(predictions).reshape(-1)
    if probs.size == 0:
        return "UNKNOWN", 0.0

    predicted_class_idx = int(np.argmax(probs))
    confidence = float(np.max(probs) * 100.0)

    names = class_names if class_names else DEFAULT_CLASS_NAMES
    if 0 <= predicted_class_idx < len(names):
        return names[predicted_class_idx], confidence
    # fallback: return numeric index if out-of-range
    return str(predicted_class_idx), confidence
# ...existing code...