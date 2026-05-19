# Precision-Floor Non-Equivalence Manipulation (PFNE)

## Summary

When computing ln(a), ln(b), and ln(ab) via the arctanh series to a common precision threshold ε, the ratio of term counts

\[
R(a,b,\varepsilon) = \frac{N(ab,\varepsilon)}{N(a,\varepsilon) + N(b,\varepsilon)}
\]

is stable across nine orders of magnitude of ε (1e-2 to 1e-10). The ratio depends only on a and b, not on ε.

## Key Result

For fixed a=2, b=3 and varying c, the normalized asymmetry follows the Lorentz identity:

\[
R^2 = 1.0000000000, \quad \text{RMSE} = 3.13 \times 10^{-17}
\]

## Reproducibility

All results can be reproduced with standard Python (code provided).

## Documents

## Repository Contents

| File | Description |
|------|-------------|
| `ABSTRACT.md` | High-level summary of PFNE |
| `Closed Form Predictor.txt` | Derivation of the precision-invariant ratio formula |
| `Desmos assumed equivalence failure mode.jpeg` | Visual intuition (not evidence) from early Desmos exploration |
| `Extended Precision Ratio Program.py` | Additional term-count ratio tests |
| `Lorentz Connection Visualized.png` | Four-panel figure showing the Lorentz identity (R² = 1) |
| `Program Listing for Precision2e.py` | Core term-count ratio program (a=13, b=31, varying ε) |
| `Python Non-Equivalence Visualization.png` | Visual intuition from early Python outputs |
| `Python Residual Feedback Visualization.png` | Visual intuition for residual propagation |
| `README.md` | This file |
| `Risk Assessment in AI Systems.txt` | Cautious, non-terrifying discussion of PFNE risks for AI |
| `Table of precision invariance results against predictor.png` | Validation table for 33 argument pairs |
| `license.txt` | CC BY-NC 4.0 open license |
| `lorentz_connection_program.py` | Full Lorentz test code (a=2, b=3, varying c) |
| `requirements.txt` | Python dependencies (numpy, scipy, matplotlib, pandas) |
| `seed.txt` | Timestamped proof of existence |
| `termcount_ratio_invariance_results.md` | Raw term-count data for (7,19,31) across ε levels |

## Status

Preliminary disclosure. Full paper in preparation.