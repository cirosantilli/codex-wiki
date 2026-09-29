"""Draw limiting-reagent-amounts.png into the current working directory.

Single-reaction stoichiometric progress; the horizontal axis is not time.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
From _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp python3 ../limiting-reagent-amounts.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    initial = np.array([3.0, 1.0, 0.0])
    stoichiometric = np.array([-2.0, -1.0, 2.0])
    limit = np.min(initial[:2] / -stoichiometric[:2])
    extent = np.linspace(0, limit, 201)
    amounts = initial[:, None] + stoichiometric[:, None] * extent
    atom_composition = np.array([[2, 0, 2], [0, 2, 1]])
    np.testing.assert_allclose(atom_composition @ stoichiometric, [0, 0])
    np.testing.assert_allclose(atom_composition @ amounts,
                               np.tile([[6], [2]], (1, extent.size)))
    np.testing.assert_allclose(amounts[:, -1], [1, 0, 2])
    assert limit == 1 and np.all(amounts >= 0)
    assert np.any(initial + stoichiometric * (limit + 0.01) < 0)
    plt.rcParams.update({"font.size": 14, "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.4, 5.4), facecolor="white")
    fig.subplots_adjust(left=0.11, right=0.79, top=0.77, bottom=0.23)
    fig.suptitle("Oxygen limits water production", fontsize=22, y=0.96)
    fig.text(0.5, 0.855, "2 H₂ + O₂ → 2 H₂O     |     Initially: 3 mol H₂ + 1 mol O₂", ha="center", fontsize=15)
    for values, color, style, label in zip(
            amounts, ["#246baa", "#c64b39", "#268452"], ["-", "--", "-."],
            ["H₂: 1 mol remains", "O₂: exhausted", "H₂O: 2 mol formed"]):
        ax.plot(extent, values, lw=2.8, color=color, ls=style)
        ax.scatter([limit], [values[-1]], color=color, s=50, zorder=4)
        ax.annotate(label, xy=(limit, values[-1]), xytext=(10, 0),
                    textcoords="offset points", color=color, fontsize=13, va="center",
                    annotation_clip=False)
    ax.axvline(limit, color="#777777", lw=1.2, ls=":")
    ax.set(xlim=(0, 1.025), ylim=(-0.12, 3.2), xlabel="Extent of reaction ξ (mol)",
           ylabel="Amount of substance n (mol)", xticks=np.linspace(0, 1, 6), yticks=[0, 1, 2, 3])
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#dddddd", lw=0.7)
    fig.text(0.5, 0.10, "Atom totals throughout: 6 mol H atoms and 2 mol O atoms.", ha="center", fontsize=14)
    fig.text(0.5, 0.045, "Complete-conversion model for one reaction; ξ measures progress, not time.",
             ha="center", fontsize=12, color="#555555")
    fig.savefig("limiting-reagent-amounts.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified ξ_max = 1 mol, final amounts (1, 0, 2) mol, nonnegativity,")
    print("and constant atom totals (6, 2) mol across all plotted points.")


if __name__ == "__main__":
    main()
