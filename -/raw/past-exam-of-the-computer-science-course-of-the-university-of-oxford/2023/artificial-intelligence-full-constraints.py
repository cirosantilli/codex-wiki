"""Draw the unreduced allocation constraint graph; Python 3.14.4, Matplotlib 3.10.7.

Run from any directory; the opaque PNG is written to the current directory.
"""

from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    names = list("ABCDE")
    angles = np.linspace(np.pi / 2, np.pi / 2 - 2 * np.pi, 5, endpoint=False)
    positions = {name: (np.cos(a), np.sin(a)) for name, a in zip(names, angles)}
    fig, ax = plt.subplots(figsize=(4.4, 3.6), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    for left, right in combinations(names, 2):
        x, y = zip(positions[left], positions[right])
        ax.plot(x, y, color="#526476", linewidth=1.5, zorder=1)
    for name, (x, y) in positions.items():
        ax.scatter([x], [y], s=1000, color="#e6f1fa", edgecolor="#1c5580", zorder=2)
        ax.text(x, y, name, ha="center", va="center", fontsize=16, zorder=3)
    ax.set_title("Before domain restriction: $K_5$", fontsize=13, pad=12)
    ax.set_aspect("equal")
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.25, 1.3)
    ax.axis("off")
    fig.tight_layout(pad=0.8)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
