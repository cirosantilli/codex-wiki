"""Generate an original sign diagram; write the PNG to the working directory."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "savefig.transparent": False,
})

x = np.linspace(-1.2, 2.5, 601)
v = np.linspace(-1.6, 1.6, 501)
xx, vv = np.meshgrid(x, v)
negative, positive = "#dbe9fb", "#ffe8d2"
fig, axes = plt.subplots(1, 3, figsize=(10.5, 4), dpi=100)
fig.subplots_adjust(left=0.055, right=0.985, bottom=0.22, top=0.76, wspace=0.24)
cases = [(0, "strict local minimum"), (-1, "degenerate saddle"), (-2, "nondegenerate saddle")]
for ax, (alpha, classification) in zip(axes, cases):
    beta = 1 - alpha**2
    difference = xx**3 + beta * xx**2 + vv**2
    ax.contourf(xx, vv, difference, levels=[-100, 0, 100], colors=[negative, positive])
    ax.contour(xx, vv, difference, levels=[-4, -2, -1, -0.25, 0.25, 1, 2, 4, 8],
               colors="#888888", linewidths=0.55, alpha=0.7)
    ax.contour(xx, vv, difference, levels=[0], colors="black", linewidths=1.1)
    ax.scatter([0], [0], marker="*", color="black", s=100, zorder=5)
    other = -2 * beta / 3
    if beta != 0:
        ax.scatter([other], [0], marker="o", facecolors="none", edgecolors="black",
                   s=55, linewidths=1.2, zorder=5)
    ax.axvline(0, color="#555555", linewidth=0.6, alpha=0.6)
    ax.axhline(0, color="#555555", linewidth=0.6, alpha=0.6)
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(v[0], v[-1])
    ax.set_xlabel("$x$")
    ax.set_ylabel("$v$")
    ax.set_title(rf"$\alpha={alpha}$" + "\n" + classification, fontsize=10)
    ax.tick_params(labelsize=8)

fig.suptitle(r"The critical point $(x,y)=(0,-1)$: nearby values above and below it",
             fontsize=12, y=0.975)
fig.text(0.5, 0.86, r"$v=y+1+\alpha x,\qquad f(x,y)-f(0,-1)=x^3+(1-\alpha^2)x^2+v^2$",
         ha="center", fontsize=11)
handles = [
    Patch(facecolor=positive, label="value above the marked point"),
    Patch(facecolor=negative, label="value below the marked point"),
    Line2D([], [], color="black", marker="*", linestyle="", markersize=10, label="point being classified"),
    Line2D([], [], color="black", marker="o", markerfacecolor="none", linestyle="",
           markersize=7, label="other critical point"),
]
fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.015),
           ncol=2, fontsize=9, frameon=False, columnspacing=2)
fig.savefig(Path("mathematics-2014-critical-point-classification.png"), dpi=100)
plt.close(fig)
