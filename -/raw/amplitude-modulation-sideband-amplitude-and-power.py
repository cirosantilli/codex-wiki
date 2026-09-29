"""Three-line AM voltage/power model; Python 3.14 and project dependencies.

Run from _media; writes this script's basename as an opaque white PNG.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def draw_lines(ax, heights, ylabel):
    positions = np.array([-1, 0, 1])
    colors = ["#d87516", "#266ba3", "#d87516"]
    ax.hlines(0, -1.5, 1.5, color="#555555", lw=1)
    for x, y, color in zip(positions, heights, colors, strict=True):
        ax.vlines(x, 0, y, color=color, lw=3)
        ax.plot(x, y, "o", color=color, ms=6)
        ax.text(x, y + 0.075, f"{y:g}", ha="center", va="bottom", fontsize=11)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(0, 1.30)
    ax.set_xticks(positions, [r"$\omega_c-\Omega$", r"$\omega_c$", r"$\omega_c+\Omega$"])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)


def main():
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.4))
    for row, m in enumerate((0.5, 1.4)):
        amplitudes = np.array([m / 2, 1, m / 2])
        powers = amplitudes ** 2
        draw_lines(axes[row, 0], amplitudes, "Peak voltage / A")
        draw_lines(axes[row, 1], powers, r"Mean power / $P_c$")
        axes[row, 0].set_title(f"m = {m:g}: amplitudes (m/2, 1, m/2)", loc="left", fontsize=11)
        axes[row, 1].set_title(f"m = {m:g}: powers; total = {powers.sum():g} Pc", loc="left", fontsize=11)
    fig.suptitle("AM has three lines: voltage amplitude and power use different scales", fontsize=14)
    fig.text(0.5, 0.068, r"One-sided cosine amplitudes; $P_c=A^2/(2R)$ for a common resistive load.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.022, r"Original infinite-duration linear model, $\omega_c/\Omega=20$; no measurements or clipping.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.855, bottom=0.155, hspace=0.46, wspace=0.24)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
