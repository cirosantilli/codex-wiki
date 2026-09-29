"""Contrast incorrect empty-slot deletion and tombstones. Python 3.14; matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_xlim(0, 11.6)
    ax.set_ylim(-0.4, 6.55)
    ax.axis("off")
    ax.text(0.1, 6.14, "A deletion marker preserves the route to key 16", fontsize=19, weight="bold")
    ax.text(0.1, 5.70, "Same original table; remove key 8, then search for 16 from h(16) = 0.", fontsize=12)
    rows = [
        ("Before deletion", [0, 8, 16, 9, "E", "E", "E", "E"], [0, 1, 2], "Finds 16 at index 2", "#247148"),
        ("Wrong: write E", [0, "E", 16, 9, "E", "E", "E", "E"], [0, 1], "Stops at index 1; misses the stored key", "#b33e32"),
        ("Correct: write D", [0, "D", 16, 9, "E", "E", "E", "E"], [0, 1, 2], "Passes D; finds 16 at index 2", "#247148"),
    ]
    for row, (label, keys, probes, outcome, outcome_color) in enumerate(rows):
        y = 4.52 - row * 1.70
        ax.text(0.1, y + 0.32, label, fontsize=13, weight="bold", va="center")
        for index, key in enumerate(keys):
            x = 3.0 + index
            color = "white" if key == "E" else "#d9e9f3"
            if key == "D":
                color = "#ffe5b7"
            if row == 1 and index == 1:
                color = "#f9d9d5"
            if key == 16 and index in probes:
                color = "#d6eedc"
            ax.add_patch(Rectangle((x, y), 0.91, 0.62, facecolor=color, edgecolor="#344a5a", linewidth=1.1))
            ax.text(x + 0.455, y + 0.31, str(key), ha="center", va="center", fontsize=15)
            ax.text(x + 0.455, y + 0.73, str(index), ha="center", fontsize=10, color="#526370")
        for number, index in enumerate(probes, start=1):
            ax.text(3.455 + index, y - 0.27, str(number), ha="center", fontsize=11, color="#af5900", weight="bold")
        for previous, current in zip(probes, probes[1:]):
            ax.annotate("", xy=(3.455 + current - 0.12, y - 0.21),
                        xytext=(3.455 + previous + 0.12, y - 0.21),
                        arrowprops={"arrowstyle": "->", "color": "#af5900", "lw": 1.7})
        ax.text(3.0, y - 0.63, outcome, color=outcome_color, fontsize=12)
    ax.text(0.1, -0.19, "E = never used (stop)     D = deleted (continue)     Orange numbers = probe order", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.985, bottom=0.025, top=0.99)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
