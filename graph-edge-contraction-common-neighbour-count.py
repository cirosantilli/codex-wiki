"""Draw two exact simple-graph contractions; Python 3.14, matplotlib 3.10.7.

Run from _media. The PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def draw_graph(ax, positions, edges, highlighted=None):
    for a, b in edges:
        color = "#c33d30" if frozenset((a, b)) == highlighted else "#34495e"
        ax.plot(*zip(positions[a], positions[b]), color=color,
                linewidth=4 if color == "#c33d30" else 2.4, zorder=1)
    for label, (x, y) in positions.items():
        ax.add_patch(Circle((x, y), 0.18, facecolor="white",
                            edgecolor="#34495e", linewidth=1.7, zorder=3))
        ax.text(x, y, label, ha="center", va="center", fontsize=14, zorder=4)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(2, 1, figsize=(9.2, 5.4), dpi=120,
                             facecolor="white")
    square = {"u": (0.9, 1.9), "v": (2.9, 1.9),
              "a": (2.9, 0.1), "b": (0.9, 0.1)}
    triangle = {"w": (7.0, 1.9), "a": (8.0, 0.1), "b": (6.0, 0.1)}
    draw_graph(axes[0], square, [("u", "v"), ("v", "a"),
                               ("a", "b"), ("b", "u")], frozenset("uv"))
    draw_graph(axes[0], triangle, [("w", "a"), ("a", "b"), ("b", "w")])
    before = {"u": (0.9, 1.9), "v": (2.9, 1.9), "a": (1.9, 0.1)}
    after = {"w": (6.0, 1.0), "a": (8.0, 1.0)}
    draw_graph(axes[1], before, [("u", "v"), ("u", "a"), ("v", "a")],
               frozenset("uv"))
    draw_graph(axes[1], after, [("w", "a")])
    captions = [
        (r"$C_4$: 4 vertices, 4 edges", r"$K_3$: 3 vertices, 3 edges",
         r"$N(u)\cap N(v)=\varnothing$", "Lose only uv: 4 − 1 = 3 edges"),
        (r"$K_3$: 3 vertices, 3 edges", r"$K_2$: 2 vertices, 1 edge",
         r"$N(u)\cap N(v)=\{a\}$", "Lose uv and one duplicate: 3 − 1 − 1 = 1 edge"),
    ]
    for ax, (left, right, common, count) in zip(axes, captions):
        ax.text(1.9, 2.55, left, ha="center", fontsize=12, weight="bold")
        ax.text(7.0, 2.55, right, ha="center", fontsize=12, weight="bold")
        ax.annotate("", xy=(5.55, 1.05), xytext=(3.6, 1.05),
                    arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#34495e"})
        ax.text(4.6, 1.65, "contract uv", color="#b33127", ha="center")
        ax.text(4.6, 0.45, common, ha="center", fontsize=12)
        ax.text(4.6, -0.65, count, ha="center", fontsize=12)
        ax.set(xlim=(0, 9.2), ylim=(-0.95, 2.95), aspect="equal")
        ax.axis("off")
    fig.suptitle("Edge contraction: merge u and v into w", fontsize=16, weight="bold")
    fig.subplots_adjust(top=0.88, bottom=0.03, hspace=0.13, left=0.025, right=0.975)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
