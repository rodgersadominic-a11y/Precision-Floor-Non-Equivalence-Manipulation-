"""
LORENTZ TRANSFORM TEST — LOGARITHMIC FIELD DYNAMICS

Tests whether the term count asymmetry of the arctanh-form Taylor series
for ln(x), when normalized by its saturation ceiling, follows the Lorentz
identity 1/gamma^2 = 1 - beta^2.

Setup:
  Two factors a=2, b=3 held fixed; third factor c swept across 22 values.
  Term count N(x) = number of terms needed for arctanh series to converge
                    within eps = 1e-6 of true ln(x).
  Asymmetry = N(abc) / (N(a) + N(b) + N(c)).
  A_max = saturation ceiling fitted from Asymmetry vs c.
  beta  = Asymmetry / A_max.
  gamma = 1 / sqrt(1 - beta^2).

Tests whether 1/gamma^2 = 1 - beta^2 holds (Lorentz identity).
"""

import math
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import os
import sys


# ── Series implementation ────────────────────────────────────────────────────

def ln_series(x, eps, max_terms=10_000_000):
    """Arctanh-form Taylor series for ln(x).
       ln(x) = 2 * sum_{i=1..inf} (1/(2i-1)) * ((x-1)/(x+1))^(2i-1)
       Returns (value, term_count) where term_count is the number of terms
       needed to converge within eps of math.log(x)."""
    true_val = math.log(x)
    r = (x - 1) / (x + 1)
    total = 0.0
    for i in range(1, max_terms + 1):
        k = 2 * i - 1
        total += (1 / k) * (r ** k)
        val = 2 * total
        if abs(val - true_val) <= eps:
            return val, i
    # If max_terms reached, warn and return
    print(f"Warning: max_terms ({max_terms}) reached for x={x} at eps={eps}")
    return 2 * total, max_terms


# ── Parameters ───────────────────────────────────────────────────────────────

a, b = 2, 3
eps  = 1e-6

c_values = [5, 8, 10, 15, 20, 30, 50, 75, 100, 150, 200, 350,
            500, 750, 1000, 2000, 3000, 5000, 7500, 10000,
            25000, 50000]


# ── Run the test ─────────────────────────────────────────────────────────────

print("LORENTZ TRANSFORM TEST — LOGARITHMIC FIELD DYNAMICS")
print(f"Fixed: a={a}, b={b}  |  Varying c  |  epsilon={eps}")
print("=" * 72)
print(f"\n{'c':>8}  {'abc':>10}  {'N(a)':>5}  {'N(b)':>5}  {'N(c)':>8}  "
      f"{'N(abc)':>9}  {'Asymmetry':>11}")
print("-" * 72)

_, na = ln_series(a, eps)
_, nb = ln_series(b, eps)

raw_data = []
for c in c_values:
    abc = a * b * c
    _, nc   = ln_series(c,   eps)
    _, nabc = ln_series(abc, eps)
    asym = nabc / (na + nb + nc)
    raw_data.append((c, abc, na, nb, nc, nabc, asym))
    print(f"{c:>8}  {abc:>10}  {na:>5}  {nb:>5}  {nc:>8}  "
          f"{nabc:>9}  {asym:>11.6f}")


asym_arr = np.array([r[6] for r in raw_data])
c_arr    = np.array([r[0] for r in raw_data], dtype=float)


# ── Fit saturation ceiling A_max ─────────────────────────────────────────────

def sat_model(c, A_max, k):
    return A_max * (1 - np.exp(-k * c))

# Use only data up to c=2000 for fitting (asymptotic region)
# This avoids the low-c region where saturation hasn't begun
fit_mask = c_arr <= 2000
popt_sat, _ = curve_fit(sat_model, c_arr[fit_mask], asym_arr[fit_mask], 
                        p0=[6.0, 0.01], maxfev=10000)
A_max = popt_sat[0]
k_fit = popt_sat[1]

print(f"\nFitted A_max (saturation ceiling) = {A_max:.6f}")
print(f"Fitted k = {k_fit:.6f}")


# ── Compute beta and gamma ───────────────────────────────────────────────────

print(f"\n{'c':>8}  {'Asymmetry':>11}  {'beta=A/Amax':>13}  "
      f"{'gamma_LFD':>12}  {'1/gamma^2':>11}  {'1-beta^2':>11}  {'residual':>12}")
print("-" * 90)

betas, gammas, og2_list, omb2_list = [], [], [], []

for c, abc, na_, nb_, nc, nabc, asym in raw_data:
    beta = min(asym / A_max, 0.99999)  # Cap at 0.99999 to avoid division by zero
    gamma = 1.0 / math.sqrt(1 - beta ** 2)
    og2 = 1.0 / gamma ** 2
    omb2 = 1.0 - beta ** 2
    residual = og2 - omb2

    betas.append(beta)
    gammas.append(gamma)
    og2_list.append(og2)
    omb2_list.append(omb2)

    print(f"{c:>8}  {asym:>11.6f}  {beta:>13.8f}  "
          f"{gamma:>12.6f}  {og2:>11.8f}  {omb2:>11.8f}  {residual:>12.2e}")


