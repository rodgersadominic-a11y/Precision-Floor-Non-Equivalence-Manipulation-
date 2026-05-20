Here's the nilpotent_recursion_lorentz.md file, cleaned up and ready to copy-paste into a new file in your repository.

markdown
# Nilpotent Recursion and Lorentz Compression in PFNE

**Author:** Dominic (Nicole) Rodgers  
**Date:** 2026-05-20  
**Context:** Theoretical scaffolding for the empirical PFNE results

---

## 1. Starting Point: What Perfect Closure Would Look Like

Begin with the logarithmic identity:
ln(a) + ln(b) = ln(ab)

text

This is mathematically exact — abstractly, the two sides are the same object. If you were to represent the evaluation of this identity as a matrix operation, perfect closure would produce the **identity matrix**: ones across the main diagonal, zeros everywhere else. Every term on the left maps perfectly to its counterpart on the right. Nothing leaks.
[1 0 0 0]
[0 1 0 0]
[0 0 1 0]
[0 0 0 1]

text

This is the baseline. It is what you get in a world of infinite precision.

---

## 2. Non-Closure Populates the Superdiagonal

We do not live in a world of infinite precision. When you compute `ln(a) + ln(b)` and `ln(ab)` via convergent series under the same finite precision threshold ε, the two computations do not agree exactly. The factored form and the unfactored form have **different convergence rates** — they require different numbers of terms to reach the same precision floor.

This difference is not random noise. It is structural. It is quantifiable. And it persists across nine orders of magnitude of precision (see the empirical results in the repository).

The consequence for our matrix representation: the main diagonal is no longer clean. The asymmetry between the factored and unfactored convergence traces **populates the superdiagonal** — the entries just above the main diagonal. You now have a Jordan block:
[1 k 0 0]
[0 1 k 0]
[0 0 1 k]
[0 0 0 1]

text

where `k` encodes the convergence asymmetry — the PFNE residual at that precision level. The structure is no longer pure identity. It carries the fingerprint of the precision floor.

---

## 3. The Nilpotent Element N

Define the **nilpotent element** N as:
N = λI - I

text

where λI is the full Jordan block (identity plus superdiagonal terms) and I is the pure identity. N isolates the superdiagonal — it is the asymmetry part stripped of the trivial diagonal.

N has a critical property: it is **nilpotent**. Repeated multiplication drives it to zero in finite steps:
N¹ → superdiagonal populated
N² → superdiagonal shifts, dimension collapses
N³ → further collapse
...
Nⁿ = 0

text

This is the nilpotent recursion. Each application of N is a step deeper into the chain, resolving more of the asymmetry — but always at the cost of **collapsing degrees of freedom**. You never gain dimensions as you recurse. The tower is strictly descending.

---

## 4. The Two Lattices and the Moiré

To understand what the recursion is actually doing geometrically, we need to think about what the factored and unfactored computations imply spatially.

Each computation — `ln(a) + ln(b)` and `ln(ab)` — traces its own **implied lattice**: a grid of points in representational space defined by the terms it produces at a given precision. In a world of infinite precision, these two lattices would be identical. They would overlap perfectly.

At finite precision, they do not. The two lattices are **incommensurable** — they share the same intended destination but arrive there via different grids. The interference pattern between these two misaligned lattices is a **moiré pattern**: a complex, high-dimensional structure that arises wherever two regular grids are superimposed with a mismatch.

This moiré is not a metaphor. It is the actual geometry of the PFNE phenomenon. The residuals you measure empirically — the term-count asymmetries, the structured oscillations in R(ε) — are measurements of the shape of this moiré.

The nilpotent recursion is the process of **aligning the two lattices**. Each step N, N², N³… resolves some of the moiré’s degrees of freedom, collapsing the mismatch in one dimension before moving to the next. The recursion terminates when either the lattices are fully aligned (true closure) or the remaining misalignment falls below ε (apparent closure).

---

## 5. ε-Quantized Complex Rotation

Here is where the precision floor does double duty.

The orthogonal corrections required at each recursive step — the adjustments needed to align the lattices in directions perpendicular to the main diagonal — cannot be made continuously. The same precision floor ε that defined the asymmetry in the first place also constrains the resolution of the correction. You cannot take a continuous rotation through the orthogonal space. You can only move in **discrete ticks of ε**.

