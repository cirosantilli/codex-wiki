"""NST IB 2023 paper 2 Q4: draw the contour; write the PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; dependencies are in pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(6.0, 4.8), facecolor="white")
    ax.set_facecolor("white")
    radius, epsilon, gap = 2.35, 0.26, 0.07
    color = "#1768ab"
    outer = np.linspace(gap, 2 * np.pi - gap, 600)
    inner = np.linspace(2 * np.pi - gap, gap, 300)
    ax.plot(radius * np.cos(outer), radius * np.sin(outer), color=color, lw=1.8)
    ax.plot(epsilon * np.cos(inner), epsilon * np.sin(inner), color=color, lw=1.8)
    for angle, start, finish in ((gap, epsilon, radius), (-gap, radius, epsilon)):
        ax.plot(np.array([epsilon, radius]) * np.cos(angle),
                np.array([epsilon, radius]) * np.sin(angle), color=color, lw=1.8)
        center = (start + finish) / 2
        direction = np.sign(finish - start)
        ax.annotate("", xy=((center + 0.2 * direction) * np.cos(angle),
                            (center + 0.2 * direction) * np.sin(angle)),
                    xytext=((center - 0.2 * direction) * np.cos(angle),
                            (center - 0.2 * direction) * np.sin(angle)),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8))
    for arc_radius, angle, direction in ((radius, np.pi / 2, 1), (epsilon, np.pi, -1)):
        before, after = angle - direction * 0.14, angle + direction * 0.14
        ax.annotate("", xy=(arc_radius * np.cos(after), arc_radius * np.sin(after)),
                    xytext=(arc_radius * np.cos(before), arc_radius * np.sin(before)),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8))
    ax.axhline(0, color="#b7bec6", lw=0.7, zorder=0)
    ax.axvline(0, color="#b7bec6", lw=0.7, zorder=0)
    ax.plot([0, 2.65], [0, 0], color="#b65032", ls=":", lw=1.4)
    ax.scatter([0, 0], [1, -1], color="#172a3a", marker="x", s=55, zorder=4)
    ax.text(0.12, 1, r"$i$ (double pole)", va="center", fontsize=11)
    ax.text(0.12, -1, r"$-i$ (double pole)", va="center", fontsize=11)
    ax.text(1.25, 0.31, r"$\sqrt{z}=+\sqrt{x}$", ha="center", fontsize=12)
    ax.text(1.25, -0.42, r"$\sqrt{z}=-\sqrt{x}$", ha="center", fontsize=12)
    ax.text(-0.34, -0.41, r"$\varepsilon$", fontsize=11)
    ax.text(-1.75, 1.72, r"$R$", fontsize=12)
    ax.text(2.55, -0.21, r"$\mathrm{Re}\,z$", fontsize=11)
    ax.text(0.1, 2.54, r"$\mathrm{Im}\,z$", fontsize=11)
    ax.set(xlim=(-2.6, 3.0), ylim=(-2.6, 2.8), aspect="equal")
    ax.axis("off")
    fig.tight_layout(pad=0.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
