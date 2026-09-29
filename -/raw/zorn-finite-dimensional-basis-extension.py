"""Illustrate finite basis extension, not the infinite theorem; Python 3.14."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, endpoint, color, label, offset):
    ax.annotate("", xy=endpoint, xytext=(0, 0),
                arrowprops={"arrowstyle": "-|>", "lw": 2.7, "color": color, "mutation_scale": 16})
    ax.annotate(label, xy=endpoint, xytext=offset, textcoords="offset points",
                color=color, fontsize=13)


def main():
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig, axes = plt.subplots(1, 2, figsize=(9, 5.3), dpi=120, facecolor="white")
    blue, orange = "#2465aa", "#ad5716"
    t = np.linspace(-2.35, 2.35, 100)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(-2.45, 2.65), ylim=(-2.45, 2.65), aspect="equal")
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-2, -1, 0, 1, 2])
        ax.grid(color="#e0e5eb", linewidth=0.7)
        ax.axhline(0, color="#828b96", linewidth=1)
        ax.axvline(0, color="#828b96", linewidth=1)
        ax.plot(t, t, color=blue, linewidth=1.5, zorder=2)
        ax.set_xlabel("x")
        ax.set_ylabel("y", rotation=0, labelpad=7)
        for spine in ax.spines.values():
            spine.set_color("#b9c2cc")
    axes[0].set_title(r"Start: $A=\{u\}$", pad=11)
    arrow(axes[0], (1, 1), blue, r"$u=(1,1)$", (-57, 15))
    axes[0].plot(2, 2, marker="x", markersize=9, color="#7f8791", markeredgewidth=2)
    axes[0].annotate(r"$2u$: redundant", (2, 2), xytext=(-94, 15), textcoords="offset points", fontsize=11)
    axes[0].text(0.5, -0.2, r"$\mathrm{span}(A)=\{(t,t):t\in\mathbb{R}\}$", transform=axes[0].transAxes,
                 ha="center", color=blue)
    axes[1].set_facecolor("#f0f6fc")
    axes[1].set_title(r"Extend: $B=\{u,w\}$", pad=11)
    arrow(axes[1], (1, 1), blue, r"$u=(1,1)$", (-57, 15))
    arrow(axes[1], (1, -1), orange, r"$w=(1,-1)$", (-20, -25))
    axes[1].text(0.5, -0.2, r"$\mathrm{span}(B)=\mathbb{R}^2$", transform=axes[1].transAxes, ha="center")
    fig.suptitle("Add a vector outside the current span", fontsize=17, weight="bold", y=0.98)
    fig.text(0.5, 0.025, "Finite-dimensional illustration; infinite basis existence requires a separate argument.",
             ha="center", fontsize=11, color="#52606e")
    fig.subplots_adjust(left=0.065, right=0.98, top=0.85, bottom=0.24, wspace=0.3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
