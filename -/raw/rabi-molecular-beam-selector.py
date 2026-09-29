"""Original functional Rabi beam schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; writes rabi-molecular-beam-selector.png to the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch


def beam_path(x):
    # Integrate two opposite constant transverse accelerations (schematic units).
    acceleration, width, separation = 0.48, 1.5, 5.0
    slope = -acceleration * width * separation / (10.0 - 0.8)
    y = 2.1 + slope * (x - 0.8)
    for left, sign in [(2.0, 1), (7.0, -1)]:
        y += sign * acceleration / 2 * (
            np.maximum(x - left, 0) ** 2
            - np.maximum(x - left - width, 0) ** 2
        )
    return y


def main():
    fig, ax = plt.subplots(figsize=(11, 4.6), dpi=110, facecolor="white")
    ax.set_facecolor("white")
    colors = {"A": "#dbeaf8", "C": "#e8f3df", "B": "#dbeaf8"}
    for label, left, width in [("A", 2.0, 1.5), ("C", 4.2, 2.0), ("B", 7.0, 1.5)]:
        ax.add_patch(Rectangle((left, 0.65), width, 2.6, facecolor=colors[label], edgecolor="#556879", lw=1.2))
        ax.text(left + width / 2, 3.5, f"{label} magnet", ha="center", fontsize=13, weight="bold")
    ax.text(2.75, 0.35, "inhomogeneous\ngradient +", ha="center", va="top", fontsize=11)
    ax.text(7.75, 0.35, "inhomogeneous\ngradient −", ha="center", va="top", fontsize=11)
    ax.text(5.2, 0.35, "uniform static field\n+ transverse RF", ha="center", va="top", fontsize=11)
    ax.add_patch(Rectangle((0.05, 1.65), 0.75, 0.9, facecolor="#fde7c8", edgecolor="#8f6a38"))
    ax.text(0.42, 2.1, "oven", ha="center", va="center", fontsize=11)
    ax.text(0.42, 3.5, "Source", ha="center", fontsize=12)
    x = np.linspace(0.8, 10.0, 1200)
    y = beam_path(x)
    ax.plot(x, y, color="#2166ac", lw=2.8, label="unchanged state: refocused")
    # Identical incoming path; changed projection alters acceleration in B.
    xb = x[x >= 5.2]
    lost = beam_path(xb) + 0.10 * np.maximum(xb - 7, 0) ** 2
    ax.plot(xb, lost, "--", color="#b83238", lw=2.5, label="RF transition: misses detector")
    slit_y = float(beam_path(np.array([3.9]))[0])
    ax.plot([3.9, 3.9], [0.7, slit_y - 0.10], color="#303030", lw=4)
    ax.plot([3.9, 3.9], [slit_y + 0.10, 3.15], color="#303030", lw=4)
    ax.text(3.9, 3.48, "slit", ha="center", fontsize=11)
    ax.plot([10.0, 10.0], [1.92, 2.28], color="#111111", lw=6)
    ax.text(10.0, 1.4, "detector", ha="center", fontsize=11)
    ax.add_patch(FancyArrowPatch((4.65, 2.7), (5.75, 2.7), arrowstyle="<->", mutation_scale=12, color="#4c782e", lw=1.8))
    ax.text(5.2, 3.0, "one RF region", ha="center", fontsize=11, color="#375a23")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=2, frameon=False, fontsize=11)
    ax.set(xlim=(-0.25, 10.65), ylim=(0.0, 4.0))
    ax.axis("off")
    fig.suptitle("Rabi beam resonance: a state change becomes particle loss", fontsize=15, y=0.98)
    fig.text(0.5, 0.015, "Original functional model • schematic paths and geometry • no measured values", ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.85, bottom=0.22)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
