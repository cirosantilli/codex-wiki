"""Illustrate all solution classes of two linear congruences modulo fifteen."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(15)
    residues = 6 * x % 15
    solutions = x[residues == 9]
    assert solutions.tolist() == [4, 9, 14]
    assert not np.any(residues == 10)
    assert sorted(set(residues)) == [0, 3, 6, 9, 12]
    assert np.all((2 * solutions) % 5 == 3)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 16})
    fig, ax = plt.subplots(figsize=(10, 4.7), dpi=120)
    fig.patch.set_facecolor("white")
    ax.vlines(x, 0, residues, color="#bbcad7", lw=2)
    ax.scatter(x, residues, s=70, color="#246b9e", zorder=4, label=r"$6x\;\mathrm{mod}\;15$")
    ax.scatter(solutions, np.full(3, 9), s=150, color="#18844f", edgecolor="white",
               linewidth=1.2, zorder=5, label="Solutions: 4, 9, 14")
    ax.axhline(9, color="#18844f", lw=1.8, linestyle="--")
    ax.axhline(10, color="#d57816", lw=1.8, linestyle=":", label="Residue 10 is never reached")
    for solution in solutions:
        ax.annotate(str(solution), (solution, 9), xytext=(0, -27), textcoords="offset points",
                    ha="center", color="#12683f", fontweight="bold")
    ax.set_xticks(x)
    ax.set_yticks([0, 3, 6, 9, 10, 12])
    ax.set_xlim(-0.6, 14.6)
    ax.set_ylim(-0.8, 13.5)
    ax.set_xlabel(r"Representative $x$ of a class modulo 15")
    ax.set_ylabel("Least nonnegative residue")
    ax.set_title("One congruence has three classes; the other has none", pad=16)
    ax.grid(axis="y", color="#dfe5e8", linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=3, frameon=False, fontsize=10)
    fig.text(0.5, 0.92, r"$6x\equiv9\;(\mathrm{mod}\;15)\ \Longleftrightarrow\ x\equiv4\;(\mathrm{mod}\;5)$",
             ha="center", fontsize=14)
    fig.subplots_adjust(left=0.09, right=0.98, top=0.79, bottom=0.23)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
