"""Draw the topological comparison in Oxford Introduction to Schemes 2021, 1(c).

Run from the desired output directory; tested with Python 3.14.4 and the NumPy/Matplotlib
versions in pyproject.toml.
Output is 2021-glued-topology.png in the current directory, with a white background.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.1), dpi=120)
    fig.patch.set_facecolor("white")
    points = np.array([0.35, 1.15, 1.95, 2.75, 3.55])
    labels = [r"$\eta$", r"$y_2$", r"$y_3$", r"$y_5$", r"$\cdots$"]
    for ax in axes:
        ax.set(xlim=(-0.25, 4.1), ylim=(-1.25, 1.55))
        ax.axis("off")
    axes[0].set_title(r"The glued scheme $Y$", fontsize=12)
    axes[0].add_patch(
        Ellipse((1.15, 0.15), 2.5, 0.9, facecolor="#d8edf9", edgecolor="#29779f")
    )
    # Only eta and y_3 belong to the highlighted open; place y_2 outside it.
    ys = [0.15, -0.65, 0.15, -0.65, -0.65]
    for x, y, label in zip(points, ys, labels):
        if label != r"$\cdots$":
            axes[0].plot(x, y, "o", color="#153b50", markersize=5)
        axes[0].text(x, y - 0.25, label, ha="center", fontsize=12)
    axes[0].text(1.15, 0.92, r"$U_3=\{\eta,y_3\}$ is open", ha="center", fontsize=11)
    fig.text(
        0.25, 0.065, "Any selection of closed points\nmay accompany the generic point.",
        ha="center", va="bottom", fontsize=10,
    )
    axes[1].set_title(r"The target $\operatorname{Spec}\mathbb{Z}$", fontsize=12)
    for x, label in zip(points, [r"$(0)$", r"$(2)$", r"$(3)$", r"$(5)$", r"$\cdots$"]):
        if label != r"$\cdots$":
            axes[1].plot(x, 0.15, "o", color="#153b50", markersize=5)
        axes[1].text(x, -0.12, label, ha="center", fontsize=12)
    axes[1].text(1.9, 0.92, r"$f(U_3)=\{(0),(3)\}$ is not open", ha="center", fontsize=11)
    fig.text(
        0.75, 0.065, "Every nonempty open contains the generic point\nand all but finitely many closed points.",
        ha="center", va="bottom", fontsize=10,
    )
    fig.subplots_adjust(left=0.025, right=0.985, top=0.84, bottom=0.27, wspace=0.16)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
