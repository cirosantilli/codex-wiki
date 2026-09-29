"""Two circle charts and their real coordinates; Python 3.14, matplotlib 3.10."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 7.4), facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[3.5, 1], hspace=0.15, wspace=0.24)
    blue, orange, gray = "#176b9b", "#d7651d", "#78828b"
    theta = np.linspace(0, 2 * np.pi, 900)
    point = np.array([3 / 5, 4 / 5])
    for col, (pole, value, variable, title) in enumerate([
        (-1, 0.5, "t", r"$U=S^1\setminus\{W\}$: omit west"),
        (1, 2, "u", r"$V=S^1\setminus\{E\}$: omit east"),
    ]):
        ax = fig.add_subplot(grid[0, col])
        ax.set_aspect("equal")
        ax.set_xlim(-1.45, 1.5)
        ax.set_ylim(-1.35, 2.5)
        ax.axis("off")
        ax.set_title(title, fontsize=13, pad=12)
        ax.axvline(0, color=gray, lw=1, zorder=0)
        ax.text(0.06, 2.3, "$x=0$", color=gray, fontsize=10)
        ax.plot(np.cos(theta), np.sin(theta), color=blue, lw=3)
        # The straight ray through the pole intersects x=0 at the chart value.
        intercept = np.array([0, value])
        end = point if pole == -1 else intercept
        ax.plot([pole, end[0]], [0, end[1]], "--", color=orange, lw=1.8)
        ax.scatter([pole], [0], s=90, facecolors="white", edgecolors=blue, lw=2, zorder=5)
        ax.scatter([-pole], [0], s=35, color=blue, zorder=4)
        for x, label in [(-1, "$W$"), (1, "$E$")]:
            ax.text(x, -0.2, label, ha="center")
        ax.scatter(*point, s=48, color=orange, zorder=5)
        ax.annotate("$P=(3/5,4/5)$", point, xytext=(0.18, 1.32),
                    arrowprops={"arrowstyle": "-", "color": gray}, fontsize=11)
        ax.scatter(*intercept, s=70, marker="D", color=orange, zorder=5)
        ax.text(-0.1, value + 0.12, f"${variable}={value:g}$", ha="right", color=orange)
        denominator = "1+x" if variable == "t" else "1-x"
        ax.text(0, -1.3, rf"${variable}=\dfrac{{y}}{{{denominator}}}$", ha="center", fontsize=16)
        line = fig.add_subplot(grid[1, col])
        line.set_xlim(-2.65, 2.65)
        line.set_ylim(-0.7, 0.75)
        line.axis("off")
        line.annotate("", xy=(2.55, 0), xytext=(-2.55, 0),
                      arrowprops={"arrowstyle": "<->", "lw": 2, "color": blue})
        for tick in [-2, -1, 0, 1, 2]:
            line.plot([tick, tick], [-0.05, 0.05], color=blue)
            line.text(tick, -0.3, str(tick), ha="center", fontsize=11)
        line.scatter([value], [0], s=55, color=orange, zorder=5)
        line.text(value, 0.23, rf"$P\mapsto {value:g}$", ha="center", color=orange)
        line.text(0, -0.65, f"{variable}=0 is {'east E' if variable == 't' else 'west W'}", ha="center", fontsize=11)
        line.text(2.5, 0.23, f"${variable}$", ha="center", color=blue)
    fig.suptitle("One circle, two coordinate descriptions", fontsize=17, y=0.98)
    fig.text(0.5, 0.043, r"Overlap: $t\ne0$, $u\ne0$ and $u=1/t$; here $1/2\leftrightarrow2$.", ha="center", fontsize=13)
    fig.text(0.5, 0.012, "Both chart images are whole real lines; together their domains cover the circle.", ha="center", fontsize=11)
    fig.subplots_adjust(top=0.88, bottom=0.12, left=0.05, right=0.96)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
