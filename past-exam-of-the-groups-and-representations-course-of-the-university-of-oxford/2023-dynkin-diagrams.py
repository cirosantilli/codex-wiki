"""Draw the numbered diagrams used in the 2023 Oxford solutions.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The only output is a PNG in the caller's current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def diagram(ax, positions, edges, title, removed=None):
    for a, b in edges:
        x1, y1 = positions[a]
        x2, y2 = positions[b]
        muted = removed in (a, b)
        ax.plot([x1, x2], [y1, y2], color="#bbbbbb" if muted else "#25364a",
                linewidth=2, linestyle="--" if muted else "-", zorder=1)
    for label, (x, y) in positions.items():
        ax.scatter([x], [y], s=240, facecolor="white",
                   edgecolor="#bf3939" if label == removed else "#25364a",
                   linewidth=2, zorder=2)
        ax.text(x, y + .30, str(label), ha="center", va="bottom", fontsize=13)
        if label == removed:
            ax.plot([x-.13, x+.13], [y-.13, y+.13], color="#bf3939", linewidth=2, zorder=3)
            ax.plot([x-.13, x+.13], [y+.13, y-.13], color="#bf3939", linewidth=2, zorder=3)
    ax.set_title(title, fontsize=13, pad=17)
    ax.set_xlim(-.5, 3.9)
    ax.set_ylim(-1.45, 1.6)
    ax.set_aspect("equal")
    ax.axis("off")


fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.5), facecolor="white")
diagram(axes[0], {1:(0,0), 2:(1.4,0), 3:(2.8,0)}, [(1,2),(2,3)], r"$A_3$")
d5 = {1:(0,0), 2:(1.15,0), 3:(2.3,0), 4:(3.4,.85), 5:(3.4,-.85)}
diagram(axes[1], d5, [(1,2),(2,3),(3,4),(3,5)], r"$D_5$")
extended = {0:(0,.85), 1:(0,-.85), 2:(1.15,0), 3:(2.3,0), 4:(3.4,.85), 5:(3.4,-.85)}
diagram(axes[2], extended, [(0,2),(1,2),(2,3),(3,4),(3,5)],
        r"Extended $D_5$: delete node 2", removed=2)
axes[2].text(1.5, -1.6, r"$A_1\oplus A_1\oplus A_3$", ha="center", fontsize=13)
fig.subplots_adjust(left=.025, right=.99, top=.85, bottom=.17, wspace=.2)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            dpi=120, facecolor="white", transparent=False,
            metadata={"Software":"Oxford 2023 Dynkin diagram generator"})
plt.close(fig)
