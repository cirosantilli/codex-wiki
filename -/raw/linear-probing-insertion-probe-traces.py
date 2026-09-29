"""Draw original capacity-eight linear-probing insertions. Python 3.14; matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_xlim(0, 11.6)
    ax.set_ylim(-0.55, 7.25)
    ax.axis("off")
    ax.text(0.1, 6.86, "Consecutive probes build one cluster", fontsize=20, weight="bold")
    ax.text(0.1, 6.46, "Capacity 8; h(k) = k mod 8. Cells show keys; associated values are omitted.", fontsize=12)
    rows = [
        ("Insert 0", [0, None, None, None, None, None, None, None], [0], 0),
        ("Insert 8", [0, 8, None, None, None, None, None, None], [0, 1], 1),
        ("Insert 16", [0, 8, 16, None, None, None, None, None], [0, 1, 2], 2),
        ("Insert 9", [0, 8, 16, 9, None, None, None, None], [1, 2, 3], 3),
        ("Find 16", [0, 8, 16, 9, None, None, None, None], [0, 1, 2], 2),
    ]
    for row, (label, keys, probes, stop) in enumerate(rows):
        y = 5.51 - row * 1.19
        ax.text(0.1, y + 0.32, label, fontsize=14, weight="bold", va="center")
        ax.text(0.1, y - 0.02, f"start {probes[0]}; {len(probes)} probe" + ("s" if len(probes) != 1 else ""), fontsize=11)
        for index, key in enumerate(keys):
            x = 3.0 + index
            color = "#d9e9f3" if key is not None else "white"
            if index == stop:
                color = "#d6eedc"
            ax.add_patch(Rectangle((x, y), 0.91, 0.62, facecolor=color,
                                   edgecolor="#344a5a", linewidth=1.1))
            ax.text(x + 0.455, y + 0.31, str(key) if key is not None else "E", ha="center", va="center", fontsize=15)
            ax.text(x + 0.455, y + 0.72, str(index), ha="center", fontsize=10, color="#526370")
        for number, index in enumerate(probes, start=1):
            center = 3.455 + index
            ax.text(center, y - 0.26, str(number), color="#af5900", ha="center", fontsize=11, weight="bold")
        for previous, current in zip(probes, probes[1:]):
            ax.annotate("", xy=(3.455 + current - 0.12, y - 0.21),
                        xytext=(3.455 + previous + 0.12, y - 0.21),
                        arrowprops={"arrowstyle": "->", "color": "#af5900", "lw": 1.7})
    ax.text(0.1, -0.25, "E = never used     Blue = earlier key     Green = placement / match     Orange = probe order", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.985, bottom=0.025, top=0.99)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
