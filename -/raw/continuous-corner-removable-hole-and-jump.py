"""Contrast continuity, a removable mismatch, and a jump; output PNG to CWD."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 5.3), dpi=100, facecolor="white")
    left = np.linspace(-1.2, 0, 200, endpoint=False)
    right = np.linspace(0, 1.2, 200)
    color = "#216b9b"
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#aeb5ba", lw=0.8)
        ax.axvline(0, color="#aeb5ba", lw=0.8)
        ax.set(xlim=(-1.3, 1.3), ylim=(-0.17, 1.7), xlabel="x", ylabel="Function value")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([0, 0.5, 1, 1.5])
        ax.grid(alpha=0.16)
    x = np.concatenate((left, right))
    axes[0].plot(x, np.abs(x), color=color, lw=2.7)
    axes[0].scatter([0], [0], s=67, color=color, zorder=5)
    axes[0].set_title(r"Continuous: $g(x)=|x|$", fontsize=13)
    axes[0].text(0, 1.52, "No jump in values\nNo derivative at zero", ha="center", fontsize=11)
    axes[1].plot(left, left ** 2, color=color, lw=2.7)
    axes[1].plot(right[1:], right[1:] ** 2, color=color, lw=2.7)
    axes[1].scatter([0], [0], s=85, facecolors="white", edgecolors=color, linewidths=2, zorder=5)
    axes[1].scatter([0], [1], s=67, color="#bf572b", zorder=5)
    axes[1].set_title("Removable mismatch", fontsize=13)
    axes[1].text(0, 1.52, r"$r(x)=x^2$ for $x\ne0$" + "\n" + r"$r(0)=1$, but the limit is 0",
                 ha="center", fontsize=11)
    axes[2].plot([-1.2, 0], [0, 0], color=color, lw=2.7)
    axes[2].plot([0, 1.2], [1, 1], color=color, lw=2.7)
    axes[2].scatter([0], [0], s=85, facecolors="white", edgecolors=color, linewidths=2, zorder=5)
    axes[2].scatter([0], [1], s=67, color=color, zorder=5)
    axes[2].set_title("Jump discontinuity", fontsize=13)
    axes[2].text(0, 1.52, "Left limit 0, right limit 1\nNo single point value repairs it", ha="center", fontsize=11)
    fig.suptitle("A corner can be continuous; a changed value or a jump can break continuity", fontsize=16)
    fig.text(0.5, 0.025, "Open marker: excluded graph point    •    Filled marker: assigned value", ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.055, 1, 0.93))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
