# Error Analysis

CV metrics on `train_data.xlsx`:

| Metric | Value |
| --- | ---: |
| State accuracy | 0.4175 |
| Intensity MAE | 1.2158 |
| Intensity exact | 0.2200 |

Weakest states: restless (0.33), overwhelmed (0.36).

## Key Failure Patterns
- Short texts mislead (e.g., "hard to focus" → focused).
- Regulation words override distress (e.g., wandering mind → calm).
- High confidence on weak evidence.
- Intensity swings (1→5).

## Insights
- Penalize short/ambiguous inputs.
- Use metadata (ambience, etc.).
- Colloquial distress under-modeled.

## Next Steps
- Add categorical features.
- Calibrate confidence.
- Ordinal intensity.
- Expand lexicon.

