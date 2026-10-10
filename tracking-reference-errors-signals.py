"""Original tracking-signal schematic; synthetic PI equilibrium, not lab data.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10.8, 5.7), dpi=110, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 6))
    ax.axis("off")
    blue, orange, green = "#2166ac", "#b35806", "#21734a"

    def box(x, y, w, h, label, color=blue):
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.08",
            facecolor="white", edgecolor=color, linewidth=1.7,
        ))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center")

    def arrow(start, end, color=blue):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.8})

    ax.text(5.5, 5.7, "A goal, a command, and a readout are different signals",
            ha="center", fontsize=16, weight="bold")
    ax.text(5.5, 5.25, "Synthetic first-order model:  2 dy/dt + y = u   (time in seconds)",
            ha="center", color="#444444")
    ax.text(0.55, 4.15, "Desired rise\nr = 1 °C", ha="center", color=blue)
    arrow((1.1, 4.15), (1.65, 4.15))
    box(1.75, 3.75, 1.1, 0.8, "r − yₘ")
    arrow((2.95, 4.15), (4.0, 4.15))
    ax.text(3.45, 4.6, "e = 0 °C", ha="center", color=blue)
    box(4.1, 3.7, 1.5, 0.9, "PI\ncontroller")
    arrow((5.7, 4.15), (7.0, 4.15))
    ax.text(6.35, 4.6, "u = 0.8 pp", ha="center", color=blue)
    box(7.1, 3.7, 1.55, 0.9, "Physical\nplant")
    arrow((8.75, 4.15), (10.25, 4.15))
    ax.text(9.6, 4.65, "Actual rise\ny = 0.8 °C", ha="center", color=green)
    arrow((9.55, 4.05), (9.55, 2.75), green)
    box(8.45, 1.8, 2.2, 0.85, "Sensor: yₘ = y + b", orange)
    ax.text(9.55, 1.38, "Bias b = +0.2 °C", ha="center", color=orange)
    arrow((8.35, 2.22), (2.3, 2.22), orange)
    arrow((2.3, 2.22), (2.3, 3.65), orange)
    ax.text(5.45, 2.55, "Measured rise yₘ = 1 °C", ha="center", color=orange)
    ax.text(5.45, 1.8, "Measured error: e = r − yₘ = 0 °C",
            ha="center", color=blue)
    ax.text(5.45, 1.28, "Physical discrepancy: ε = r − y = +0.2 °C",
            ha="center", color=green, weight="bold")
    ax.text(5.5, 0.56, "All rises use one fixed ambient baseline.  pp = heater-command percentage points.",
            ha="center", fontsize=11, color="#444444")
    ax.text(5.5, 0.16, "Zero measured error does not establish correct physical temperature.",
            ha="center", fontsize=12)
    fig.tight_layout(pad=0.7)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
