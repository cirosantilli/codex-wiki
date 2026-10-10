"""Draw the original bounded queue example; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def box(ax, x, y, w, h, text, color, size=13):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor="#344054", linewidth=1.5))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size)


def arrow(ax, start, end, color="#245b8c", dashed=False):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=17,
                                color=color, linewidth=2,
                                linestyle="--" if dashed else "-"))


def main():
    fig, ax = plt.subplots(figsize=(11, 6.6), dpi=110, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 6.6))
    ax.axis("off")
    ax.text(5.5, 6.3, "A bounded queue protects transitions, not just fields",
            ha="center", fontsize=18, weight="bold")
    ax.text(5.5, 5.85, "Original sequential example • capacity C = 3 • immutable labels",
            ha="center", fontsize=12, color="#475467")
    box(ax, 0.35, 3.1, 2.1, 1.2, "Client code\nrequests operations", "#edf3fa")
    box(ax, 3.25, 2.55, 2.15, 2.35,
        "API\n\nenqueue / dequeue\npeek / size\n\nfull / empty: unchanged", "#e3f2e8", 12)
    ax.add_patch(FancyBboxPatch((6.05, 2.1), 4.5, 3.15, boxstyle="round,pad=0.03",
                               facecolor="#f8fafc", edgecolor="#245b8c", linewidth=2))
    ax.text(8.3, 4.95, "Implementation boundary", ha="center", fontsize=14, weight="bold")
    box(ax, 6.4, 3.45, 1.55, 0.8, "q = (A, B)\nn = 2", "#edf3fa", 12)
    box(ax, 8.65, 3.45, 1.55, 0.8, "q = (A, B, C)\nn = 3", "#e3f2e8", 12)
    arrow(ax, (7.99, 3.85), (8.6, 3.85))
    ax.text(8.28, 4.4, "enqueue(C): ok", ha="center", fontsize=11)
    ax.text(8.3, 2.95, "Valid storage: 0 ≤ n ≤ 3", ha="center", fontsize=13)
    ax.text(8.3, 2.5, "enqueue(D) now returns full; state unchanged", ha="center", fontsize=11)
    arrow(ax, (2.5, 3.7), (3.2, 3.7))
    arrow(ax, (5.45, 3.7), (6.0, 3.7))
    arrow(ax, (1.4, 3.0), (7.4, 1.3), color="#b42318", dashed=True)
    box(ax, 7.4, 0.85, 2.65, 0.95, "Raw write: n ← 4\ninvalid storage", "#fce9e6", 12)
    ax.text(3.5, 1.7, "Unrestricted mutation bypasses the API", ha="center",
            fontsize=12, color="#b42318", rotation=-15)
    ax.text(5.5, 0.2, "Even n ← 1 from (A, B) meets the bounds but discards B without a permitted call.",
            ha="center", fontsize=11, color="#475467")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
