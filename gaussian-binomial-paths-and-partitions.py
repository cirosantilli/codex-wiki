"""Render the six paths/partitions counted by the Gaussian polynomial G_4,2."""
from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, axes = plt.subplots(2, 3, figsize=(11.5, 7.0), dpi=110)
    fig.patch.set_facecolor("white")
    fig.suptitle("Six paths, with the area retained in the count", fontsize=19, y=0.98)
    for ax, north_positions in zip(axes.flat, combinations(range(4), 2)):
        north_positions = set(north_positions)
        word = "".join("N" if i in north_positions else "E" for i in range(4))
        x = y = area = 0
        points = [(x, y)]
        for step in word:
            if step == "N":
                for col in range(x):
                    ax.add_patch(Rectangle((col, y), 1, 1, color="#f3c66c", alpha=0.75))
                area += x
                y += 1
            else:
                x += 1
            points.append((x, y))
        for v in range(3):
            ax.plot([0, 2], [v, v], color="#b7bcc3", linewidth=0.8)
            ax.plot([v, v], [0, 2], color="#b7bcc3", linewidth=0.8)
        ax.plot(*zip(*points), color="#2368a4", linewidth=3.4, marker="o", markersize=5)
        ax.set(xlim=(-0.12, 2.12), ylim=(-0.12, 2.12), aspect="equal")
        monomial = "1" if area == 0 else ("t" if area == 1 else rf"t^{area}")
        ax.set_title(rf"{word}: area {area}, weight ${monomial}$", fontsize=13, pad=8)
        ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
        ax.tick_params(labelsize=10)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.02, r"$G_{4,2}(t)=1+t+2t^2+t^3+t^4$     |     shaded cells lie to the left of north steps", ha="center", fontsize=15)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.87, bottom=0.10, hspace=0.38, wspace=0.20)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
