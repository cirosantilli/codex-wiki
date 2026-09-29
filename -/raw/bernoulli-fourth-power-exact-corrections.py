"""Show an exact power sum and magnify its small final correction.

Run from the output directory. Tested with Python 3.14, matplotlib 3.10.7,
and numpy 2.3.5. The calculation uses standard-library rational arithmetic.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def main():
    n = 10
    integral = Fraction(n**5, 5)
    endpoint = Fraction(n**4, 2)
    b2 = Fraction(n**3, 3)
    b4 = -Fraction(n, 30)
    before_final = integral + endpoint + b2
    exact = before_final + b4
    assert exact == sum(k**4 for k in range(1, n + 1)) == 25333
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2), layout="constrained",
                             gridspec_kw={"width_ratios": (1.35, 1)})
    fig.patch.set_facecolor("white")
    fig.suptitle("An exact fourth-power sum: $1^4 + 2^4 + \\cdots + 10^4$", fontsize=17)
    ax, zoom = axes
    for panel in axes:
        panel.set_facecolor("white")
    levels = [Fraction(0), integral, integral + endpoint, before_final]
    colors = ["#82bddf", "#e0b15a", "#73b7a0"]
    for i, (bottom, top, color) in enumerate(zip(levels, levels[1:], colors)):
        ax.bar(i, float(top - bottom), bottom=float(bottom), width=0.65,
               color=color, edgecolor="#38495a")
        if i < 2:
            ax.plot([i + 0.325, i + 0.675], [float(top)] * 2,
                    color="#6a7580", linestyle="--")
    for i, text in enumerate(["20000", "+5000", "$+1000/3$"]):
        ax.text(i, float(levels[i + 1]) + 600, text, ha="center", fontsize=13)
    ax.set(xticks=range(3), xticklabels=["Integral", "Endpoint", "$B_2$ term"],
           ylim=(0, 29200), yticks=(0, 10000, 20000), ylabel="Accumulated sum")
    ax.set_title("Build the sum from its integral", fontsize=13)
    ax.text(0.5, -0.17, "$20000 + 5000 + 1000/3$", transform=ax.transAxes,
            ha="center", fontsize=14)
    zoom.set_title("Magnify the final $B_4$ correction", fontsize=13)
    zoom.plot([0, 1], [float(before_final), float(exact)], color="#bc493c",
              marker="o", linewidth=3, markersize=9)
    zoom.axhline(float(exact), color="#38495a", linestyle="--", linewidth=1)
    zoom.annotate("$-1/3$", xy=(0.5, float(exact + Fraction(1, 6))),
                  xytext=(0.82, float(exact + Fraction(1, 4))), fontsize=16,
                  arrowprops={"arrowstyle": "->", "color": "#bc493c"})
    zoom.set(xlim=(-0.25, 1.3), ylim=(25332.87, 25333.48),
             xticks=(0, 1), xticklabels=["Before $B_4$", "Exact sum"],
             yticks=(25333, float(before_final)))
    zoom.yaxis.set_major_formatter(FuncFormatter(
        lambda value, _: "$25333$" if abs(value - 25333) < 0.01 else "$25333 + 1/3$"))
    zoom.text(0.5, -0.17, "Direct addition also gives 25333", transform=zoom.transAxes,
              ha="center", fontsize=12, fontweight="bold")
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
