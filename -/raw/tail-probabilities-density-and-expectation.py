"""Analytic rate-two exponential density and survival areas.

Python 3.14 / NumPy 2.3 / Matplotlib 3.10. Run from _media.
The finite display is explicitly distinguished from the exact infinite areas.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, orange = "#236a9e", "#bd5b15"
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.4), layout="constrained")
    fig.suptitle("Exponential model, rate 2: two different areas", fontsize=16)
    x = np.linspace(0, 3, 1201)
    tail_x = np.linspace(1, 3, 801)
    ax = axes[0]
    ax.plot(x, 2 * np.exp(-2 * x), color=blue, linewidth=2.2)
    ax.fill_between(tail_x, 0, 2 * np.exp(-2 * tail_x), color=orange, alpha=0.35)
    ax.vlines(1, 0, 2 * np.exp(-2), color=orange, linestyle="--")
    ax.plot(1, 2 * np.exp(-2), "o", color=blue)
    ax.annotate(r"Height $f(1)=2e^{-2}\approx0.2707$",
                xy=(1, 2 * np.exp(-2)), xytext=(0.6, 1.1),
                arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    ax.text(1.95, 0.67, "Tail area to infinity:\n" + r"$P(X\geq1)=e^{-2}\approx0.1353$",
            color=orange, ha="center")
    ax.set(title="Density: area beyond one threshold", xlabel="Outcome x",
           ylabel=r"Density $f(x)=2e^{-2x}$", xlim=(0, 3), ylim=(0, 2.15))
    ax = axes[1]
    ax.plot(x, np.exp(-2 * x), color=blue, linewidth=2.2)
    ax.fill_between(x, 0, np.exp(-2 * x), color=blue, alpha=0.25)
    ax.vlines(1, 0, np.exp(-2), color=orange, linestyle="--")
    ax.plot(1, np.exp(-2), "o", color=orange)
    ax.annotate(r"Height $S(1)=e^{-2}$", xy=(1, np.exp(-2)), xytext=(1.3, 0.31),
                arrowprops={"arrowstyle": "->", "color": orange}, color=orange)
    ax.text(1.7, 0.65, "Total area to infinity:\n" + r"$E[X]=\int_0^\infty S(t)\,dt=1/2$",
            color=blue, ha="center")
    ax.set(title="Survival: area over all thresholds", xlabel="Threshold t",
           ylabel=r"Probability $S(t)=e^{-2t}$", xlim=(0, 3), ylim=(0, 1.08))
    for ax in axes:
        ax.set_xticks([0, 1, 2, 3])
        ax.grid(color="#e6e9ec", linewidth=0.7)
        ax.set_axisbelow(True)
    fig.text(0.5, -0.025, "Analytical illustration • curves continue beyond 3 • formulas describe the full infinite areas",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
