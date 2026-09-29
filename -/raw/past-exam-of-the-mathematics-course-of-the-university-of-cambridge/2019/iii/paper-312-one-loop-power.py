#!/usr/bin/env python3
"""Render the P22 and P13 Wick-contraction diagrams to the current directory."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.path import Path as MplPath
from matplotlib.patches import FancyArrowPatch, PathPatch

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), dpi=100, facecolor="white")
blue = "#24658a"
red = "#a23f37"

for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(-2.4, 3.8)
    ax.axis("off")
    ax.plot([0.5, 2.7], [0, 0], color="#333333", lw=2)
    ax.plot([7.3, 9.5], [0, 0], color="#333333", lw=2)
    ax.scatter([0.5, 9.5], [0, 0], color="#333333", s=42, zorder=5)
    ax.text(0.5, -0.55, r"$\delta(\mathbf{k})$", ha="center", fontsize=13)
    ax.text(9.5, -0.55, r"$\delta(-\mathbf{k})$", ha="center", fontsize=13)

ax = axes[0]
ax.set_title(r"$P_{22}$: two second-order density fields", fontsize=14, pad=8)
ax.scatter([2.7, 7.3], [0, 0], color=red, s=100, zorder=5)
for curvature in [-0.65, 0.65]:
    ax.add_patch(FancyArrowPatch(
        (2.7, 0), (7.3, 0), connectionstyle=f"arc3,rad={curvature}",
        arrowstyle="-", linestyle="--", mutation_scale=1,
        color=blue, lw=2.2,
    ))
ax.text(5, 1.8, r"$P_{\rm lin}(q)$", ha="center", fontsize=13, color=blue)
ax.text(5, -2.1, r"$P_{\rm lin}(|\mathbf{k}-\mathbf{q}|)$",
        ha="center", fontsize=13, color=blue)
ax.text(2.5, 0.5, r"$F_{2,s}$", ha="right", fontsize=14, color=red)
ax.text(7.5, 0.5, r"$F_{2,s}$", ha="left", fontsize=14, color=red)

ax = axes[1]
ax.set_title(r"$P_{13}$: one linear and one cubic field", fontsize=14, pad=8)
ax.scatter([2.7, 7.3], [0, 0], color=red, s=100, zorder=5)
ax.plot([2.7, 7.3], [0, 0], color=blue, lw=2.2, ls="--")
# A loop pairs two of the three inputs to the cubic kernel.
loop = MplPath(
    [(7.3, 0), (4.5, 3.5), (10.1, 3.5), (7.3, 0)],
    [MplPath.MOVETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4],
)
ax.add_patch(PathPatch(loop, facecolor="none", edgecolor=blue, lw=2.2, ls="--"))
ax.text(5, -0.55, r"$P_{\rm lin}(k)$", ha="center", fontsize=13, color=blue)
ax.text(7.3, 2.95, r"$P_{\rm lin}(q)$", ha="center", fontsize=13, color=blue)
ax.text(2.7, 0.5, r"$F_1=1$", ha="center", fontsize=13, color=red)
ax.text(7.5, -0.55, r"$F_{3,s}$", ha="left", fontsize=14, color=red)
ax.text(5, -1.7, "Add the reflected external ordering: total $2P_{13}$",
        ha="center", fontsize=11)

fig.text(0.5, 0.055,
         "Red vertices: density kernels     Dashed blue lines: paired linear fields",
         ha="center", fontsize=12)
fig.subplots_adjust(left=0.04, right=0.96, top=0.84, bottom=0.18, wspace=0.20)
fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
plt.close(fig)
