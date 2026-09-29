"""Original functional diagram; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes nuclear-emulsion-record-develop-scan.png to CWD.
All dots and paths are schematic, with no physical scale or measured counts.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 6.2), facecolor="white")
    fig.suptitle("Nuclear emulsion: record → develop → scan", fontsize=18, y=.97)
    ax = fig.add_axes((.025, .03, .95, .87))
    ax.set(xlim=(0, 11), ylim=(0, 6))
    ax.axis("off")
    blue, orange = "#156a9a", "#b45b13"
    for x, title, body in [
        (.15, "1  RECORD", "Silver halide in gelatin\nExclude light\nParticles pass"),
        (3.95, "2  DEVELOP + FIX", "Develop silver grains\nRemove residual halide"),
        (7.75, "3  SCAN + RECONSTRUCT", "Focus through depth\nTrace branches\nMeasure range"),
    ]:
        ax.add_patch(FancyBboxPatch((x, 4.15), 3.1, 1.5,
                     boxstyle="round,pad=.08", facecolor="#eef5fa", edgecolor=blue))
        ax.text(x+.12, 5.35, title, weight="bold", color=blue, fontsize=11)
        ax.text(x+.12, 4.9, body, va="top", linespacing=1.6, fontsize=10.5)
    for x in (3.35, 7.15):
        ax.add_patch(FancyArrowPatch((x, 4.9), (x+.48, 4.9),
                     arrowstyle="-|>", mutation_scale=18, color=blue, lw=2))

    ax.text(.2, 3.55, "Coating before processing", weight="bold", fontsize=13)
    ax.add_patch(Rectangle((.2, 1.7), 4.4, 1.5, facecolor="#fbf2dc", edgecolor="#b49462"))
    ax.add_patch(Rectangle((.2, 1.48), 4.4, .22, facecolor="#cde4ef", edgecolor=blue))
    gx, gy = np.meshgrid(np.linspace(.48, 4.3, 14), np.linspace(1.92, 2.95, 5))
    ax.scatter(gx, gy, s=27, facecolors="white", edgecolors="#9e875a", linewidths=.6)
    ax.plot([.1, 4.6], [2.96, 2.0], color=orange, lw=2.2)
    ax.annotate("particle path", xy=(3.4, 2.26), xytext=(3.1, 3.58),
                fontsize=10, color=orange, arrowprops={"arrowstyle": "->", "color": orange})
    ax.text(.2, 1.1, "support", color=blue)
    ax.text(.2, .63, "Circles: sensitive crystals\nNot a scaled section or a grain measurement", fontsize=10)

    ax.text(6.0, 3.55, "Developed pattern: one schematic candidate", weight="bold", fontsize=12)
    ax.add_patch(Rectangle((6, 1.48), 4.7, 1.72, facecolor="#fafafa", edgecolor="#9a9a9a"))
    t = np.linspace(0, 1, 35)
    ax.scatter(6.2+2.0*t, 2.84-.65*t, s=10+13*t, color="#262626", zorder=3)
    ax.scatter(8.2+1.2*t, 2.19+.65*t, s=10+12*t, color="#262626", zorder=3)
    ax.annotate("joined branches?", xy=(8.2, 2.19), xytext=(6.3, 1.75),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    ax.text(6, 1.05, "Follow through focal depths, not just a projection.", fontsize=10)
    ax.text(6, .63, "Grains record interactions along a path.\nThey are not pictures of whole particles.", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
