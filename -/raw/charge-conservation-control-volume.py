"""Signed charge transport through a fixed boundary; opaque PNG in CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.6, 5.0), dpi=100)
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    ax.add_patch(Rectangle((3.0, 1.45), 4.0, 2.4, fill=False,
                           edgecolor="#34495e", linestyle="--", linewidth=2))
    ax.text(5, 3.5, "Fixed control volume V", ha="center", weight="bold")
    ax.text(5, 2.55, r"Stored charge $Q(t)$", ha="center", fontsize=16)
    ax.text(5, 1.9, r"$Q(0)=10\ \mu\mathrm{C}$", ha="center", fontsize=13)
    for start, end, color in [(0.6, 3.65, "#2268a5"),
                               (6.35, 9.4, "#b45a20")]:
        ax.annotate("", (end, 2.65), (start, 2.65),
                    arrowprops={"arrowstyle": "-|>", "lw": 3, "color": color})
    ax.text(1.6, 3.15, r"$I_{\mathrm{in}}=3\ \mu\mathrm{A}$",
            ha="center", color="#2268a5")
    ax.text(8.4, 3.15, r"$I_{\mathrm{out}}=1\ \mu\mathrm{A}$",
            ha="center", color="#b45a20")
    for start, end, label_x in [(3, 2.2, 2.5), (7, 7.8, 7.5)]:
        ax.annotate("", (end, 1.55), (start, 1.55),
                    arrowprops={"arrowstyle": "->", "lw": 1.6, "color": "#34495e"})
        ax.text(label_x, 1.1, r"Outward $\mathbf{n}$", ha="center", fontsize=11)
    ax.text(1.7, 2.0, r"Outward contribution: $-I_{\mathrm{in}}$",
            ha="center", fontsize=11)
    ax.text(8.3, 2.0, r"Outward contribution: $+I_{\mathrm{out}}$",
            ha="center", fontsize=11)
    ax.text(5, 0.6, r"$dQ/dt=I_{\mathrm{in}}-I_{\mathrm{out}}=+2\ \mu\mathrm{C/s}$",
            ha="center", fontsize=16)
    ax.set_title("Charge conservation: inflow minus outflow is storage",
                 fontsize=15, weight="bold", pad=10)
    fig.text(0.5, 0.04, "Conventional-current arrows; schematic lengths; stipulated rates",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.85, bottom=0.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
