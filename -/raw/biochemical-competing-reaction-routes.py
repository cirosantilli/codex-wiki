"""Illustrate selective reaction routes with chosen first-order kinetics.

Python 3.14.4; Matplotlib 3.10.7 and NumPy 2.3.5 as in pyproject.toml.
Labels are hypothetical species of equal elemental composition, not structures.
Run in _media; the opaque white PNG is written to cwd with this basename.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    ink, blue, orange = "#253947", "#167294", "#b35e22"
    fig = plt.figure(figsize=(9.0, 5.4), facecolor="white")
    fig.text(0.5, 0.945, "Choosing a route through chemistry", ha="center",
             fontsize=17, color=ink, weight="bold")
    fig.text(0.5, 0.887, "Illustrative first-order model; all rate constants chosen",
             ha="center", fontsize=11, color=ink)
    network = fig.add_axes((0.03, 0.25, 0.42, 0.57))
    network.set(xlim=(0, 10), ylim=(0, 8))
    network.axis("off")
    for x, y, label, color in [(1.5, 4, "S", ink), (8, 6.5, "P", blue),
                                (8, 1.5, "Q", orange)]:
        network.add_patch(FancyBboxPatch((x - 0.7, y - 0.7), 1.4, 1.4,
                          boxstyle="round,pad=0.15", facecolor="white",
                          edgecolor=color, linewidth=2))
        network.text(x, y, label, ha="center", va="center", fontsize=20,
                     color=color, weight="bold")
    for endpoint, color in [((7.1, 6.2), blue), ((7.1, 1.8), orange)]:
        network.add_patch(FancyArrowPatch((2.4, 4), endpoint,
                          arrowstyle="-|>", mutation_scale=18,
                          linewidth=2.5, color=color))
    network.text(4.65, 6.1, r"$k_P = 0.08$ or $0.32$", ha="center",
                 fontsize=11, color=blue)
    network.text(4.65, 1.75, r"$k_Q = 0.02$", ha="center", fontsize=11,
                 color=orange)
    network.text(4.8, 0.1, "Effective rates in min⁻¹", ha="center", fontsize=10,
                 color=ink)
    ax = fig.add_axes((0.56, 0.30, 0.40, 0.49), facecolor="white")
    kp = np.array([0.08, 0.32])
    kq = 0.02
    p = 100 * kp / (kp + kq)
    q = 100 - p
    positions = np.array([1, 0])
    ax.barh(positions, p, height=0.48, color=blue, label="P")
    ax.barh(positions, q, left=p, height=0.48, color=orange, label="Q")
    for y, pv, qv in zip(positions, p, q):
        ax.text(pv / 2, y, f"P: {pv:.1f}", ha="center", va="center",
                color="white", fontsize=12, weight="bold")
        ax.text(pv + qv / 2, y + 0.34, f"Q: {qv:.1f}", ha="center",
                va="center", color=orange, fontsize=10)
        ax.plot([pv + qv / 2] * 2, [y + 0.27, y + 0.24], color=orange)
    ax.set(xlim=(0, 104), ylim=(-0.5, 1.7), yticks=[1, 0],
           yticklabels=["Original", "P route ×4"], xticks=[0, 20, 40, 60, 80, 100],
           xlabel="Limiting product amount (µmol)")
    ax.set_title("From 100 µmol of S", fontsize=12, color=ink, pad=15)
    ax.tick_params(labelsize=10)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.text(0.5, 0.15, "Desired fraction = kP / (kP + kQ): 80% → 94.1%",
             ha="center", color=ink, fontsize=12,
             bbox={"facecolor": "#edf6f8", "edgecolor": blue, "pad": 7})
    fig.text(0.5, 0.055, "Speeding both routes equally leaves the split unchanged.  No experimental data.",
             ha="center", color=ink, fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Limiting desired fractions: {p[0]/100:.12g}, {p[1]/100:.12g}")


if __name__ == "__main__":
    main()
