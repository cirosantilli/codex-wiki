"""Draw particle inventories, not an atomic geometry or orbit model.

Writes atomic-number-isotopes-and-ions.png in the current working directory.
Run from _media to produce the repository image.
Tested with Python 3.14.4, Matplotlib 3.10.7 (+dfsg1), NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


# name, isotope symbol, atomic number, mass number, charge in units of e
INVENTORIES = (
    ("Carbon-12: neutral", r"$^{12}_{6}\mathrm{C}$", 6, 12, 0),
    ("Carbon-13: neutral", r"$^{13}_{6}\mathrm{C}$", 6, 13, 0),
    ("Sodium-23: neutral", r"$^{23}_{11}\mathrm{Na}$", 11, 23, 0),
    ("Sodium-23: singly positive", r"$^{23}_{11}\mathrm{Na}^{+}$", 11, 23, 1),
)


def tokens(ax, count, y, color):
    """One evenly spaced token per particle; positions have no spatial meaning."""
    xs = 1.56 + np.arange(count) * 0.215
    ax.scatter(xs, np.full(count, y), s=77, color=color,
               edgecolors="white", linewidths=0.5, zorder=3)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.8), dpi=120)
    fig.subplots_adjust(left=0.035, right=0.985, bottom=0.13, top=0.84,
                        wspace=0.09, hspace=0.36)
    fig.suptitle("Same element: change neutrons or electrons", fontsize=17, y=0.975)
    fig.text(0.5, 0.916, "Top pair: different isotopes   |   Bottom pair: neutral atom and ion",
             ha="center", fontsize=12)
    blue, gray, orange = "#2476a3", "#707b84", "#bd5a24"
    for ax, (name, symbol, z, a, q) in zip(axes.flat, INVENTORIES):
        neutrons, electrons = a - z, z - q
        ax.set(xlim=(0, 4.2), ylim=(0, 3.1))
        ax.axis("off")
        ax.text(0.12, 3.02, name, fontsize=12, weight="bold", va="top")
        ax.text(3.9, 3.04, symbol, fontsize=17, ha="right", va="top")
        ax.add_patch(Rectangle((0.07, 1.27), 4.08, 1.18, facecolor="#f4f7f9",
                               edgecolor="#9ca7af", lw=1))
        ax.text(0.19, 2.24, "Nucleus inventory", fontsize=10, color="#3f4d56", va="center")
        ax.text(0.2, 1.97, f"{z} protons", va="center", color=blue)
        ax.text(0.2, 1.53, f"{neutrons} neutrons", va="center", color=gray)
        tokens(ax, z, 1.97, blue)
        tokens(ax, neutrons, 1.53, gray)
        ax.text(0.2, 0.88, f"{electrons} electrons", va="center", color=orange)
        tokens(ax, electrons, 0.88, orange)
        charge = "0" if q == 0 else f"+{q}e"
        ax.text(0.2, 0.28, f"Z = {z}     A = {a}     Q = {charge}", fontsize=11)
    fig.text(0.5, 0.070, "One dot = one counted particle. Rows are inventories, not physical positions or orbits.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.026, r"$N=A-Z$     and     $n_e=Z-Q/e$", ha="center", fontsize=13)
    fig.savefig(Path("atomic-number-isotopes-and-ions.png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
