"""Coordinate seminorm strips and their intersection.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the basename PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.3), dpi=110)
    a, b, limit = 1.0, 0.5, 1.65
    points = np.array([[0.8, 0.4], [0.8, 0.7], [1.2, 0.4]])
    labels = ["A", "B", "C"]
    colors = ["#167747", "#a94621", "#713b9a"]
    assert np.array_equal(np.all(np.abs(points) < [a, b], axis=1), [True, False, False])
    definitions = [
        (r"$p_x(x,y)=|x|<1$", "Vertical strip: y is unrestricted", (-a, -limit, 2*a, 2*limit), "#d4e9f5"),
        (r"$p_y(x,y)=|y|<1/2$", "Horizontal strip: x is unrestricted", (-limit, -b, 2*limit, 2*b), "#fce4bf"),
        (r"$\max\{|x|,2|y|\}<1$", "Intersection: both tests must pass", (-a, -b, 2*a, 2*b), "#d3eadb"),
    ]
    for i, (ax, (title, subtitle, box, fill)) in enumerate(zip(axes, definitions)):
        ax.add_patch(Rectangle(box[:2], box[2], box[3], facecolor=fill, edgecolor="none", zorder=0))
        if i != 1:
            for x in [-a, a]:
                extent = (-limit, limit) if i == 0 else (-b, b)
                ax.plot([x, x], extent, "--", color="#337ca6", lw=1.6)
        if i != 0:
            for y in [-b, b]:
                extent = (-limit, limit) if i == 1 else (-a, a)
                ax.plot(extent, [y, y], "--", color="#af7627", lw=1.6)
        ax.axhline(0, color="#45545d", lw=0.7)
        ax.axvline(0, color="#45545d", lw=0.7)
        for point, label, color in zip(points, labels, colors):
            ax.scatter(*point, color=color, s=35, zorder=3)
            ax.annotate(label, point, xytext=(5, 6), textcoords="offset points", color=color, weight="bold")
        ax.set(xlim=(-limit, limit), ylim=(-limit, limit), xlabel="x", ylabel="y", aspect="equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, -0.5, 0, 0.5, 1])
        ax.set_title(title + "\n" + subtitle, pad=12)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Two incomplete measurements together detect every direction", fontsize=15, y=.98)
    fig.text(.5, .025, "A = (0.8, 0.4): both     B = (0.8, 0.7): x only     C = (1.2, 0.4): y only\nDashed boundaries are excluded; the strips continue beyond the plotted window.", ha="center", fontsize=10)
    fig.subplots_adjust(left=.055, right=.985, bottom=.19, top=.78, wspace=.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
