"""Schematic neighboring echelle orders; save PNG in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7, 3.6), dpi=100, facecolor="white")
    x = np.linspace(-1.8, 1.8, 300)
    for offset, label, color in [(1.1, r"Order $m$", "#c66b22"), (-.5, r"Order $m+1$", "#1766aa")]:
        y = offset+.12*x+.04*x*x
        ax.plot(x, y, color=color, lw=3)
        ax.annotate("", xy=(.8, offset+.12*.8+.04*.8**2),
                    xytext=(-.2, offset-.024+.0016),
                    arrowprops=dict(arrowstyle="->", color=color, lw=2))
        ax.text(-1.95, offset+.23, label, color=color, fontsize=12)
    ax.axvline(0, color="0.55", ls="--", lw=1)
    ax.text(.06, 1.73, r"$y$-axis", fontsize=10, color="0.4")
    ax.annotate("", xy=(1.9, -1.28), xytext=(-1.4, -1.28),
                arrowprops=dict(arrowstyle="->", color="0.2", lw=1.5))
    ax.text(.25, -1.53, r"Main dispersion: increasing $\lambda$", ha="center", fontsize=11)
    ax.annotate("", xy=(2.25, 1.65), xytext=(2.25, -.85),
                arrowprops=dict(arrowstyle="->", color="0.2", lw=1.5))
    ax.text(2.4, .4, r"Cross-dispersion: increasing $\lambda$", rotation=90,
            va="center", fontsize=10)
    ax.set(xlim=(-2.25, 2.85), ylim=(-1.8, 2.0))
    ax.set_title("Cross-disperser separates overlapping orders", fontsize=12)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
