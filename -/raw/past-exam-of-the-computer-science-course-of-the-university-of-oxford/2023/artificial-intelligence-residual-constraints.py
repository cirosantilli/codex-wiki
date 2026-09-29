"""Draw the residual allocation constraint tree; Python 3.14.4, Matplotlib 3.10.7.

Run from any directory; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    positions = {"B": (0, 1.5), "A": (-1.4, 0.5), "C": (-1.4, -0.7), "D": (0, 0.1), "E": (1.4, 0.5)}
    edges = [("B", "A", "3"), ("A", "C", "1, 2"), ("B", "D", "4, 5"), ("B", "E", "6, 7")]
    fig, ax = plt.subplots(figsize=(5.0, 3.6), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    for left, right, label in edges:
        x, y = zip(positions[left], positions[right])
        ax.plot(x, y, color="#1c5580", linewidth=2, zorder=1)
        ax.text(sum(x) / 2 + (0.16 if left == "A" or right == "D" else 0), sum(y) / 2 + (0.13 if right in "AE" else 0), label,
                ha="left" if right in "CD" else "center", va="center", fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5}, zorder=3)
    for name, (x, y) in positions.items():
        ax.scatter([x], [y], s=1000, color="#e6f1fa", edgecolor="#1c5580", zorder=2)
        ax.text(x, y, name, ha="center", va="center", fontsize=16, zorder=3)
    ax.set_title("After no-waste restriction: a tree", fontsize=13, pad=12)
    ax.text(0, -1.15, "Edge labels: items valued by both endpoints", fontsize=10, ha="center")
    ax.set_aspect("equal")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.3, 2)
    ax.axis("off")
    fig.tight_layout(pad=0.8)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
