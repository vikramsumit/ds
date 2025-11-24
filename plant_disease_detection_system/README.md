# 🌱 Plant Disease Detection System

An advanced deep learning-based system for automated plant disease detection and classification using Convolutional Neural Networks (CNNs). This project leverages TensorFlow and Keras to identify plant species and diagnose various diseases affecting crops, helping farmers and agricultural professionals make informed decisions to improve crop health and yield.

## 📋 Table of Contents

- [🌟 Features](#-features)
- [🎯 Importance](#-importance)
- [🏗️ Project Structure](#️-project-structure)
- [🛠️ Installation](#️-installation)
- [📊 Supported Plants and Diseases](#-supported-plants-and-diseases)
- [🚀 Usage](#-usage)
- [🧠 Model Architecture](#-model-architecture)
- [📈 Performance](#-performance)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🌟 Features

- **Multi-Plant Support**: Classifies 9 different plant species
- **Disease Detection**: Identifies specific diseases for each plant type
- **Two-Stage Classification**: First identifies plant species, then detects diseases
- **Ensemble Learning**: Uses multiple models for improved accuracy
- **Batch Processing**: Supports prediction on multiple images
- **CSV Export**: Generates detailed prediction reports
- **Data Augmentation**: Includes image preprocessing and augmentation techniques
- **Modular Design**: Individual classifiers for each plant plus unified predictor
- **CLI Interface**: Command-line interface for easy integration and automation
- **GUI Development**: Graphical user interface currently under development for user-friendly interaction

## 🎯 Importance

Plant diseases pose a significant threat to global food security, causing substantial economic losses in agriculture. Traditional disease detection methods are often time-consuming, labor-intensive, and require expert knowledge. This automated system provides:

- **Early Detection**: Identifies diseases at early stages when treatment is most effective
- **Scalability**: Processes large numbers of images quickly
- **Consistency**: Provides objective, reproducible results
- **Accessibility**: Makes expert-level disease diagnosis accessible to farmers
- **Cost Efficiency**: Reduces the need for manual inspection and expert consultation

*[Add importance graph/chart here]*

## 🏗️ Project Structure

```
plant_disease_detection_system/
├── combined_predict.py              # Unified predictor for plant + disease classification
├── README.md                        # Project documentation
├── all_data/                        # Combined data and models
│   ├── data/                        # Training/validation/test datasets
│   ├── models/                      # Trained plant classification models
│   ├── notebooks/
│   │   └── model_training.ipynb     # Plant classification training notebook
│   ├── src/
│   │   ├── predict.py               # Batch prediction script
│   │   ├── top.py                   # Model evaluation script
│   │   ├── data_loader.py           # Data loading utilities
│   │   └── csv_maker.py             # CSV generation utilities
│   └── csv/                         # Prediction result CSVs
├── apple_disease_classifier/        # Apple-specific classifier
├── bellpepper_disease_classifier/   # Bell pepper classifier
├── cherry_disease_classifier/       # Cherry classifier
├── corn(maize)_disease_classifier/  # Corn classifier
├── grape_disease_classifier/        # Grape classifier
├── peach_disease_classifier/        # Peach classifier
├── potato_disease_classifier/       # Potato classifier
├── strawberry_disease_classifier/   # Strawberry classifier
└── tomato_disease_classifier/       # Tomato classifier
```

*[Add project structure diagram here]*

Each plant classifier follows a similar structure:
```
plant_disease_classifier/
├── data/                    # Plant-specific image datasets
├── models/                  # Trained disease classification models
├── notebooks/               # Training notebooks
├── src/                     # Prediction and utility scripts
├── csv/                     # Prediction results
├── requirements.txt         # Dependencies
└── README.md               # Plant-specific documentation
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- TensorFlow 2.10+
- GPU recommended for training (optional for inference)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vikramsumit/ds/tree/main/plant_disease_detection_system
   cd plant_disease_detection_system
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r apple_disease_classifier/requirements.txt
   # Or install core dependencies manually:
   pip install tensorflow==2.10.0 numpy matplotlib pandas pathlib
   ```

4. **Prepare data:**
   - Place training images in `all_data/data/Train/`
   - Place validation images in `all_data/data/Val/`
   - Place test images in `all_data/data/Test/`
   - Organize images in subdirectories by class name

## 📊 Supported Plants and Diseases

### Plant Classification (9 Classes)
- Apple
- Bell Pepper
- Cherry
- Corn (Maize)
- Grape
- Peach
- Potato
- Strawberry
- Tomato

### Disease Classification by Plant

| Plant | Diseases |
|-------|----------|
| **Apple** | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| **Bell Pepper** | Bacterial Spot, Healthy |
| **Cherry** | Healthy, Powdery Mildew |
| **Corn (Maize)** | Blight, Common Rust, Gray Leaf Spot, Healthy |
| **Grape** | Black Measles, Black Rot, Healthy |
| **Peach** | Bacterial Spot, Healthy |
| **Potato** | Early Blight, Healthy, Late Blight |
| **Strawberry** | Healthy, Leaf Scorch |
| **Tomato** | Bacterial Spot, Early Blight, Healthy, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Tomato Mosaic Virus, Tomato Yellow Leaf Curl Virus |

## 🚀 Usage

### Current Interface: CLI Mode

The system currently operates through a command-line interface. GUI development is in progress for enhanced user experience.

### Training

#### Plant Classification Model
```bash
# Open the training notebook
jupyter notebook all_data/notebooks/model_training.ipynb
```

The notebook includes:
- Data loading and preprocessing
- CNN model architecture with data augmentation
- Training with early stopping and learning rate scheduling
- Model evaluation and visualization

#### Individual Plant Disease Classifiers
Each plant has its own training setup. Example for Apple:
```bash
cd apple_disease_classifier
jupyter notebook notebooks/model_training.ipynb
```

### Prediction

#### Single Image Prediction
```python
from combined_predict import combined_predict

# Predict plant and disease
result = combined_predict("path/to/image.jpg")
print(f"Plant: {result['plant']} ({result['plant_confidence']:.1f}%)")
print(f"Disease: {result['disease']} ({result['disease_confidence']:.1f}%)")
```

#### Batch Prediction
```bash
# Generate CSV predictions for all models
python all_data/src/predict.py

# Evaluate model performance
python all_data/src/top.py
```

#### Individual Plant Prediction
```bash
cd apple_disease_classifier
python src/predict.py
```

### Example Output

```
🔍 Analyzing image: tomato_lateblight.jpg
🌱 Plant Prediction: tomato (95.2%, Model: best_model.keras)
🦠 Disease Prediction: Late Blight (87.3%)
```

*[Add input/output example images here]*

## 🧠 Model Architecture

### Plant Classification Model
- **Input**: 256x256 RGB images
- **Architecture**: CNN with 4 convolutional blocks
- **Layers**:
  - Conv2D (32, 64, 128, 128 filters)
  - Batch Normalization
  - Max Pooling
  - Global Average Pooling
  - Dense (128 units) + Dropout (0.5)
  - Output: 9 classes (softmax)

### Data Augmentation
- Random horizontal/vertical flip
- Random rotation (±10°)
- Random zoom (±10%)
- Random contrast adjustment

### Disease Classification Models
- Similar CNN architecture adapted for disease-specific classes
- Ensemble prediction using multiple trained models
- Majority voting for final classification

*[Add model architecture diagram here]*

## 📈 Performance

### Plant Classification
- **Test Accuracy**: ~97-100%
- **Validation Accuracy**: ~95-98%
- **Training Time**: ~10-20 minutes (It depends on GPU)
- **Average Confidence**: ~97.7%
- **Low Confidence Cases**: ~1-5% of predictions (typically 40-50% confidence)

### Disease Classification
- **Accuracy Range**: 95-100% (varies by plant/disease)
- **Ensemble Improvement**: +2-3% over single models
- **High Accuracy**: 97-100% confidence on most predictions
- **Occasional Low Confidence**: 1 in 20 images may show 40-50% confidence

*[Add performance graphs/charts here]*

### Sample Results
```
Model Performance Summary (Based on CSV Analysis):
- Plant Classification: 97.7% average confidence across models
- High Confidence Predictions: 90-95% of cases (90%+ confidence)
- Low Confidence Cases: 5-10% of predictions (below 90% confidence)
- Very Low Confidence: Rare (below 50% confidence)
- Best Performance: 100% confidence on many predictions
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-plant`)
3. Commit changes (`git commit -am 'Add new plant classifier'`)
4. Push to branch (`git push origin feature/new-plant`)
5. Create a Pull Request

### Adding New Plants
1. Create new directory: `new_plant_disease_classifier/`
2. Follow the established structure
3. Update `combined_predict.py` with new plant and diseases
4. Add training data and train models
5. Update this README

## 📄 License

<!-- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->

---

**Built with ❤️ for sustainable agriculture**

*For questions or support, please open an issue on GitHub.*
