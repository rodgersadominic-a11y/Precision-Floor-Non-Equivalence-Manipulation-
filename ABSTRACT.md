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

- `seed.txt` — Proof of existence, timestamped
- `lorentz_test.md` — Full Lorentz correspondence data
- `term_count_ratios.md` — 33-pair validation
- `nilpotent_framework.md` — Algebraic interpretation
- `blueprint.md` — Engineering implications

## Status

Preliminary disclosure. Full paper in preparation.