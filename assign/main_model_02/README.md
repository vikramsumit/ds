# Model 02: Local Wellbeing Reflection Desk

This folder contains a local wellbeing prediction system built around a Flask UI and API. The app reads reflective journal-style text plus a few numeric context fields and predicts:

- `predicted_state`
- `predicted_intensity`
- `confidence`

It also includes a test-export mode that scores the provided Excel test sheet and writes `predictions.csv`.

## Project Files

- `main.py`: Flask entry point, routes, and batch export CLI
- `predictor.py`: model training, preprocessing, and prediction logic
- `templates/index.html`: active UI template rendered by Flask
- `templates/index1.html`: older archived template variant
- `static/classic.css`: local stylesheet from the earlier classical UI pass
- `train_data.xlsx`: labeled training data
- `test_data.xlsx`: unlabeled test data
- `predictions.csv`: latest batch export output
- `01.ipynb`: consolidated exploratory notebook with EDA and modeling work

Note: the current active `index.html` uses Tailwind CDN and Google Fonts. The local `classic.css` file is present in the folder but is not referenced by the active template right now.

## Setup Instructions

From the `model_02` folder:

```bash
pip install -r requirements.txt
python main.py
```

This starts the Flask app at `http://127.0.0.1:5000` by default.

If you want to export predictions for the provided test sheet instead of starting the server:

```bash
python main.py --test-export test_data.xlsx --output predictions.csv
```

If you run from the repository root instead:

```bash
pip install -r model_02/requirements.txt
python model_02/main.py
```

## Approach

The system is intentionally lightweight and fully local:

1. Train a text-first model on `train_data.xlsx`.
2. Clean and normalize the journal text.
3. Build a small feature set from TF-IDF text vectors plus engineered numeric features.
4. Use a bootstrap ensemble for both state prediction and intensity prediction.
5. Expose the fitted model through:
   - a browser form at `/`
   - a JSON API at `/api/predict`
   - a batch export mode through `--test-export`

The Flask app lazily trains and caches the model using `lru_cache`, so the first real prediction request pays the training cost and later requests reuse the same fitted system.

## Feature Engineering

### Text Processing

- lowercasing
- punctuation stripping with regex cleanup
- whitespace normalization
- TF-IDF word features with unigrams and bigrams
- vocabulary capped at 100 text features

### Regex-Derived Text Signals

- conflict terms: `but`, `still`, `yet`, `however`, `although`, `though`
- activation terms: `racing`, `buzz`, `chaotic`, `tense`, `wired`, `restless`, `overwhelmed`
- regulation terms: `calm`, `settled`, `focused`, `steady`, `grounded`, `clear`, `relaxed`

### Numeric Features

- `duration_min`
- `sleep_hours`
- `energy_level`
- `stress_level`

### Derived Features

- `text_word_count`
- `text_char_count`
- `text_conflict_terms`
- `text_activation_terms`
- `text_regulation_terms`
- `sleep_debt = 7 - sleep_hours`
- `stress_energy_gap = stress_level - energy_level`
- `stress_energy_sum = stress_level + energy_level`
- `duration_log1p = log(1 + duration_min)`

### Missing-Value Handling

- `sleep_hours` defaults to `7`
- `stress_level` defaults to `3`
- `energy_level` defaults to `3`
- `duration_min` defaults to `0`

Observed missingness in the training set:

- `sleep_hours`: 7 rows missing
- `previous_day_mood`: 15 rows missing
- `face_emotion_hint`: 123 rows missing

Important current limitation: the UI collects `ambience_type`, `time_of_day`, `previous_day_mood`, `face_emotion_hint`, and `reflection_quality`, but the current feature builder does not include those categorical fields in the actual model vector yet.

## Model Choice

### Emotional State Model

- `LogisticRegression`
- trained inside a 5-model bootstrap ensemble
- final state chosen by majority vote
- confidence estimated from vote share across the ensemble

Why this choice:

- the journal entries are short, so linear text models are a good starting point
- TF-IDF plus logistic regression is fast, local, and easy to debug
- bootstrapping adds some stability and gives a simple confidence score

### Intensity Model

- `RandomForestRegressor`
- also trained as a 5-model bootstrap ensemble
- final intensity is the mean prediction, rounded and clipped to `1..5`

Why this choice:

- the intensity label is ordinal but noisy
- averaging across bootstrap regressors is a simple way to smooth variance

### Measured Performance

Using 5-fold stratified cross-validation on `train_data.xlsx` with the current implementation:

| Metric | Value |
| --- | ---: |
| State accuracy | 0.4175 |
| State macro F1 | 0.4158 |
| Intensity MAE | 1.2158 |
| Intensity exact accuracy | 0.2200 |
| Intensity within-one accuracy | 0.6158 |

Per-class state recall from the same run:

| State | Recall |
| --- | ---: |
| calm | 0.5139 |
| mixed | 0.4817 |
| neutral | 0.4229 |
| focused | 0.3938 |
| overwhelmed | 0.3632 |
| restless | 0.3254 |

Interpretation:

- the model is usable as a lightweight local baseline
- it is strongest on clearer calm/mixed phrasing
- it struggles more on `restless`, `overwhelmed`, and short ambiguous entries
- intensity is often only approximately correct rather than exact

## How To Run

### Start the Flask UI

```bash
python main.py
```

Open:

- `http://127.0.0.1:5000/`

### Start the API on a custom host/port

```bash
python main.py --host 0.0.0.0 --port 8000
```

### Call the API directly

```bash
curl -X POST http://127.0.0.1:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "journal_text": "The rain helped me settle, but part of my mind is still looping through tomorrow'\''s work.",
    "ambience_type": "rain",
    "duration_min": 15,
    "sleep_hours": 6.5,
    "energy_level": 3,
    "stress_level": 4,
    "time_of_day": "evening",
    "previous_day_mood": "mixed",
    "face_emotion_hint": "tired_face",
    "reflection_quality": "clear"
  }'
```

### Export the Provided Test Sheet

```bash
python main.py --test-export test_data.xlsx --output predictions.csv
```

This writes a CSV with:

- `id`
- `predicted_state`
- `predicted_intensity`
- `confidence`
