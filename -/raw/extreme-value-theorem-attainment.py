"""Original attainment and counterexample graphs; PNG basename to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.3), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    x = np.linspace(-1, 2, 501)
    ax.plot(x, (x-1)**2, color="#2878a5", lw=2.5)
    ax.scatter([-1, 1, 2], [4, 0, 1], color="#2878a5", s=50, zorder=3)
    ax.annotate("maximum 4", (-1, 4), xytext=(-.85, 3.55), fontsize=10)
    ax.annotate("minimum 0", (1, 0), xytext=(.25, .65), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set_title(r"$f(x)=(x-1)^2,\quad x\in[-1,2]$", fontsize=12, pad=13)
    ax.set_xlim(-1.2, 2.2)
    ax.set_ylim(-.3, 4.5)
    ax.set_xticks([-1, 0, 1, 2])
    ax.text(.5, -.27, "Both extrema are attained", transform=ax.transAxes,
            ha="center", fontsize=11)
    for ax, is_closed in zip(axes[1:], [False, True]):
        x = np.linspace(0, 1, 401)
        ax.plot(x, x, color="#2878a5", lw=2.5)
        ax.axhline(1, color="#c05b20", ls="--", lw=1.3)
        ax.scatter([1], [1], facecolor="white", edgecolor="#2878a5",
                   s=70, linewidth=1.8, zorder=4)
        ax.scatter([0], [0], facecolor="#2878a5" if is_closed else "white",
                   edgecolor="#2878a5", s=70, linewidth=1.8, zorder=4)
        if is_closed:
            ax.scatter([1], [0], color="#2878a5", s=70, zorder=4)
            title = "Closed domain, endpoint jump"
            footer = "Supremum 1 is not attained"
            ax.annotate(r"$h(1)=0$", (1, 0), xytext=(.48, .12),
                        fontsize=11)
        else:
            title = r"$g(x)=x,\quad x\in(0,1)$"
            footer = "Neither endpoint value is attained"
        ax.text(.1, 1.035, "supremum 1", fontsize=10, color="#9b4815")
        ax.set_title(title, fontsize=12, pad=13)
        ax.set_xlim(-.1, 1.1)
        ax.set_ylim(-.13, 1.15)
        ax.set_xticks([0, .5, 1])
        ax.set_yticks([0, .5, 1])
        ax.text(.5, -.27, footer, transform=ax.transAxes,
                ha="center", fontsize=10.5)
    for ax in axes:
        ax.set_xlabel("x", fontsize=11)
        ax.set_ylabel("Function value", fontsize=11)
        ax.grid(alpha=.17)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("The best value must occur at an allowed input",
                 fontsize=14, y=.98)
    fig.subplots_adjust(left=.065, right=.98, top=.79, bottom=.25, wspace=.33)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
