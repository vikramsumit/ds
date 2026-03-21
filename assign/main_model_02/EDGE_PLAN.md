# Edge Deployment Plan

Deploy `model_02` for production. Prioritize these steps.

## Core Steps
- **WSGI Server**: Use Gunicorn for `main.py` (routes: /, /predict, /api/predict, /health).
- **Separate Training**: Train offline from `train_data.xlsx`, serialize (joblib/pickle), load at startup.
- **UI Assets**: Localize CSS/fonts (remove CDN dependency).
- **Targets**: VM (Nginx+Gunicorn), Docker (ECS/Cloud Run), edge appliance.

## Top Optimizations
1. **Pre-serialize Model**: Faster startup, no retraining.
2. **Sparse Features**: Use `scipy.sparse.hstack`, avoid `.toarray()`.
3. **Add Metadata**: OneHotEncode ambience/time/prev_mood etc. via ColumnTransformer.

## Rollout Phases
1. **Stabilize**: Serialize, Gunicorn, validation.
2. **Accuracy**: Categorical features, confidence calibration.
3. **Harden**: Local assets, monitoring, tests.

Clean UI: Remove `index1.html`, unused `classic.css` references.

