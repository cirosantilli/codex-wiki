"""Draw Question 3(c)'s projections; output only to the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository's root pyproject.toml.
Run from the mirrored _media directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(6.6, 6.1), facecolor="white")
    ax.set_facecolor("white")
    outer = Circle((0, -1), np.sqrt(11), facecolor="#dcecf8", edgecolor="#256394", lw=2,
                   label=r"$D:\ x^2+(y+1)^2\leq 11$")
    inner = Circle((-1, 0), np.sqrt(3), facecolor="#f9d6ab", edgecolor="#ab5b13", lw=2,
                   label=r"$E:\ (x+1)^2+y^2\leq 3$")
    ax.add_patch(outer)
    ax.add_patch(inner)
    ax.axhline(0, color="#87939d", lw=.75, zorder=0)
    ax.axvline(0, color="#87939d", lw=.75, zorder=0)
    ax.plot([0, -1], [-1, 0], "o", color="#303b43", ms=4)
    ax.annotate(r"$(0,-1)$", (0, -1), xytext=(9, -3), textcoords="offset points", fontsize=10)
    ax.annotate(r"$(-1,0)$", (-1, 0), xytext=(-48, 10), textcoords="offset points", fontsize=10)
    ax.text(-1.02, .83, "lower plane controls", ha="center", color="#723b0d", fontsize=10)
    ax.text(.2, -3.15, "paraboloid controls", ha="center", color="#204f73", fontsize=10)
    ax.set(xlim=(-3.7, 3.7), ylim=(-4.7, 3.55), xlabel="$x$", ylabel="$y$",
           title="Question 3(c): nested planar projections")
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", frameon=True, facecolor="white", framealpha=1, fontsize=10)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "mathematics-v-resit-projections.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
