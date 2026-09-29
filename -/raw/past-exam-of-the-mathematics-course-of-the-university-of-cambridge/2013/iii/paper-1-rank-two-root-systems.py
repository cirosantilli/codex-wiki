"""Original crystallographic root diagrams; write the opaque PNG to the cwd."""
import os
from pathlib import Path
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

SQRT3 = np.sqrt(3.0)
SYSTEMS = [
    (r"$A_1\times A_1$: 4 roots, 4 chambers", (1, 0), (0, 1), [(1, 0), (0, 1)], 0, 90),
    (r"$A_2$: 6 roots, 6 chambers", (1, 0), (-0.5, SQRT3 / 2), [(1, 0), (0, 1), (1, 1)], 30, 90),
    (r"$B_2$: 8 roots, 8 chambers", (1, -1), (0, 1), [(1, 0), (0, 1), (1, 1), (1, 2)], 0, 45),
    (r"$G_2$: 12 roots, 12 chambers", (1, 0), (-1.5, SQRT3 / 2), [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)], 60, 90),
]

def main():
    fig, axes = plt.subplots(2, 2, figsize=(10, 7), dpi=100)
    fig.patch.set_facecolor("white")
    for ax, (title, aa, bb, coeffs, theta1, theta2) in zip(axes.flat, SYSTEMS):
        a, b = np.array(aa, dtype=float), np.array(bb, dtype=float)
        positive = np.array([i * a + j * b for i, j in coeffs])
        roots = np.concatenate((positive, -positive))
        extent = 1.32 * max(np.linalg.norm(roots, axis=1))
        ax.set_facecolor("white")
        ax.add_patch(Wedge((0, 0), 0.96 * extent, theta1, theta2, facecolor="#f8cf82", alpha=0.65, edgecolor="none"))
        walls = set()
        for root in positive:
            angle = float((np.arctan2(root[1], root[0]) + np.pi / 2) % np.pi)
            key = round(angle, 10)
            if key not in walls:
                walls.add(key)
                direction = np.array([np.cos(angle), np.sin(angle)]) * 1.5 * extent
                ax.plot([-direction[0], direction[0]], [-direction[1], direction[1]], color="#999999", linestyle="--", linewidth=0.8, zorder=1)
        for root in roots:
            simple = np.allclose(root, a) or np.allclose(root, b)
            color = "#b23b20" if simple else "#225f91"
            ax.annotate("", xy=root, xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": color, "lw": 1.6 if simple else 1.1}, zorder=3)
            ax.plot(*root, "o", color=color, ms=3, zorder=4)
        for root, label in [(a, r"$\alpha_1$"), (b, r"$\alpha_2$")]:
            spot = root * 1.13
            ax.text(*spot, label, color="#a1321c", ha="center", va="center", fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.3}, zorder=5)
        ax.plot(0, 0, "o", color="#333333", ms=2, zorder=6)
        ax.set(xlim=(-extent, extent), ylim=(-extent, extent), xticks=[], yticks=[])
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=12, pad=5)
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.suptitle("Rank-two root systems and their reflecting lines", fontsize=15, y=0.975)
    fig.text(0.5, 0.025, "Red: chosen simple roots    Dashed: reflection walls    Orange: fundamental chamber", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.035, right=0.965, top=0.90, bottom=0.075, hspace=0.22, wspace=0.12)
    fig.savefig("paper-1-rank-two-root-systems.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