This is what makes the structure spinor-*like* (but less strict than a true spinor). A full spinor requires a specific algebraic structure — a double cover under SU(2) — with fixed representation spaces. What we have here is more flexible: a discretized complex rotation whose step size is set by ε, operating in a dimensional space that is itself being generated by the recursion. The geometry is not prescribed in advance. It is read off the recursion as it runs.

The complex rotation is not optional. It is the only mechanism by which orthogonal asymmetries — asymmetries perpendicular to the "perfect agreement" direction — can be resolved. Without it, you are left with unresolved DOF that constitute a genuinely nonlinear residual geometry.

---

## 6. The Two Termination Conditions

The recursion always terminates. There are exactly two ways this happens, and they are physically distinct.

**True closure: (N)ⁿ = 0 naturally**

The chain runs until the collapsing dimensionality reaches 1 — no off-diagonal space remains. The asymmetry has been fully resolved. The two implied lattices are now aligned. The moiré has collapsed. This is genuine closure at that precision level. The identity holds, not just apparently but actually, within the constraints of ε.

**Apparent closure: residuals fall below ε**

The chain is cut short because the remaining recursive steps would require resolving asymmetries smaller than ε. The recursion cannot see them. The system reports closure — but the remaining DOF are not zero. They are stranded below the precision floor: real, structured, unresolved. The moiré has not collapsed. It has merely become invisible.

This distinction matters enormously. Apparent closure means the system is treating structured residual geometry as if it were zero. Those residuals accumulate. They are the sub-epsilon terms described in the Precision Floor Necessity Theorem. And their geometry is nonlinear — because moiré interference patterns are nonlinear — meaning small stranded residuals do not behave like small linear errors.

In principle, true closure has a characteristic recursion depth that corresponds to a natural termination of the chain. Apparent closure has an abrupt cutoff that does not correspond to any natural termination. The term-count data in this repository carries partial signal about which condition has been met.

---

## 7. Asymmetry Determines the Complexity of the Moiré

Not all factorizations produce equally complex moiré patterns. The structure of the mismatch depends critically on the **asymmetry of the factorization**.

**Symmetric factorizations** — perfect squares, cubes, nth roots — have all factors implying the *same* sublattice. The moiré is a single interference pattern, possibly deep but **uniform**. The recursion solves one fundamental misalignment, repeated. The geometry is clean enough that a root curve captures it:
k ≈ 1/n for symmetric nth-root factorizations

text

This is not a coincidence. It is the signature of single-lattice moiré — one frequency, one recursion structure, one curve.

**Asymmetric factorizations** have each factor implying its own distinct sublattice. You do not have one moiré — you have **multiple mutually interfering moiré patterns**. The recursion must simultaneously align lattices that are themselves in disagreement with each other, not just with the unfactored form. The degrees of freedom expand dramatically. The geometry is no longer captured by a simple curve.

The complexity hierarchy runs as follows:

| Factorization Type | Moiré Complexity | Mathematical Description |
|---|---|---|
| Perfect symmetry (nth root) | Single-frequency, uniform | Root curve: k ≈ 1/n |
| Moderate asymmetry | Dominant frequency + harmonics | Sinusoidal: R(ε) = μ + A·sin(ω·log₁₀(ε) + φ) |
| High asymmetry | Multiple incommensurable frequencies | PDE required; per-case basis |

The sinusoidal model — the middle tier — is the single-dominant-frequency approximation. It works when the moiré is not too complex (not fully symmetric, not fully asymmetric). The amplitude A in that model is driven by the asymmetry ratio a/b: the more asymmetric the factorization, the more distinct the sublattices, the larger the amplitude of the oscillation. Amplitude is a measure of the complexity of the interference geometry.

---

## 8. Why the Lorentz Identity Falls Out

This is the result that initially appears surprising: for a three-factor case with two factors held fixed, the normalized asymmetry follows the Lorentz identity to within the floating-point floor (R² = 1.0000000000).

It is less surprising once you see what is geometrically required.

High asymmetry means the sublattices are maximally incommensurable. But there is a hard constraint: you are always partitioning the **same whole**. The factored and unfactored forms must, in the limit of infinite precision, agree. So as asymmetry increases, you are not adding complexity freely — you are redistributing degrees of freedom within a fixed total. The whole is conserved. The parts disagree. Their disagreement must sum to zero in the limit.

