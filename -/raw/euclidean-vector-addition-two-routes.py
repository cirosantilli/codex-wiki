"""Draw two head-to-tail orders for an exact Euclidean-vector example."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def arrow(ax, start, end, color, dashed=False):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "mutation_scale": 18,
                            "lw": 2.6, "color": color,
                            "linestyle": "--" if dashed else "-", "shrinkA": 0, "shrinkB": 0})


def main():
    u = np.array([2., 1.])
    w = np.array([1., 3.])
    total = u + w
    origin = np.zeros(2)
    blue, orange, green = "#2878a3", "#c47b2b", "#268153"
    fig, ax = plt.subplots(figsize=(7.8, 7), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    arrow(ax, origin, u, blue)
    arrow(ax, u, total, orange)
    arrow(ax, origin, w, orange, True)
    arrow(ax, w, total, blue, True)
    arrow(ax, origin, total, green)
    for p in [origin, u, w, total]:
        ax.scatter(*p, c="#293843", s=34, zorder=5)
    labels = [(u / 2, r"$\mathbf{u}=(2,1)$", (0, -29)),
              (u + w / 2, r"Translated $\mathbf{w}$", (37, -5)),
              (w / 2, r"Translated $\mathbf{w}$", (-56, 0)),
              (w + u / 2, r"Translated $\mathbf{u}$", (0, 22)),
              (total / 2, r"$\mathbf{u}+\mathbf{w}=(3,4)$", (-50, 20))]
    for point, text, offset in labels:
        ax.annotate(text, point, xytext=offset, textcoords="offset points", fontsize=11,
                    ha="center", color=green if "\\mathbf{u}+\\mathbf{w}" in text else "#202c36",
                    arrowprops={"arrowstyle": "->", "color": green} if "\\mathbf{u}+\\mathbf{w}" in text else None,
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9, "pad": 1})
    ax.annotate("(3, 4)", total, xytext=(10, 5), textcoords="offset points", fontsize=12)
    ax.annotate("Start", origin, xytext=(-25, -22), textcoords="offset points", fontsize=11)
    ax.set(xlim=(-.9, 4.15), ylim=(-.5, 4.9), xlabel="x", ylabel="y")
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(range(5)); ax.set_yticks(range(5))
    ax.grid(alpha=.19)
    handles = [Line2D([0], [0], color="#596673", lw=2.4, label="Solid route: u then w"),
               Line2D([0], [0], color="#596673", lw=2.4, ls="--", label="Dashed route: w then u"),
               Line2D([0], [0], color=green, lw=2.4, label="Same vector sum")]
    ax.legend(handles=handles, loc="lower right", fontsize=10, framealpha=1)
    fig.suptitle("Vector addition: either order reaches the same endpoint", fontsize=16)
    fig.tight_layout(rect=(0, 0, 1, .95))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
