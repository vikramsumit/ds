# 🍇 Grape Disease Classifier

A specialized deep learning model for detecting and classifying diseases in grape plants using Convolutional Neural Networks (CNNs). This classifier identifies various fungal diseases that commonly affect grape vineyards.

## 📊 Supported Diseases

| Disease | Description | Symptoms |
|---------|-------------|----------|
| **Black Measles** | Fungal disease caused by Pseudocercospora vitis | Dark spots with yellow halos on leaves |
| **Black Rot** | Fungal disease caused by Guignardia bidwellii | Brown to black lesions on leaves and fruit |
| **Healthy** | No disease present | Normal green leaves and healthy fruit development |

## 🏗️ Project Structure

```
grape_disease_classifier/
├── data/
│   ├── Train/                 # Training images organized by disease class
│   ├── Val/                   # Validation images
│   └── Test/                  # Test images
├── models/                    # Trained CNN models (.keras files)
├── notebooks/
│   └── model_training.ipynb   # Jupyter notebook for training the model
├── src/
│   ├── predict.py             # Script for making predictions on new images
│   └── utils.py               # Utility functions for image processing
├── csv/                       # Prediction results and evaluation metrics
├── requirements.txt           # Python dependencies
└── README.md                  # This documentation
```

## 🚀 Quick Start

### Installation
```bash
cd grape_disease_classifier
pip install -r requirements.txt
```

### Training
```bash
jupyter notebook notebooks/model_training.ipynb
```

### Prediction
```bash
python src/predict.py
```

### Single Image Prediction
```python
from src.predict import predict_grape_disease

result = predict_grape_disease("path/to/grape_image.jpg")
print(f"Disease: {result['disease']}")
print(f"Confidence: {result['confidence']:.2f}%")
```

## 📈 Performance

- **Test Accuracy**: ~89%
- **Validation Accuracy**: ~86%
- **Training Time**: ~20-40 minutes (GPU)
- **Model Size**: ~47MB per trained model

## 🔧 Model Details

- **Architecture**: CNN with 4 convolutional blocks
- **Input Size**: 256x256 RGB images
- **Output Classes**: 3 (Black Measles, Black Rot, Healthy)
- **Framework**: TensorFlow/Keras
- **Data Augmentation**: Random flips, rotations, and contrast adjustments

## 📝 Usage Notes

- Images should be clear, well-lit photos of grape leaves or fruit
- Best results with images showing clear disease symptoms
- Model performs best on images similar to training data
- Black rot can severely affect fruit quality and yield

## 🤝 Contributing

To improve the grape disease classifier:
1. Add more training images for better accuracy
2. Fine-tune model hyperparameters
3. Add support for additional grape diseases
4. Improve data preprocessing techniques

---

*Part of the Plant Disease Detection System*
