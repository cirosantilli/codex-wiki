"""Original analytic characteristics; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media. Dashed trajectories after t=1 are formal continuations,
not a single-valued Burgers solution. No experimental data are used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.4, 5.6), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    ax.axhspan(1, 1.65, color="#f1f1f1", zorder=0)
    before = np.linspace(0, 1, 201)
    after = np.linspace(1, 1.65, 151)
    for label in np.linspace(-1.5, 1.5, 13):
        speed = 1 - np.tanh(label)
        color = "#b3261e" if np.isclose(abs(label), 1) else "#4383a8"
        width = 2.1 if np.isclose(abs(label), 1) else 1.2
        ax.plot(label + before * speed, before, color=color, lw=width)
        ax.plot(label + after * speed, after, color=color, lw=width,
                ls="--", alpha=0.8)
    pair_time = 1 / np.tanh(1)
    ax.scatter([1, pair_time], [1, pair_time], c=["black", "#b3261e"],
               s=35, zorder=5)
    ax.axhline(1, color="black", lw=0.9, ls=":")
    ax.annotate("First gradient blow-up\n(x, t) = (1, 1)", xy=(1, 1),
                xytext=(-1.48, 1.12), arrowprops={"arrowstyle": "->"},
                fontsize=10, va="bottom")
    ax.annotate("Labels −1 and +1 intersect\nformally at t ≈ 1.313",
                xy=(pair_time, pair_time), xytext=(2.06, 1.16),
                arrowprops={"arrowstyle": "->", "color": "#b3261e"},
                fontsize=10, color="#b3261e")
    ax.text(-1.5, 1.58, "Dashed: formal continuation after breaking", fontsize=10)
    ax.text(1.8, 0.13, "Solid: valid before t = 1", fontsize=10)
    ax.set(xlim=(-1.65, 3.45), ylim=(0, 1.65), xlabel="Position x",
           ylabel="Time t", title="Burgers characteristics for u₀(ξ) = 1 − tanh ξ")
    ax.grid(alpha=0.15)
    fig.text(0.5, 0.025, "Exact calculation: x = ξ + t(1 − tanh ξ); chosen dimensionless data",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