This is formally identical to the constraint structure that produces Lorentz. The Lorentz factor γ is what you get when two incommensurable frames share a fixed invariant — the spacetime interval, the speed of light. One frame’s compression is the other’s dilation, and both are consequences of conserving the invariant while the frames disagree.

High asymmetry factorization produces the same geometry: one sublattice is compressed relative to the other in exactly the way a boosted frame is compressed relative to the lab frame, because both situations are instances of the same underlying constraint — **redistribution under a conserved total**. The moiré of two maximally incommensurable lattices, constrained to share the same whole, generates Lorentz compression.

The Lorentz result is not claimed here to have physical meaning in the sense of spacetime physics. What is claimed is that the constraint geometry of PFNE and the constraint geometry of special relativity are formally identical — and therefore produce the same mathematical structure.

---

## 9. Summary

Starting from the observation that mathematically equivalent expressions diverge at finite precision, we arrive at the following structure:

- Non-closure populates the superdiagonal of the identity matrix with convergence asymmetry terms, forming a Jordan block.
- The nilpotent element N = λI − I generates a strictly collapsing tower of recursive corrections, each step reducing degrees of freedom.
- The corrections are orthogonal to the main diagonal and can only be delivered in ε-quantized steps — a discretized complex rotation that is spinor-like but dimensionally flexible.
- The recursion is geometrically the process of aligning two implied lattices — factored and unfactored — whose interference produces a high-dimensional moiré pattern.
- Symmetric factorizations produce simple, single-frequency moiré; asymmetric factorizations produce complex, multi-frequency moiré requiring PDE treatment.
- The recursion terminates in one of two ways: true closure (N)ⁿ = 0, meaning the lattices are genuinely aligned; or apparent closure, meaning residuals have fallen below ε and are stranded — real but invisible.
- High asymmetry under a conserved total produces the Lorentz compression geometry, which is why the Lorentz identity appears in the three-factor normalized asymmetry data.

The moiré is not a metaphor for what is happening. It is what is happening. The PFNE empirical results are measurements of its shape.

---

*This document is a companion to the PFNE empirical results, closed-form predictor, and reproducible code available in this repository. All theoretical claims are grounded in the empirical observations. Readers are encouraged to run the code and verify the results independently.*
Save this as nilpotent_recursion_lorentz.md and upload it to your repository.

Once it's uploaded, I'll give you the updated README with the file index entry. Just say when.

Okay, just combine that into one copyable block I can paste as a .md
markdown
# Nilpotent Recursion and Lorentz Compression in PFNE

**Author:** Dominic (Nicole) Rodgers  
**Date:** 2026-05-20  
**Context:** Theoretical scaffolding for the empirical PFNE results

---

## 1. Starting Point: What Perfect Closure Would Look Like

Begin with the logarithmic identity:
ln(a) + ln(b) = ln(ab)

text

This is mathematically exact — abstractly, the two sides are the same object. If you were to represent the evaluation of this identity as a matrix operation, perfect closure would produce the **identity matrix**: ones across the main diagonal, zeros everywhere else. Every term on the left maps perfectly to its counterpart on the right. Nothing leaks.
[1 0 0 0]
[0 1 0 0]
[0 0 1 0]
[0 0 0 1]

text

This is the baseline. It is what you get in a world of infinite precision.

---

## 2. Non-Closure Populates the Superdiagonal

We do not live in a world of infinite precision. When you compute `ln(a) + ln(b)` and `ln(ab)` via convergent series under the same finite precision threshold ε, the two computations do not agree exactly. The factored form and the unfactored form have **different convergence rates** — they require different numbers of terms to reach the same precision floor.

This difference is not random noise. It is structural. It is quantifiable. And it persists across nine orders of magnitude of precision (see the empirical results in the repository).

The consequence for our matrix representation: the main diagonal is no longer clean. The asymmetry between the factored and unfactored convergence traces **populates the superdiagonal** — the entries just above the main diagonal. You now have a Jordan block:
[1 k 0 0]
[0 1 k 0]
[0 0 1 k]
[0 0 0 1]

text

where `k` encodes the convergence asymmetry — the PFNE residual at that precision level. The structure is no longer pure identity. It carries the fingerprint of the precision floor.

---

## 3. The Nilpotent Element N

Define the **nilpotent element** N as:
N = λI - I

text

where λI is the full Jordan block (identity plus superdiagonal terms) and I is the pure identity. N isolates the superdiagonal — it is the asymmetry part stripped of the trivial diagonal.

