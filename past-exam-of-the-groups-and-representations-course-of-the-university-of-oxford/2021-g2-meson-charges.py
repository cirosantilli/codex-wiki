"""Original weight plots for Oxford A15090W1 (2021), question 3.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Run in the desired output directory; only the same-basename PNG is saved.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a2_positive = np.array([[2, -1], [-1, 2], [1, 1]])
    octet_weights = np.concatenate([a2_positive, -a2_positive])
    charge_map = np.array([[2, 1], [1, 2]]) / 3
    octet = octet_weights @ charge_map.T
    g2_short = np.array([[0, 1], [1, -1], [-1, 2]])
    extra_weights = np.concatenate([g2_short, -g2_short])
    projection = np.array([[1, 1], [1, 0]])
    extra = extra_weights @ projection.T @ charge_map.T

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.22, top=0.88, wspace=0.30)
    known_color, new_color = "#244a73", "#b64424"
    for ax, title in zip(axes, ["SU(3): eight octet states", "G₂: fourteen adjoint states"]):
        ax.set_facecolor("white")
        ax.axhline(0, color="0.75", linewidth=0.8, zorder=0)
        ax.axvline(0, color="0.75", linewidth=0.8, zorder=0)
        ax.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), xlabel="Electric charge Q / e", ylabel="Flavour hypercharge Y", title=title)
        ax.set_aspect("equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.grid(alpha=0.15)
        ax.scatter(*octet.T, color=known_color, s=62, zorder=3)
        ax.scatter([0], [0], color=known_color, s=95, zorder=3)
        ax.annotate("2 states", (0, 0), xytext=(7, -16), textcoords="offset points", color=known_color, fontsize=10)
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)
    names = [r"$\pi^+$", r"$K^0$", r"$K^+$", r"$\pi^-$", r"$\bar K^0$", r"$K^-$"]
    offsets = [(6, 5), (7, 5), (5, 5), (-25, 5), (7, -15), (-26, -15)]
    for xy, name, offset in zip(octet, names, offsets):
        axes[0].annotate(name, xy, xytext=offset, textcoords="offset points", color=known_color)
    axes[0].text(0.02, -0.21, "Neutral pair: π⁰ and η₈", transform=axes[0].transAxes, color=known_color)
    axes[1].scatter(*extra.T, color=new_color, marker="D", s=48, zorder=4)
    axes[1].text(0.02, -0.21, "● known octet     ◆ six additional states", transform=axes[1].transAxes, fontsize=10)
    for xy, label, offset in [
        ((2 / 3, 1 / 3), "(⅔, ⅓)", (7, 6)),
        ((-1 / 3, 1 / 3), "(−⅓, ⅓)", (-60, 6)),
        ((-1 / 3, -2 / 3), "(−⅓, −⅔)", (-63, -17)),
        ((-2 / 3, -1 / 3), "(−⅔, −⅓)", (-65, -3)),
        ((1 / 3, -1 / 3), "(⅓, −⅓)", (7, -14)),
        ((1 / 3, 2 / 3), "(⅓, ⅔)", (7, 6)),
    ]:
        axes[1].annotate(label, xy, xytext=offset, textcoords="offset points", fontsize=9, color=new_color)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
