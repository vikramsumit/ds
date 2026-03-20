from __future__ import annotations

from pathlib import Path
import re
from typing import Any, Mapping

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


ROOT = Path(__file__).resolve().parent
TRAIN_PATH = ROOT / "train_data.xlsx"
TEXT_COLUMN = "text_clean"

PATTERNS = {
    "conflict": re.compile(r"\b(?:but|still|yet|however|although|though)\b", re.I),
    "activation": re.compile(r"\b(?:racing|buzz|chaotic|heavy|tense|wired|restless|spinning|overwhelmed)\b", re.I),
    "regulation": re.compile(r"\b(?:calm|settled|focused|steady|grounded|clear|relaxed|ease|centered)\b", re.I),
}

CATEGORICAL_FIELDS = [
    "ambience_type",
    "time_of_day",
    "previous_day_mood",
    "face_emotion_hint",
    "reflection_quality",
]

INPUT_FIELDS = [
    "journal_text",
    "ambience_type",
    "duration_min",
    "sleep_hours",
    "energy_level",
    "stress_level",
    "time_of_day",
    "previous_day_mood",
    "face_emotion_hint",
    "reflection_quality",
]

DEFAULT_INPUT = {
    "journal_text": "The rain helped me settle, but part of my mind is still looping through tomorrow's work.",
    "ambience_type": "rain",
    "duration_min": 15,
    "sleep_hours": 6.5,
    "energy_level": 3,
    "stress_level": 4,
    "time_of_day": "evening",
    "previous_day_mood": "mixed",
    "face_emotion_hint": "tired_face",
    "reflection_quality": "clear",
}


class WellbeingSupportSystem:
    def __init__(self, n_bootstrap_models=5, random_state=42):
        self.n_bootstrap_models = n_bootstrap_models
        self.random_state = random_state
        self.state_models = []
        self.intensity_models = []
        self.vectorizer = TfidfVectorizer(max_features=100, ngram_range=(1, 2))
        self.label_encoder = LabelEncoder()

    def prepare_dataframe(self, df):
        df = df.copy()

        text = df["journal_text"].fillna("").astype(str)
        clean = (
            text.str.lower()
            .str.replace(r"[^a-z0-9\s']", " ", regex=True)
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
        )
        df[TEXT_COLUMN] = clean

        df["text_word_count"] = clean.str.split().str.len()
        df["text_char_count"] = clean.str.len()
        df["text_conflict_terms"] = clean.str.count(PATTERNS["conflict"])
        df["text_activation_terms"] = clean.str.count(PATTERNS["activation"])
        df["text_regulation_terms"] = clean.str.count(PATTERNS["regulation"])

        df["sleep_hours"] = df["sleep_hours"].fillna(7)
        df["stress_level"] = df["stress_level"].fillna(3)
        df["energy_level"] = df["energy_level"].fillna(3)
        df["duration_min"] = df["duration_min"].fillna(0)

        df["sleep_debt"] = 7 - df["sleep_hours"]
        df["stress_energy_gap"] = df["stress_level"] - df["energy_level"]
        df["stress_energy_sum"] = df["stress_level"] + df["energy_level"]
        df["duration_log1p"] = np.log1p(df["duration_min"])

        return df

    def _build_features(self, df, fit=False):
        if fit:
            text_features = self.vectorizer.fit_transform(df[TEXT_COLUMN])
        else:
            text_features = self.vectorizer.transform(df[TEXT_COLUMN])

        numeric_cols = [
            "text_word_count",
            "text_char_count",
            "text_conflict_terms",
            "text_activation_terms",
            "text_regulation_terms",
            "sleep_debt",
            "stress_energy_gap",
            "stress_energy_sum",
            "duration_log1p",
        ]
        numeric_features = df[numeric_cols].values

        return np.hstack([text_features.toarray(), numeric_features])

    def fit(self, df):
        df = self.prepare_dataframe(df)
        X = self._build_features(df, fit=True)

        y_state = self.label_encoder.fit_transform(df["emotional_state"])
        y_intensity = df["intensity"].values

        self.state_models = []
        self.intensity_models = []

        rng = np.random.default_rng(self.random_state)
        for i in range(self.n_bootstrap_models):
            sample_idx = rng.choice(len(df), len(df), replace=True)

            X_sample = X[sample_idx]
            y_state_sample = y_state[sample_idx]
            y_intensity_sample = y_intensity[sample_idx]

            state_model = LogisticRegression(
                max_iter=2000,
                solver="newton-cg",
                random_state=self.random_state + i,
            )
            intensity_model = RandomForestRegressor(random_state=self.random_state + i)

            state_model.fit(X_sample, y_state_sample)
            intensity_model.fit(X_sample, y_intensity_sample)

            self.state_models.append(state_model)
            self.intensity_models.append(intensity_model)

    def predict(self, df):
        if not self.state_models or not self.intensity_models:
            raise RuntimeError("The wellbeing system must be fitted before prediction.")

        df = self.prepare_dataframe(df)
        X = self._build_features(df)

        state_predictions = []
        intensity_predictions = []

        for state_model, intensity_model in zip(self.state_models, self.intensity_models):
            state_predictions.append(state_model.predict(X))
            intensity_predictions.append(intensity_model.predict(X))

        state_predictions = np.array(state_predictions)
        intensity_predictions = np.array(intensity_predictions)

        final_state_idx = []
        confidence = []

        for column_index in range(state_predictions.shape[1]):
            values, counts = np.unique(state_predictions[:, column_index], return_counts=True)
            best_index = np.argmax(counts)
            final_state_idx.append(values[best_index])
            confidence.append(np.max(counts) / self.n_bootstrap_models)

        final_state = self.label_encoder.inverse_transform(final_state_idx)
        final_intensity = np.clip(np.mean(intensity_predictions, axis=0).round().astype(int), 1, 5)

        return pd.DataFrame(
            {
                "predicted_state": final_state,
                "predicted_intensity": final_intensity,
                "confidence": confidence,
            }
        )


