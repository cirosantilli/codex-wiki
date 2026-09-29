"""Plot powers on two domains; emit the matching opaque PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), dpi=120)
    fig.patch.set_facecolor("white")
    colors = ["#2264a5", "#29957a", "#cf8620", "#a74368"]
    for ax, endpoint in zip(axes, [1.0, 0.8]):
        x = np.linspace(0, endpoint, 1400)
        for n, color in zip([1, 4, 12, 32], colors):
            ax.plot(x, x**n, color=color, lw=2, label=f"n = {n}")
        ax.plot([0, endpoint], [0, 0], color="#20252a", lw=3,
                linestyle="--", label="limit f")
        ax.set(xlim=(-0.025, endpoint + 0.035), ylim=(-0.075, 1.08),
               xlabel="input x", ylabel="function value")
        ax.grid(alpha=0.18)
    left, right = axes
    left.scatter([1], [0], s=75, facecolors="white", edgecolors="#20252a",
                 linewidths=2, zorder=6, clip_on=False)
    left.scatter([1], [1], s=60, color="#20252a", zorder=6)
    left.annotate("f(1) = 1", xy=(1, 1), xytext=(0.45, 0.95),
                  arrowprops={"arrowstyle": "->", "color": "#20252a"})
    left.text(0.10, 0.17, "f(x) = 0 for x < 1", color="#20252a")
    left.set_title("On [0, 1]: a discontinuous limit", pad=13)
    right.axvline(0.8, color="#555555", ls=":", lw=1.4)
    right.scatter([0.8], [0], s=60, color="#20252a", zorder=6)
    right.annotate(r"largest error = $0.8^n$", xy=(0.8, 0.8**4),
                   xytext=(0.09, 0.62), arrowprops={"arrowstyle": "->"})
    right.text(0.08, 0.17, "f(x) = 0 everywhere", color="#20252a")
    right.set_title("On [0, 0.8]: a uniform limit", pad=13)
    left.legend(loc="center left", bbox_to_anchor=(0.02, 0.61),
                fontsize=9, framealpha=0.95)
    fig.suptitle(r"Same powers $f_n(x)=x^n$, different domain endpoints",
                 fontsize=14, y=0.98)
    fig.text(0.5, 0.025,
             "Open circle: excluded limit value.  Filled circle: actual limit value.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.17, top=0.81, wspace=0.27)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
