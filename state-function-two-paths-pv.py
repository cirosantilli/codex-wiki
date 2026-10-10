"""Original equilibrium paths; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; emits the matching opaque PNG into the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    blue, orange = "#1768a5", "#bf5b17"
    fig = plt.figure(figsize=(9, 6), dpi=120, facecolor="white")
    ax = fig.add_axes((0.11, 0.29, 0.84, 0.57), facecolor="white")
    x = np.linspace(1, 3, 600)
    ax.fill_between(x, 1 / x, 2 / x, color="#d9e8f5", zorder=0)
    ax.plot([1, 1], [1, 2], color=blue, lw=3)
    ax.plot(x, 2 / x, color=blue, lw=3)
    ax.plot(x, 1 / x, color=orange, lw=3)
    ax.plot([3, 3], [1 / 3, 2 / 3], color=orange, lw=3)
    for x1, y1, x2, y2, color in (
        (1, 1.33, 1, 1.68, blue),
        (1.55, 2 / 1.55, 1.92, 2 / 1.92, blue),
        (1.55, 1 / 1.55, 1.92, 1 / 1.92, orange),
        (3, 0.40, 3, 0.61, orange),
    ):
        ax.annotate("", (x2, y2), (x1, y1), arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.3, "mutation_scale": 18})
    points = ((1, 1, "A", (12, 1)), (1, 2, "C", (10, 3)), (3, 2 / 3, "B", (-21, 9)), (3, 1 / 3, "D", (-21, -24)))
    for px, py, label, offset in points:
        ax.plot(px, py, "o", color="#17212b", ms=7, zorder=5)
        ax.annotate(label, (px, py), xytext=offset, textcoords="offset points", fontsize=14, fontweight="bold")
    ax.text(2.00, 1.30, r"Upper route: $T=2T_0$", color=blue)
    ax.text(1.46, 0.24, r"Lower route: $T=T_0$", color=orange)
    ax.text(1.77, 0.84, r"$\Delta W_{\rm by}=E_0\ln 3$", fontsize=13)
    ax.text(0.86, 1.50, "heat at fixed volume", rotation=90, va="center", ha="center", fontsize=10, color=blue)
    ax.text(3.18, 0.53, "heat at fixed volume", rotation=90, va="center", ha="center", fontsize=10, color=orange)
    ax.set(xlim=(0.77, 3.30), ylim=(0, 2.17), xlabel=r"Volume $V/V_0$", ylabel=r"Pressure $p/p_0$")
    ax.set_xticks([1, 2, 3])
    ax.set_yticks([0, 1 / 3, 2 / 3, 1, 1.5, 2], ["0", r"$1/3$", r"$2/3$", "1", "1.5", "2"])
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.16, zorder=-1)
    fig.suptitle("Same equilibrium endpoints, different paths", y=0.96, fontsize=17, fontweight="bold")
    fig.text(0.5, 0.155, r"$A=(V_0,T_0,p_0)$   to   $B=(3V_0,2T_0,2p_0/3)$", ha="center", fontsize=13)
    fig.text(0.5, 0.098, r"$W_{\rm upper}=2E_0\ln 3$       $W_{\rm lower}=E_0\ln 3$       $E_0=nRT_0$", ha="center", fontsize=13)
    fig.text(0.5, 0.045, "Idealized reversible paths; shaded area is the work difference.", ha="center", fontsize=11, color="#45515c")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
