import os
import tensorflow as tf
import numpy as np

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
    predictions = [model.predict(processed_image) for model in models]
    return np.mean(predictions, axis=0)  # Average predictions

def format_predictions(predictions, class_names):
    predicted_class_idx = np.argmax(predictions)
    confidence = float(np.max(predictions) * 100.0)
    return class_names[predicted_class_idx], confidence