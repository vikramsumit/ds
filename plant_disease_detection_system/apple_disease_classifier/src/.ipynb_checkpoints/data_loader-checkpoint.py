import os
import tensorflow as tf

def load_models(models_dir):
    models = []
    for model_file in os.listdir(models_dir):
        if model_file.endswith('.keras'):
            model_path = os.path.join(models_dir, model_file)
            model = tf.keras.models.load_model(model_path)
            models.append(model)
            print(f"Loaded model from {model_path}")
    return models

def load_data(data_dir, image_size=(256, 256), batch_size=12):
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        labels="inferred",
        label_mode="int",
        image_size=image_size,
        batch_size=batch_size,
        shuffle=True,
        seed=123
    )
    return dataset

def prepare_datasets(base_dir):
    train_ds = load_data(os.path.join(base_dir, "Train"))
    val_ds = load_data(os.path.join(base_dir, "Val"))
    test_ds = load_data(os.path.join(base_dir, "Test"), shuffle=False)
    return train_ds, val_ds, test_ds

def augment_data(dataset):
    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal_and_vertical"),
        tf.keras.layers.RandomRotation(0.1),
        tf.keras.layers.RandomZoom(0.1),
        tf.keras.layers.RandomContrast(0.1),
    ])
    return dataset.map(lambda x, y: (data_augmentation(x, training=True), y))