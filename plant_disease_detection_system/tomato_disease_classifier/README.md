# 🍅 Tomato Disease Classifier

A specialized deep learning model for detecting and classifying diseases in tomato plants using Convolutional Neural Networks (CNNs). This classifier identifies a wide range of diseases that commonly affect tomato crops, from fungal to viral infections.

## 📊 Supported Diseases

| Disease | Description | Symptoms |
|---------|-------------|----------|
| **Bacterial Spot** | Bacterial disease caused by Xanthomonas spp. | Small, dark spots with yellow halos on leaves and fruits |
| **Early Blight** | Fungal disease caused by Alternaria solani | Dark spots with concentric rings on older leaves |
| **Late Blight** | Fungal disease caused by Phytophthora infestans | Water-soaked lesions, white fungal growth on leaf undersides |
| **Leaf Mold** | Fungal disease caused by Fulvia fulva | Yellow spots on upper leaves, grayish mold on undersides |
| **Septoria Leaf Spot** | Fungal disease caused by Septoria lycopersici | Small, circular spots with dark borders on leaves |
| **Spider Mites** | Pest damage causing two-spotted spider mites | Yellow stippling, fine webbing on leaves |
| **Target Spot** | Fungal disease caused by Corynespora cassiicola | Dark spots with concentric rings, yellow halos |
| **Tomato Mosaic Virus** | Viral disease | Mottled yellow and green leaves, distorted growth |
| **Tomato Yellow Leaf Curl Virus** | Viral disease transmitted by whiteflies | Yellowing and curling of leaves, stunted growth |
| **Healthy** | No disease present | Normal green leaves and healthy fruit development |

## 🏗️ Project Structure

```
tomato_disease_classifier/
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
cd tomato_disease_classifier
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
from src.predict import predict_tomato_disease

result = predict_tomato_disease("path/to/tomato_image.jpg")
print(f"Disease: {result['disease']}")
print(f"Confidence: {result['confidence']:.2f}%")
```

## 📈 Performance

- **Test Accuracy**: ~97-100%
- **Validation Accuracy**: ~95-98%
- **Training Time**: ~10-30 minutes (Depends on GPU)
- **Model Size**: ~130MB per trained model
- **Average Confidence**: ~97.7%
- **High Confidence Rate**: 90-95% of predictions above 90%

## 🔧 Model Details

- **Architecture**: CNN with 4 convolutional blocks
- **Input Size**: 256x256 RGB images
- **Output Classes**: 10 (9 diseases + Healthy)
- **Framework**: TensorFlow/Keras
- **Data Augmentation**: Random flips, rotations, and contrast adjustments

## 📝 Usage Notes

- Images should be clear, well-lit photos of tomato leaves or fruits
- Best results with images showing clear disease symptoms
- Model performs best on images similar to training data
- Tomato has the most disease classes, making it the most complex classifier

## 🤝 Contributing

To improve the tomato disease classifier:
1. Add more training images for better accuracy
2. Fine-tune model hyperparameters
3. Add support for additional tomato diseases
4. Improve data preprocessing techniques

---

*Part of the Plant Disease Detection System*
