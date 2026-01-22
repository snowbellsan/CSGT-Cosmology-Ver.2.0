# CSGT Cosmology  
**Cosmic Self-Generating Theory (CSGT)**  
*A Unified Information-Theoretic Resolution of Cosmological Tensions*

---

## Overview

Cosmic Self-Generating Theory (CSGT) is an information-theoretic cosmological
framework in which the universe is modeled as a self-optimizing dynamical
system.  
Rather than treating cosmological parameters as static inputs, CSGT introduces
a conserved informational functional that dynamically constrains the cosmic
expansion history.

This approach naturally yields a late-time attractor solution that resolves
the long-standing **H₀ tension** and related observational inconsistencies,
while remaining consistent with standard cosmological datasets.

---

## Core Idea

At the heart of CSGT lies a conserved functional:

\[
\frac{d\mathcal{F}}{dt} = 0
\]

where \(\mathcal{F}\) encodes global information coherence of the universe.
This conservation law induces a nonlinear dynamical equation for the Hubble
parameter \(H(z)\).

The cosmic expansion is therefore not arbitrary, but evolves toward a
self-selected attractor that minimizes informational inconsistency.

---

## Key Results

- **Unique late-time attractor**
  - Redshift: \( z \approx 0.7 \)
  - Hubble constant:  
    \( H_0 \approx 73 \ \mathrm{km\,s^{-1}\,Mpc^{-1}} \)

- **Natural resolution of the H₀ tension**
  - No ad-hoc dark energy modifications
  - No dataset-dependent parameter tuning

- **Dynamical stability**
  - The attractor is stable under perturbations of \(H(z)\)
  - Competing fixed points are unstable or transient

---

## Relation to Standard Cosmology

CSGT is compatible with ΛCDM at early times and large scales, while introducing
a late-time informational correction that becomes dynamically relevant near
\(z \sim 1\).

This allows CSGT to:
- Preserve the empirical success of ΛCDM
- Explain why late-time measurements prefer higher \(H_0\) values
- Avoid introducing new fundamental fields

---

## Repository Contents

- `CSGT_TensionResolution.py`  
  Numerical integration and phase-flow analysis of the CSGT evolution equation

- `data/`  
  Observational datasets (Pantheon+, BAO, etc.)

- `image/`  
  Phase portraits, residual plots, and attractor diagrams

- `doccument/`  
  LaTeX sources for theorems and analytical derivations

---

## Current Status

- Analytical attractor theorems established (Theorem 1.x series)
- Numerical stability verified
- Visualization of phase structure completed

Work in progress:
- Full derivation of the minimal functional basis of \(\mathcal{F}\)
- Gauge redundancy analysis
- Extension to structure growth (S₈ tension)

---

## Philosophy (Optional Reading)

CSGT treats the universe as a system that evolves toward **informational
self-consistency**.  
In this view, cosmic acceleration is not driven by an external component, but
emerges as the universe selects expansion histories that preserve global
coherence.

---

## Citation

If you use or discuss this work, please cite as:

> Jack et al., *Cosmic Self-Generating Theory (CSGT):  
> An Information-Theoretic Resolution of Cosmological Tensions*, 2026.

(arXiv submission in preparation)

---

## Contact

Questions, discussions, and constructive skepticism are welcome.

---

*This universe does not merely expand — it optimizes itself.*
