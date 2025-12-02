# 🍎 Apple Disease Classifier

A specialized deep learning model for detecting and classifying diseases in apple plants using Convolutional Neural Networks (CNNs). This classifier identifies various fungal and bacterial diseases that commonly affect apple crops.

## 📊 Supported Diseases

| Disease | Description | Symptoms |
|---------|-------------|----------|
| **Apple Scab** | Fungal disease caused by Venturia inaequalis | Dark, olive-green spots on leaves and fruits, often with velvety texture |
| **Black Rot** | Fungal disease caused by Botryosphaeria obtusa | Brown to black lesions on leaves, fruit rot, and cankers on branches |
| **Cedar Apple Rust** | Fungal disease requiring both apple and cedar hosts | Bright orange spots on leaves, yellow-orange lesions on fruit |
| **Healthy** | No disease present | Normal green leaves and healthy fruit development |

## 🏗️ Project Structure

```
apple_disease_classifier/
├── data/
│   ├── Train/                 
│   ├── Val/                   
│   └── Test/                  
├── models/                    
├── notebooks/
│   └── model_training.ipynb   
├── src/
│   ├── predict.py             
│   └── utils.py               
├── csv/                       
├── requirements.txt           
├── test_plot.png              
└── README.md                  
```

## 🚀 Quick Start

### Installation
```bash
cd apple_disease_classifier
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
from src.predict import predict_apple_disease

result = predict_apple_disease("path/to/apple_image.jpg")
print(f"Disease: {result['disease']}")
print(f"Confidence: {result['confidence']:.2f}%")
```

## 📈 Performance

- **Test Accuracy**: ~97-100%
- **Validation Accuracy**: ~95-98%
- **Training Time**: ~20-40 minutes (GPU)
- **Model Size**: ~50MB per trained model
- **Average Confidence**: ~97.7%
- **High Confidence Rate**: 90-95% of predictions above 90%

## 🔧 Model Details

- **Architecture**: CNN with 4 convolutional blocks
- **Input Size**: 256x256 RGB images
- **Output Classes**: 4 (Apple Scab, Black Rot, Cedar Apple Rust, Healthy)
- **Framework**: TensorFlow/Keras
- **Data Augmentation**: Random flips, rotations, and contrast adjustments

## 📝 Usage Notes

- Images should be clear, well-lit photos of apple leaves or fruits
- Best results with images showing clear disease symptoms
- Model performs best on images similar to training data
- For best accuracy, use multiple images of the same plant from different angles

## 🤝 Contributing

To improve the apple disease classifier:
1. Add more training images for better accuracy
2. Fine-tune model hyperparameters
3. Add support for additional apple diseases
4. Improve data preprocessing techniques

---

*Part of the Plant_Disease_Detection_System*
