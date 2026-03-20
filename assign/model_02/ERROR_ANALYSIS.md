# Error Analysis

This document summarizes failure patterns from a 5-fold stratified cross-validation run on `train_data.xlsx` using the current `WellbeingSupportSystem` implementation.

## Summary

Overall metrics from the analysis run:

| Metric | Value |
| --- | ---: |
| State accuracy | 0.4175 |
| State macro F1 | 0.4158 |
| Intensity MAE | 1.2158 |
| Intensity exact accuracy | 0.2200 |
| Intensity within-one accuracy | 0.6158 |

Weakest state recalls:

- `restless`: 0.3254
- `overwhelmed`: 0.3632
- `focused`: 0.3938

Stronger state recalls:

- `calm`: 0.5139
- `mixed`: 0.4817

## 10 Failure Cases

The cases below were selected from the same cross-validation run because they illustrate the main failure modes of the current model.

| ID | True State -> Predicted State | True Intensity -> Predicted Intensity | Confidence | Journal Snippet | Likely Failure Cause |
| --- | --- | --- | ---: | --- | --- |
| 504 | calm -> neutral | 1 -> 5 | 0.60 | `Honestly felt lighter, not fully though.` | Very short text plus a conflict cue (`though`) leaves too little signal, and intensity swings wildly upward. |
| 910 | overwhelmed -> focused | 1 -> 4 | 1.00 | `hard to focus` | Extremely short text contains the token `focus`, which likely outweighs the negative phrasing. |
| 1007 | mixed -> focused | 1 -> 4 | 1.00 | `started off split between calm and tension, but i had to restart once.` | Mixed and contradictory signals are collapsed into a cleaner, action-oriented label. |
| 602 | restless -> calm | 1 -> 4 | 1.00 | `breathing slowed down` | Regulation language dominates even though the gold label says the person remained restless. |
| 783 | neutral -> calm | 1 -> 4 | 1.00 | `a little lighter` | Mild positive wording is pushed all the way into `calm`, and intensity is overstated. |
| 221 | restless -> calm | 5 -> 2 | 0.80 | `during the session my mind kept wandering and i tried to notice it.` | The reflective ending sounds regulated, so the model underweights the wandering/restless part. |
| 551 | overwhelmed -> calm | 5 -> 2 | 0.80 | `I guess mind was all over the place.` | Colloquial wording like `all over the place` is not explicitly captured by the activation regex list. |
| 828 | overwhelmed -> neutral | 1 -> 4 | 0.80 | `lowkey felt mentally flooded, but forest sounds worked for a bit.` | Slang plus contrastive phrasing leads to a softer label than the true one. |
| 260 | restless -> overwhelmed | 1 -> 4 | 0.80 | `At one point I couldn't sit still mentally which surprised me.` | High-activation language is detected, but the model confuses `restless` with the stronger `overwhelmed` class. |
| 677 | neutral -> calm | 5 -> 2 | 0.80 | `okay session ...` | Minimal, vague text gives the ensemble almost nothing to anchor on, yet confidence remains fairly high. |

## Insights

### 1. Short texts are dangerous

Entries such as `hard to focus`, `a little lighter`, and `okay session ...` are consistently hard for the model. With so little context, single keywords dominate the decision.

### 2. Confidence is optimistic on weak evidence

Several wrong predictions above still have `0.8` to `1.0` confidence. The current confidence estimate is just ensemble vote share, so it can overstate certainty when every bootstrap model latches onto the same misleading token.

### 3. Regulation words can overpower the real label

Words or phrases like `calm`, `lighter`, `breathing slowed down`, and other settling cues can pull predictions toward `calm` even when the labeled state is `restless`, `neutral`, or `overwhelmed`.

### 4. Intensity is unstable

The largest misses are not subtle. The model sometimes predicts `1 -> 4`, `1 -> 5`, or `5 -> 2`. That suggests the current intensity regressor is not capturing ordinal severity reliably enough.

### 5. Colloquial and implied distress are under-modeled

Phrases like `all over the place`, `lowkey`, and `mentally flooded` do not line up cleanly with the handcrafted activation lexicon, so the classifier misses some real distress patterns.

### 6. `Restless` and `overwhelmed` are the hardest states

This shows up both in recall and in the examples. The model often either softens them to `calm` or `neutral`, or escalates them incorrectly into each other.

### 7. The app collects metadata that the model does not use

The UI and API accept:

- `ambience_type`
- `time_of_day`
- `previous_day_mood`
- `face_emotion_hint`
- `reflection_quality`

But the current feature builder uses only journal text and numeric signals. That leaves useful context on the table and likely hurts borderline cases.

## Practical Next Steps

- add categorical encoders for the currently ignored metadata fields
- calibrate or redesign confidence so short texts are penalized
- treat intensity as a true ordinal problem instead of plain regression
- expand the lexicon with colloquial distress phrases and negation-aware patterns
- add explicit tests for short, contradictory, and slang-heavy inputs
