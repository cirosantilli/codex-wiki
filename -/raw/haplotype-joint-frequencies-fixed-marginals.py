"""Draw synthetic two-locus haplotype tables with fixed allele frequencies.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the matching opaque PNG is written to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    p, q = 0.60, 0.40
    associations = [(-0.12, "Negative association"), (0.0, "Linkage equilibrium"),
                    (0.12, "Positive association")]
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.4), facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.995, bottom=0.18, top=0.78, wspace=0.09)
    for ax, (d, label) in zip(axes, associations):
        table = np.array([[p*q+d, p*(1-q)-d],
                          [(1-p)*q-d, (1-p)*(1-q)+d]])
        assert np.all(table >= 0)
        np.testing.assert_allclose(table.sum(axis=1), [p, 1-p])
        np.testing.assert_allclose(table.sum(axis=0), [q, 1-q])
        np.testing.assert_allclose(table.sum(), 1)
        np.testing.assert_allclose(np.linalg.det(table), d, atol=1e-14)
        lower = min(p*q, (1-p)*(1-q))
        upper = min(p*(1-q), (1-p)*q)
        dprime = d / (upper if d > 0 else lower) if d else 0
        r2 = d*d / (p*(1-p)*q*(1-q))
        for row in range(2):
            for col in range(2):
                value = table[row, col]
                ax.add_patch(Rectangle((col, 1-row), 1, 1,
                                       facecolor=plt.cm.Blues(0.12 + 0.65*value/0.5),
                                       edgecolor="white", linewidth=2))
                haplotype = ("A" if row == 0 else "a") + ("B" if col == 0 else "b")
                ax.text(col+0.5, 1-row+0.62, haplotype, ha="center", va="center",
                        fontsize=12, color="#17324d")
                ax.text(col+0.5, 1-row+0.34, f"{value:.2f}", ha="center", va="center",
                        fontsize=16, color="#102331", fontweight="bold")
        for row, marginal in enumerate([p, 1-p]):
            ax.text(2.17, 1-row+0.5, f"{marginal:.2f}", ha="center", va="center", fontsize=12)
        for col, marginal in enumerate([q, 1-q]):
            ax.text(col+0.5, -0.24, f"{marginal:.2f}", ha="center", va="center", fontsize=12)
        ax.text(2.17, 2.10, "Total", ha="center", fontsize=10, color="#555555")
        ax.text(-0.03, -0.25, "Total", ha="right", fontsize=10, color="#555555")
        ax.text(1, -0.63, f"D′ = {dprime:.2f}    r² = {r2:.2f}", ha="center", fontsize=12)
        ax.set_title(f"{label}\nD = {d:.2f}", fontsize=12, pad=14)
        ax.set_xlim(-0.36, 2.5)
        ax.set_ylim(-0.77, 2.18)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.suptitle("Same allele frequencies, different haplotype association", fontsize=16, y=0.97)
    fig.text(0.5, 0.045, "Synthetic frequencies: P(A) = 0.60 and P(B) = 0.40 in every table",
             ha="center", fontsize=12, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
