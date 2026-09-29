"""Original Q5 force diagram; writes its PNG into the current directory.

Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7 (root pyproject.toml).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, displacement, label, offset=(0, 0)):
    end = np.asarray(start) + displacement
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": "#b04430", "lw": 2})
    ax.text(*(end + offset), label, fontsize=12, ha="center", va="center")


def main():
    fig, ax = plt.subplots(figsize=(7.4, 5.0), facecolor="white")
    ax.plot([-2.7, 0, 2.7], [-2.7, 0, -2.7], color="#999999", lw=3)
    ax.plot([0, 1.8], [0, -1.8], color="#17658a", lw=2)
    ax.plot([0, 0], [0, -3.35], color="#17658a", lw=2)
    ax.scatter([1.8, 0], [-1.8, -3.35], s=95, color="#222222", zorder=4)
    ax.scatter([0], [0], s=24, color="#222222", zorder=4)
    ax.text(-0.22, 0.17, "$O$", fontsize=12)
    ax.text(1.5, -1.67, "$m_1$", fontsize=12, ha="right")
    ax.text(-0.22, -3.32, "$m_2$", fontsize=12, ha="right")
    arrow(ax, (1.8, -1.8), (0, -0.8), "$m_1g$", (0.35, 0))
    arrow(ax, (1.8, -1.8), (-0.62, 0.62), r"$\mathbf{T}_1$", (-0.2, 0.08))
    arrow(ax, (1.8, -1.8), (0.62, 0.62), r"$\mathbf{N}$", (0.15, 0.15))
    arrow(ax, (0, -3.35), (0, 0.8), r"$\mathbf{T}_2$", (0.32, 0))
    arrow(ax, (0, -3.35), (0, -0.7), "$m_2g$", (0.35, 0))
    ax.text(-2.65, -2.35, "Cone: $z=-r$", fontsize=11)
    ax.text(0.7, -0.5, r"$|\mathbf{r}_1|=\sqrt{2}r_1$", fontsize=10, rotation=-45)
    ax.text(-0.2, -1.55, "$-z_2$", fontsize=11, rotation=90, ha="right")
    arrow(ax, (-2.4, -3.9), (0.65, 0), r"$\mathbf{e}_r$", (0.2, 0))
    arrow(ax, (-2.4, -3.9), (0, 0.65), r"$\mathbf{e}_z$", (0, 0.2))
    ax.set_title("Cone and hanging particle: all applied forces")
    ax.set(xlim=(-3.1, 3.1), ylim=(-4.35, 0.55))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
