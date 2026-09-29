"""Relative Kepler ellipse with equal-time samples; tested with Python 3.14."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # NumPy 2.3.5 and Matplotlib 3.10.7; same exact model as energy figure.
    eccentricity = 0.6
    minor = np.sqrt(1 - eccentricity**2)
    anomaly = np.linspace(0, 2 * np.pi, 1001)
    x = np.cos(anomaly) - eccentricity
    y = minor * np.sin(anomaly)
    mean_samples = np.arange(24) * 2 * np.pi / 24
    sample_anomaly = mean_samples.copy()
    for _ in range(12):
        sample_anomaly -= (sample_anomaly - eccentricity * np.sin(sample_anomaly) - mean_samples) / (
            1 - eccentricity * np.cos(sample_anomaly)
        )
    sample_x = np.cos(sample_anomaly) - eccentricity
    sample_y = minor * np.sin(sample_anomaly)

    plt.rcParams.update({"font.size": 11})
    fig, ax = plt.subplots(figsize=(8, 5.4))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(x, y, color="#1769aa", lw=2.2)
    ax.scatter(sample_x, sample_y, s=25, color="#1769aa", zorder=4,
               label=r"Equal time steps $\Delta t=P/24$")
    ax.scatter([0], [0], marker="*", s=180, color="#d35f16", zorder=6)
    ax.annotate("Attracting focus\n(relative coordinate)", xy=(0, 0), xytext=(-0.35, -0.42),
                ha="center", arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.scatter([-eccentricity], [0], marker="+", s=65, color="#777777", zorder=5)
    ax.text(-eccentricity - 0.05, -0.14, "Ellipse centre", ha="right", fontsize=10, color="#555555")
    ax.annotate("Periapsis: r = 0.4\nK = 2, U = −2.5\n2K + U = 1.5", xy=(0.4, 0),
                xytext=(0.65, 0.72), ha="center",
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    ax.annotate("Apoapsis: r = 1.6\nK = 0.125, U = −0.625\n2K + U = −0.375", xy=(-1.6, 0),
                xytext=(-1.75, -0.98), ha="center",
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    # Arrow follows counterclockwise motion, from eta=0.6 to eta=0.85.
    ax.annotate("", xy=(np.cos(0.85) - eccentricity, minor * np.sin(0.85)),
                xytext=(np.cos(0.6) - eccentricity, minor * np.sin(0.6)),
                arrowprops={"arrowstyle": "->", "color": "#1769aa", "lw": 2})
    ax.annotate("", xy=(0.4, -1.02), xytext=(-0.6, -1.02),
                arrowprops={"arrowstyle": "<->", "color": "#555555"})
    ax.text(-0.1, -1.12, "Semimajor axis a = 1", ha="center", fontsize=10)
    ax.set_aspect("equal")
    ax.set_xlim(-2.3, 1.17)
    ax.set_ylim(-1.28, 1.22)
    ax.set_xlabel(r"Relative position $x/a$")
    ax.set_ylabel(r"Relative position $y/a$")
    ax.set_title("Kepler ellipse: fast near periapsis, slow near apoapsis", pad=13)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.95)
    ax.grid(alpha=0.17)
    fig.text(0.5, 0.015, "m = a = κ = 1, e = 0.6; total energy E = −0.5 everywhere",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.045, 1, 1))
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
