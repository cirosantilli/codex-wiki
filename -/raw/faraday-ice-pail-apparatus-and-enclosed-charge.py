"""Original qualitative apparatus and ideal closed-enclosure charge diagrams.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


BLUE = "#176798"
RED = "#b33c35"
GRAY = "#dbe1e6"


def ground(ax, x, y):
    ax.plot([x, x], [y + 0.3, y], color="black", lw=1.5)
    for i, width in enumerate([0.3, 0.2, 0.1]):
        ax.plot([x - width, x + width], [y - i * 0.12] * 2, color="black", lw=1.5)


def label(ax, x, y, text, **kwargs):
    ax.text(x, y, text, ha="center", va="center", fontsize=11, **kwargs)


fig, axes = plt.subplots(1, 3, figsize=(12, 6.3), facecolor="white")
for ax in axes:
    ax.set(xlim=(0, 5), ylim=(0, 8), aspect="equal")
    ax.axis("off")

ax = axes[0]
ax.set_title("Open-pail apparatus", fontsize=14, fontweight="bold")
ax.plot([0.5, 0.5, 3.2, 3.2], [5.5, 1.6, 1.6, 5.5], color=BLUE, lw=3)
ax.plot([1, 1, 2.7, 2.7], [5.2, 2.2, 2.2, 5.2], color="#535b65", lw=8)
for x in [1.4, 2.3]:
    ax.add_patch(Rectangle((x - 0.12, 1.65), 0.24, 0.45, color="#b79365"))
ax.plot([1.85, 1.85], [4, 6.5], color="#b79365", lw=4)
ax.add_patch(Circle((1.85, 3.7), 0.28, facecolor=RED))
label(ax, 1.85, 3.7, "+q", color="white")
label(ax, 1.85, 6.95, "Insulating handle")
label(ax, 1.85, 5.8, "No wall contact")
ax.plot([2.75, 3.65, 3.65], [3, 3, 4.3], color=RED, lw=2)
ax.add_patch(Rectangle((3.1, 4.3), 1.4, 1.1, facecolor="white", edgecolor="black"))
label(ax, 3.8, 4.85, "Meter\nV > 0")
ax.plot([3.2, 4, 4], [1.6, 1.6, 4.3], color=BLUE, lw=2)
ground(ax, 3.8, 1.25)
label(ax, 2.4, 0.4, "Outer shield + reference: grounded\nInner pail + signal: isolated")
ax.annotate("Inner metal pail", xy=(1, 2.7), xytext=(0.1, 7.7),
            fontsize=10, arrowprops={"arrowstyle": "-", "color": "#535b65"})

for ax, grounded in zip(axes[1:], [False, True]):
    ax.set_title("Grounded enclosure" if grounded else "Neutral isolated enclosure",
                 fontsize=14, fontweight="bold")
    ax.add_patch(Circle((2.5, 4.25), 1.7, facecolor=GRAY, edgecolor="#535b65", lw=2))
    ax.add_patch(Circle((2.5, 4.25), 1.3, facecolor="white", edgecolor="#535b65", lw=2))
    ax.add_patch(Circle((2.15, 4.15), 0.28, facecolor=RED))
    label(ax, 2.15, 4.15, "+q", color="white")
    for x, y in [(1.35, 4.5), (1.7, 3.45), (2.8, 3.05), (3.65, 4), (3, 5.35)]:
        ax.text(x, y, "−", color=BLUE, ha="center", va="center", fontsize=16)
    if not grounded:
        for x, y in [(0.75, 4.2), (1.15, 5.6), (2.7, 6.05), (4, 5.15), (3.7, 2.9)]:
            ax.text(x, y, "+", color=RED, ha="center", va="center", fontsize=15)
    else:
        ax.plot([2.5, 2.5], [2.55, 1.95], color="black", lw=1.5)
        ground(ax, 2.5, 1.65)
    label(ax, 2.5, 7.1, "Closed cavity; body held without contact")
    label(ax, 2.5, 0.6, "Inner wall: −q\nOuter wall: 0; metal total: −q" if grounded
          else "Inner wall: −q\nOuter wall: +q; metal total: 0")
    label(ax, 2.5, 1.4 if not grounded else 7.65,
          "Exterior field generally nonzero" if not grounded else "Exterior field zero*")

fig.suptitle("Induction redistributes charge; grounding can supply charge", fontsize=17, y=0.98)
fig.text(0.5, 0.025,
         "Qualitative schematics: signs show totals, not charge density. Closed-enclosure panels assume equilibrium,\n"
         "no exterior sources and zero potential at infinity. Open rim and mesh prevent exact enclosure.",
         ha="center", fontsize=10)
fig.subplots_adjust(left=0.02, right=0.98, top=0.87, bottom=0.13, wspace=0.18)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
