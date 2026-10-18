"""Original symmetric-cavity sketch and waist curve; Python 3.14,
NumPy 2.3.5, Matplotlib 3.10.7. Writes one PNG in the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, green, gray = "#126782", "#287d53", "#5b6570"
    fig, (sketch, ax) = plt.subplots(1, 2, figsize=(11.4, 5.8),
                                    gridspec_kw={"width_ratios": (1, 1.15)})
    y = np.linspace(-0.5, 0.5, 200)
    sketch.plot(-0.5 + 0.15 * y**2, y, lw=4, color=gray)
    sketch.plot(0.5 - 0.15 * y**2, y, lw=4, color=gray)
    z = np.linspace(-0.495, 0.495, 600)
    radius = 0.12 * np.sqrt(1 + (z / 0.5) ** 2)
    sketch.fill_between(z, -radius, radius, color=blue, alpha=0.12)
    sketch.plot(z, radius, color=blue, lw=2)
    sketch.plot(z, -radius, color=blue, lw=2)
    sketch.axhline(0, color="#aab2b8", ls="--", lw=0.8)
    sketch.axvline(0, ymin=0.30, ymax=0.71, color="#aab2b8", ls=":", lw=0.8)
    sketch.annotate("", (0, 0), (0, 0.12),
                    arrowprops={"arrowstyle": "<->", "color": blue, "shrinkA": 0, "shrinkB": 0})
    sketch.annotate(r"$w_0$", (0, 0.06), (0.13, 0.30), color=blue,
                    arrowprops={"arrowstyle": "-", "color": blue}, fontsize=15)
    for x, label in ((-0.5, r"Concave mirror 1"), (0.5, r"Concave mirror 2")):
        sketch.text(x, 0.57, label, ha="center", fontsize=11)
        sketch.text(x, 0.45, r"$R$", ha="center", fontsize=13)
        sketch.plot([x, x], [-0.52, -0.7], color=gray, lw=0.8)
    sketch.annotate("", (-0.5, -0.64), (0.5, -0.64),
                    arrowprops={"arrowstyle": "<->", "color": gray})
    sketch.text(0, -0.59, r"Mirror separation $l$", ha="center")
    sketch.text(0, -0.28, "Central waist", ha="center", color=blue)
    sketch.text(0, -0.40, "Fundamental Gaussian mode", ha="center", fontsize=11)
    sketch.set(xlim=(-0.77, 0.77), ylim=(-0.79, 0.82), title="Symmetric resonator (schematic)")
    sketch.set_axis_off()
    x = np.linspace(0, 2, 1001)
    waist = np.sqrt((x / 2) * (1 - x / 2))
    ax.axvspan(0, 2, color=green, alpha=0.07)
    ax.plot(x, waist, color=blue, lw=2.5)
    ax.scatter([0, 2], [0, 0], s=65, facecolors="white", edgecolors=blue, lw=1.7, zorder=4)
    ax.axvline(1, color=green, ls=":", lw=1.3)
    ax.scatter([1], [0.5], color=green, s=55, zorder=4)
    ax.annotate("Confocal: $l=R$\nStable, including this exact point", (1, 0.5),
                (1, 0.62), ha="center", fontsize=11, color=green,
                arrowprops={"arrowstyle": "->", "color": green})
    ax.text(1, 0.15, r"Stable: $0<l<2R$", ha="center", color=green, fontsize=14)
    ax.text(0.5, 0.035, "Planar limit", ha="center", fontsize=10, color=gray)
    ax.text(1.64, 0.035, "Concentric limit", ha="center", fontsize=10, color=gray)
    ax.set(xlim=(-0.08, 2.08), ylim=(-0.025, 0.74), xticks=(0, 0.5, 1, 1.5, 2),
           yticks=(0, 0.25, 0.5), xlabel=r"Mirror separation $l/R$",
           ylabel=r"Normalized waist area $\pi w_0^2/(\lambda R)$",
           title="Waist area across the stable interval")
    ax.grid(alpha=0.16)
    fig.suptitle("Symmetric concave-mirror cavity", fontsize=17, y=0.97)
    fig.text(0.5, 0.095,
             r"$\frac{\pi w_0^2}{\lambda R}=\sqrt{\frac{l}{2R}\left(1-\frac{l}{2R}\right)}$",
             ha="center", fontsize=18)
    fig.text(0.5, 0.025, "Open endpoints are limiting geometries; no finite, confined Gaussian mode there.",
             ha="center", fontsize=11, color=gray)
    fig.subplots_adjust(left=0.035, right=0.975, bottom=0.25, top=0.84, wspace=0.26)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
