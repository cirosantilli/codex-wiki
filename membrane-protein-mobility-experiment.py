"""Draw qualitative sampling logic of a membrane antigen mixing experiment.

Emits basename.png to CWD. Tested with Python 3.14, matplotlib 3.10.7,
and numpy 2.3.5. Marker counts and geometry are original illustrations,
not observed data, trajectories, or reproduced published figures.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np


GREEN = "#247853"
RED = "#b83d63"
DARK = "#293440"


def surface(ax, cx, cy, radius, mixed=False):
    ax.add_patch(Circle((cx, cy), radius, facecolor="#f7f9fa", edgecolor=DARK, lw=1.5))
    angles = np.linspace(0, 2 * np.pi, 20, endpoint=False)
    for i, angle in enumerate(angles):
        color = (GREEN if i % 2 == 0 else RED) if mixed else (GREEN if np.cos(angle) < 0 else RED)
        ax.plot(cx + radius * np.cos(angle), cy + radius * np.sin(angle), "o",
                color=color, ms=6.5, markeredgecolor="white", markeredgewidth=0.5)


def arrow(ax, start, end):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "color": DARK, "lw": 1.5})


def main():
    plt.rcParams.update({"font.size": 11, "text.color": DARK})
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.975, bottom=0.13, top=0.86)
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    ax.text(1.6, 5.70, "Mouse + human cells", ha="center", weight="bold")
    for x, color in [(0.85, GREEN), (2.35, RED)]:
        ax.add_patch(Circle((x, 4.70), 0.45, facecolor="white", edgecolor=color, lw=2))
    ax.text(1.6, 3.9, "Virus-induced fusion", ha="center")
    arrow(ax, (3.0, 4.7), (3.65, 4.7))
    ax.add_patch(FancyBboxPatch((3.9, 3.95), 2.3, 1.5, boxstyle="round,pad=0.05",
                               edgecolor=DARK, facecolor="#edf3f8", lw=1.5))
    ax.text(5.05, 4.7, "Shared membrane\nIncubate suspension", ha="center", va="center")
    ax.text(5.05, 3.48, "Remove separate aliquots", ha="center", weight="bold",
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    arrow(ax, (4.0, 3.86), (3.10, 3.16))
    arrow(ax, (6.1, 3.86), (7.40, 3.16))
    for cx, mixed, title in [(3.1, False, "Earlier sample"), (7.4, True, "Later sample")]:
        ax.text(cx, 2.94, title, ha="center", weight="bold")
        surface(ax, cx, 1.72, 0.70, mixed)
        ax.text(cx, 0.75, "Stain, then observe", ha="center")
    ax.text(1.05, 1.75, "Surface\nreadouts", ha="center", va="center")
    ax.text(5.12, 1.65, "Compare\ndistributions", ha="center", va="center")
    for x, color, label in [(2.2, GREEN, "Mouse marker"), (6.3, RED, "Human marker")]:
        ax.plot(x, 0.15, "o", color=color, ms=7)
        ax.text(x + 0.2, 0.15, label, va="center")
    fig.suptitle("Membrane mobility: make redistribution visible", fontsize=16, y=0.97)
    fig.text(0.5, 0.905, "Original qualitative schematic of the Frye–Edidin experiment", ha="center")
    fig.text(0.5, 0.055, "Illustrative dots, counts and shapes; separate samples, not one filmed cell or a measured mixing curve.",
             ha="center", fontsize=10.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
