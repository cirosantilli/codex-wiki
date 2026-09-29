"""Original adsorption schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; emits adsorption-sites-and-occupation.png in the CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 6), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 6, height_ratios=(1, 1.12))
    occupied_sets = ({0, 5, 10}, {0, 2, 5, 7, 8, 10}, set(range(12)))
    blue, gray = "#167da5", "#64748b"
    for panel, (occupied, fraction) in enumerate(zip(occupied_sets, ("1/4", "1/2", "1"))):
        ax = fig.add_subplot(grid[0, 2 * panel:2 * panel + 2])
        ax.set(xlim=(-0.5, 3.5), ylim=(-0.6, 2.9), aspect="equal")
        ax.axis("off")
        for i in range(12):
            x, y = i % 4, 2 - i // 4
            ax.add_patch(Rectangle((x - 0.31, y - 0.31), 0.62, 0.62,
                                   edgecolor=gray, facecolor="#f1f5f9", linewidth=1.4))
            if i in occupied:
                ax.add_patch(Circle((x, y), 0.21, facecolor=blue, edgecolor="white"))
        ax.set_title(f"{len(occupied)} of 12 occupied\n" + rf"$\theta = {fraction}$", pad=8)
    for k, title in enumerate(("Adsorption: at the boundary", "Absorption: within the bulk")):
        ax = fig.add_subplot(grid[1, k * 3:k * 3 + 3])
        ax.set(xlim=(0, 6), ylim=(-0.4, 3), aspect="equal")
        ax.axis("off")
        ax.add_patch(Rectangle((0.3, 0), 5.4, 1.65, facecolor="#e2e8f0", edgecolor=gray))
        ax.text(3, 0.25, "Material interior", ha="center", color="#334155")
        positions = ((1.1, 1.65), (2.1, 1.65), (4.0, 1.65), (5.0, 1.65)) if k == 0 else (
            (1.0, 1.1), (2.4, 0.7), (3.5, 1.3), (4.9, 0.9))
        for x, y in positions:
            ax.add_patch(Circle((x, y), 0.14, facecolor=blue, edgecolor="white"))
        ax.annotate("Surrounding phase", (3, 2.4), ha="center", color="#334155")
        ax.set_title(title, pad=2)
    fig.suptitle("A site can be vacant or occupied by one molecule", fontsize=16)
    fig.supxlabel("Schematic configurations and locations; not microscopy or measured data", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
