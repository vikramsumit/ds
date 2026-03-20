# Edge Deployment Plan

This document outlines how to deploy `model_02` beyond local development and what to optimize first.

## Deployment Approach

### 1. Package the Flask App as the Serving Layer

The current serving entry point is `main.py`, which already exposes:

- `GET /`
- `POST /predict`
- `POST /api/predict`
- `GET /health`

For production, the Flask app should be served through a WSGI server such as `gunicorn` instead of Flask's built-in development server.

Recommended shape:

1. Build a container image for `model_02`
2. Install dependencies from `requirements.txt`
3. Expose the Flask app through `gunicorn`
4. Put it behind Nginx, a load balancer, or a platform ingress
5. Use `/health` for startup and readiness checks

### 2. Separate Training from Inference

Right now the model is trained lazily on first prediction request through `lru_cache`. That is acceptable for local use, but not ideal for production because:

- the first real request is slow
- every restart retrains the model
- inference behavior depends on startup timing

Better production flow:

1. Train offline from `train_data.xlsx`
2. Serialize the fitted vectorizer, label encoder, and ensemble models
3. Load those artifacts at startup
4. Keep the API process focused on inference only

### 3. Decide on Asset Strategy for the UI

The active `templates/index.html` currently pulls:

- Tailwind from CDN
- Google Fonts from CDN

That is convenient for development, but risky for edge or offline-style deployments because styling now depends on third-party network access.

For production, pick one of these approaches:

- keep CDN assets and accept the external dependency
- compile the UI styles locally and serve everything from the Flask app

The second option is more reliable and better aligned with the rest of this project, which is otherwise local-first.

### 4. Deployment Environments

Reasonable targets:

- a small VM with Nginx + Gunicorn
- Docker on ECS, Cloud Run, Fly.io, or Render
- an internal edge appliance if the goal is private/local wellbeing tooling

For edge-style or privacy-sensitive deployments, prefer:

- local artifact loading
- no external font/CDN dependency
- filesystem or object-store based model versioning

## Optimizations

### 1. Pre-serialize the Fitted Model

Highest-value optimization:

- train once
- save with `joblib` or `pickle`
- load directly in the Flask process

Benefits:

- faster cold start
- predictable startup time
- no repeated training cost

### 2. Keep Features Sparse

The current code calls `text_features.toarray()` and then `np.hstack(...)`. That densifies the TF-IDF matrix.

Why this matters:

- unnecessary memory growth
- slower training and inference at scale

Better approach:

- keep the text matrix sparse
- use `scipy.sparse.hstack` for numeric features
- train models directly on the sparse representation when supported

### 3. Use the Metadata Already Collected

The UI/API already accept:

- ambience type
- time of day
- previous day mood
- face emotion hint
- reflection quality

But the current model ignores them. Adding one-hot encoded categorical features is one of the clearest accuracy opportunities.

Recommended implementation:

- `ColumnTransformer`
- `OneHotEncoder(handle_unknown="ignore")`
- merge categorical, numeric, and text features into a single reproducible pipeline

### 4. Improve Confidence Estimation

Current confidence is only vote share across the bootstrap classifiers. That creates visibly overconfident mistakes on short inputs.

Better options:

- penalize very short journal entries
- lower confidence when text contains both regulation and activation cues
- incorporate class probability margin, not just hard votes
- calibrate confidence using a held-out validation set

### 5. Revisit the Intensity Model

The intensity head has a relatively weak exact accuracy. It is often within one level, but exact scoring is poor.

Promising alternatives:

- ordinal classification instead of regression
- gradient boosting regressors with tighter tuning
- a smaller, faster baseline like ridge regression for stability checks

### 6. Add Input Validation and Observability

Before deployment, add:

- structured request validation
- request logging
- latency metrics
- prediction counters by endpoint
- error-rate tracking

Useful signals:

- average inference time
- cold-start time
- API validation failures
- proportion of short-text predictions
- distribution shift in journal length and numeric inputs

### 7. Clean Up the UI Path

The folder currently has:

- an active `index.html`
- an archived `index1.html`
- a local `classic.css` that is not used by the active template

Before production, choose one UI path and remove the dead branch. That reduces maintenance overhead and avoids confusion about which interface is the real deployed version.

## Recommended Rollout Order

### Phase 1: Stabilize

- serialize trained artifacts
- switch to Gunicorn
- add structured validation
- keep current model behavior

### Phase 2: Improve Accuracy

- add categorical features
- recalibrate confidence
- improve the intensity head

### Phase 3: Harden for Production

- localize CSS/fonts
- add monitoring
- add automated regression tests for known failure cases
- version model artifacts and document rollback steps
