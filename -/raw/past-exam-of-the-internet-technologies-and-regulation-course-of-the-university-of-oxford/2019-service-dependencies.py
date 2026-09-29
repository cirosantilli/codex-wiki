"""Illustrative mandatory dependencies, not a measurement of a real service.

Run from the desired output directory; uses Matplotlib only.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, ax = plt.subplots(figsize=(8.4, 4.0), dpi=120, facecolor="white")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_axis_off()

def box(center, text, color):
    x, y = center
    width, height = 0.29, 0.21
    patch = FancyBboxPatch((x-width/2, y-height/2), width, height,
                          boxstyle="round,pad=0.015,rounding_size=0.018",
                          facecolor=color, edgecolor="#34495e", linewidth=1.5)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", linespacing=1.45)

box((0.22, 0.69), "Replica A\nlocal data copy", "#e5f0fa")
box((0.78, 0.69), "Replica B\nlocal data copy", "#e5f0fa")
box((0.50, 0.25), "Shared identity provider\nrequired for a fresh login", "#fff0dc")
for start, end, label_at in [((0.28, 0.565), (0.43, 0.37), (0.28, 0.43)),
                             ((0.72, 0.565), (0.57, 0.37), (0.72, 0.43))]:
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=17, linewidth=1.8,
                                color="#7d3434", shrinkA=2, shrinkB=2))
    ax.text(*label_at, "requires", ha="center", va="center", color="#643333")
ax.text(0.5, 0.96, "Two replicas, one mandatory shared dependency",
        ha="center", va="top", fontsize=15, fontweight="bold")
ax.text(0.5, 0.035, "Assumption: a new login must receive a fresh response from the provider.",
        ha="center", va="bottom", fontsize=10, color="#444444")
fig.subplots_adjust(left=0.025, right=0.975, top=0.975, bottom=0.035)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, facecolor="white")
plt.close(fig)
