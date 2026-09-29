"""Plot independent-site equilibrium occupancy; write basename.png in cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
The 10 nM dissociation constant is illustrative, not fitted experimental data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    kd = 10.0  # nM; all concentrations below refer to free ligand.
    points = np.array([1.0, 10.0, 100.0])
    occupied = points / (kd + points)
    np.testing.assert_allclose(occupied, [1 / 11, 0.5, 10 / 11])
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.9), sharey=True)
    fig.subplots_adjust(left=0.085, right=0.97, bottom=0.23, top=0.80, wspace=0.13)
    fig.patch.set_facecolor("white")
    for ax, logarithmic in zip(axes, (False, True)):
        ligand = np.geomspace(0.1, 1000, 500) if logarithmic else np.linspace(0, 120, 500)
        ax.plot(ligand, ligand / (kd + ligand), color="#236d99", lw=2.5)
        ax.scatter(points, occupied, color="#b6531f", s=42, zorder=5)
        ax.axhline(0.5, color="#777777", ls="--", lw=1)
        ax.axvline(kd, color="#777777", ls="--", lw=1)
        ax.set_ylim(0, 1.02)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_xlabel("Free ligand concentration [L] (nM)", fontsize=11)
        ax.set_title("Logarithmic concentration axis" if logarithmic else "Linear concentration axis", fontsize=12)
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
        if logarithmic:
            ax.set_xscale("log")
            ax.set_xlim(0.1, 1000)
            ax.set_xticks([0.1, 1, 10, 100, 1000], labels=["0.1", "1", "10", "100", "1000"])
            labels = ["1 nM: 1/11", "10 nM: 1/2", "100 nM: 10/11"]
            for x, y, label, offset in zip(points, occupied, labels, [(8, 14), (8, -28), (-75, -28)]):
                ax.annotate(label, (x, y), xytext=offset, textcoords="offset points", fontsize=10,
                            color="#8b421b", bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
        else:
            ax.set_xlim(0, 120)
    axes[0].set_ylabel(r"Fraction of sites occupied, $\theta$", fontsize=11)
    fig.suptitle(r"Reversible independent-site binding: $\theta=[L]/(K_d+[L])$", fontsize=15, y=0.97)
    fig.text(0.5, 0.86, r"Toy $K_d=10$ nM; homogeneous sites, equilibrium, negligible ligand depletion", ha="center", fontsize=11)
    fig.text(0.5, 0.10, "Half occupancy at 10 nM; approaching saturation at high free ligand concentration.", ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Fraction occupied does not by itself specify the cellular response.", ha="center", fontsize=11, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}; occupancies: {occupied.tolist()}")


if __name__ == "__main__":
    main()
