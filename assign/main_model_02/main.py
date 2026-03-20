from __future__ import annotations

import argparse
from functools import lru_cache
from pathlib import Path

from flask import Flask, jsonify, render_template, request

try:
    from predictor import (
        DEFAULT_INPUT,
        TRAIN_PATH,
        get_form_options,
        load_training_dataframe,
        normalize_payload,
        predict_single,
        score_test_file,
        train_default_system,
    )
except ImportError:
    from .predictor import (
        DEFAULT_INPUT,
        TRAIN_PATH,
        get_form_options,
        load_training_dataframe,
        normalize_payload,
        predict_single,
        score_test_file,
        train_default_system,
    )


ROOT = Path(__file__).resolve().parent


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")

    @lru_cache(maxsize=1)
    def get_system():
        return train_default_system(TRAIN_PATH)

    @lru_cache(maxsize=1)
    def get_options():
        return get_form_options(load_training_dataframe(TRAIN_PATH))

    def render_home(form_values=None, prediction=None, error_message=None, status_code=200):
        values = DEFAULT_INPUT.copy()
        if form_values:
            values.update(form_values)

        return (
            render_template(
                "index.html",
                form_values=values,
                prediction=prediction,
                error_message=error_message,
                options=get_options(),
            ),
            status_code,
        )

    @app.get("/")
    def home():
        return render_home()

    @app.post("/predict")
    def predict_from_form():
        raw_form = request.form.to_dict()

        try:
            normalized = normalize_payload(raw_form)
            prediction = predict_single(get_system(), normalized)
        except ValueError as exc:
            return render_home(form_values=raw_form, error_message=str(exc), status_code=400)

        return render_home(form_values=normalized, prediction=prediction)

    @app.post("/api/predict")
    def predict_from_api():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Send a JSON object in the request body."}), 400

        try:
            normalized = normalize_payload(payload)
            prediction = predict_single(get_system(), normalized)
        except ValueError as exc:
            return jsonify({"error": str(exc)}), 400

        return jsonify(
            {
                "input": normalized,
                "prediction": prediction,
            }
        )

    @app.get("/health")
    def health():
        system = get_system()
        return jsonify(
            {
                "status": "ok",
                "bootstrap_models": len(system.state_models),
                "train_file": str(TRAIN_PATH),
            }
        )

    return app


def parse_args():
    parser = argparse.ArgumentParser(description="Serve the wellbeing predictor with a classic Flask UI.")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface for the Flask server.")
    parser.add_argument("--port", type=int, default=5000, help="Port for the Flask server.")
    parser.add_argument("--debug", action="store_true", help="Enable Flask debug mode.")
    parser.add_argument(
        "--test-export",
        default="",
        help="Optional Excel file to score and export as CSV, then exit.",
    )
    parser.add_argument(
        "--output",
        default=str(ROOT / "predictions.csv"),
        help="CSV path used with --test-export.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.test_export:
        results = score_test_file(args.test_export, args.output, TRAIN_PATH)
        print(results.head().to_string(index=False))
        print(f"\nSaved predictions to {Path(args.output).resolve()}")
        return

    app = create_app()
    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
