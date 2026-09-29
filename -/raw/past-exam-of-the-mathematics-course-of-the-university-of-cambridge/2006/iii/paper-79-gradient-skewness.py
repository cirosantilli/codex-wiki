"""Illustrative derivative PDF, not simulation data. Output is in the CWD.

Tested with the Python, NumPy and Matplotlib versions in pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    weights = np.array([0.2, 0.8])
    means = np.array([-0.8, 0.2])
    deviations = np.array([0.75, 0.6])
    mean = float(weights @ means)
    variance = float(weights @ (deviations**2 + means**2) - mean**2)
    third_moment = float(weights @ ((means - mean)**3 + 3*(means - mean)*deviations**2))
    scale = np.sqrt(variance)
    skewness = third_moment / scale**3
    z = np.linspace(-5, 4, 1500)
    density = np.zeros_like(z)
    for weight, center, deviation in zip(weights, means, deviations):
        density += weight * scale / (np.sqrt(2*np.pi)*deviation) * np.exp(
            -0.5*((mean + scale*z - center)/deviation)**2
        )
    reference = np.exp(-z*z/2) / np.sqrt(2*np.pi)
    assert abs(mean) < 1e-12 and skewness < 0
    fig, ax = plt.subplots(figsize=(9, 5), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(z, density, color="#176b9b", linewidth=2.5, label=f"Illustration (skewness {skewness:.2f})")
    ax.plot(z, reference, color="#686868", linewidth=1.8, linestyle="--", label="Standard normal reference")
    ax.axvline(0, color="#a0a0a0", linewidth=0.8)
    ax.annotate("Longer negative tail\n(compressive gradients)", xy=(-2.3, np.interp(-2.3,z,density)),
                xytext=(-4.4, 0.22), fontsize=11, arrowprops={"arrowstyle":"->", "color":"#176b9b"})
    ax.set(xlim=(-5,4), ylim=(0,0.53), xlabel=r"Standardized longitudinal derivative $G/\sqrt{\langle G^2\rangle}$",
           ylabel="Probability density", title="Negative skewness of a longitudinal velocity gradient")
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    ax.grid(alpha=0.18)
    fig.text(0.5, 0.025, "An illustrative Gaussian mixture; not measured or simulated turbulence data.",
             ha="center", fontsize=9, color="#555555")
    fig.tight_layout(rect=(0,0.065,1,1))
    fig.savefig(Path.cwd() / "paper-79-gradient-skewness.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
