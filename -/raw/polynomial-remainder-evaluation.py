"""Show evaluation of an original cubic and its linear remainder."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.8), dpi=110, facecolor="white", gridspec_kw={"width_ratios": [1.2, 1]})
    fig.subplots_adjust(left=0.065, right=0.97, bottom=0.19, top=0.77, wspace=0.29)
    blue, orange, green, ink = "#1765a3", "#be5b0b", "#138565", "#243746"
    fig.suptitle("A remainder preserves values at divisor roots", y=0.97, fontsize=19, color=ink)
    fig.text(0.5, 0.875, r"$f=2X^3+3X^2-5X+6\qquad r=-2X+8\qquad f-r=(X-1)(X+2)(2X+1)$", ha="center", fontsize=14, color=ink)
    x = np.linspace(-2.45, 1.45, 700)
    f = 2*x**3 + 3*x**2 - 5*x + 6
    r = -2*x + 8
    for ax in axes:
        ax.set_xlim(x[0], x[-1])
        ax.set_xlabel(r"$x$")
        ax.grid(color="#e4e9ed", linewidth=0.8)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xticks([-2, -1, 0, 1])
    ax = axes[0]
    ax.set_title("The cubic and its remainder", fontsize=14, pad=12)
    ax.plot(x, f, color=blue, lw=2.4, label=r"$f(x)$")
    ax.plot(x, r, color=orange, lw=2.2, label=r"$r(x)$")
    ax.set_ylim(3, 15)
    ax.set_ylabel("Value")
    ax.legend(loc="upper right", frameon=True, facecolor="white", framealpha=1)
    for a, value, label, offset in [(-2, 12, r"$f(-2)=r(-2)=12$", (12, 22)), (1, 6, r"$f(1)=r(1)=6$", (-120, -30))]:
        ax.scatter([a], [value], s=74, facecolor="white", edgecolor=blue, lw=2, zorder=5)
        ax.annotate(label, (a, value), xytext=offset, textcoords="offset points", color=blue, fontsize=12, arrowprops={"arrowstyle": "-", "color": blue})
    ax.scatter([-0.5], [9], s=60, marker="D", facecolor="white", edgecolor=green, lw=2, zorder=5)
    ax.annotate(r"$q(-1/2)=0$", (-0.5, 9), xytext=(12, 14), textcoords="offset points", color=green, fontsize=12, arrowprops={"arrowstyle": "-", "color": green})
    ax = axes[1]
    ax.set_title("Why the values agree", fontsize=14, pad=12)
    ax.plot(x, (x-1)*(x+2)*(2*x+1), color=ink, lw=2.2)
    ax.axhline(0, color="#778690", lw=1.1)
    ax.set_ylim(-7, 7)
    ax.set_ylabel(r"$f(x)-r(x)=g(x)q(x)$")
    ax.scatter([-2, 1], [0, 0], s=74, facecolor="white", edgecolor=blue, lw=2, zorder=5)
    ax.scatter([-0.5], [0], s=60, marker="D", facecolor="white", edgecolor=green, lw=2, zorder=5)
    for a, label, offset, color in [(-2, r"$g(-2)=0$", (9, -36), blue), (1, r"$g(1)=0$", (-67, 30), blue), (-0.5, r"$q(-1/2)=0$", (-47, -55), green)]:
        ax.annotate(label, (a, 0), xytext=offset, textcoords="offset points", color=color, fontsize=12, arrowprops={"arrowstyle": "-", "color": color})
    fig.text(0.5, 0.065, "Circles: divisor roots.  Diamond: an extra intersection caused by a quotient root.", ha="center", fontsize=12, color=ink)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
