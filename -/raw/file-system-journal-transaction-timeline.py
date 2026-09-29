"""Draw a full-data redo journal timeline; tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5. Run from _media to write the PNG there.
The horizontal positions express dependencies, not measured durations.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(12, 6.1), dpi=100, facecolor="white")
    ax.set(xlim=(-0.25, 12), ylim=(-0.6, 5.5))
    ax.axis("off")
    fig.subplots_adjust(left=0.015, right=0.985, top=0.93, bottom=0.09)
    ax.text(5.8, 5.3, "Full-data journaling: commit before checkpoint", ha="center",
            fontsize=18, weight="bold", color="#15354a")
    ax.text(5.8, 4.91, "One append • atomic records • honored flushes • no other writer",
            ha="center", fontsize=12, color="#435667")

    def box(x, y, width, text, color, fontsize=12):
        ax.add_patch(FancyBboxPatch((x, y), width, 0.75, boxstyle="round,pad=0.07",
                                   facecolor=color, edgecolor="#365466", linewidth=1.2))
        ax.text(x + width / 2, y + 0.375, text, ha="center", va="center",
                fontsize=fontsize, color="#132e3e")

    for y, label in [(3.75, "Journal"), (2.55, "Final locations"), (1.25, "Crash outcome")]:
        ax.text(0, y, label, fontsize=12, weight="bold", va="center")

    box(1.6, 3.4, 2.0, "Write payload\nI + B + D", "#dcecf7")
    box(4.0, 3.4, 1.75, "Write commit\nmarker", "#c8e9e4")
    box(9.65, 3.4, 1.8, "Retire journal\nspace reusable", "#e4e7ec", 11)
    box(6.1, 2.2, 2.75, "Checkpoint I + B + D\n(any write order)", "#f7e3bb")
    ax.plot([1.6, 5.75], [2.58, 2.58], color="#7d94a1", lw=2)
    ax.text(3.65, 2.82, "Keep final records old", ha="center", fontsize=11)
    ax.annotate("", xy=(9.6, 2.58), xytext=(8.9, 2.58),
                arrowprops={"arrowstyle": "->", "color": "#365466", "lw": 1.5})

    for x, label in [(3.8, "Payload\nflush"), (5.95, "Commit\nflush"), (9.2, "Checkpoint\nflush")]:
        ax.plot([x, x], [1.85, 4.3], color="#b84c35", lw=1.6, linestyle="--")
        ax.text(x, 4.48, label, ha="center", va="center", fontsize=11,
                color="#a13d2d", weight="bold")

    ax.annotate("", xy=(6.06, 2.92), xytext=(5.72, 3.39),
                arrowprops={"arrowstyle": "->", "color": "#365466", "lw": 1.5})
    ax.text(6.25, 3.65, "Durable decision:\nacknowledgment may follow", fontsize=11,
            color="#126b5c", va="center")
    box(1.6, 0.85, 4.1, "No durable commit → old file\nIgnore incomplete payload", "#edf3f8", 11)
    box(6.05, 0.85, 3.25, "Durable commit → new file\nReplay any missing copies", "#e3f2ee", 11)
    box(9.65, 0.85, 1.8, "New file\nalready durable", "#edf0f3", 11)
    ax.annotate("", xy=(11.7, 0.47), xytext=(1.6, 0.47),
                arrowprops={"arrowstyle": "->", "color": "#365466", "lw": 1.4})
    ax.text(6.6, 0.2, "Persistence dependencies (not elapsed time)", ha="center", fontsize=11)
    fig.text(0.5, 0.025, "I: inode size 4 → 8, references 7 → 7 & 9    B: block 9 free → allocated    D: block 9 → EFGH",
             ha="center", fontsize=11, color="#435667")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
