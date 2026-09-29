"""Highlight a maximum triangle and a smaller maximal edge in one graph."""
from pathlib import Path
import matplotlib.pyplot as plt

POSITIONS = {"a": (-1.1, 1.), "b": (-1.1, -1.), "c": (0., 0.), "d": (1.3, 0.), "e": (2.6, 0.)}
EDGES = [("a", "b"), ("a", "c"), ("b", "c"), ("c", "d"), ("d", "e")]


def panel(ax, selected, color, title, caption):
    for u, v in EDGES:
        inside = u in selected and v in selected
        x1, y1 = POSITIONS[u]; x2, y2 = POSITIONS[v]
        ax.plot([x1, x2], [y1, y2], color=color if inside else "#a1abb3", lw=3 if inside else 1.7, zorder=1)
    for v, (x, y) in POSITIONS.items():
        ax.scatter([x], [y], s=480, facecolor=color if v in selected else "#e1e6ea", edgecolor="white", lw=1.3, zorder=3)
        ax.text(x, y, v, color="white" if v in selected else "#243542", fontsize=15,
                ha="center", va="center", zorder=4)
    ax.set_aspect("equal"); ax.set(xlim=(-1.5, 3), ylim=(-1.5, 1.55)); ax.axis("off")
    ax.set_title(title, fontsize=14)
    ax.text(.5, -.015, caption, transform=ax.transAxes, fontsize=11, ha="center", va="top")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.9), dpi=100, facecolor="white")
    panel(axes[0], {"a", "b", "c"}, "#b64a3b", "Maximum clique: {a, b, c}",
          "All three pairs are edges.\nNo clique in this graph has four vertices.")
    panel(axes[1], {"c", "d"}, "#235e88", "Maximal clique: {c, d}",
          "No outside vertex can join this pair.\nIt is smaller than the maximum clique.")
    fig.suptitle("Maximal means inclusion cannot grow; maximum means largest size", fontsize=16)
    fig.tight_layout(rect=(0, .12, 1, .91), w_pad=3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
