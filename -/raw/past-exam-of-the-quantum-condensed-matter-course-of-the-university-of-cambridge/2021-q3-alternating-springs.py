"""Original equal-mass alternating-spring normal modes; write PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
The displacement arrows are mode patterns, not time-evolution trajectories.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    weak = 0.06
    q_scaled = np.linspace(-1, 1, 1501)
    qa = np.pi * q_scaled / 2
    split = np.sqrt((1 - weak)**2 + 4 * weak * np.cos(qa)**2)
    acoustic = np.sqrt(np.maximum(1 + weak - split, 0))
    optical = np.sqrt(1 + weak + split)
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.2),
                             gridspec_kw={"width_ratios": [1.05, 1]}, facecolor="white")
    ax = axes[0]
    ax.plot(q_scaled, acoustic, lw=2, color="#1768ab", label="Acoustic")
    ax.plot(q_scaled, optical, lw=2, color="#bd6426", label="Optical")
    ax.axhspan(np.sqrt(2 * weak), np.sqrt(2), color="#e7ebef")
    for edge in (-1, 1):
        ax.axvline(edge, color="#687580", ls=":", lw=1)
    ax.set(xlim=(-1.08, 1.08), ylim=(0, 1.65),
           xlabel=r"$q/[π/(2a)]$", ylabel=r"$\omega/\sqrt{K/m}$")
    ax.set_xticks([-1, 0, 1])
    ax.set_title(r"Two-atom cell: $\kappa/K=0.06$", fontsize=11)
    ax.text(0, .85, "Frequency gap", ha="center", color="#586572")
    ax.legend(loc="center right", frameon=False, fontsize=10)

    ax = axes[1]
    patterns = [(1, 1, 1, 1), (1, -1, 1, -1),
                (1, 1, -1, -1), (1, -1, -1, 1)]
    labels = [r"$q=0$: acoustic", r"$q=0$: optical",
              r"$q=\pi/(2a)$: acoustic", r"$q=\pi/(2a)$: optical"]
    for row, (pattern, label) in enumerate(zip(patterns, labels)):
        y = 3.4 - row
        ax.text(-.25, y + .29, label, fontsize=10)
        for bond in range(3):
            strong = bond % 2 == 0
            ax.plot([bond, bond + 1], [y, y], color="#8b969e",
                    lw=3 if strong else 1.4, ls="-" if strong else "--", zorder=0)
        ax.scatter(range(4), [y]*4, s=72, facecolor="white", edgecolor="#263d4b", zorder=2)
        for site, direction in enumerate(pattern):
            ax.annotate("", xy=(site + .34*direction, y + .15), xytext=(site, y + .15),
                        arrowprops={"arrowstyle": "->", "lw": 1.6,
                                    "color": "#1768ab" if row % 2 == 0 else "#bd6426"})
    ax.plot([.1, .65], [-.42, -.42], lw=3, color="#8b969e")
    ax.text(.78, -.42, r"strong $K$", va="center", fontsize=9)
    ax.plot([1.85, 2.4], [-.42, -.42], lw=1.4, ls="--", color="#8b969e")
    ax.text(2.52, -.42, r"weak $\kappa$", va="center", fontsize=9)
    ax.set(xlim=(-.35, 3.8), ylim=(-.65, 4.05))
    ax.set_title("Relative displacements", fontsize=11)
    ax.axis("off")
    axes[0].spines[["top", "right"]].set_visible(False)
    fig.tight_layout(w_pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
