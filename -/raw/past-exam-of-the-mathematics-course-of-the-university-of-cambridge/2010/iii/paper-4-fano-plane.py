"""Original Fano-plane diagram. Python 3.14 / matplotlib 3.10.
Write the same-basename opaque PNG into the caller's working directory.
The caller's MPLCONFIGDIR is used unchanged.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

points = {
    "100": (0, 1), "010": (-1, -.8), "001": (1, -.8),
    "110": (-.5, .1), "101": (.5, .1), "011": (0, -.8),
    "111": (0, -.2),
}
fig, axes = plt.subplots(1, 2, figsize=(10, 5.6), dpi=100, facecolor="white")
for ax, chosen, label, order in zip(
    axes, ("100", "001"), ("Incident pair", "Nonincident pair"), (8, 6)
):
    ax.set_aspect("equal")
    for first, last in (
        ("100", "010"), ("100", "001"), ("010", "001"),
        ("100", "011"), ("010", "101"), ("001", "110"),
    ):
        x, y = zip(points[first], points[last])
        ax.plot(x, y, color="#a1a8b3", linewidth=1.4, zorder=1)
    ax.add_patch(Circle((0, -19 / 90), 53 / 90, fill=False,
                        edgecolor="#a1a8b3", linewidth=1.4))
    x, y = zip(points["100"], points["010"])
    ax.plot(x, y, color="#1767a0", linewidth=4, zorder=2)
    for name, (x, y) in points.items():
        ax.scatter([x], [y], s=65, color="#303846", zorder=3)
        offsets = {
            "100": (0, .13), "010": (-.12, -.12), "001": (.12, -.12),
            "110": (-.18, .04), "101": (.18, .04),
            "011": (0, -.15), "111": (.13, .04),
        }
        dx, dy = offsets[name]
        ax.text(x + dx, y + dy, name, ha="center", va="center",
                fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    x, y = points[chosen]
    ax.scatter([x], [y], s=220, facecolors="none", edgecolors="#c74927",
               linewidth=2.5, zorder=4)
    ax.set_title(label, fontsize=15, pad=14)
    ax.text(0, -1.18, rf"$|G_p\cap G_L|={order}$", ha="center", fontsize=16)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.35, 1.35)
    ax.axis("off")
fig.suptitle("Fano plane: point–line stabilizers", fontsize=18, y=.96)
fig.text(.5, .045, "Blue line L = {100, 010, 110}; orange ring marks point p.",
         ha="center", fontsize=11)
fig.subplots_adjust(left=.03, right=.97, bottom=.13, top=.83, wspace=.14)
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
plt.close(fig)
