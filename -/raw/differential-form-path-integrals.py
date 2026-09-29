"""Compare two explicit path integrals; write the PNG to the current directory."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Each leg has a constant coordinate; these four contributions are exact.
    alpha_a = 0 + 1
    alpha_b = 0 + 0
    beta_a = 0 + 1
    beta_b = 0 + 1
    assert alpha_a - alpha_b == 1
    assert beta_a == beta_b == 1

    orange, blue = "#c76716", "#1675a9"
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.4), dpi=120)
    fig.patch.set_facecolor("white")
    for ax, exact in zip(axes, (False, True)):
        ax.set_aspect("equal")
        ax.set_xlim(-0.18, 1.2)
        ax.set_ylim(-0.19, 1.18)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.spines[["top", "right"]].set_visible(False)
        ax.fill([0, 1, 1, 0], [0, 0, 1, 1], "#f3f5f7", zorder=0)
        ax.plot([0, 1, 1], [0, 0, 1], color=orange, lw=3)
        ax.plot([0, 0, 1], [0, 1, 1], color=blue, lw=3)
        legs = [
            ((0.32, 0), (0.61, 0), orange),
            ((1, 0.32), (1, 0.61), orange),
            ((0, 0.32), (0, 0.61), blue),
            ((0.32, 1), (0.61, 1), blue),
        ]
        for start, end, color in legs:
            ax.annotate("", xy=end, xytext=start,
                        arrowprops={"arrowstyle": "-|>", "color": color,
                                    "lw": 2.5, "mutation_scale": 16})
        ax.scatter([0, 1], [0, 1], color="#222222", s=35, zorder=5)
        ax.text(0.06, -0.11, "start", ha="left", fontsize=10)
        ax.text(0.94, 1.07, "finish", ha="right", fontsize=10)
        ax.text(0.5, -0.065, "leg: 0", color=orange, ha="center", va="top")
        ax.text(1.045, 0.5, "leg: 1", color=orange, va="center", rotation=90)
        ax.text(-0.055, 0.5, "leg: 0", color=blue, va="center",
                ha="right", rotation=90)
        ax.text(0.5, 1.04, f"leg: {1 if exact else 0}", color=blue,
                ha="center", va="bottom")
        ax.set_title(r"$\beta=d(xy)=y\,dx+x\,dy$" if exact else r"$\alpha=x\,dy$",
                     fontsize=15, pad=18)
        ax.text(0.5, -0.28, f"Bottom then right: {beta_a if exact else alpha_a}",
                color=orange, transform=ax.transAxes, ha="center", fontsize=12)
        ax.text(0.5, -0.36, f"Left then top: {beta_b if exact else alpha_b}",
                color=blue, transform=ax.transAxes, ha="center", fontsize=12)
    fig.suptitle("Integrating a one-form along a directed path", fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.08, right=0.95, bottom=0.29, top=0.82, wspace=0.38)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