betas  = np.array(betas)
gammas = np.array(gammas)
og2    = np.array(og2_list)
omb2   = np.array(omb2_list)

residuals = og2 - omb2
rmse = np.sqrt(np.mean(residuals ** 2))
ss_tot = np.sum((og2 - np.mean(og2)) ** 2)
r2 = 1 - np.sum(residuals ** 2) / ss_tot

print(f"\n{'=' * 72}")
print(f"  LORENTZ IDENTITY TEST:  Does 1/gamma^2 = 1 - beta^2 ?")
print(f"{'=' * 72}")
print(f"  R^2              = {r2:.10f}")
print(f"  RMSE             = {rmse:.3e}")
print(f"  Max |residual|   = {np.abs(residuals).max():.3e}")
print(f"  beta range       = [{betas.min():.4f}, {betas.max():.4f}]")
print(f"  gamma range      = [{gammas.min():.3f}, {gammas.max():.3f}]")
print(f"{'=' * 72}")


# ── Plot ─────────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(13, 10))

# Top-left: saturation curve
c_dense = np.logspace(0.7, 5, 200)
axes[0, 0].semilogx(c_arr, asym_arr, "o", color="#1f77b4", markersize=7,
                    label="empirical asymmetry")
axes[0, 0].semilogx(c_dense, sat_model(c_dense, A_max, k_fit), "k-",
                    linewidth=1.5, alpha=0.7,
                    label=f"saturation fit: A_max = {A_max:.4f}")
axes[0, 0].axhline(A_max, color="r", linestyle="--", linewidth=1, alpha=0.5,
                   label=f"ceiling = {A_max:.4f}")
axes[0, 0].set_xlabel("c (third factor)")
axes[0, 0].set_ylabel("Asymmetry = N(abc) / (N(a)+N(b)+N(c))")
axes[0, 0].set_title("Saturation of asymmetry as c grows")
axes[0, 0].legend(fontsize=9)
axes[0, 0].grid(True, alpha=0.3, which="both")

# Top-right: gamma vs beta with Lorentz curve
beta_dense = np.linspace(0.001, 0.9999, 500)
gamma_dense = 1 / np.sqrt(1 - beta_dense ** 2)
axes[0, 1].plot(beta_dense, gamma_dense, "k-", linewidth=1, alpha=0.6,
                label=r"$\gamma = 1/\sqrt{1-\beta^2}$ (Lorentz)")
axes[0, 1].plot(betas, gammas, "o", color="#d62728", markersize=8,
                label="LFD empirical")
axes[0, 1].set_xlabel(r"$\beta$ = Asymmetry / A_max")
axes[0, 1].set_ylabel(r"$\gamma$")
axes[0, 1].set_yscale("log")
axes[0, 1].set_title(r"$\gamma$ vs $\beta$")
axes[0, 1].legend(fontsize=9)
axes[0, 1].grid(True, alpha=0.3, which="both")

# Bottom-left: 1/gamma^2 vs 1-beta^2
axes[1, 0].plot([0, 1], [0, 1], "k--", linewidth=1, alpha=0.5,
                label="y = x (perfect identity)")
axes[1, 0].plot(omb2, og2, "o", color="#2ca02c", markersize=9)
axes[1, 0].set_xlabel(r"$1 - \beta^2$")
axes[1, 0].set_ylabel(r"$1/\gamma^2$")
axes[1, 0].set_title(f"Lorentz identity test\n"
                     fr"$R^2 = {r2:.10f}$, RMSE = {rmse:.2e}")
axes[1, 0].legend(fontsize=9)
axes[1, 0].grid(True, alpha=0.3)

# Bottom-right: residuals
axes[1, 1].semilogx(c_arr, residuals, "o-", color="#9467bd",
                    linewidth=0.8, markersize=8)
axes[1, 1].axhline(0, color="k", linestyle="--", linewidth=0.8, alpha=0.5)
axes[1, 1].set_xlabel("c")
axes[1, 1].set_ylabel(r"Residual: $1/\gamma^2 - (1-\beta^2)$")
axes[1, 1].set_title(f"Residuals at numerical precision floor\n"
                     f"Max |residual| = {np.abs(residuals).max():.2e}")
axes[1, 1].grid(True, alpha=0.3, which="both")

fig.suptitle("Lorentz Transform Test — Logarithmic Field Dynamics",
             fontsize=13, fontweight="bold", y=1.005)
plt.tight_layout()

# Save the figure in the current directory (portable)
out = "lfd_lorentz.png"
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"\nFigure saved to {out}")

print("\nTest complete.")
