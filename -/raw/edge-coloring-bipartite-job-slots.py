"""Draw six resource-pair jobs and their three matching slots.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5
(root pyproject.toml). All job assignments are exact illustrative data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


COLORS = {1: "#0072B2", 2: "#D55E00", 3: "#7B4397"}
SLOTS = {1: [("A", "X"), ("B", "Y")], 2: [("A", "Y"), ("B", "Z")], 3: [("A", "Z"), ("B", "X")]}


def main():
    fig, (graph, table) = plt.subplots(
        1, 2, figsize=(10, 4.8), dpi=120, facecolor="white", gridspec_kw={"width_ratios": [1, 1.45]}
    )
    fig.suptitle("Six jobs, three slots: each slot is a matching", fontsize=17, y=0.97)
    positions = {"A": (0, 0.75), "B": (0, -0.75), "X": (2, 1.1), "Y": (2, 0), "Z": (2, -1.1)}
    graph.set_aspect("equal")
    graph.set_xlim(-0.5, 2.5)
    graph.set_ylim(-1.65, 1.75)
    graph.axis("off")
    graph.set_title(r"Resource graph $K_{2,3}$", fontsize=15, pad=10)
    graph.text(0, 1.58, "Technicians", ha="center", fontsize=12)
    graph.text(2, 1.58, "Instruments", ha="center", fontsize=12)
    for slot, jobs in SLOTS.items():
        for u, v in jobs:
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            graph.plot([x1, x2], [y1, y2], color=COLORS[slot], lw=3.5, zorder=1)
            fraction = 0.22 if u == "A" else 0.78
            graph.text(
                x1 + fraction * (x2 - x1),
                y1 + fraction * (y2 - y1),
                str(slot),
                ha="center",
                va="center",
                fontsize=11,
                fontweight="bold",
                bbox={"boxstyle": "round,pad=0.16", "facecolor": "white", "edgecolor": COLORS[slot]},
                zorder=3,
            )
    for vertex, (x, y) in positions.items():
        graph.plot(x, y, "o", ms=12, color="#26323B", zorder=4)
        graph.text(x + (-0.22 if x == 0 else 0.23), y, vertex, ha="center", va="center", fontsize=14)
    graph.text(1, -1.57, "Edge number = slot number", ha="center", fontsize=12)
    table.set_xlim(-0.15, 3.15)
    table.set_ylim(-0.3, 3.4)
    table.axis("off")
    table.set_title("Execute both jobs in each column together", fontsize=15, pad=10)
    for slot, jobs in SLOTS.items():
        x = slot - 1
        table.text(x + 0.5, 2.85, f"Slot {slot}", ha="center", fontsize=14, color=COLORS[slot], fontweight="bold")
        for row, (technician, instrument) in enumerate(jobs):
            y = 1.7 - row * 0.85
            table.add_patch(
                FancyBboxPatch(
                    (x + 0.08, y), 0.84, 0.62,
                    boxstyle="round,pad=0.02", facecolor="white", edgecolor=COLORS[slot], linewidth=2.5,
                )
            )
            table.text(x + 0.5, y + 0.31, f"{technician}{instrument}", ha="center", va="center", fontsize=19)
        table.text(x + 0.5, 0.35, "No shared\nresource", ha="center", va="center", fontsize=12, color="#34444F")
    fig.text(0.5, 0.055, "A has three jobs ⇒ at least three slots. This schedule achieves three.", ha="center", fontsize=14)
    fig.subplots_adjust(left=0.04, right=0.97, top=0.78, bottom=0.18, wspace=0.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
