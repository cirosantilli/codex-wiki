"""Equal-volume mixing and a conditional AB saturation test.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def box(ax, x, y, width, height, label, color):
    ax.add_patch(FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.025", facecolor=color, edgecolor="#687986", lw=1.3))
    ax.text(x + width / 2, y + height / 2, label, ha="center", va="center", fontsize=12)


def main():
    fig = plt.figure(figsize=(11, 5.8), dpi=100, facecolor="white")
    fig.suptitle("Mix first; then compare the ion product", fontsize=20, weight="bold", y=0.97)
    fig.text(0.5, 0.898, r"Toy AB model: $K_{\mathrm{sp},c}=10^{-8}\ \mathrm{M}^2$; fixed activity coefficient product", ha="center", fontsize=12)
    left = fig.add_axes((0.025, 0.16, 0.43, 0.68))
    left.set(xlim=(0, 10), ylim=(0, 10))
    left.axis("off")
    box(left, 0.4, 6.5, 4, 2.4, "Stock AX: volume V\n[A+] = C\n[B−] = 0", "#e9f3fb")
    box(left, 5.5, 6.5, 4, 2.4, "Stock YB: volume V\n[A+] = 0\n[B−] = C", "#fff3e3")
    for x in [2.4, 7.5]:
        left.add_patch(FancyArrowPatch((x, 6.3), (5, 5.0), arrowstyle="-|>", mutation_scale=18, lw=1.5, color="#405463"))
    box(left, 1.2, 2.7, 7.4, 2.4, "Just mixed: volume 2V\n[A+] = [B−] = C/2\n" + r"$Q_{c,0} = C^2/4$", "#f0f7f3")
    left.text(5, 1.7, "Each reacting ion is diluted by two.\nTheir product is divided by four.", ha="center", va="center", fontsize=12)
    ax = fig.add_axes((0.56, 0.24, 0.405, 0.56), facecolor="white")
    c_units = np.linspace(0, 4.65, 300)
    ratio = c_units**2 / 4
    ax.axhspan(0, 1, color="#e9f3fb")
    ax.axhspan(1, 5.6, color="#fff3e3")
    ax.plot(c_units, ratio, lw=2.7, color="#2675ac")
    ax.axhline(1, color="#404040", lw=1.2, ls="--")
    ax.axvline(2, color="#71818c", lw=1.0, ls=":")
    ax.scatter([1, 4], [0.25, 4], s=55, color=["#2675ac", "#b66914"], zorder=4)
    ax.annotate("C = 1 × 10⁻⁴ M\nQ / K = 0.25", (1, 0.25), xytext=(0.15, 1.8), fontsize=11, arrowprops={"arrowstyle": "->", "color": "#2675ac"})
    ax.annotate("C = 4 × 10⁻⁴ M\nQ / K = 4", (4, 4), xytext=(2.45, 4.85), fontsize=11, arrowprops={"arrowstyle": "->", "color": "#b66914"})
    ax.text(1.2, 3.65, "Precipitation favored\n(nucleation still needed)", ha="center", fontsize=11, color="#805318")
    ax.text(3.55, 0.42, "Undersaturated", ha="center", fontsize=11, color="#225471")
    ax.text(2.06, 1.14, "saturation", fontsize=10)
    ax.set(xlim=(0, 4.65), ylim=(0, 5.6), xlabel=r"Stock concentration $C$ (in $10^{-4}$ M)", ylabel=r"Initial mixed $Q_{c,0}/K_{\mathrm{sp},c}$")
    ax.tick_params(labelsize=11)
    ax.xaxis.label.set_size(12)
    ax.yaxis.label.set_size(12)
    fig.text(0.5, 0.055, "Threshold: C = 2 × 10⁻⁴ M   •   Calculated compositions, not measured cloudiness or time", ha="center", fontsize=12)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