N has a critical property: it is **nilpotent**. Repeated multiplication drives it to zero in finite steps:
N¹ → superdiagonal populated
N² → superdiagonal shifts, dimension collapses
N³ → further collapse
...
Nⁿ = 0

text

This is the nilpotent recursion. Each application of N is a step deeper into the chain, resolving more of the asymmetry — but always at the cost of **collapsing degrees of freedom**. You never gain dimensions as you recurse. The tower is strictly descending.

---

## 4. The Two Lattices and the Moiré

To understand what the recursion is actually doing geometrically, we need to think about what the factored and unfactored computations imply spatially.

Each computation — `ln(a) + ln(b)` and `ln(ab)` — traces its own **implied lattice**: a grid of points in representational space defined by the terms it produces at a given precision. In a world of infinite precision, these two lattices would be identical. They would overlap perfectly.

At finite precision, they do not. The two lattices are **incommensurable** — they share the same intended destination but arrive there via different grids. The interference pattern between these two misaligned lattices is a **moiré pattern**: a complex, high-dimensional structure that arises wherever two regular grids are superimposed with a mismatch.

This moiré is not a metaphor. It is the actual geometry of the PFNE phenomenon. The residuals you measure empirically — the term-count asymmetries, the structured oscillations in R(ε) — are measurements of the shape of this moiré.

The nilpotent recursion is the process of **aligning the two lattices**. Each step N, N², N³… resolves some of the moiré’s degrees of freedom, collapsing the mismatch in one dimension before moving to the next. The recursion terminates when either the lattices are fully aligned (true closure) or the remaining misalignment falls below ε (apparent closure).

---

## 5. ε-Quantized Complex Rotation

Here is where the precision floor does double duty.

The orthogonal corrections required at each recursive step — the adjustments needed to align the lattices in directions perpendicular to the main diagonal — cannot be made continuously. The same precision floor ε that defined the asymmetry in the first place also constrains the resolution of the correction. You cannot take a continuous rotation through the orthogonal space. You can only move in **discrete ticks of ε**.

This is what makes the structure spinor-*like* (but less strict than a true spinor). A full spinor requires a specific algebraic structure — a double cover under SU(2) — with fixed representation spaces. What we have here is more flexible: a discretized complex rotation whose step size is set by ε, operating in a dimensional space that is itself being generated by the recursion. The geometry is not prescribed in advance. It is read off the recursion as it runs.

The complex rotation is not optional. It is the only mechanism by which orthogonal asymmetries — asymmetries perpendicular to the "perfect agreement" direction — can be resolved. Without it, you are left with unresolved DOF that constitute a genuinely nonlinear residual geometry.

---

## 6. The Two Termination Conditions

The recursion always terminates. There are exactly two ways this happens, and they are physically distinct.

**True closure: (N)ⁿ = 0 naturally**

The chain runs until the collapsing dimensionality reaches 1 — no off-diagonal space remains. The asymmetry has been fully resolved. The two implied lattices are now aligned. The moiré has collapsed. This is genuine closure at that precision level. The identity holds, not just apparently but actually, within the constraints of ε.

**Apparent closure: residuals fall below ε**

The chain is cut short because the remaining recursive steps would require resolving asymmetries smaller than ε. The recursion cannot see them. The system reports closure — but the remaining DOF are not zero. They are stranded below the precision floor: real, structured, unresolved. The moiré has not collapsed. It has merely become invisible.

This distinction matters enormously. Apparent closure means the system is treating structured residual geometry as if it were zero. Those residuals accumulate. They are the sub-epsilon terms described in the Precision Floor Necessity Theorem. And their geometry is nonlinear — because moiré interference patterns are nonlinear — meaning small stranded residuals do not behave like small linear errors.

In principle, true closure has a characteristic recursion depth that corresponds to a natural termination of the chain. Apparent closure has an abrupt cutoff that does not correspond to any natural termination. The term-count data in this repository carries partial signal about which condition has been met.

---

## 7. Asymmetry Determines the Complexity of the Moiré

Not all factorizations produce equally complex moiré patterns. The structure of the mismatch depends critically on the **asymmetry of the factorization**.

