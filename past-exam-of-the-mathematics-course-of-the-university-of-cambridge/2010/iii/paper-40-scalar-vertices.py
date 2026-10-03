"""Draw Wess--Zumino cubic scalar vertices; tested with Python 3.14.4.

Writes paper-40-scalar-vertices.png to the caller's working directory.
"""

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/paper-40-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.1), dpi=110, facecolor="white")
vertices = [([r"$\phi$", r"$\phi$", r"$\phi^*$"], r"$-2i\,m^*g$"),
            ([r"$\phi^*$", r"$\phi^*$", r"$\phi$"], r"$-2i\,mg^*$")]
for ax, (labels, rule) in zip(axes, vertices):
    ax.set_facecolor("white")
    for (x, y), label in zip([(-1.2, 0.8), (-1.2, -0.8), (1.2, 0.0)], labels):
        ax.plot([0, x], [0, y], lw=2, color="#355a84", ls=(0, (5, 3)))
        ax.text(x + (-0.24 if x < 0 else 0.24), y, label,
                fontsize=21, ha="center", va="center")
    ax.scatter([0], [0], s=48, color="#222222", zorder=3)
    ax.text(0, -1.38, rule, ha="center", va="center", fontsize=21)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.8, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
fig.suptitle("Wess–Zumino trilinear scalar interactions", fontsize=17, y=0.96)
fig.text(0.5, 0.87, "All field legs incoming; identical-leg factors included", fontsize=12, ha="center")
fig.subplots_adjust(left=0.025, right=0.975, bottom=0.08, top=0.8, wspace=0.12)
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
plt.close(fig)
