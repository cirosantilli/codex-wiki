"""Original entry-game tree; Python 3.14.4, Matplotlib 3.10.7.

Write the opaque PNG beside the current working directory's files.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(6, 3.2), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    nodes = {"Ann": (0, 1.8), "Out": (-1.4, 0.8), "Bob": (1.1, 0.8), "Fight": (0.2, -0.35), "Acquiesce": (2, -0.35)}
    for start, end, label, dx in [("Ann", "Out", "stay out", -0.16), ("Ann", "Bob", "enter", 0.14), ("Bob", "Fight", "fight", -0.13), ("Bob", "Acquiesce", "acquiesce", 0.24)]:
        x0, y0 = nodes[start]
        x1, y1 = nodes[end]
        ax.plot([x0, x1], [y0, y1], color="#526476", linewidth=1.7)
        ax.text((x0+x1)/2+dx, (y0+y1)/2, label, ha="center", va="center", fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for name in ["Ann", "Bob"]:
        x, y = nodes[name]
        ax.scatter([x], [y], s=1300, color="#e6f1fa", edgecolor="#1c5580", zorder=3)
        ax.text(x, y, name, ha="center", va="center", fontsize=12, zorder=4)
    for name, payoff in [("Out", "(2, 6)"), ("Fight", "(1, 1)"), ("Acquiesce", "(3, 3)")]:
        x, y = nodes[name]
        ax.scatter([x], [y], s=35, color="#1c5580", zorder=3)
        ax.text(x, y-0.25, payoff, ha="center", va="top", fontsize=13)
    ax.set_title("Payoffs: (Ann, Bob), in millions", fontsize=13, pad=12)
    ax.set_xlim(-2, 2.7)
    ax.set_ylim(-1.0, 2.2)
    ax.axis("off")
    fig.tight_layout(pad=0.8)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
