"""Compare a sharp directed cut with a cut having incoming original flow."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


def draw_panel(ax, pos, left, cut_x, offsets):
    ax.set(xlim=(-0.55, 4.3), ylim=(-1.65, 1.65), aspect="equal")
    ax.axis("off")
    ax.add_patch(Rectangle((-0.45, -1.5), cut_x + 0.45, 3,
                           facecolor="#edf5fc", edgecolor="none", zorder=0))
    ax.plot([cut_x, cut_x], [-1.5, 1.5], linestyle="--", color="#6a7d8b", linewidth=1.5)
    ax.text(-0.20, 1.34, "S", color="#246ba8", fontsize=15, weight="bold")
    ax.text(cut_x + 0.22, 1.34, "V ∖ S", color="#526570", fontsize=13)
    edges = [("s", "a", 3), ("s", "b", 2), ("a", "b", 1), ("a", "t", 2), ("b", "t", 3)]
    for u, v, amount in edges:
        forward = u in left and v not in left
        backward = u not in left and v in left
        color = "#237b50" if forward else "#b84436" if backward else "#a7b3bc"
        ax.add_patch(FancyArrowPatch(pos[u], pos[v], arrowstyle="-|>",
                                    mutation_scale=19, shrinkA=17, shrinkB=17,
                                    linewidth=2.7 if forward or backward else 1.7,
                                    color=color, zorder=2))
        dx, dy = offsets[u, v]
        ax.text((pos[u][0] + pos[v][0]) / 2 + dx,
                (pos[u][1] + pos[v][1]) / 2 + dy, f"{amount}/{amount}",
                ha="center", va="center", fontsize=13, color=color,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2}, zorder=4)
    for node, xy in pos.items():
        ax.add_patch(Circle(xy, 0.16, facecolor="white", edgecolor="#23465d", linewidth=2, zorder=5))
        ax.text(*xy, node, ha="center", va="center", fontsize=16, zorder=6)


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.8, 5.6), dpi=100, facecolor="white")
    left_ax = fig.add_axes((0.035, 0.25, 0.45, 0.57))
    right_ax = fig.add_axes((0.52, 0.25, 0.45, 0.57))
    left_pos = {"s": (0, 0), "a": (2, 1), "b": (2, -1), "t": (3.8, 0)}
    left_offsets = {("s", "a"): (-0.04, 0.24), ("s", "b"): (-0.04, -0.24),
                    ("a", "b"): (0.32, 0), ("a", "t"): (0.1, 0.24), ("b", "t"): (0.1, -0.24)}
    draw_panel(left_ax, left_pos, {"s"}, 0.68, left_offsets)
    right_pos = {"s": (0, 0.9), "b": (0, -0.9), "a": (3.2, 0.9), "t": (3.2, -0.9)}
    right_offsets = {("s", "a"): (0, 0.23), ("s", "b"): (-0.35, 0),
                     ("a", "b"): (-0.08, -0.30), ("a", "t"): (0.34, 0), ("b", "t"): (0, -0.24)}
    draw_panel(right_ax, right_pos, {"s", "b"}, 1.60, right_offsets)
    fig.text(0.5, 0.94, "Cut capacity counts only forward edges", ha="center", fontsize=20, weight="bold")
    fig.text(0.26, 0.84, "S = {s}: an optimality certificate", ha="center", fontsize=14, weight="bold")
    fig.text(0.74, 0.84, "S = {s, b}: a looser bound", ha="center", fontsize=14, weight="bold")
    fig.text(0.26, 0.235, "Cut capacity = 3 + 2 = 5", ha="center", fontsize=14, color="#237b50")
    fig.text(0.74, 0.235, "Cut capacity = 3 + 3 = 6", ha="center", fontsize=14, color="#237b50")
    fig.text(0.26, 0.177, "Net flow = 5 − 0 = 5", ha="center", fontsize=14)
    fig.text(0.74, 0.177, "Net flow = 6 − 1 = 5", ha="center", fontsize=14)
    fig.text(0.5, 0.104, "Green: forward crossing    Red: backward crossing    Gray: internal", ha="center", fontsize=12)
    fig.text(0.5, 0.049, "Labels: flow / capacity. The red edge's capacity is excluded from the cut sum.", ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
