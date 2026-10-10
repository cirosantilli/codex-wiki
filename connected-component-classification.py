"""Illustrate components of three exact subsets of the usual real line.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(3, 1, figsize=(9, 5.8), facecolor="white")
    blue, orange, green = "#1769aa", "#c65a13", "#237f59"
    titles = (
        r"$[-2,2]$: one connected component",
        r"$[-2,2]\setminus\{0\}$: two connected components",
        r"$\{-2,0,2\}$: three singleton components",
    )
    for ax, title in zip(axes, titles, strict=True):
        ax.set_facecolor("white")
        ax.set_title(title, loc="left", pad=13, fontsize=14)
        ax.axhline(0, color="#acb4bc", linewidth=1, zorder=0)
        ax.set_xlim(-2.7, 2.7)
        ax.set_ylim(-0.42, 0.5)
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([])
        ax.tick_params(axis="x", length=0)
        for spine in ax.spines.values():
            spine.set_visible(False)

    axes[0].plot([-2, 2], [0, 0], color=blue, linewidth=7, solid_capstyle="butt")
    axes[0].scatter([-2, 2], [0, 0], color=blue, s=80, zorder=3)
    axes[0].text(0, 0.19, "All points belong to the same maximal connected set", ha="center", fontsize=12)

    for endpoints, color in [([-2, 0], blue), ([0, 2], orange)]:
        axes[1].plot(endpoints, [0, 0], color=color, linewidth=7, solid_capstyle="butt")
    axes[1].scatter([-2, 2], [0, 0], color=[blue, orange], s=80, zorder=3)
    axes[1].scatter([0], [0], facecolor="white", edgecolor="#333333", linewidth=2, s=120, zorder=4)
    axes[1].text(-1, 0.19, r"$C_-=[-2,0)$", color=blue, ha="center")
    axes[1].text(1, 0.19, r"$C_+=(0,2]$", color=orange, ha="center")
    axes[1].text(0, -0.3, "0 is absent", ha="center", fontsize=11)

    axes[2].scatter([-2, 0, 2], [0, 0, 0], color=[blue, orange, green], s=95, zorder=3)
    for x, color in zip([-2, 0, 2], [blue, orange, green], strict=True):
        axes[2].text(x, 0.19, rf"$\{{{x}\}}$", color=color, ha="center")

    fig.suptitle("Connected components classify points", fontsize=18, y=0.98)
    fig.text(0.5, 0.022, "Every row uses the subspace topology from the usual real line.", ha="center", fontsize=12)
    fig.subplots_adjust(top=0.84, bottom=0.12, left=0.08, right=0.97, hspace=0.95)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
