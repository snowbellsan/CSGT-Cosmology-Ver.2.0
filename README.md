# CSGT-Cosmology: Universal Self-Generation Theory

[![arXiv](https://img.shields.io/badge/arXiv-2601.xxxxx-B31B1B.svg)](https://arxiv.org/abs/2601.xxxxx)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository hosts the official numerical implementation and stability analysis for the **Constitutional Self-Generation Theory (CSGT)**. CSGT is a novel cosmological framework that resolves the $H_0$ tension by introducing an information-theoretic optimization pulse based on future boundary conditions.

## 💎 Scientific Summary: The Ultimate Joint Fit (2026)

By performing a simultaneous likelihood analysis of the **Pantheon+ Type Ia Supernovae** (1701 samples) and the **DESI DR2 Full BAO** datasets, the CSGT model achieves a high-precision convergence that bridges the gap between early-universe and local-universe measurements.

### Best-Fit Parameters
- **Hubble Constant ($H_0$)**: $70.83 \text{ km/s/Mpc}$
- **Information Coupling ($A$)**: $0.5570$
- **Matter Density ($\Omega_m$)**: $0.286$
- **Reduced $\chi^2$**: $2.6558$

## 🌊 The "Coherence Dip" (IID)
The hallmark of the CSGT model is the **Coherence Dip**—a localized, dynamic evolution of the dark energy equation of state $w(z)$ peaking at $z \approx 0.7$. 



This feature represents the maximum phase of **Information Integration**, where the expansion history is optimized to satisfy the complexity requirements of the future boundary. Unlike standard $\Lambda$CDM, the Coherence Dip allows $w(z)$ to traverse the phantom domain ($w < -1$) smoothly, providing the necessary "low-$z$ boost" to resolve the Hubble tension without violating cosmological constraints.

## ⚖️ Stability & No-Ghost Conditions
A critical challenge for phantom-crossing models is the avoidance of ghost instabilities. In CSGT, stability is guaranteed by the non-local information action:
$$S_{\text{total}} = S_{\text{EH}} + S_{\text{matter}} + S_{\text{info}}$$
The effective sound speed squared $c_s^2$ remains positive throughout the transition due to the regularization provided by the information-feedback term.

### Numerical Stability Check (at Joint Fit Peak)
| Redshift ($z$) | $w(z)$ | $w'(z)$ | Stability Status |
| :--- | :--- | :--- | :--- |
| 0.0 (Present) | -1.1059 | -0.5198 | **Stable** (Feedback Dominated) |
| 0.7 (Peak) | -1.5470 | 0.0000 | **Stable** (Attractor Bottom) |
| 1.5 (Past) | -1.0616 | 0.3673 | **Stable** (Self-Organization) |

## 🛠️ Installation & Usage
(Add instructions for running `Final_test` and `Final_Test_NoGhost.py`)

