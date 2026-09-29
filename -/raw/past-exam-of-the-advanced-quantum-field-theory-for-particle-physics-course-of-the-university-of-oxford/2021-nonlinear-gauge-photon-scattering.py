"""Draw the four tree graphs; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def wave(ax, start, end, amplitude=0.035):
    start, end = np.array(start, dtype=float), np.array(end, dtype=float)
    vector = end - start
    length = np.linalg.norm(vector)
    t = np.linspace(0, 1, 400)
    normal = np.array([-vector[1], vector[0]]) / length
    cycles = max(3, round(length * 7))
    pts = start[:, None] + vector[:, None] * t + normal[:, None] * amplitude * np.sin(2 * np.pi * cycles * t)
    ax.plot(pts[0], pts[1], color="#185b99", linewidth=1.7)


def main():
    fig, axes = plt.subplots(2, 2, figsize=(9, 5.7), dpi=130, facecolor="white")
    ends = [(-1, .58), (-1, -.58), (1, .58), (1, -.58)]
    panels = [("Contact", (1, 2, 3, 4)),
              ("s exchange: 12 | 34", (1, 2, 3, 4)),
              ("t exchange: 13 | 24", (1, 3, 2, 4)),
              ("u exchange: 14 | 23", (1, 4, 2, 3))]
    for ax, (title, labels) in zip(axes.flat, panels):
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-1.45, 1.45)
        ax.set_ylim(-.92, 1.02)
        ax.set_title(title, fontsize=13, pad=5)
        if title == "Contact":
            nodes = [(0, 0)] * 4
            ax.plot(0, 0, "o", color="black", markersize=5)
        else:
            nodes = [(-.32, 0)] * 2 + [(.32, 0)] * 2
            wave(ax, (-.32, 0), (.32, 0))
            ax.plot([-.32, .32], [0, 0], "o", color="black", markersize=4)
        for end, node, label in zip(ends, nodes, labels):
            wave(ax, node, end)
            ax.text(end[0] * 1.15, end[1] * 1.12, rf"$p_{label}$", fontsize=13,
                    ha="center", va="center")
    fig.text(.5, .025, "All external momenta incoming; wavy lines denote photons", ha="center", fontsize=11)
    fig.subplots_adjust(left=.03, right=.97, top=.94, bottom=.09, hspace=.35, wspace=.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
