# Abstract

**Precision-Floor Non-Equivalence Manipulation (PFNE)** describes a structural phenomenon in finite-precision arithmetic: mathematically equivalent expressions — such as `ln(a) + ln(b)` and `ln(ab)` — produce systematically different execution traces when computed via convergent series. This difference is not random noise. It is structured, quantifiable, and persists across nine orders of magnitude of precision.

This repository presents empirical evidence, closed-form predictors, and reproducible code demonstrating:

- **Term-count ratio invariance** – The ratio \( R(a,b) = N(ab) / (N(a) + N(b)) \) depends only on \(a\) and \(b\), not on the precision threshold \(\varepsilon\).
- **Lorentz correspondence** – For three factors with two held fixed, the normalized asymmetry follows the Lorentz identity \( 1/\gamma^2 = 1 - \beta^2 \) to within the floating-point floor (\(R^2 = 1.0000000000\)).
- **Nilpotent algebraic structure** – Symmetry breaking at the precision floor generates Jordan chains, superdiagonal terms, and spinor-like objects requiring complex rotation for resolution.
- **Engineering implications** – A cautious risk assessment for AI systems, including architectural mitigations and a blueprint for residual memory encoding.

All results are reproducible. Code, raw data, and visual intuition are provided.

**Keywords:** finite-precision arithmetic, term-count invariance, Lorentz transform, nilpotent algebra, AI risk, residual channels
