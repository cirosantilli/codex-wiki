"""Original qualitative ice-pail schematic, not measured data.

Tested with Python 3.14.4 and matplotlib; run from _media to save there.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, axes = plt.subplots(1, 4, figsize=(11.2, 4.7), facecolor="white")
blue, red, gray = "#2266a0", "#b83c3c", "#384452"
titles = ["1. Zero, then isolate", "2. Insert without touching", "3. Withdraw without touching", "4. Touch, then withdraw"]
for ax, title in zip(axes, titles):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.set_title(title, fontsize=10.5, fontweight="bold", pad=13)
    # Cross-section of an open conducting pail; dashed outer grounded shield.
    ax.plot([.13, .13, .78, .78], [.72, .2, .2, .72], color=gray, lw=4)
    ax.plot([.04, .04, .87, .87], [.76, .12, .12, .76], color="#89929b", lw=1.5, ls="--")
    ax.plot([.78, .93, .93], [.35, .35, .51], color=gray, lw=1.4)
    ax.add_patch(Circle((.93, .56), .055, facecolor="white", edgecolor=gray, lw=1.4))
    ax.text(.93, .56, "V", ha="center", va="center", fontsize=10)
    ax.text(.45, .03, "Pail + high-impedance meter", ha="center", fontsize=9)

axes[0].text(.45, .48, "Initially neutral", ha="center", color=gray)
axes[1].plot([.45, .45], [.94, .58], color="#89929b", lw=3)
axes[1].add_patch(Circle((.45, .52), .09, facecolor="white", edgecolor=red, lw=2))
axes[1].text(.45, .52, "+Q", ha="center", va="center", color=red)
axes[1].text(.45, .85, "insulating handle", ha="center", fontsize=9,
             bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
for x in [.19, .71]:
    for y in [.33, .47, .61]:
        axes[1].text(x, y, "−", color=blue, fontsize=17, ha="center")
for x in [.075, .835]:
    for y in [.33, .47, .61]:
        axes[1].text(x, y, "+", color=red, fontsize=14, ha="center")
axes[1].text(.45, .28, "redistribution", ha="center", fontsize=10)
axes[2].text(.45, .48, "Neutral again", ha="center", color=gray)
for x in [.075, .835]:
    for y in [.33, .47, .61]:
        axes[3].text(x, y, "+", color=red, fontsize=14, ha="center")
axes[3].text(.45, .53, "Transferred +q", ha="center", color=red)
axes[3].text(.45, .43, r"$0<q\leq Q$", ha="center", color=gray)
for ax, total, reading in zip(axes, ["0", "0", "0", "+q"], ["0", "positive", "0", "positive"]):
    ax.text(.45, -.08, "Net pail charge: " + total, ha="center", fontsize=10)
    ax.text(.45, -.17, "Meter: " + reading, ha="center", fontsize=10)
fig.suptitle("A meter response can mean redistribution or net charge transfer", fontsize=15, y=.97)
fig.text(.5, .025, "Original idealized schematic • symbols are qualitative, not particle counts or measured readings", ha="center", fontsize=10, color=gray)
fig.subplots_adjust(left=.03, right=.97, top=.81, bottom=.23, wspace=.2)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white", transparent=False)
plt.close(fig)