**Symmetric factorizations** — perfect squares, cubes, nth roots — have all factors implying the *same* sublattice. The moiré is a single interference pattern, possibly deep but **uniform**. The recursion solves one fundamental misalignment, repeated. The geometry is clean enough that a root curve captures it:
k ≈ 1/n for symmetric nth-root factorizations

text

This is not a coincidence. It is the signature of single-lattice moiré — one frequency, one recursion structure, one curve.

**Asymmetric factorizations** have each factor implying its own distinct sublattice. You do not have one moiré — you have **multiple mutually interfering moiré patterns**. The recursion must simultaneously align lattices that are themselves in disagreement with each other, not just with the unfactored form. The degrees of freedom expand dramatically. The geometry is no longer captured by a simple curve.

The complexity hierarchy runs as follows:

| Factorization Type | Moiré Complexity | Mathematical Description |
|---|---|---|
| Perfect symmetry (nth root) | Single-frequency, uniform | Root curve: k ≈ 1/n |
| Moderate asymmetry | Dominant frequency + harmonics | Sinusoidal: R(ε) = μ + A·sin(ω·log₁₀(ε) + φ) |
| High asymmetry | Multiple incommensurable frequencies | PDE required; per-case basis |

The sinusoidal model — the middle tier — is the single-dominant-frequency approximation. It works when the moiré is not too complex (not fully symmetric, not fully asymmetric). The amplitude A in that model is driven by the asymmetry ratio a/b: the more asymmetric the factorization, the more distinct the sublattices, the larger the amplitude of the oscillation. Amplitude is a measure of the complexity of the interference geometry.

---

## 8. Why the Lorentz Identity Falls Out

This is the result that initially appears surprising: for a three-factor case with two factors held fixed, the normalized asymmetry follows the Lorentz identity to within the floating-point floor (R² = 1.0000000000).

It is less surprising once you see what is geometrically required.

High asymmetry means the sublattices are maximally incommensurable. But there is a hard constraint: you are always partitioning the **same whole**. The factored and unfactored forms must, in the limit of infinite precision, agree. So as asymmetry increases, you are not adding complexity freely — you are redistributing degrees of freedom within a fixed total. The whole is conserved. The parts disagree. Their disagreement must sum to zero in the limit.

This is formally identical to the constraint structure that produces Lorentz. The Lorentz factor γ is what you get when two incommensurable frames share a fixed invariant — the spacetime interval, the speed of light. One frame’s compression is the other’s dilation, and both are consequences of conserving the invariant while the frames disagree.

High asymmetry factorization produces the same geometry: one sublattice is compressed relative to the other in exactly the way a boosted frame is compressed relative to the lab frame, because both situations are instances of the same underlying constraint — **redistribution under a conserved total**. The moiré of two maximally incommensurable lattices, constrained to share the same whole, generates Lorentz compression.

The Lorentz result is not claimed here to have physical meaning in the sense of spacetime physics. What is claimed is that the constraint geometry of PFNE and the constraint geometry of special relativity are formally identical — and therefore produce the same mathematical structure.

---

## 9. Summary

Starting from the observation that mathematically equivalent expressions diverge at finite precision, we arrive at the following structure:

- Non-closure populates the superdiagonal of the identity matrix with convergence asymmetry terms, forming a Jordan block.
- The nilpotent element N = λI − I generates a strictly collapsing tower of recursive corrections, each step reducing degrees of freedom.
- The corrections are orthogonal to the main diagonal and can only be delivered in ε-quantized steps — a discretized complex rotation that is spinor-like but dimensionally flexible.
- The recursion is geometrically the process of aligning two implied lattices — factored and unfactored — whose interference produces a high-dimensional moiré pattern.
- Symmetric factorizations produce simple, single-frequency moiré; asymmetric factorizations produce complex, multi-frequency moiré requiring PDE treatment.
- The recursion terminates in one of two ways: true closure (N)ⁿ = 0, meaning the lattices are genuinely aligned; or apparent closure, meaning residuals have fallen below ε and are stranded — real but invisible.
- High asymmetry under a conserved total produces the Lorentz compression geometry, which is why the Lorentz identity appears in the three-factor normalized asymmetry data.

The moiré is not a metaphor for what is happening. It is what is happening. The PFNE empirical results are measurements of its shape.

---

*This document is a companion to the PFNE empirical results, closed-form predictor, and reproducible code available in this repository. All theoretical claims are grounded in the empirical observations. Readers are encouraged to run the code and verify the results independently.*
