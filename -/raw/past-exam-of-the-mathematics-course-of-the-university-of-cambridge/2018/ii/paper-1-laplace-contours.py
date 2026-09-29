from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


def arrow_path(ax, x, y, color, label=None):
    ax.plot(x, y, color=color, linewidth=2.4, label=label)
    k = len(x) // 2
    ax.add_patch(
        FancyArrowPatch(
            (x[k - 1], y[k - 1]),
            (x[k + 1], y[k + 1]),
            arrowstyle="-|>",
            mutation_scale=14,
            color=color,
            linewidth=2.4,
        )
    )


def setup(ax, title, xlim):
    ax.axhline(0, color="0.65", linewidth=0.8)
    ax.axvline(0, color="0.65", linewidth=0.8)
    ax.scatter([0, 0], [1, -1], color="black", zorder=5)
    ax.text(0.08, 1.03, r"$i$", fontsize=12)
    ax.text(0.08, -1.15, r"$-i$", fontsize=12)
    ax.set_xlim(*xlim)
    ax.set_ylim(-1.45, 1.45)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel(r"$\operatorname{Re}t$")
    ax.set_ylabel(r"$\operatorname{Im}t$")
    ax.set_title(title)
    ax.grid(alpha=0.18)


fig, axes = plt.subplots(1, 3, figsize=(12, 4), constrained_layout=True)

s = np.linspace(0, 1, 240)
y = -1 + 2 * s
setup(axes[0], "Finite contours", (-1.65, 1.65))
arrow_path(axes[0], -1.15 * np.sin(np.pi * s), y, "#1f77b4", r"$\gamma_L$")
arrow_path(axes[0], 1.15 * np.sin(np.pi * s), y, "#d62728", r"$\gamma_R$")
axes[0].plot([0, 0], [-1, 1], color="0.4", linestyle="--", linewidth=1, label="branch cut")
axes[0].legend(loc="lower center", fontsize=9)

setup(axes[1], r"Infinite contours for $z>0$", (-3.2, 0.55))
x = np.linspace(-3, 0, 240)
bend = (x + 3) / 3
arrow_path(axes[1], x, bend**3, "#1f77b4", r"$-\infty\to i$")
arrow_path(axes[1], x, -bend**3, "#d62728", r"$-\infty\to-i$")
axes[1].text(-3.08, 0.13, r"$-\infty$", fontsize=11)
axes[1].legend(loc="lower center", fontsize=9)

setup(axes[2], r"Infinite contours for $z<0$", (-0.55, 3.2))
x = np.linspace(0, 3, 240)
bend = x / 3
arrow_path(axes[2], x, 1 - bend**3, "#1f77b4", r"$i\to+\infty$")
arrow_path(axes[2], x, -1 + bend**3, "#d62728", r"$-i\to+\infty$")
axes[2].text(2.7, 0.13, r"$+\infty$", fontsize=11)
axes[2].legend(loc="lower center", fontsize=9)

fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=100, facecolor="white")