def load_training_dataframe(train_path=TRAIN_PATH):
    return pd.read_excel(train_path)


def train_default_system(train_path=TRAIN_PATH):
    train_df = load_training_dataframe(train_path)
    system = WellbeingSupportSystem()
    system.fit(train_df)
    return system


def get_form_options(train_df=None):
    if train_df is None:
        train_df = load_training_dataframe(TRAIN_PATH)

    return {
        column: sorted(train_df[column].dropna().astype(str).unique().tolist())
        for column in CATEGORICAL_FIELDS
    }


def _coerce_float(value: Any, field_name: str, default: float) -> float:
    if value in (None, ""):
        return default

    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must be a number.") from exc


def _coerce_int(value: Any, field_name: str, default: int) -> int:
    return int(round(_coerce_float(value, field_name, default)))


def normalize_payload(payload: Mapping[str, Any]):
    journal_text = str(payload.get("journal_text", "")).strip()
    if not journal_text:
        raise ValueError("journal_text is required.")

    normalized = {
        "journal_text": journal_text,
        "ambience_type": str(payload.get("ambience_type", DEFAULT_INPUT["ambience_type"]) or DEFAULT_INPUT["ambience_type"]).strip(),
        "duration_min": max(0, _coerce_int(payload.get("duration_min"), "duration_min", DEFAULT_INPUT["duration_min"])),
        "sleep_hours": min(24.0, max(0.0, _coerce_float(payload.get("sleep_hours"), "sleep_hours", DEFAULT_INPUT["sleep_hours"]))),
        "energy_level": min(5, max(1, _coerce_int(payload.get("energy_level"), "energy_level", DEFAULT_INPUT["energy_level"]))),
        "stress_level": min(5, max(1, _coerce_int(payload.get("stress_level"), "stress_level", DEFAULT_INPUT["stress_level"]))),
        "time_of_day": str(payload.get("time_of_day", DEFAULT_INPUT["time_of_day"]) or DEFAULT_INPUT["time_of_day"]).strip(),
        "previous_day_mood": str(
            payload.get("previous_day_mood", DEFAULT_INPUT["previous_day_mood"]) or DEFAULT_INPUT["previous_day_mood"]
        ).strip(),
        "face_emotion_hint": str(
            payload.get("face_emotion_hint", DEFAULT_INPUT["face_emotion_hint"]) or DEFAULT_INPUT["face_emotion_hint"]
        ).strip(),
        "reflection_quality": str(
            payload.get("reflection_quality", DEFAULT_INPUT["reflection_quality"]) or DEFAULT_INPUT["reflection_quality"]
        ).strip(),
    }

    return normalized


def payload_to_frame(payload: Mapping[str, Any]):
    normalized = normalize_payload(payload)
    return pd.DataFrame([{field: normalized[field] for field in INPUT_FIELDS}])


def predict_single(system: WellbeingSupportSystem, payload: Mapping[str, Any]):
    prediction_row = system.predict(payload_to_frame(payload)).iloc[0]
    confidence = float(prediction_row["confidence"])

    return {
        "predicted_state": str(prediction_row["predicted_state"]),
        "predicted_intensity": int(prediction_row["predicted_intensity"]),
        "confidence": round(confidence, 3),
        "confidence_percent": round(confidence * 100, 1),
    }


def score_test_file(test_path, output_path, train_path=TRAIN_PATH):
    system = train_default_system(train_path)
    test_df = pd.read_excel(test_path)
    results = system.predict(test_df)

    if "id" in test_df.columns:
        results.insert(0, "id", test_df["id"].values)

    results.to_csv(output_path, index=False)
    return results
