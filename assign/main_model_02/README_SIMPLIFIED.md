# Model 02: Local Wellbeing Predictor

Flask app predicts emotional state, intensity, confidence from journal text + numerics.

## Files
- `main.py`: Flask server + batch export.
- `predictor.py`: Model training/prediction.
- `templates/index.html`: UI (Tailwind CDN).
- Data: `train_data.xlsx`, `test_data.xlsx`.

## Setup & Run
```bash
pip install -r requirements.txt
python main.py  # http://127.0.0.1:5000
python main.py --test-export test_data.xlsx --output predictions.csv
```

## Features
**Text**: TF-IDF (uni/bi-grams), regex (conflict/activation/regulation).
**Numerics**: duration, sleep, energy, stress + derived (sleep_debt, etc.).
**Unused**: ambience, time_of_day, etc. (add via ColumnTransformer).

## Model
- **State**: Bootstrap LogisticRegression (vote confidence).
- **Intensity**: Bootstrap RandomForestRegressor (mean).

**CV Metrics**:
| Metric | Value |
| --- | ---: |
| State acc/F1 | 0.42 |
| Intensity MAE | 1.22 |

Weak: restless/overwhelmed, short texts.

## API Example
```bash
curl -X POST http://127.0.0.1:5000/api/predict -H "Content-Type: application/json" -d '{"journal_text": "rain helped settle but mind looping"}'
```

