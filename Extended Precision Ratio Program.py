"""
Term-count ratio validation across 33 argument pairs.
Computes predicted R, mean actual R, standard deviation across epsilon levels,
and percent error.
"""

import math
import numpy as np
import pandas as pd

# ------------------------------------------------------------
# 1. Function: predicted R (closed-form)
# ------------------------------------------------------------
def predicted_R(a, b):
    """Closed-form predictor for term-count ratio R(a,b)."""
    def lam(x):
        return math.log((x + 1) / (x - 1))
    return (1 / lam(a * b)) / ((1 / lam(a)) + (1 / lam(b)))


# ------------------------------------------------------------
# 2. Function: actual term count N(x, epsilon) via arctanh series
# ------------------------------------------------------------
def ln_series_term_count(x, eps, max_terms=10_000_000):
    """
    Returns the number of terms needed for the arctanh series of ln(x)
    to converge within `eps` of math.log(x).
    """
    true_val = math.log(x)
    r = (x - 1) / (x + 1)
    total = 0.0
    for i in range(1, max_terms + 1):
        k = 2 * i - 1
        total += (1 / k) * (r ** k)
        val = 2 * total
        if abs(val - true_val) <= eps:
            return i
    # If max_terms reached, warn and return max
    print(f"Warning: max_terms reached for x={x} at eps={eps}")
    return max_terms


# ------------------------------------------------------------
# 3. Function: compute actual R(a,b) across multiple epsilon levels
# ------------------------------------------------------------
def compute_actual_R(a, b, eps_list):
    """
    For each epsilon in eps_list, compute R_actual = N(ab) / (N(a) + N(b)).
    Returns (mean_R, std_R) over all epsilon levels.
    """
    ratios = []
    for eps in eps_list:
        Na = ln_series_term_count(a, eps)
        Nb = ln_series_term_count(b, eps)
        Nab = ln_series_term_count(a * b, eps)
        if Na + Nb > 0:
            ratios.append(Nab / (Na + Nb))
    return np.mean(ratios), np.std(ratios)


# ------------------------------------------------------------
# 4. Define the argument pairs (the 33 pairs from your table)
# ------------------------------------------------------------
pairs = [
    (2,3), (2,5), (2,7), (2,11), (2,13), (2,101),
    (3,5), (3,7), (3,11), (3,13), (3,17), (3,199),
    (5,7), (5,11), (5,13), (5,17), (5,19), (5,251),
    (7,11), (7,13), (7,17), (7,19), (7,23), (7,503),
    (11,13), (11,17), (11,19), (11,23),
    (13,31), (13,201),
    (17,53),
    (23,97),
    (41,137)
]

# ------------------------------------------------------------
# 5. Epsilon levels (seven orders of magnitude: 1e-3 to 1e-9)
# ------------------------------------------------------------
eps_levels = [10.0 ** (-k) for k in range(3, 10)]  # 1e-3, 1e-4, ..., 1e-9

# ------------------------------------------------------------
# 6. Compute and build table
# ------------------------------------------------------------
table_data = []
for a, b in pairs:
    pred = predicted_R(a, b)
    mean_actual, std_actual = compute_actual_R(a, b, eps_levels)
    error_pct = (mean_actual - pred) / pred * 100
    table_data.append({
        "A": a,
        "B": b,
        "Predicted R": pred,
        "Mean Actual R": mean_actual,
        "StdDev (ε)": std_actual,
        "Error %": error_pct
    })

df = pd.DataFrame(table_data)

# ------------------------------------------------------------
# 7. Display or save
# ------------------------------------------------------------
print(df.to_string(index=False, float_format="%.4f"))
# Optionally save to CSV
df.to_csv("termcount_ratio_validation.csv", index=False)
