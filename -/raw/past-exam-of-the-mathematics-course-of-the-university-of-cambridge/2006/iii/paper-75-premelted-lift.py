"""Original premelted-film lift curve. Python 3.14; NumPy/Matplotlib root pins.

Write an opaque basename PNG to the caller's current directory.
Caller owns MPLCONFIGDIR and MPLBACKEND.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(9.0, 5.2), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.16, top=0.82)
    x = np.linspace(1.0, 12.0, 801)
    ax.plot(x, 1 - 1/x, color="#1769a8", linewidth=2.5, label="Positive lifting branch")
    ax.plot([0, 1], [0, 0], color="0.4", linewidth=3, label="No positive steady lift")
    ax.axhline(1, color="#ac3c38", linestyle="--", linewidth=1.4, label="Ideal limiting speed")
    ax.axvline(1, color="0.6", linestyle=":", linewidth=1.1)
    ax.scatter([1], [0], s=35, color="#1769a8", zorder=4)
    ax.annotate("Load threshold", xy=(1, 0), xytext=(2.5, 0.14),
                arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=11)
    ax.text(6.1, 0.59, r"$U/U_\infty=1-\Delta_c/\Delta$", fontsize=15)
    ax.text(6.1, 0.42, "Stronger driving pressure,\nbut a thinner, less conductive film", fontsize=11)
    ax.set(xlim=(0, 12), ylim=(-0.04, 1.13),
           xlabel=r"Undercooling $\Delta/\Delta_c$", ylabel=r"Separation rate $U/U_\infty$")
    ax.set_title("Premelted-film lifting of a loaded disk", fontsize=16, pad=18)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.05), ncol=3, fontsize=9, frameon=False)
    ax.set_facecolor("white")
    ax.grid(alpha=0.15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.savefig(Path.cwd()/"paper-75-premelted-lift.png", facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
