"""Original Q6 side view; writes its PNG into the current directory.

Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7 (root pyproject.toml).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def arrow(ax, start, end, label, label_position):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": "#b04430", "lw": 2})
    ax.text(*label_position, label, fontsize=12, ha="center", va="center")


def main():
    fig, ax = plt.subplots(figsize=(7.1, 5.2), facecolor="white")
    radius, inner, alpha = 1.35, 0.6, np.deg2rad(57)
    ax.add_patch(Circle((0, 0), radius, fill=False, ec="#666666", lw=2))
    ax.add_patch(Circle((0, 0), inner, fc="#edf3f5", ec="#17658a", lw=2))
    ax.plot([-2.05, 2.05], [-radius, -radius], color="#666666", lw=2)
    ax.scatter([0, 0], [0, -radius], color="#222222", s=22, zorder=5)
    q = inner * np.array([np.sin(alpha), -np.cos(alpha)])
    end = q + 1.65 * np.array([np.cos(alpha), np.sin(alpha)])
    arrow(ax, q, end, "$T$", end + (0.13, 0.13))
    ax.scatter(*q, s=22, color="#222222", zorder=5)
    ax.text(*(q + (0.12, -0.18)), "$Q$", fontsize=12)
    ax.plot([0, q[0]], [0, q[1]], color="#17658a", ls="--", lw=1)
    ax.text(0.2, -0.15, "$a$", fontsize=11)
    ax.plot([0, -0.9], [0, 1.0], color="#888888", ls="--", lw=1)
    ax.text(-0.65, 0.48, "$R$", fontsize=11)
    arrow(ax, (0, 0), (0, -0.8), "$mg$", (-0.22, -0.65))
    arrow(ax, (0, -radius), (0, -radius + 0.65), "$2N$", (0.24, -0.92))
    arrow(ax, (0, -radius), (-0.85, -radius), "$2F$", (-0.63, -radius - 0.2))
    ax.text(-0.17, 0.13, "$G$", fontsize=12)
    ax.text(0.16, -radius - 0.18, "$P$", fontsize=12)
    ax.plot([q[0], q[0] + 0.5], [q[1], q[1]], color="#999999", lw=1)
    arc = np.linspace(0, alpha, 50)
    ax.plot(q[0] + 0.35 * np.cos(arc), q[1] + 0.35 * np.sin(arc), color="#777777")
    ax.text(q[0] + 0.45, q[1] + 0.18, r"$\alpha$", fontsize=11)
    arrow(ax, (-1.95, -0.65), (-1.4, -0.65), r"$\mathbf{e}_1$", (-1.3, -0.65))
    arrow(ax, (-1.95, -0.65), (-1.95, -0.1), r"$\mathbf{e}_2$", (-1.95, 0.05))
    ax.text(0, -1.95, "Contact forces shown are totals from the two rails", ha="center", fontsize=10)
    ax.set_title("Tension gives $+aT$ torque; rail friction gives $-2RF$")
    ax.set(xlim=(-2.2, 2.1), ylim=(-2.1, 1.75))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
