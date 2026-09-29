"""Original thin-film paths and spectral filters; tested with Python 3.14.

Uses the NumPy and Matplotlib versions declared in the root pyproject.toml.
Writes its PNG basename in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle
import numpy as np


def ray(ax, start, end, color, width=2):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": color, "lw": width})


def main():
    fig, (ax, spectral) = plt.subplots(1, 2, figsize=(11, 4.7), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.add_patch(Rectangle((-1.4, -1.2), 4.3, 1.2, facecolor="#e3f3fb", edgecolor="none"))
    ax.axhline(0, color="#555555", lw=1)
    ax.axhline(-1.2, color="#555555", lw=1)
    dx = 1.2 * np.tan(np.arcsin(np.sin(np.deg2rad(35)) / 1.33))
    ray(ax, (-1.2, 1.71), (0, 0), "#333333")
    ray(ax, (0, 0), (1.2, 1.71), "#0068a0")
    ray(ax, (0, 0), (dx, -1.2), "#b55713")
    ray(ax, (dx, -1.2), (2 * dx, 0), "#b55713")
    ray(ax, (2 * dx, 0), (2 * dx + 1.2, 1.71), "#b55713")
    ax.plot([0, 0], [-0.8, 0.7], "--", color="#999999", lw=1)
    ax.add_patch(Arc((0, 0), 0.85, 0.85, theta1=270, theta2=295.5, color="#555555"))
    ax.text(0.13, -0.65, r"$\theta_t$", fontsize=12)
    ax.annotate("", xy=(-1.03, 0), xytext=(-1.03, -1.2),
                arrowprops={"arrowstyle": "<->", "color": "#555555"})
    ax.text(-1.22, -0.65, r"$d$", fontsize=13)
    ax.text(-1.3, 1.9, "Incident light", fontsize=11)
    ax.text(0.9, 1.9, r"First reflection: $\pi$ shift", fontsize=10, color="#0068a0")
    ax.text(1.75, 0.3, "Second\nreflection", fontsize=10, color="#b55713")
    ax.text(1.5, -0.65, r"Film: index $n$", fontsize=11)
    ax.text(-0.9, -1.53, "Air", fontsize=11)
    ax.text(-0.9, 0.45, "Air", fontsize=11)
    ax.set(xlim=(-1.55, 2.95), ylim=(-1.8, 2.18), title="Two paths at a local film patch")
    ax.set_aspect("equal")
    ax.axis("off")

    wavelength = np.linspace(380, 750, 700)
    for d, color in [(120, "#0068a0"), (240, "#b55713"), (400, "#654c9e")]:
        filt = np.sin(2 * np.pi * 1.33 * d / wavelength) ** 2
        spectral.plot(wavelength, filt, label=f"d = {d} nm", color=color, lw=2)
    spectral.set(xlabel="Vacuum wavelength (nm)", ylabel="Normalized spectral filter",
                 ylim=(0, 1.08), xlim=(380, 750), title="Broad maxima mix visible wavelengths")
    spectral.text(0.03, 0.04, "Illustrative n = 1.33; normal incidence\nWeak-reflection model; not perceived colour",
                  transform=spectral.transAxes, fontsize=9,
                  bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.88})
    spectral.legend(loc="upper right", fontsize=9)
    spectral.grid(alpha=0.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
