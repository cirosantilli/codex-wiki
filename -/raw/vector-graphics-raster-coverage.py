"""Exact geometric coverage versus pixel-centre sampling of a synthetic edge.

No measured curves or renderer benchmark: integrate y <= x + 1/4 over
square footprints in [0, 4]^2. Tested with Python 3.14, NumPy 2.3,
Matplotlib 3.10. Run from _media; output goes to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


EDGE_OFFSET = 0.25


def coverage_grid(n):
    """Integrate a clipped linear height using its positive-part primitive."""
    h = 4.0 / n
    x0, y0 = np.meshgrid(np.arange(n) * h, np.arange(n) * h)
    x1, y1 = x0 + h, y0 + h

    def primitive(x, y):
        return 0.5 * np.maximum(x + EDGE_OFFSET - y, 0.0) ** 2

    area = primitive(x1, y0) - primitive(x0, y0) - primitive(x1, y1) + primitive(x0, y1)
    return np.clip(area / h**2, 0.0, 1.0)


def centre_grid(n):
    centres = (np.arange(n) + 0.5) * 4.0 / n
    x, y = np.meshgrid(centres, centres)
    return (y <= x + EDGE_OFFSET).astype(float)


def encode_srgb(linear):
    return np.where(linear <= 0.0031308, 12.92 * linear, 1.055 * linear**(1 / 2.4) - 0.055)


def main():
    coarse, fine, centre = coverage_grid(4), coverage_grid(16), centre_grid(4)
    np.testing.assert_allclose(coarse[0, 0], 23 / 32)
    np.testing.assert_allclose(coarse[1, 0], 1 / 32)
    exact_area = 287 / 32
    for n in (4, 16):
        np.testing.assert_allclose(coverage_grid(n).sum() * (4 / n)**2, exact_area)
    assert centre.sum() == 10

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.1), dpi=110)
    fig.subplots_adjust(left=0.05, right=0.98, bottom=0.25, top=0.76, wspace=0.28)
    fig.suptitle("One stored boundary, three finite raster outputs", y=0.98, fontsize=16)
    fig.text(0.5, 0.91, r"Analytical model: black fill where $y\leq x+1/4$ in $[0,4]^2$; white background",
             ha="center", fontsize=12)
    fig.text(0.5, 0.855, "Shades: area-averaged linear luminance, then sRGB encoding • Orange: geometric boundary overlay",
             ha="center", fontsize=10)
    panels = [(centre, "4 × 4: centre decisions", "Estimated area = 10"),
              (coarse, "4 × 4: exact area coverage", "Summed area = 287/32"),
              (fine, "16 × 16: geometry rendered again", "Summed area = 287/32")]
    for ax, (coverage, title, note) in zip(axes, panels):
        n = len(coverage)
        ax.imshow(encode_srgb(1 - coverage), cmap="gray", vmin=0, vmax=1,
                  interpolation="nearest", extent=(0, 4, 4, 0))
        x = np.linspace(0, 3.75, 100)
        ax.plot(x, x + EDGE_OFFSET, color="#d56a23", lw=1.5)
        boundaries = np.linspace(0, 4, n + 1)
        for boundary in boundaries:
            ax.axhline(boundary, color="#a9bfd1", lw=0.45, alpha=0.85)
            ax.axvline(boundary, color="#a9bfd1", lw=0.45, alpha=0.85)
        ax.set(xlim=(0, 4), ylim=(4, 0), xticks=range(5), yticks=range(5), xlabel="x", ylabel="y ↓")
        ax.set_title(title, fontsize=11, pad=12)
        ax.text(0.5, -0.25, note, transform=ax.transAxes, ha="center", fontsize=11)
    axes[0].scatter([0.5, 0.5], [0.5, 1.5], color="#d56a23", s=24)
    axes[1].text(0.5, 0.5, "23/32", ha="center", va="center", fontsize=10, color="white",
                 bbox={"facecolor": "#303030", "edgecolor": "none", "pad": 2})
    axes[1].text(0.5, 1.5, "1/32", ha="center", va="center", fontsize=10, color="#222222")
    fig.text(0.5, 0.08, "Middle labels are coverage α, not stored grayscale codes. Enlarging that raster repeats or interpolates its values.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.035, "Re-rendering on a finer grid evaluates new footprints; it does not remove finite sampling limits.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
