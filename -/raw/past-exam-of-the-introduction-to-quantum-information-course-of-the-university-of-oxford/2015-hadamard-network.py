"""Draw the parallel Hadamard circuit; write its PNG only to the current directory.

Dependencies: the repository pyproject.toml (matplotlib and NumPy).
Tested with Python 3.14.4, matplotlib 3.10.7, and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, ax = plt.subplots(figsize=(8.4, 3.0), facecolor="white")
    ax.set_facecolor("white")
    for y, label in [(2.4, "1"), (1.55, "2"), (0.25, "n")]:
        ax.plot([0.9, 2.4], [y, y], color="#26364a", lw=1.8)
        ax.plot([3.2, 5.0], [y, y], color="#26364a", lw=1.8)
        ax.add_patch(Rectangle((2.4, y - 0.28), 0.8, 0.56,
                               facecolor="#e6effa", edgecolor="#26364a", lw=1.8))
        ax.text(2.8, y, "$H$", ha="center", va="center", fontsize=19)
        ax.text(0.65, y, rf"$|x_{label}\rangle$", ha="right", va="center", fontsize=15)
    ax.text(2.8, 0.94, r"$\vdots$", ha="center", va="center", fontsize=22)
    ax.text(5.35, 1.4, r"$H^{\otimes n}$", ha="left", va="center", fontsize=23)
    ax.text(2.8, -0.38, "One gate per qubit; one parallel layer", ha="center", fontsize=12)
    ax.set_xlim(-0.1, 7.1)
    ax.set_ylim(-0.65, 2.95)
    ax.axis("off")
    fig.tight_layout(pad=0.7)
    fig.savefig(Path.cwd() / "2015-hadamard-network.png", dpi=115,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
