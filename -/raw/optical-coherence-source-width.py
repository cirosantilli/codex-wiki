"""Uniform incoherent angular-source model; no measured data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../optical-coherence-source-width.py
Writes only the matching PNG basename in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(10.5, 5.8), facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=(1.4, 1), left=0.07, right=0.98, top=0.83, bottom=0.17, hspace=0.42, wspace=0.28)
    geometry, curves = fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1])
    strips = fig.add_subplot(grid[1, :])
    fig.suptitle("Spatial coherence: averaging fringes from an extended source", fontsize=14, y=0.97)
    geometry.axis("off")
    geometry.set(xlim=(-0.7, 6.5), ylim=(-1.8, 1.8))
    geometry.set_title("Two openings sample the field (schematic)", fontsize=11)
    geometry.plot([0, 0], [-0.9, 0.9], lw=7, color="#b95516", solid_capstyle="butt")
    for source_y in (-0.9, 0.9):
        for hole_y in (-0.48, 0.48):
            geometry.plot([0, 3.1], [source_y, hole_y], color="#b95516", lw=1, alpha=0.6)
    geometry.plot([3.1, 3.1], [-1.2, 1.2], color="#333333", lw=3)
    for hole_y in (-0.48, 0.48):
        geometry.plot(3.1, hole_y, "o", color="white", markeredgecolor="#1768ac", ms=8, zorder=5)
        geometry.plot([3.1, 5.8], [hole_y, 0], color="#1768ac", lw=1.5)
    geometry.plot([5.8, 5.8], [-1.2, 1.2], color="#333333", lw=3)
    geometry.annotate("", xy=(3.45, 0.48), xytext=(3.45, -0.48), arrowprops={"arrowstyle": "<->", "color": "#333333"})
    geometry.text(3.64, 0, r"$d$", va="center", fontsize=12)
    geometry.annotate("", xy=(-0.37, 0.9), xytext=(-0.37, -0.9), arrowprops={"arrowstyle": "<->", "color": "#333333"})
    geometry.text(-0.52, 0, r"$w$", va="center", ha="right", fontsize=12)
    geometry.text(0, 1.33, "incoherent\nluminous slit", ha="center", fontsize=9)
    geometry.text(5.8, 1.4, "screen", ha="center", fontsize=9)
    geometry.annotate("", xy=(3.1, -1.46), xytext=(0, -1.46), arrowprops={"arrowstyle": "<->", "color": "#333333"})
    geometry.text(1.55, -1.36, r"$R\gg w,d$; full angular width $\Theta\simeq w/R$", ha="center", fontsize=9)
    q = np.linspace(0, 2.5, 800)
    gamma = np.sinc(q)  # NumPy sinc(q) = sin(pi q)/(pi q).
    curves.plot(q, np.abs(gamma), color="#1768ac", lw=2.5, label=r"Visibility $|g^{(1)}_{12}|$")
    curves.plot(q, gamma, color="#b95516", ls="--", lw=1.8, label=r"Signed correlation $g^{(1)}_{12}$")
    curves.axhline(0, color="#999999", lw=0.8)
    curves.set(xlim=(0, 2.5), ylim=(-0.3, 1.05), xlabel=r"Source width parameter $q=d\Theta/\lambda$", ylabel="Correlation / contrast")
    curves.set_title("Uniform angular brightness; equal beam intensities", fontsize=10)
    curves.grid(alpha=0.2)
    curves.legend(loc="upper right", fontsize=9)
    phi = np.linspace(-4 * np.pi, 4 * np.pi, 1200)
    values = np.array([0.0, 0.5, 1.0, 1.5])
    image = 1 + np.sinc(values)[:, None] * np.cos(phi)[None, :]
    strips.imshow(image, cmap="gray", vmin=0, vmax=2, interpolation="nearest", aspect="auto", extent=(-4, 4, 3.5, -0.5))
    strips.set_yticks(range(4), [r"$q=0$: point-source limit", r"$q=0.5$: contrast $2/\pi$", r"$q=1$: zero contrast", r"$q=1.5$: inverted fringes"])
    strips.tick_params(axis="y", length=0, labelsize=9)
    strips.set_xticks(range(-4, 5))
    strips.set_xlabel(r"Common phase coordinate $\phi/\pi$ (not a distance scale)", fontsize=9)
    for boundary in (0.5, 1.5, 2.5):
        strips.axhline(boundary, color="white", lw=2)
    fig.text(0.5, 0.057, r"Calculated model, not measured data: $I/(I_1+I_2)=1+g^{(1)}_{12}\cos\phi$. Grayscale runs from 0 (black) to 2 (white).", ha="center", fontsize=9)
    fig.text(0.5, 0.018, "Narrow spectrum, small source angles, matched delays and negligible opening widths; diffraction envelope omitted.", ha="center", fontsize=9)
    # Reserve horizontal space for the explanatory strip labels.
    pos = strips.get_position()
    strips.set_position([0.27, pos.y0, 0.71, pos.height])
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
