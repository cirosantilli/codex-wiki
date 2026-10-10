"""Draw a selected-speed electron curvature readout, not a historical reconstruction.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(9, 5), dpi=120, facecolor="white")
    ax = fig.add_axes((.045, .16, .58, .7))
    note = fig.add_axes((.66, .17, .32, .67))
    fig.suptitle("Selected speed + magnetic curvature → charge-to-mass ratio", fontsize=16, y=.96)
    ax.add_patch(Rectangle((0, -.1), 1.35, 2.3, facecolor="#eaf3fa", edgecolor="none"))
    for x in [.2, .55, .9, 1.25]:
        for y in [.3, .7, 1.1, 1.5, 1.9]:
            ax.plot(x, y, ".", ms=5, color="#8da4b4")
    # Electron q<0, v initially +x, B out of page: magnetic force points +y.
    theta = np.linspace(0, np.pi, 300)
    x, y = np.sin(theta), 1 - np.cos(theta)
    ax.plot(x, y, lw=3, color="#087c73")
    ax.plot([-.8, 0], [0, 0], color="#087c73", lw=3)
    ax.annotate("", xy=(-.03, .08), xytext=(-.65, .08), arrowprops={"arrowstyle": "->", "lw": 1.7})
    ax.text(-.82, -.2, r"selected $e^-$", fontsize=12)
    ax.text(-.82, -.38, r"$v=E/B_s$", fontsize=12)
    ax.plot([0, 0], [.06, 2.08], color="#536877", lw=3)
    ax.plot(0, 2, "o", color="#b45b1a", ms=9)
    ax.text(-.05, 2.25, "screen hit", ha="right", fontsize=11)
    ax.text(.74, 2.3, r"$B_a$ out of page", ha="center", fontsize=12)
    ax.plot([0, 1], [1, 1], "--", color="#536877", lw=1.4)
    ax.plot(0, 1, "o", color="#536877", ms=4)
    ax.text(.4, 1.07, r"$r$", fontsize=15)
    ax.annotate("", xy=(-.31, 2), xytext=(-.31, 0), arrowprops={"arrowstyle": "<->", "lw": 1.5})
    ax.text(-.38, 1.1, r"$D=2r$", rotation=90, va="center", ha="right")
    ax.text(.68, -.4, r"analyzer: $\mathbf{E}=0$", fontsize=12)
    ax.set(xlim=(-.95, 1.45), ylim=(-.55, 2.5), aspect="equal")
    ax.axis("off")
    note.axis("off")
    rows = [
        ("Stipulated example (SI)", 15, "#263c49"),
        (r"$E=2.00\times10^3\ \mathrm{V/m}$", 13, "#263c49"),
        (r"$B_s=1.00\times10^{-3}\ \mathrm{T}$", 13, "#263c49"),
        (r"$v=2.00\times10^6\ \mathrm{m/s}$", 13, "#087c73"),
        (r"$B_a=2.00\times10^{-4}\ \mathrm{T}$", 13, "#263c49"),
        (r"$D=0.1136\ \mathrm{m}$", 13, "#b45b1a"),
        (r"$r=D/2=0.0568\ \mathrm{m}$", 13, "#263c49"),
        (r"$\dfrac{e}{m}=\dfrac{v}{B_a r}$", 17, "#087c73"),
        (r"$=1.76\times10^{11}\ \mathrm{C/kg}$", 14, "#087c73"),
    ]
    for i, (label, size, color) in enumerate(rows):
        y = .035 if i == 8 else .98 - i * .108
        note.text(0, y, label, fontsize=size, color=color, va="top")
    fig.text(.05, .065, "Original ideal semicircle readout; illustrative inputs, not historical measurements.", fontsize=11, color="#495965")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
