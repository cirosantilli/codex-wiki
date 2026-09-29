"""Plot a finite sample of exp(1/z)=1 solutions approaching zero.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; write a same-basename opaque PNG.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    k = np.concatenate((np.arange(-50, 0), np.arange(1, 51)))
    z = 1 / (2j * np.pi * k)
    assert np.allclose(np.exp(1 / z), 1, atol=1e-12)
    assert np.allclose(np.abs(z), 1 / (2 * np.pi * np.abs(k)))
    for w in [1, 2, -1, 1 + 2j, -0.1 - 0.3j]:
        denominator = np.log(abs(w)) + 1j * (np.angle(w) + 2 * np.pi * np.arange(-8, 9))
        preimages = 1 / denominator[denominator != 0]
        assert np.allclose(np.exp(1 / preimages), w, atol=1e-12)
    for radius in [0.1, 0.01, 0.001]:
        first = int(np.floor(1 / (2 * np.pi * radius))) + 1
        assert 1 / (2 * np.pi * first) < radius

    plt.rcParams.update({"font.size": 11})
    blue, orange, red = "#176fa1", "#bc6016", "#b63a40"
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 5.4), dpi=130)
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.axhline(0, color="0.8", lw=0.8)
        ax.axvline(0, color="0.8", lw=0.8)
        for mask, color in [(k > 0, blue), (k < 0, orange)]:
            ax.scatter(z[mask].real, z[mask].imag, s=22, color=color, zorder=4)
        ax.scatter([0], [0], s=75, facecolors="white", edgecolors=red,
                   linewidths=1.7, zorder=5)
        ax.set(xlabel=r"$\operatorname{Re}z$", ylabel=r"$\operatorname{Im}z$",
               aspect="equal", facecolor="white")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set(xlim=(-0.12, 0.12), ylim=(-0.18, 0.18),
                title=r"$z_k=1/(2\pi i k)$, $1\leq |k|\leq50$")
    axes[0].add_patch(Rectangle((-0.022, -0.025), 0.044, 0.05,
                               facecolor="#edf4f9", edgecolor="0.45", lw=1, zorder=1))
    for index, xtext in [(1, 0.035), (2, -0.1), (-1, 0.035), (-2, -0.1)]:
        ypoint = -1 / (2 * np.pi * index)
        color = blue if index > 0 else orange
        axes[0].annotate(f"$k={index}$", (0, ypoint), (xtext, ypoint),
                         va="center", color=color, fontsize=10,
                         arrowprops={"arrowstyle": "->", "color": color})
    axes[0].annotate("Magnified at right", (0.02, 0.02), (0.035, 0.045),
                     fontsize=9, arrowprops={"arrowstyle": "->", "color": "0.4"})
    axes[1].set(xlim=(-0.022, 0.022), ylim=(-0.025, 0.025),
                title="Closer to zero: the same finite sample")
    for index in [7, -7, 25, -25]:
        ypoint = -1 / (2 * np.pi * index)
        xtext = 0.005 if abs(index) == 7 else -0.02
        color = blue if index > 0 else orange
        axes[1].annotate(f"$k={index}$", (0, ypoint), (xtext, ypoint),
                         va="center", color=color, fontsize=10,
                         arrowprops={"arrowstyle": "->", "color": color})
    axes[1].annotate("0 is excluded", (0, 0), (0.004, 0.002),
                     color=red, fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": red})
    axes[1].ticklabel_format(axis="both", style="plain", useOffset=False)
    fig.suptitle(r"$e^{1/z}=1$: solutions approach the essential singularity", fontsize=15)
    fig.text(0.5, 0.065, r"$|z_k|=1/(2\pi|k|)\to0$: every $|k|>1/(2\pi r)$ gives a solution in $0<|z|<r$.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.022, "Only 100 points are drawn; the formula establishes infinitely many solutions.",
             ha="center", fontsize=10, color="0.3")
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.2, top=0.82, wspace=0.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified exp(1/z) preimages, five nonzero target values, and three neighborhood bounds.")


if __name__ == "__main__":
    main()
