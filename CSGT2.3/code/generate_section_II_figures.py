"""
Generate figures for CSGT Section II: Mathematical Necessity of C→1

This script creates four key figures demonstrating the mathematical
inevitability of the C→1 limit in Cosmic Self-Generating Theory.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# Set publication-quality parameters
rc('font', size=11, family='serif')
rc('text', usetex=False)  # Set to True if LaTeX is available
plt.rcParams['figure.dpi'] = 150

# Create output directory
import os
os.makedirs('figures', exist_ok=True)

# ===================================================================
# Figure 1: Logistic Evolution C(t) for Different Initial Conditions
# ===================================================================

def plot_logistic_evolution():
    """Plot C(t) = 1/(1 + A*exp(-κt)) for various A values"""
    
    kappa = 1.0
    t = np.linspace(0, 10, 1000)
    
    # Different initial conditions
    C0_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for C0 in C0_values:
        A = (1 - C0) / C0
        C = 1 / (1 + A * np.exp(-kappa * t))
        ax.plot(t, C, label=f'$C_0 = {C0}$', linewidth=2)
    
    # Reference line at C=1
    ax.axhline(1, color='black', linestyle='--', linewidth=1, 
               label='$C=1$ (attractor)')
    
    ax.set_xlabel('Time $t$ (arbitrary units)', fontsize=12)
    ax.set_ylabel('Coherence $C(t)$', fontsize=12)
    ax.set_title('Logistic Evolution: All Initial Conditions → $C=1$', 
                 fontsize=13, pad=15)
    ax.legend(loc='lower right', framealpha=0.95)
    ax.grid(alpha=0.3)
    ax.set_ylim([0, 1.1])
    
    plt.tight_layout()
    plt.savefig('figures/Fig_1_logistic_evolution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Figure 1 saved: logistic_evolution.png")


# ===================================================================
# Figure 2: Lyapunov Functions V₁(C) and V₂(C)
# ===================================================================

def plot_lyapunov_functions():
    """Plot both Lyapunov functions demonstrating stability at C=1"""
    
    C = np.linspace(0.01, 0.99, 500)
    
    # V1: Quadratic Lyapunov
    V1 = (1 - C)**2
    
    # V2: Entropic Lyapunov
    V2 = -C * np.log(C) - (1 - C) * np.log(1 - C)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot V1
    ax1.plot(C, V1, linewidth=2.5, color='steelblue')
    ax1.axvline(1, color='red', linestyle='--', linewidth=1.5, 
                label='$C=1$ (minimum)')
    ax1.set_xlabel('Coherence $C$', fontsize=12)
    ax1.set_ylabel('$V_1(C) = (1-C)^2$', fontsize=12)
    ax1.set_title('Quadratic Lyapunov Function', fontsize=13, pad=15)
    ax1.legend(loc='upper right')
    ax1.grid(alpha=0.3)
    
    # Plot V2
    ax2.plot(C, V2, linewidth=2.5, color='darkorange')
    ax2.axvline(1, color='red', linestyle='--', linewidth=1.5, 
                label='$C=1$ (minimum)')
    ax2.set_xlabel('Coherence $C$', fontsize=12)
    ax2.set_ylabel('$V_2(C) = -C\ln C - (1-C)\ln(1-C)$', fontsize=12)
    ax2.set_title('Entropic Lyapunov Function', fontsize=13, pad=15)
    ax2.legend(loc='upper right')
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figures/Fig_2_lyapunov_functions.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Figure 2 saved: lyapunov_functions.png")


# ===================================================================
# Figure 3: Vacuum Structure V(C) = λC²(1-C)²
# ===================================================================

def plot_vacuum_structure():
    """Plot the double-well potential showing C=1 as true vacuum"""
    
    C = np.linspace(-0.1, 1.2, 1000)
    lambda_val = 1.0  # Normalized
    
    V = lambda_val * C**2 * (1 - C)**2
    
    # Second derivative for curvature analysis
    V_prime_prime = 2 * lambda_val * (1 - 6*C + 6*C**2)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), 
                                    gridspec_kw={'height_ratios': [2, 1]})
    
    # Plot potential
    ax1.plot(C, V, linewidth=3, color='darkviolet')
    ax1.axvline(0, color='red', linestyle='--', linewidth=1.5, alpha=0.7,
                label='$C=0$ (unstable)')
    ax1.axvline(1, color='green', linestyle='--', linewidth=1.5, alpha=0.7,
                label='$C=1$ (stable vacuum)')
    ax1.scatter([0, 1], [0, 0], s=100, c=['red', 'green'], zorder=5,
                edgecolors='black', linewidths=1.5)
    ax1.set_ylabel('$V(C) = \lambda C^2(1-C)^2$', fontsize=12)
    ax1.set_title('Vacuum Structure: Double-Well Potential', fontsize=13, pad=15)
    ax1.legend(loc='upper right', fontsize=11)
    ax1.grid(alpha=0.3)
    ax1.set_xlim([-0.1, 1.2])
    ax1.set_ylim([-0.02, 0.08])
    
    # Plot second derivative (curvature)
    ax2.plot(C, V_prime_prime, linewidth=2.5, color='navy')
    ax2.axhline(0, color='black', linestyle='-', linewidth=0.8)
    ax2.axvline(0, color='red', linestyle='--', linewidth=1.5, alpha=0.5)
    ax2.axvline(1, color='green', linestyle='--', linewidth=1.5, alpha=0.5)
    ax2.fill_between(C, 0, V_prime_prime, where=(V_prime_prime > 0), 
                      alpha=0.2, color='green', label='Stable ($V\'\' > 0$)')
    ax2.fill_between(C, 0, V_prime_prime, where=(V_prime_prime < 0), 
                      alpha=0.2, color='red', label='Unstable ($V\'\' < 0$)')
    ax2.set_xlabel('Coherence $C$', fontsize=12)
    ax2.set_ylabel('$V\'\'(C)$', fontsize=12)
    ax2.set_title('Curvature Analysis', fontsize=11)
    ax2.legend(loc='upper right', fontsize=10)
    ax2.grid(alpha=0.3)
    ax2.set_xlim([-0.1, 1.2])
    
    plt.tight_layout()
    plt.savefig('figures/Fig_3_vacuum_structure.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Figure 3 saved: vacuum_structure.png")


# ===================================================================
# Figure 4: Perturbation Decay in FRW Spacetime
# ===================================================================

def plot_perturbation_decay():
    """Plot δC decay with Hubble friction + effective mass"""
    
    # Time array
    t = np.linspace(0, 5, 1000)
    
    # Parameters (normalized)
    H = 0.3          # Hubble parameter
    m_eff_sq = 2.0   # Effective mass squared (√(2λ))
    gamma = 3*H/2 + np.sqrt(m_eff_sq)
    
    # Different k modes
    k_over_a = [0.5, 1.0, 2.0, 5.0]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for k in k_over_a:
        omega_sq = k**2 + m_eff_sq
        # Approximate solution (overdamped regime)
        delta_C = np.exp(-gamma * t) * np.cos(np.sqrt(omega_sq) * t)
        ax.plot(t, np.abs(delta_C), label=f'$k/a = {k}$', linewidth=2)
    
    # Envelope
    envelope = np.exp(-gamma * t)
    ax.plot(t, envelope, 'k--', linewidth=2, alpha=0.7, 
            label='Decay envelope $\\sim e^{-\\gamma t}$')
    
    ax.set_xlabel('Time $t$ (arbitrary units)', fontsize=12)
    ax.set_ylabel('$|\\delta C|$ (normalized)', fontsize=12)
    ax.set_title('Perturbation Decay in FRW Background ($\\gamma \\gg H$)', 
                 fontsize=13, pad=15)
    ax.legend(loc='upper right', framealpha=0.95)
    ax.grid(alpha=0.3)
    ax.set_yscale('log')
    ax.set_ylim([1e-4, 2])
    
    # Add annotation
    ax.annotate(f'$\\gamma = 3H/2 + \\sqrt{{2\\lambda}} \\approx {gamma:.2f}$',
                xy=(0.5, 0.3), xycoords='axes fraction',
                fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('figures/Fig_4_perturbation_decay.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Figure 4 saved: perturbation_decay.png")


# ===================================================================
# Main Execution
# ===================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Generating figures for CSGT Section II")
    print("="*60 + "\n")
    
    plot_logistic_evolution()
    plot_lyapunov_functions()
    plot_vacuum_structure()
    plot_perturbation_decay()
    
    print("\n" + "="*60)
    print("All figures generated successfully!")
    print("Location: ./figures/")
    print("="*60 + "\n")
