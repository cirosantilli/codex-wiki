"""Mean-field phase diagram; Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.

Writes an opaque 600 x 500 PNG to the current working directory. The shared
Makefile can generate its _media target after central integration of this file.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon

fig, ax = plt.subplots(figsize=(6, 5), dpi=100, facecolor="white")
fig.subplots_adjust(left=.12, right=.96, bottom=.16, top=.91)
L = 2.5
ax.add_patch(Polygon([(0, 0), (L, 0), (L, L), (0, L)], facecolor="#eeeeee"))
ax.add_patch(Polygon([(-L, -L), (-L, L), (0, L), (0, 0)], facecolor="#cde4f6"))
ax.add_patch(Polygon([(-L, -L), (0, 0), (L, 0), (L, -L)], facecolor="#ffe0bc"))
ax.plot([0, 0], [0, L], color="#2268a0", linewidth=2.5)
ax.plot([0, L], [0, 0], color="#2268a0", linewidth=2.5)
ax.plot([-L, 0], [-L, 0], color="#b53030", linewidth=2.5, linestyle="--")
ax.plot([0], [0], marker="*", markersize=13, color="#282828", zorder=5)
ax.text(1.15, 1.45, "Disordered\n" + r"$\phi_1=\phi_2=0$", ha="center", va="center")
ax.text(-1.3, 1.1, r"$\phi_1$ ordered" + "\n" + r"$\phi_2=0$", ha="center", va="center")
ax.text(1.1, -1.35, r"$\phi_2$ ordered" + "\n" + r"$\phi_1=0$", ha="center", va="center")
ax.text(-1.53, -1.0, "Circle of minima", rotation=37, color="#922020", fontsize=9)
ax.annotate("Bicritical point", xy=(0, 0), xytext=(.3, .48), fontsize=9,
            arrowprops={"arrowstyle": "->", "color": "#555555"})
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)
ax.set_xlabel(r"$r_1=\mu_1^2$", fontsize=12)
ax.set_ylabel(r"$r_2=\mu_2^2$", fontsize=12)
ax.set_xticks([-2, 0, 2])
ax.set_yticks([-2, 0, 2])
ax.set_title("Mean-field phases for a radial quartic interaction", fontsize=11)
handles = [Line2D([], [], color="#2268a0", linewidth=2.5, label="Continuous transition"),
           Line2D([], [], color="#b53030", linewidth=2.5, linestyle="--", label="First-order transition")]
fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(.54, .008), ncol=2, frameon=False, fontsize=9)
fig.savefig(Path.cwd() / "paper-303-phase-diagram.png", dpi=100, facecolor="white", transparent=False)
plt.close(fig)
