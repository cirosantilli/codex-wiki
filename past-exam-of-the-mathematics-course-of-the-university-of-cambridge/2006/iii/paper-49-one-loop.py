"""Draw one-loop proper scalar vertices; write the opaque PNG to caller CWD.

Compatible with repository Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The caller controls MPLBACKEND and MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 4, figsize=(13.6, 3.7), dpi=100, facecolor="white")
    for ax in axes:
        ax.set(xlim=(-0.08, 1.08), ylim=(0, 1))
        ax.set_aspect("equal")
        ax.axis("off")
    ax = axes[0]
    ax.set_title("Two-point tadpole", fontsize=13, pad=15)
    ax.plot([0.02, 0.98], [0.40, 0.40], color="black", lw=1.9)
    theta = np.linspace(-np.pi / 2, 3 * np.pi / 2, 241)
    ax.plot(0.5 + 0.17 * np.cos(theta), 0.57 + 0.17 * np.sin(theta), color="black", lw=1.9)
    ax.plot(0.5, 0.40, "o", color="black", ms=5.5)
    ax.text(0.03, 0.30, r"$p$", fontsize=12, ha="center")
    ax.text(0.97, 0.30, r"$-p$", fontsize=12, ha="center")
    ax.text(0.5, 0.10, r"$\tau_2$: symmetry factor $1/2$", ha="center", fontsize=11)
    pairs = [(1, 2, 3, 4), (1, 3, 2, 4), (1, 4, 2, 3)]
    for ax, (a, b, c, d) in zip(axes[1:], pairs):
        ax.set_title(f"Four-point: ({a}{b}|{c}{d})", fontsize=13, pad=15)
        t = np.linspace(0, 1, 121)
        for sign in (-1, 1):
            ax.plot(0.28 + 0.44 * t, 0.50 + sign * 0.17 * np.sin(np.pi * t), color="black", lw=1.9)
        for px, py, vx, label in [(0.02, 0.75, 0.28, a), (0.02, 0.25, 0.28, b),
                                  (0.98, 0.75, 0.72, c), (0.98, 0.25, 0.72, d)]:
            ax.plot([px, vx], [py, 0.50], color="black", lw=1.9)
            ax.text(px, py + (0.05 if py > 0.5 else -0.075), rf"$p_{label}$", fontsize=12, ha="center")
        ax.plot([0.28, 0.72], [0.50, 0.50], "o", color="black", ms=5.5)
        ax.text(0.50, 0.07, "Each channel: symmetry factor 1/2", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.86, bottom=0.02, wspace=0.30)
    fig.savefig(Path.cwd() / "paper-49-one-loop.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
