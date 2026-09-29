"""Original measurement-chain diagram; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Run from _media; the output filename follows this generator's basename.
All profiles and velocities below are illustrative, not observed ELODIE data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 7), facecolor="white")
    flow = fig.add_axes((0.02, 0.53, 0.96, 0.36))
    flow.set(xlim=(0, 10), ylim=(0, 3))
    flow.axis("off")
    blue, orange = "#176497", "#ba531b"

    def box(x, y, w, h, label, color):
        flow.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                     facecolor="white", edgecolor=color, linewidth=1.6))
        flow.text(x+w/2, y+h/2, label, ha="center", va="center", fontsize=10)

    def arrow(a, b, color=blue):
        flow.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=13,
                                      color=color, linewidth=1.7))

    box(0.1, 1.7, 1.55, 0.85, "Telescope\n+ starlight", blue)
    box(0.1, 0.18, 1.55, 0.85, "Reference lamp\n(known lines)", orange)
    box(2.25, 1.7, 1.5, 0.85, "Star fiber", blue)
    box(2.25, 0.18, 1.5, 0.85, "Reference fiber", orange)
    box(4.45, 0.65, 2.5, 1.45, "Echelle grating\n+ cross-disperser\n+ camera", blue)
    box(7.7, 0.65, 2.0, 1.45, "CCD image:\nseparate orders\nand reference traces", blue)
    arrow((1.7, 2.12), (2.18, 2.12))
    arrow((1.7, 0.60), (2.18, 0.60), orange)
    arrow((3.82, 2.12), (4.38, 1.75))
    arrow((3.82, 0.60), (4.38, 1.05), orange)
    arrow((7.02, 1.37), (7.62, 1.37))
    flow.text(5, 2.75, "Simultaneous reference mode (functional schematic)",
              ha="center", fontsize=12, fontweight="bold")

    # A toy correlation dip, typical of an absorption-line mask convention.
    ax = fig.add_axes((0.09, 0.13, 0.36, 0.32))
    velocity = np.linspace(-10_000, 10_000, 2001)
    center, sigma = 60.0, 3000.0
    ccf = 1 - 0.3*np.exp(-0.5*((velocity-center)/sigma)**2)
    ax.plot(velocity/1000, ccf, color=blue, linewidth=2)
    ax.axvline(center/1000, color=orange, linestyle="--", linewidth=1.4)
    ax.annotate("Fitted center: +60 m/s", xy=(0.06, 0.702), xytext=(-9, 0.88),
                arrowprops={"arrowstyle": "->", "color": orange}, color=orange,
                fontsize=10)
    ax.set(xlabel="Trial velocity (km/s)", ylabel="Normalized correlation",
           title="Calibrate wavelengths; correlate many lines", ylim=(0.68, 1.03))
    ax.title.set_fontsize(10)
    ax.text(0.5, -0.27, "Center precision can be finer than line width.",
            transform=ax.transAxes, ha="center", fontsize=9)

    rv = fig.add_axes((0.61, 0.13, 0.35, 0.32))
    phase = np.linspace(0, 2, 801)
    rv.plot(phase, 60*np.cos(2*np.pi*phase), color=blue, linewidth=2)
    sample = np.array([0.02, .13, .31, .49, .72, .9, 1.12, 1.33, 1.54, 1.78, 1.96])
    rv.scatter(sample, 60*np.cos(2*np.pi*sample), color=orange, s=23, zorder=3)
    rv.axhline(0, color="0.75", linewidth=0.7)
    rv.set(xlabel="Time / chosen period", ylabel="Relative radial velocity (m/s)",
           title="Repeat after drift and observer corrections", ylim=(-80, 80))
    rv.title.set_fontsize(10)
    rv.text(0.5, -0.27, "Illustrative centers on an exact periodic model.",
            transform=rv.transAxes, ha="center", fontsize=9)
    fig.text(0.51, 0.30, "→", ha="center", fontsize=28, color=blue)
    fig.suptitle("From starlight to a radial-velocity time series", y=0.97,
                 fontsize=16, fontweight="bold")
    fig.text(0.5, 0.025, "Original schematic and synthetic signals; no discovery data reproduced.",
             ha="center", fontsize=10, color="0.3")
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
