"""Exact connectivity of opposite corners of a four-edge square."""

from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    edges = [(0, 1), (1, 2), (0, 3), (3, 2)]
    connected_counts = np.zeros(5, dtype=int)
    for states in product([False, True], repeat=4):
        reached = {0}
        for _ in range(4):
            for (a, b), opened in zip(edges, states):
                if opened and (a in reached or b in reached):
                    reached.update([a, b])
        if 2 in reached:
            connected_counts[sum(states)] += 1
    assert connected_counts.tolist() == [0, 0, 2, 4, 1]
    p = np.linspace(0, 1, 401)
    enumerated = sum(connected_counts[k] * p**k * (1-p)**(4-k)
                     for k in range(5))
    assert np.allclose(enumerated, 2*p*p-p**4)
    assert sum(connected_counts) == 7
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.7), dpi=120)
    blue, orange = "#176997", "#b55d20"
    ax = axes[0]
    coordinates = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    for indexes, color in [([0, 1, 2], blue), ([0, 3, 2], orange)]:
        points = coordinates[indexes]
        ax.plot(points[:, 0], points[:, 1], color=color, lw=4)
    ax.scatter(coordinates[:, 0], coordinates[:, 1], s=80, color="#243746", zorder=3)
    for name, (x, y), (dx, dy) in zip("ABCD", coordinates,
                                    [(-.1, -.13), (.1, -.13), (.1, .1), (-.1, .1)]):
        ax.text(x+dx, y+dy, name, ha="center", va="center", fontsize=14)
    ax.text(.5, -.27, r"Path A–B–C: probability $p^2$", color=blue,
            ha="center", fontsize=11)
    ax.text(.5, -.39, r"Path A–D–C: probability $p^2$", color=orange,
            ha="center", fontsize=11)
    ax.text(.5, 1.28, "Both paths open: probability p⁴", ha="center", fontsize=11)
    ax.set_xlim(-.35, 1.35)
    ax.set_ylim(-.46, 1.40)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Two paths, four independent edges", fontsize=12)
    ax = axes[1]
    ax.plot(p, p**2, color=blue, lw=2, label="One specified path: p²")
    ax.plot(p, enumerated, color=orange, lw=2.5, label="Either path: 2p² − p⁴")
    ax.scatter([.5, .5], [.25, 7/16], color=[blue, orange], zorder=4)
    ax.vlines(.5, .25, 7/16, color="#687a87", ls=":")
    ax.annotate("7/16", (.5, 7/16), xytext=(.60, .40), fontsize=11,
                color=orange, arrowprops={"arrowstyle": "->", "color": orange})
    ax.annotate("1/4", (.5, .25), xytext=(.60, .15), fontsize=11,
                color=blue, arrowprops={"arrowstyle": "->", "color": blue})
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="Edge opening probability p",
           ylabel="Connection probability")
    ax.set_title("Exact probabilities, no simulation", fontsize=12)
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    ax.grid(alpha=.17)
    fig.suptitle("Alternative routes improve connectivity", fontsize=15)
    fig.subplots_adjust(left=.055, right=.97, bottom=.15, top=.82, wspace=.26)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
