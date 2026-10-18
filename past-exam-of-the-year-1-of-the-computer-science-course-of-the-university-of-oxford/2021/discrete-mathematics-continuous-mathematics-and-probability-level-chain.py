"""Original level-exit chain for the 2021 A10100W1 solution.
Python 3.14.4, Matplotlib 3.10.7. Writes its PNG basename to the current directory.
No source illustration or third-party image is used.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(10.8, 3.6), dpi=160, facecolor="white")
ax.set_facecolor("white")
ax.set_xlim(-1.0, 10.0)
ax.set_ylim(-1.65, 1.65)
ax.axis("off")
centres = [0, 3, 6, 9]
labels = ["OUT", "Lower level\n(start)", "Upper level", "FOOD"]
probabilities = ["0", "1/13", "4/13", "1"]
colours = ["#eeeeee", "#dceafb", "#ddf2e8", "#fff0bf"]
for x, label, probability, colour in zip(centres, labels, probabilities, colours):
    patch = FancyBboxPatch((x - 0.82, -0.30), 1.64, 0.60,
        boxstyle="round,pad=0.06,rounding_size=0.10", linewidth=1.2,
        facecolor=colour, edgecolor="#283344", zorder=3)
    ax.add_patch(patch)
    ax.text(x, 0, label, ha="center", va="center", fontsize=10.3, zorder=4)
    ax.text(x, -0.72, "$h=" + probability + "$", ha="center", va="center", fontsize=12)
for start, end, label, colour, y in [(1, 0, "3/4", "#a74531", -0.22),
        (1, 2, "1/4", "#1a669a", 0.22),
        (2, 1, "3/4", "#a74531", -0.22),
        (2, 3, "1/4", "#1a669a", 0.22)]:
    x1, x2 = centres[start], centres[end]
    direction = 1 if x2 > x1 else -1
    arc = FancyArrowPatch((x1 + 0.88 * direction, y),
        (x2 - 0.88 * direction, y), arrowstyle="-|>", mutation_scale=14,
        linewidth=1.8, color=colour, connectionstyle="arc3,rad=-0.20", zorder=2)
    ax.add_patch(arc)
    label_y = 0.67 if y > 0 else -0.58
    ax.text((x1 + x2) / 2, label_y, "$" + label + "$", color=colour,
        fontsize=12, ha="center", va="center")
ax.text(4.5, 1.26, "Unbiased room choices produce a biased level chain",
        ha="center", fontsize=14, color="#172334")
ax.text(4.5, -1.20, "Each arrow summarizes a complete excursion from local room 1 to a boundary.",
        ha="center", fontsize=10, color="#394657")
fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
output = Path.cwd() / (Path(__file__).stem + ".png")
fig.savefig(output, facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
plt.close(fig)
