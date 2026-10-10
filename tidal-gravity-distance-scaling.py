"""Compare inverse-square gravity, inverse-cube tides and a finite baseline.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; the matching opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.5), dpi=120)
    distance = np.geomspace(1, 16, 300)
    ticks = np.array([1, 2, 4, 8, 16])
    ax = axes[0]
    ax.loglog(distance, distance ** -2, color="#24699c", lw=2.3,
              label=r"Gravity $g/g_0=(R/R_0)^{-2}$")
    ax.loglog(distance, distance ** -3, color="#c45c1b", lw=2.3,
              label=r"Radial tide $\lambda_r/\lambda_{r0}=(R/R_0)^{-3}$")
    ax.scatter(ticks, ticks.astype(float) ** -2, color="#24699c", s=22, zorder=3)
    ax.scatter(ticks, ticks.astype(float) ** -3, color="#c45c1b", s=22, zorder=3)
    ax.set_xticks(ticks, [str(v) for v in ticks])
    ax.set_xlim(1, 16)
    ax.set_ylim(1e-4, 1.7)
    ax.set_xlabel(r"Distance $R/R_0$ (log scale)")
    ax.set_ylabel("Normalized magnitude (log scale)")
    ax.set_title("Same source, increasing distance", fontsize=12, fontweight="bold")
    ax.legend(loc="lower left", fontsize=9, framealpha=1)
    ax.grid(alpha=0.20, which="major")
    ax.annotate("At twice the distance:\ngravity = 1/4, radial tide = 1/8", xy=(2, 0.25), xytext=(3.3, 0.65),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#767d85"})

    ax = axes[1]
    separation = np.linspace(0, 1.5, 400)
    correction = (1 - separation ** 2 / 4) ** -2
    ax.axvspan(0, 0.2, color="#eef2f6", zorder=0)
    ax.plot(separation, correction, color="#c45c1b", lw=2.3, label="Exact result / linear result")
    ax.axhline(1, color="#24699c", lw=1.6, linestyle="--", label="Linear approximation")
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0.75, 5.7)
    ax.set_xlabel(r"Separation / midpoint distance $L/R$")
    ax.set_ylabel(r"$\Delta a\,/\,(2\mu L/R^3)$")
    ax.set_title("Same midpoint, increasing separation", fontsize=12, fontweight="bold")
    ax.grid(alpha=0.20)
    ax.legend(loc="upper left", fontsize=9, framealpha=1)
    ax.text(0.38, 2.9, r"$(1-L^2/(4R^2))^{-2}$", fontsize=14, color="#c45c1b")
    example = 0.02
    ratio = (1 - example ** 2 / 4) ** -2
    ax.scatter([example], [ratio], color="#30343b", s=30, zorder=4)
    ax.annotate("Example L/R = 0.02\nexact / linear = 1.00020003", xy=(example, ratio), xytext=(0.32, 1.75),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#767d85"})
    fig.suptitle("A tidal gradient falls faster than gravity itself", fontsize=15, y=0.99)
    fig.text(0.5, 0.025, "Point-mass model. Left: each quantity normalized to its own value at R₀. Right: symmetric radial endpoints R ± L/2.",
             ha="center", fontsize=9.5, color="#555c64")
    fig.subplots_adjust(left=0.075, right=0.98, top=0.84, bottom=0.17, wspace=0.27)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
