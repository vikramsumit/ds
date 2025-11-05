# Apple Disease Classifier

This project is designed to classify apple diseases using deep learning techniques. It leverages TensorFlow and Keras to train models on a dataset of apple images, and provides functionality to make predictions using multiple trained models.

## Project Structure

```
apple_disease_classifier
├── notebooks
│   └── model_training.ipynb      # Jupyter notebook for training the model
├── src
│   ├── predict.py                 # Script for making predictions using multiple models
│   ├── utils.py                   # Utility functions for image processing and result formatting
│   └── data_loader.py             # Module for loading and preparing datasets
├── models
│   ├── 1.keras                    # First version of the trained model
│   ├── 2.keras                    # Second version of the trained model
│   └── best_model.keras           # Best performing model based on validation metrics
├── data
│   ├── Train                      # Directory containing training images
│   ├── Val                        # Directory containing validation images
│   └── Test                       # Directory containing test images
├── requirements.txt               # List of dependencies for the project
├── .gitignore                     # Files and directories to be ignored by Git
└── README.md                      # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd apple_disease_classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare your dataset by placing images in the appropriate directories under `data/Train`, `data/Val`, and `data/Test`.

## Usage

- To train the model, open and run the `model_training.ipynb` notebook. This will load the data, define the model architecture, and train the model on the training dataset.

- To make predictions using the trained models, run the `predict.py` script. This script will load all models from the `models` directory and use them to predict the classes of input images.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.