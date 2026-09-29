"""Triangle deletion-contraction, with exact three-color counts; PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt


def draw(ax, positions, edges, highlight=None):
    for edge in edges:
        x1, y1 = positions[edge[0]]
        x2, y2 = positions[edge[1]]
        selected = edge == highlight
        ax.plot([x1, x2], [y1, y2],
                color="#ba3a3a" if selected else "#404040",
                lw=3 if selected else 2, zorder=1)
    for label, (x, y) in positions.items():
        ax.scatter(x, y, s=1600, facecolor="#e8f0f6",
                   edgecolor="#246a9b", linewidth=2, zorder=2)
        ax.text(x, y, label, ha="center", va="center", fontsize=13, zorder=3)
    ax.set(xlim=(-1.2, 1.2), ylim=(-1.05, 1.15), aspect="equal")
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.5), dpi=120)
    fig.patch.set_facecolor("white")
    pos = {"A": (-0.75, 0.6), "B": (0, -0.6), "C": (0.75, 0.6)}
    draw(axes[0], pos, [("A", "B"), ("B", "C"), ("A", "C")], ("A", "C"))
    draw(axes[1], pos, [("A", "B"), ("B", "C")])
    draw(axes[2], {"AC": (0, 0.6), "B": (0, -0.6)}, [("AC", "B")])
    titles = ["G: triangle", "G − e: delete AC", "G / e: merge A and C"]
    counts = ["6 colourings", "12 colourings", "6 colourings"]
    for ax, title, count in zip(axes, titles, counts):
        ax.set_title(title, fontsize=12, pad=7)
        ax.text(0.5, -0.015, count, transform=ax.transAxes,
                ha="center", fontsize=13, weight="bold")
    fig.suptitle(r"$P_G(t)=P_{G-e}(t)-P_{G/e}(t)$", fontsize=18, y=0.97)
    fig.text(0.5, 0.035,
             "At t = 3: 6 = 12 − 6. Duplicate edges after contraction impose the same constraint.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.77, bottom=0.18, wspace=0.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
