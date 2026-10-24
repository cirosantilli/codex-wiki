"""Original incidence drawing. Run from the desired PNG output directory.

Tested with Python 3.14.4, Matplotlib 3.10.7+dfsg1, NumPy 2.3.5.
"""
from pathlib import Path
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCOPES = {1: (1, 2, 4), 2: (2, 3, 5), 3: (4, 5, 6), 4: (6, 7, 8), 5: (1, 4, 9)}
VARIABLES = {1: (-2.4, 2.2), 2: (-0.5, 2.2), 3: (2.5, 2.2),
             4: (-1.3, 0), 5: (1.3, 0), 6: (0, -2),
             7: (-1.25, -3.7), 8: (1.25, -3.7), 9: (-4, 0.1)}
EDGES = {1: (-1.4, 1.15), 2: (1.25, 1.15), 3: (0, -0.85),
         4: (0, -3), 5: (-2.9, 0.4)}

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "figure.facecolor": "white", "axes.facecolor": "white",
                     "savefig.facecolor": "white", "savefig.transparent": False})
fig, ax = plt.subplots(figsize=(8.2, 7), layout="constrained")
for e, scope in SCOPES.items():
    for v in scope:
        ax.plot([EDGES[e][0], VARIABLES[v][0]], [EDGES[e][1], VARIABLES[v][1]],
                color="#617386", lw=1.7, zorder=1)
for v, (x, y) in VARIABLES.items():
    ax.scatter(x, y, s=950, facecolor="#fff1cd", edgecolor="#76551f", linewidth=1.5, zorder=3)
    ax.text(x, y, f"$X_{v}$", ha="center", va="center", fontsize=14, zorder=4)
for e, (x, y) in EDGES.items():
    ax.scatter(x, y, s=740, marker="s", facecolor="#d9edf6", edgecolor="#225875", linewidth=1.5, zorder=3)
    ax.text(x, y, f"$E_{e}$", ha="center", va="center", fontsize=13, zorder=4)
ax.set_title("Constraint hypergraph: incidence representation", fontsize=15, pad=16)
ax.text(-0.8, -4.45, "Round: original variable     Square: constraint scope", ha="center", fontsize=12)
ax.set(xlim=(-4.65, 3.25), ylim=(-4.75, 2.85), aspect="equal")
ax.axis("off")
buffer = io.BytesIO()
fig.savefig(buffer, format="png", dpi=140, facecolor="white", transparent=False,
            metadata={"Software": "Matplotlib"})
Path(Path(__file__).with_suffix(".png").name).write_bytes(buffer.getvalue())
plt.close(fig)
