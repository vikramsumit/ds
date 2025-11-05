# 🍑 Peach Disease Classifier

A specialized deep learning model for detecting and classifying diseases in peach plants using Convolutional Neural Networks (CNNs). This classifier focuses on bacterial diseases that commonly affect peach orchards.

## 📊 Supported Diseases

| Disease | Description | Symptoms |
|---------|-------------|----------|
| **Bacterial Spot** | Bacterial disease caused by Xanthomonas arboricola | Small, dark spots on leaves and fruits, often with water-soaked margins |
| **Healthy** | No disease present | Normal green leaves and healthy fruit development |

## 🏗️ Project Structure

```
peach_disease_classifier/
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
cd peach_disease_classifier
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
from src.predict import predict_peach_disease

result = predict_peach_disease("path/to/peach_image.jpg")
print(f"Disease: {result['disease']}")
print(f"Confidence: {result['confidence']:.2f}%")
```

## 📈 Performance

- **Test Accuracy**: ~97-100%
- **Validation Accuracy**: ~95-98%
- **Training Time**: ~15-30 minutes (GPU)
- **Model Size**: ~45MB per trained model
- **Average Confidence**: ~97.7%
- **High Confidence Rate**: 90-95% of predictions above 90%

## 🔧 Model Details

- **Architecture**: CNN with 4 convolutional blocks
- **Input Size**: 256x256 RGB images
- **Output Classes**: 2 (Bacterial Spot, Healthy)
- **Framework**: TensorFlow/Keras
- **Data Augmentation**: Random flips, rotations, and contrast adjustments

## 📝 Usage Notes

- Images should be clear, well-lit photos of peach leaves or fruits
- Best results with images showing clear disease symptoms
- Model performs best on images similar to training data
- Bacterial spot can spread rapidly in wet conditions

## 🤝 Contributing

To improve the peach disease classifier:
1. Add more training images for better accuracy
2. Fine-tune model hyperparameters
3. Add support for additional peach diseases
4. Improve data preprocessing techniques

---

*Part of the Plant Disease Detection System*
