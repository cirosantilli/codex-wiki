"""Original sensor schematic and fixed-volume Newton-cooling model.

Run from _media; tested with Python 3.14.4, NumPy 2.3.5,
and Matplotlib 3.10.7. Curves are analytical, not measured data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def arrow(ax, start, end, color="#394750", style="->", width=1.8):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                               mutation_scale=13, linewidth=width, color=color))


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(11, 6.4), dpi=100)
    fig.suptitle("Measure the stroke; use the hold to assess heat leakage", fontsize=17, y=.97)
    grid = fig.add_gridspec(1, 2, left=.055, right=.96, top=.85, bottom=.23, wspace=.34)
    ax = fig.add_subplot(grid[0, 0])
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.axis("off")
    ax.set_title("Generic sealed-cylinder schematic", fontsize=12, pad=15)
    # Jacket lies outside the walls; heat can still cross the real boundary.
    ax.add_patch(Rectangle((2.8, 1.8), 3.8, 6.7, fill=False,
                           edgecolor="#899599", linewidth=9, alpha=.25))
    ax.add_patch(Rectangle((3.0, 2.0), 3.4, 6.3, facecolor="white",
                           edgecolor="#394750", linewidth=2))
    ax.add_patch(Rectangle((3.05, 2.05), 3.3, 3.55, facecolor="#e5f1fa", edgecolor="none"))
    ax.add_patch(Rectangle((3.0, 5.6), 3.4, .45, facecolor="#a5afb6", edgecolor="#394750"))
    ax.plot([4.7, 4.7], [6.05, 9.0], color="#394750", lw=5)
    ax.plot([3.8, 5.6], [9, 9], color="#394750", lw=3)
    arrow(ax, (5.8, 8.8), (5.8, 6.8), style="<->")
    ax.text(6.3, 7.4, "Stroke\nchanges V", fontsize=11, va="center")
    ax.text(4.7, 4.2, "Trapped air", ha="center", fontsize=12)
    ax.plot([3.65, 3.65], [1.1, 3.0], color="#b85a2a", lw=2)
    ax.plot([3.45, 3.85], [3.0, 3.0], color="#b85a2a", lw=2)
    ax.text(.0, .65, "Small temperature probe", color="#b85a2a", fontsize=11)
    arrow(ax, (2.7, .9), (3.65, 2.8), color="#b85a2a")
    ax.add_patch(Rectangle((5.35, 1.85), .55, .35, facecolor="#26709b", edgecolor="#26709b"))
    ax.text(6.1, 1.1, "Pressure\nreadout", color="#26709b", fontsize=11)
    arrow(ax, (6.15, 1.8), (5.65, 2.1), color="#26709b")
    ax.plot([3, 1.9], [6.9, 6.9], color="#394750", lw=2)
    ax.plot([2.3, 2.3], [6.6, 7.2], color="#394750", lw=2)
    ax.text(.1, 7.3, "Valve closed", fontsize=11)
    ax.text(.0, 5.6, "Insulating\njacket", fontsize=11)
    arrow(ax, (1.7, 5.8), (2.8, 5.4))
    arrow(ax, (6.6, 3.1), (9.2, 3.1), color="#8b795f", style="<->")
    ax.text(7.8, 3.5, "Possible heat\nexchange", ha="center", fontsize=10, color="#8b795f")
    ax.text(7.8, 2.4, r"Walls / room: $T_b$", ha="center", fontsize=10)
    bx = fig.add_subplot(grid[0, 1])
    s = np.linspace(0, 4, 401)
    for sign, color, label in [(1, "#b85a2a", "Hold after compression"),
                               (-1, "#26709b", "Hold after loaded expansion")]:
        bx.plot(s, sign * np.exp(-s), color=color, lw=2.7, label=label)
    bx.axhline(0, color="#667178", lw=1)
    bx.axvline(1, color="#899599", lw=1.2, ls=":")
    bx.scatter([1, 1], [np.exp(-1), -np.exp(-1)], color=["#b85a2a", "#26709b"], zorder=4)
    bx.text(1.08, .43, r"$e^{-1}=0.368$ remains", fontsize=10)
    bx.text(1.08, -.52, "63.2% of anomaly erased", fontsize=10)
    bx.set(xlim=(0, 4), ylim=(-1.15, 1.15), xlabel=r"Hold time $t/\tau_{\rm heat}$",
           ylabel=r"Temperature anomaly $(T-T_b)/|T(0)-T_b|$")
    bx.set_title("Analytical hold model: no piston motion", fontsize=12, pad=15)
    bx.legend(loc="upper right", fontsize=9, frameon=False)
    bx.grid(alpha=.17)
    fig.text(.5, .125, r"Sufficient resolved-stroke window:  $\tau_{\rm eq},\,\tau_{\rm probe}"
             r"\ll t_{\rm move}\ll\tau_{\rm heat}$, with negligible friction", ha="center", fontsize=12)
    fig.text(.5, .06, "The curves model only the hold after internal equilibration. No measured waveform or timing scale.",
             ha="center", fontsize=10, color="#4f5a60")
    fig.savefig(Path(__file__).with_suffix('.png').name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
