"""A rank-one linear map decomposes input into visible and kernel components.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; opaque PNG to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, a, b, color, label=None):
    ax.annotate("", b, a, arrowprops={"arrowstyle": "-|>", "color": color,
                                     "lw": 2.4, "mutation_scale": 16})
    if label:
        ax.text(*label[0], label[1], color=color, fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})


def main():
    A = np.array([[1, 2], [0, 0]])
    visible, hidden = np.array([1, 2]), np.array([2, -1])
    np.testing.assert_array_equal(A @ visible, [5, 0])
    np.testing.assert_array_equal(A @ hidden, [0, 0])
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=120)
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#bbbbbb", lw=1)
        ax.axvline(0, color="#bbbbbb", lw=1)
        ax.set_aspect("equal")
        ax.grid(alpha=0.12)
    t = np.linspace(-2.2, 2.2, 100)
    axes[0].plot(2*t, -t, color="#2768a6", ls="--", lw=1.5,
                 label=r"Kernel: $x+2y=0$")
    arrow(axes[0], [0, 0], visible, "#238367", ((0.0, 2.4), "Visible (1, 2)"))
    arrow(axes[0], visible, [3, 1], "#2768a6",
          ((1.9, 1.9), "Kernel (2, −1)"))
    arrow(axes[0], [0, 0], [3, 1], "#80519d",
          ((2.5, 0.3), "Input (3, 1)"))
    axes[0].set(xlim=(-3, 4.4), ylim=(-2.1, 3.6), xlabel="Input x",
                ylabel="Input y", title="Input: dimension 2")
    axes[0].legend(loc="lower left", frameon=False, fontsize=10)
    axes[1].plot([-1, 6], [0, 0], color="#238367", lw=3,
                 label="Image: horizontal line")
    arrow(axes[1], [0, 0], [5, 0], "#80519d")
    axes[1].scatter([0, 5], [0, 0], c=["#2768a6", "#80519d"], s=60, zorder=4)
    axes[1].text(0, -0.6, "Kernel component\nmaps to zero",
                 ha="center", color="#2768a6", fontsize=11)
    axes[1].text(5, 0.5, "Both inputs map\nto (5, 0)",
                 ha="center", color="#80519d", fontsize=11)
    axes[1].set(xlim=(-1, 6), ylim=(-2.1, 3.6), xlabel="Output coordinate 1",
                ylabel="Output coordinate 2", title="Output image: dimension 1")
    axes[1].legend(loc="lower left", frameon=False, fontsize=10)
    fig.suptitle(r"$T(x,y)=(x+2y,0)$:  input dimension 2 = nullity 1 + rank 1",
                 fontsize=14, y=0.98)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
