"""Draw exact rational and computed irrational circle orbits; PNG in CWD.

Run from _media: python3 ../rational-versus-irrational-rotations.py
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Rational angles use integer residues; irrational angles use direct k*alpha.
Finite samples illustrate the orbit and do not prove density.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def panel(ax, fractions, title, color, label_points):
    theta = np.linspace(0, 2 * np.pi, 721)
    ax.plot(np.cos(theta), np.sin(theta), color="#a3adb5", linewidth=1.3)
    ax.axhline(0, color="#e5e9ed", linewidth=1)
    ax.axvline(0, color="#e5e9ed", linewidth=1)
    angles = 2 * np.pi * fractions
    points = np.column_stack((np.cos(angles), np.sin(angles)))
    ax.scatter(points[:, 0], points[:, 1], color=color,
               s=44 if label_points else 19, zorder=3)
    ax.scatter([1], [0], s=95, facecolors="white", edgecolors=color,
               linewidths=2, zorder=4)
    if label_points:
        for k, point in enumerate(points):
            ax.text(*(1.18 * point), str(k), ha="center", va="center",
                    fontsize=12, color=color)
    ax.set_title(title, fontsize=12, pad=12)
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.4, 1.4), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    rational = (2 * np.arange(7) % 7) / 7
    irrational = np.remainder(np.arange(64) * (np.sqrt(2) - 1), 1)
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.4), dpi=100)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=.035, right=.965, top=.73, bottom=.22, wspace=.26)
    fig.suptitle("Powers of a circle rotation", y=.955, fontsize=16)
    fig.text(.5, .85, r"$z_k=e^{2\pi ik\alpha}$; labels give k, open ring marks k = 0",
             ha="center", fontsize=12)
    panel(axes[0], rational, r"$\alpha=2/7$:  seven points", "#187ca2", True)
    panel(axes[1], irrational[:8], r"$\alpha=\sqrt{2}-1$:  first eight", "#c76821", True)
    panel(axes[2], irrational, r"$\alpha=\sqrt{2}-1$:  first 64", "#c76821", False)
    fig.text(.19, .18, "k = 7 returns to k = 0", ha="center", color="#187ca2")
    fig.text(.5, .08, "Finite samples illustrate the infinite orbit; they do not prove density.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "rational-versus-irrational-rotations.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
