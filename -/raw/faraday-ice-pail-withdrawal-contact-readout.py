"""Original stipulated ideal-model sequence; no measured voltages are plotted.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


fig, ax = plt.subplots(figsize=(12, 6.3), facecolor="white")
ax.set(xlim=(0, 12), ylim=(0, 6.3))
ax.axis("off")
ax.text(6, 6.0, "Withdrawal, contact and grounding give different outcomes",
        ha="center", fontsize=17, fontweight="bold")
ax.text(6, 5.6, "Stipulated +q body; initially neutral enclosure; equilibrium at each step",
        ha="center", fontsize=11)
rows = [
    (4.25, "No contact", "#176798", [
        "Zero, then isolate\nEmpty: V = 0\nMetal charge 0",
        "Insert +q deeply\nV > 0\nMetal charge still 0",
        "Withdraw without touching\nV returns to 0\nBody retains +q"]),
    (2.7, "Conducting contact", "#b33c35", [
        "Fresh zero + insertion\nV > 0\nBody initially +q",
        "Touch inner wall\nWait for equilibrium\nIdeal body becomes neutral",
        "Withdraw body\nV remains positive\nMetal retains +q"]),
    (1.15, "Grounding induction", "#626b39", [
        "Insert +q; keep grounded\nV = 0\nMetal acquires −q",
        "Disconnect ground FIRST\nKeep +q inside\nMetal retains −q",
        "Then withdraw +q\nV < 0\nNo body–wall contact"]),
]
for y, name, color, boxes in rows:
    ax.text(0.1, y + 0.69, name, fontsize=12, color=color, fontweight="bold")
    for i, content in enumerate(boxes):
        x = 0.25 + 4 * i
        ax.add_patch(FancyBboxPatch((x, y - 0.5), 3.45, 1.0,
                     boxstyle="round,pad=0.08", facecolor="white", edgecolor=color, lw=1.8))
        ax.text(x + 1.725, y, content, ha="center", va="center", fontsize=11)
        if i < 2:
            ax.annotate("", xy=(x + 3.86, y), xytext=(x + 3.55, y),
                        arrowprops={"arrowstyle": "->", "color": color, "lw": 1.8})
ax.text(6, 0.22, "Qualitative signs only; no measured voltage scale. Exact totals require complete enclosure.\n"
        "An open pail approximates this model at sufficient depth; insulating surfaces may retain charge after contact.",
        ha="center", fontsize=10)
fig.subplots_adjust(left=0.025, right=0.99, top=0.99, bottom=0.02)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
