# 🍓 Strawberry Disease Classifier

A specialized deep learning model for detecting and classifying diseases in strawberry plants using Convolutional Neural Networks (CNNs). This classifier focuses on leaf diseases that commonly affect strawberry crops.

## 📊 Supported Diseases

| Disease | Description | Symptoms |
|---------|-------------|----------|
| **Leaf Scorch** | Fungal disease caused by Diplocarpon earlianum | Purple borders around leaf edges, brown centers |
| **Healthy** | No disease present | Normal green leaves and healthy fruit development |

## 🏗️ Project Structure

```
strawberry_disease_classifier/
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
cd strawberry_disease_classifier
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
from src.predict import predict_strawberry_disease

result = predict_strawberry_disease("path/to/strawberry_image.jpg")
print(f"Disease: {result['disease']}")
print(f"Confidence: {result['confidence']:.2f}%")
```

## 📈 Performance

- **Test Accuracy**: ~97-100%
- **Validation Accuracy**: ~95-98%
- **Training Time**: ~15-30 minutes (GPU)
- **Model Size**: ~44MB per trained model
- **Average Confidence**: ~97.7%
- **High Confidence Rate**: 90-95% of predictions above 90%

## 🔧 Model Details

- **Architecture**: CNN with 4 convolutional blocks
- **Input Size**: 256x256 RGB images
- **Output Classes**: 2 (Leaf Scorch, Healthy)
- **Framework**: TensorFlow/Keras
- **Data Augmentation**: Random flips, rotations, and contrast adjustments

## 📝 Usage Notes

- Images should be clear, well-lit photos of strawberry leaves
- Best results with images showing clear disease symptoms
- Model performs best on images similar to training data
- Leaf scorch appears as reddish-purple discoloration on leaf edges

## 🤝 Contributing

To improve the strawberry disease classifier:
1. Add more training images for better accuracy
2. Fine-tune model hyperparameters
3. Add support for additional strawberry diseases
4. Improve data preprocessing techniques

---

*Part of the Plant Disease Detection System*
