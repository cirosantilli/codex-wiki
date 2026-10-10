"""Original thermocouple measurement schematic; calculated toy values, not data.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested: Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 5.4), dpi=120)
    ax.set(xlim=(0, 12), ylim=(0, 6.3))
    ax.axis("off")
    ax.text(6, 6.02, "Where the reference temperature is measured", ha="center", weight="bold", fontsize=17)
    def box(x, y, w, h, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12", facecolor=color, edgecolor="#536475", lw=1.5))
    box(.45, 2.0, 1.85, 2.55, "#fff0df")
    box(5.1, 1.55, 2.4, 3.25, "#e9f3fb")
    box(9.65, 2.0, 1.85, 2.55, "#f4f4f4")
    ax.plot([1.4, 2.45, 6.3], [3.25, 4.0, 4.0], color="#b45323", lw=3)
    ax.plot([1.4, 2.45, 6.3], [3.25, 2.5, 2.5], color="#217490", lw=3)
    for y in (4.0, 2.5):
        ax.plot([6.3, 10.0], [y, y], color="#555", lw=2)
        ax.plot(6.3, y, "o", color="#222", ms=7)
    ax.plot(1.4, 3.25, "o", color="#222", ms=8)
    ax.text(1.4, 5.12, "A–B measuring\njunction", ha="center")
    ax.text(1.4, 2.35, "$T_h=80$ °C", ha="center")
    ax.text(3.65, 4.25, "A", color="#b45323", weight="bold", ha="center")
    ax.text(3.65, 2.13, "B", color="#217490", weight="bold", ha="center")
    ax.text(6.3, 5.12, "Isothermal terminal block\nboth transitions at $T_c$", ha="center")
    ax.text(6.3, 4.27, "A–Cu", ha="center", fontsize=11)
    ax.text(6.3, 2.08, "B–Cu", ha="center", fontsize=11)
    ax.text(6.3, 3.35, "$T_c=20$ °C\nlocal temperature sensor", ha="center", va="center", fontsize=11)
    ax.text(8.48, 4.28, "Cu lead", ha="center", color="#555", fontsize=11)
    ax.text(8.48, 2.12, "Cu lead", ha="center", color="#555", fontsize=11)
    ax.text(10.55, 5.12, "Meter input\nboth at $T_m$", ha="center")
    ax.text(10.05, 4.0, "+", ha="left", va="center", fontsize=18)
    ax.text(10.05, 2.5, "−", ha="left", va="center", fontsize=18)
    ax.text(10.6, 3.25, "+2.4 mV\n$I\\approx0$", ha="center", va="center", fontsize=14)
    ax.text(6, 1.13, "Matched homogeneous Cu leads: equal endpoint temperatures → cancelling contributions", ha="center", fontsize=11)
    ax.text(6, .63, "Block is thermally uniform; its two electrical terminals remain insulated.", ha="center", fontsize=11)
    ax.text(6, .15, "Stipulated model only: $S_A-S_B=40$ µV/K. No real material calibration is claimed.", ha="center", fontsize=11)
    fig.subplots_adjust(left=.01, right=.99, bottom=.02, top=.99)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
