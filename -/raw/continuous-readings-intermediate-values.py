"""Contrast a continuous model reading with a discontinuous step.

These are exact mathematical models, not measured data.
Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.5), facecolor="white")
    blue, orange, grey = "#1769aa", "#c65a13", "#5c6670"
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlim(-0.06, 1.06)
        ax.set_ylim(-0.12, 1.14)
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 0.5, 1])
        ax.set_xlabel("Parameter t")
        ax.set_ylabel("Reading")
        ax.axhline(0.5, linestyle="--", color=grey, linewidth=1.3)
        ax.spines[["top", "right"]].set_visible(False)

    t = np.linspace(0, 1, 401)
    crossing = 1 / np.sqrt(2)
    assert abs(crossing**2 - 0.5) < 1e-14
    axes[0].plot(t, t**2, color=blue, linewidth=3)
    axes[0].scatter([0, crossing, 1], [0, 0.5, 1], color=blue, s=55, zorder=3)
    axes[0].plot([crossing, crossing], [0, 0.5], linestyle=":", color=blue, linewidth=1.5)
    axes[0].annotate(r"$t=1/\sqrt{2}$", xy=(crossing, 0.5), xytext=(0.28, 0.72), arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    axes[0].set_title(r"Continuous: $r(t)=t^2$", pad=14, fontsize=14)
    axes[0].text(0.5, -0.3, "Every value between 0 and 1 is attained", transform=axes[0].transAxes, ha="center", fontsize=11)

    axes[1].plot([0, 0.5], [0, 0], color=orange, linewidth=3)
    axes[1].plot([0.5, 1], [1, 1], color=orange, linewidth=3)
    axes[1].scatter([0.5], [0], facecolor="white", edgecolor=orange, linewidth=2, s=75, zorder=4)
    axes[1].scatter([0.5], [1], color=orange, s=75, zorder=4)
    axes[1].annotate("No input attains 1/2", xy=(0.72, 0.5), xytext=(0.13, 0.28), arrowprops={"arrowstyle": "->", "color": grey}, color=grey, fontsize=11)
    axes[1].set_title("Step: discontinuous at t = 1/2", pad=14, fontsize=14)
    axes[1].text(0.5, -0.3, "0 for t < 1/2; 1 for t ≥ 1/2", transform=axes[1].transAxes, ha="center", fontsize=11)

    fig.suptitle("A continuous reading cannot skip a middle value", fontsize=17, y=0.97)
    fig.text(0.5, 0.035, "Synthetic mathematical models; no experimental data.", ha="center", fontsize=11)
    fig.subplots_adjust(top=0.77, bottom=0.29, left=0.08, right=0.97, wspace=0.3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
