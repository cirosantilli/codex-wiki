"""Original analytical real slices of forms on C^2.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; output is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.1), facecolor="white")
    fig.subplots_adjust(left=0.065, right=0.98, bottom=0.19, top=0.73, wspace=0.35)
    fig.suptitle("What does a real diagonal measure?", y=0.965, fontsize=17)
    fig.text(0.5, 0.88, r"Analytical illustration: $z=(x,y)\in\mathbb{R}^2\subset\mathbb{C}^2$; not the full complex domain",
             ha="center", fontsize=12)
    colors = ["#1767a8", "#b24c19", "#6f4696"]
    names = ["Positive definite", "Indefinite", "Positive semidefinite"]
    formulas = [r"$q_+=|z_1|^2+2|z_2|^2$", r"$q_-=|z_1|^2-|z_2|^2$", r"$q_0=|z_1|^2$"]
    for ax, name, formula, color in zip(axes, names, formulas, colors):
        ax.set(xlim=(-1.8, 1.8), ylim=(-1.8, 1.8), xlabel=r"$x=\mathrm{Re}\,z_1$", ylabel=r"$y=\mathrm{Re}\,z_2$")
        ax.set_aspect("equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.grid(alpha=0.18)
        ax.axhline(0, color="#aaaaaa", lw=0.7)
        ax.axvline(0, color="#aaaaaa", lw=0.7)
        ax.set_title(name + "\n" + formula, color=color, pad=12)
        for spine in ax.spines.values():
            spine.set_color("#bbbbbb")
    t = np.linspace(0, 2 * np.pi, 721)
    axes[0].plot(np.cos(t), np.sin(t) / np.sqrt(2), color=colors[0], lw=2.8)
    axes[0].scatter([0], [0], s=35, c="black", zorder=5)
    axes[0].text(0.63, 0.91, r"$q_+=1$", color=colors[0])
    axes[0].text(0.13, -0.23, r"$q_+=0$ only here", fontsize=10)
    h = np.linspace(-1.15, 1.15, 301)
    for sign in [-1, 1]:
        axes[1].plot(sign * np.cosh(h), np.sinh(h), color=colors[1], lw=2.8)
    x = np.linspace(-1.8, 1.8, 200)
    axes[1].plot(x, x, "--", color="#555555", lw=1.3)
    axes[1].plot(x, -x, "--", color="#555555", lw=1.3)
    axes[1].scatter([1], [1], color="black", s=30, zorder=5)
    axes[1].text(-0.42, 1.45, r"$q_-<0$", color=colors[1])
    axes[1].text(0.97, -0.19, r"$q_-=1$", color=colors[1], fontsize=10)
    axes[1].text(-1.7, -1.62, r"dashed: $q_-=0$", fontsize=10)
    for a in [-1, 1]:
        axes[2].axvline(a, color=colors[2], lw=2.8)
    axes[2].axvline(0, color="#555555", ls="--", lw=1.6)
    axes[2].scatter([0], [1], s=30, color="black", zorder=5)
    axes[2].text(1.1, -0.2, r"$q_0=1$", color=colors[2], rotation=90)
    axes[2].text(-0.63, -1.6, r"dashed: $q_0=0$", fontsize=10)
    notes = ["Unit level: ellipse\nZero diagonal forces zero vector",
             "Unit level: hyperbolas\nNonzero vectors can have zero diagonal",
             "Unit level: parallel lines\nWhole coordinate line has zero diagonal"]
    for ax, note in zip(axes, notes):
        ax.text(0.5, -0.19, note, transform=ax.transAxes, ha="center", va="top", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
