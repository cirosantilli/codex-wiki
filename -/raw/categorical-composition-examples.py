"""Computed composition and singleton naturality; write the PNG to cwd."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def arrow(ax, start, end, label, color, offset=(0, 0.12)):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "lw": 2,
                            "color": color, "shrinkA": 28, "shrinkB": 28,
                            "mutation_scale": 18})
    midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    ax.text(midpoint[0] + offset[0], midpoint[1] + offset[1], label,
            ha="center", va="center", fontsize=12, color=color,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})


def node(ax, location, label):
    ax.text(*location, label, ha="center", va="center", fontsize=15,
            bbox={"boxstyle": "round,pad=0.35", "fc": "#f1f5f8",
                  "ec": "#b6c1cc"}, zorder=5)


def main():
    f = lambda x: x + 1
    g = lambda x: 2 * x
    assert g(f(3)) == 8 and f(g(3)) == 7
    assert {f(x) for x in {3}} == {f(3)} == {4}
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9), dpi=120)
    blue, orange = "#176997", "#b95f22"
    for ax in axes:
        ax.set_xlim(-0.5, 2.5)
        ax.set_ylim(-0.7, 1.7)
        ax.axis("off")
    ax = axes[0]
    for y, values, maps, color in [
        (1.0, [3, 4, 8], ["f: add 1", "g: double"], blue),
        (0.0, [3, 6, 7], ["g: double", "f: add 1"], orange),
    ]:
        for x, value in enumerate(values):
            node(ax, (x, y), str(value))
        for x, label in enumerate(maps):
            arrow(ax, (x, y), (x + 1, y), label, color, (0, 0.3))
    ax.set_title("Composition can depend on order", fontsize=13, pad=14)
    ax.text(1, -0.5, r"$g\circ f=2x+2$     $f\circ g=2x+1$",
            ha="center", fontsize=13)
    ax = axes[1]
    a, b, c, d = (0, 1.05), (2, 1.05), (0, 0), (2, 0)
    for point, label in [(a, "3"), (b, "4"), (c, "{3}"), (d, "{4}")]:
        node(ax, point, label)
    arrow(ax, a, b, "f: add 1", blue, (0, 0.3))
    arrow(ax, c, d, r"$\mathcal{P}(f)$: take image", blue, (0, -0.32))
    arrow(ax, a, c, r"$\eta_X$", orange, (-0.22, 0))
    arrow(ax, b, d, r"$\eta_Y$", orange, (0.22, 0))
    ax.set_title("Naturality: both routes agree", fontsize=13, pad=14)
    ax.text(1, -0.6, r"$f(\{3\})=\{f(3)\}=\{4\}$", ha="center", fontsize=13)
    fig.suptitle("Arrow equations can be checked on actual inputs", fontsize=16)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.8, bottom=0.08,
                        wspace=0.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
