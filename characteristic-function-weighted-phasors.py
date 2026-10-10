"""Render a Bernoulli characteristic function as weighted complex arrows."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.8), layout="constrained")
    fig.set_facecolor("white")
    angle = 2 * np.pi / 3
    z = np.exp(1j * angle)
    mean = 2 / 3 + z / 3
    circle = np.exp(1j * np.linspace(0, 2 * np.pi, 600))
    blue, orange, green = "#2864a5", "#c05b16", "#08765b"
    for ax in axes:
        ax.set_facecolor("white")
        ax.plot(circle.real, circle.imag, "--", color="0.7", lw=1)
        ax.axhline(0, color="0.75", lw=0.8)
        ax.axvline(0, color="0.75", lw=0.8)
        ax.set(xlim=(-1.15, 1.25), ylim=(-1.15, 1.2),
               xlabel="Real part", ylabel="Imaginary part", aspect="equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])

    def arrow(ax, start, end, color, style="-"):
        ax.annotate("", (end.real, end.imag), (start.real, start.imag),
                    arrowprops={"arrowstyle": "->", "color": color,
                                "lw": 2.4, "linestyle": style})

    ax = axes[0]
    ax.set_title("Unit arrows, then average", pad=14)
    arrow(ax, 0j, 1 + 0j, blue)
    arrow(ax, 0j, z, orange)
    ax.plot([1, z.real], [0, z.imag], color="0.45", lw=1.4)
    ax.scatter([1, z.real], [0, z.imag], color=[blue, orange], s=40)
    ax.scatter(mean.real, mean.imag, color=green, s=65, zorder=5)
    ax.annotate(r"$1$ (weight $2/3$)", (1, 0), xytext=(0.38, -0.27), color=blue)
    ax.annotate(r"$e^{2\pi i/3}$ (weight $1/3$)", (z.real, z.imag),
                xytext=(-1.1, 1.05), color=orange)
    ax.annotate(r"$\varphi_B(2\pi/3)$", (mean.real, mean.imag),
                xytext=(0.45, 0.65), color=green,
                arrowprops={"arrowstyle": "-", "color": green})
    ax = axes[1]
    ax.set_title("Weighted arrows add head to tail", pad=14)
    arrow(ax, 0j, 2 / 3 + 0j, blue)
    arrow(ax, 2 / 3 + 0j, mean, orange)
    arrow(ax, 0j, mean, green)
    ax.scatter(mean.real, mean.imag, color=green, s=45, zorder=5)
    ax.text(0.28, -0.2, r"$2/3$", color=blue)
    ax.text(0.76, 0.2, r"$e^{2\pi i/3}/3$", color=orange, fontsize=11)
    ax.text(-0.98, 0.69, r"$\varphi_B=\frac{1}{2}+\frac{\sqrt{3}}{6}i$", color=green, fontsize=16)
    ax.text(-0.98, -0.89, r"$|\varphi_B|=1/\sqrt{3}<1$", fontsize=14)
    fig.suptitle(r"$P(B=0)=2/3,\quad P(B=1)=1/3,\quad t=2\pi/3$", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
