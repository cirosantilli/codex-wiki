"""Original width-2 decomposition. Run from the desired PNG output directory.

Tested with Python 3.14.4, Matplotlib 3.10.7+dfsg1, NumPy 2.3.5.
"""
from pathlib import Path
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BAGS = {0: (2, 4, 5), 1: (1, 2, 4), 2: (2, 3, 5),
        3: (4, 5, 6), 4: (6, 7, 8), 5: (1, 4, 9)}
POSITIONS = {0: (0, 0), 1: (-3, 1.5), 2: (3, 1.5),
             3: (0, -2), 4: (0, -4), 5: (-3, 3.5)}
TREE = [(0, 1), (0, 2), (0, 3), (3, 4), (1, 5)]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "figure.facecolor": "white", "axes.facecolor": "white",
                     "savefig.facecolor": "white", "savefig.transparent": False})
fig, ax = plt.subplots(figsize=(8.4, 7.1), layout="constrained")
for a, b in TREE:
    ax.plot([POSITIONS[a][0], POSITIONS[b][0]], [POSITIONS[a][1], POSITIONS[b][1]],
            color="#617386", lw=2, zorder=1)
for i, (x, y) in POSITIONS.items():
    numbers = ", ".join(map(str, BAGS[i]))
    label = f"$B_{i}$\n{{{numbers}}}"
    ax.text(x, y, label, ha="center", va="center", fontsize=14,
            bbox={"boxstyle": "round,pad=.65", "facecolor": "#fff1cd" if i == 0 else "#d9edf6",
                  "edgecolor": "#76551f" if i == 0 else "#225875", "linewidth": 1.6}, zorder=3)
ax.set_title("Minimum tree decomposition: width = 3 − 1 = 2", fontsize=15, pad=16)
ax.text(0, -5, "Bag entries are variable indices.\nThe central bag joins the three overlapping scopes.",
        ha="center", va="center", fontsize=12, linespacing=1.5)
ax.set(xlim=(-4.5, 4.5), ylim=(-5.7, 4.3), aspect="equal")
ax.axis("off")
buffer = io.BytesIO()
fig.savefig(buffer, format="png", dpi=140, facecolor="white", transparent=False,
            metadata={"Software": "Matplotlib"})
Path(Path(__file__).with_suffix(".png").name).write_bytes(buffer.getvalue())
plt.close(fig)
