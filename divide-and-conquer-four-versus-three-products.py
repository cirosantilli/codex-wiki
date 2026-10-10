"""Compare exact four-product and Karatsuba ledgers for 47 times 63."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(10.6, 6.6), dpi=120, facecolor="white")
    ax = fig.add_axes((0, 0, 1, 1), facecolor="white")
    ax.set(xlim=(0, 10.6), ylim=(0, 6.6))
    ax.axis("off")
    ink, blue, orange = "#172d41", "#17618f", "#b25a16"
    ax.text(0.4, 6.17, "47 × 63: count the required block products", color=ink,
            fontsize=19, weight="bold")
    ax.text(0.4, 5.72, r"$47=4\cdot10+7,\qquad 63=6\cdot10+3$", color=ink, fontsize=16)

    def box(x, y, width, height, fill, edge):
        ax.add_patch(FancyBboxPatch((x, y), width, height,
                                   boxstyle="round,pad=0.04,rounding_size=0.08",
                                   facecolor=fill, edgecolor=edge, linewidth=1))

    for x, title, edge, fill in [(0.42, "4 block multiplications", orange, "#fff4e9"),
                                (5.52, "3 block multiplications", blue, "#eef5fa")]:
        box(x, 2.28, 4.65, 2.98, fill, edge)
        ax.text(x + 2.325, 4.91, title, color=edge, fontsize=16, ha="center", weight="bold")
    left_rows = [r"$ac=4\cdot6=24$", r"$bd=7\cdot3=21$",
                 r"$ad=4\cdot3=12$", r"$bc=7\cdot6=42$"]
    right_rows = [r"$u=ac=4\cdot6=24$", r"$v=bd=7\cdot3=21$",
                  r"$w=(4+7)(6+3)$", r"$w=11\cdot9=99$"]
    for j, (left, right) in enumerate(zip(left_rows, right_rows)):
        y = 4.41 - 0.46 * j
        ax.text(0.77, y, left, fontsize=15, color=ink)
        ax.text(5.87, y, right, fontsize=15, color=ink)
    ax.text(2.74, 2.51, "Cross sum: 12 + 42 = 54", ha="center", color=orange, fontsize=13)
    ax.text(7.84, 2.51, "Cross sum: 99 − 24 − 21 = 54", ha="center", color=blue, fontsize=13)

    ax.text(2.74, 1.92, "Compute both cross products", ha="center", color=orange, fontsize=12)
    ax.text(7.84, 1.92, "Reuse the outer products", ha="center", color=blue, fontsize=12)
    box(0.8, 0.86, 9.0, 0.70, "#f0f6ee", "#5e8053")
    ax.text(5.3, 1.21, r"$24\cdot100+54\cdot10+21=2400+540+21=2961$",
            ha="center", va="center", fontsize=17, color=ink)
    ax.text(0.42, 0.37, "The third product has an extra digit (11); this ledger counts one split, not timings.",
            color=ink, fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
