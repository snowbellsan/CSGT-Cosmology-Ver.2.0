import numpy as np
import matplotlib.pyplot as plt

# =========================
# Cosmological parameters
# =========================
H0_local = 73.0      # Local H0 [km/s/Mpc]
H0_CMB   = 67.0      # CMB inferred H0
Omega_m = 0.3
Omega_L = 0.7

# =========================
# Hubble functions
# =========================
def H_FRW(z, H0):
    """Standard FRW (flat LCDM)"""
    return H0 * np.sqrt(Omega_m * (1 + z)**3 + Omega_L)

def H_CSGT(z, H0=H0_local, z_star=-1.5):
    """
    CSGT unified Hubble function
    H(z) = H_FRW(z) * |z - z*| / |z*|
    """
    phi = np.abs(z - z_star) / np.abs(z_star)
    return H_FRW(z, H0) * phi

# =========================
# Redshift range
# =========================
z = np.logspace(-3, 3, 1000)  # 0.001 -> 1000

# =========================
# z* scan candidates
# =========================
z_star_values = [-0.8, -1.2, -1.5, -2.0, -3.0]

# =========================
# Plot
# =========================
plt.figure(figsize=(10, 7))

# CSGT curves
for z_star in z_star_values:
    plt.plot(
        z,
        H_CSGT(z, H0_local, z_star),
        linewidth=2,
        label=f"CSGT  z* = {z_star}"
    )

# LCDM comparison
plt.plot(
    z,
    H_FRW(z, H0_CMB),
    "k--",
    linewidth=2,
    label="LCDM (H0 = 67)"
)

# Anchors
plt.scatter([0.001], [H0_local], c="red", s=80, zorder=5, label="Local H0")
plt.scatter([1100], [H_FRW(1100, H0_CMB)], c="blue", s=80, zorder=5, label="CMB")

# Axes
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Redshift z")
plt.ylabel("H(z)  [km/s/Mpc]")
plt.title("CSGT: Unified Resolution of the H0 Tension")

plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
