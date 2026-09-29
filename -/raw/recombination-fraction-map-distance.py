"""Original Haldane model curve; save an opaque white basename PNG to cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7 (+dfsg1), NumPy 2.3.5.
d is the mean Poisson exchange count on the transmitted chromatid, in morgans.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../recombination-fraction-map-distance.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    d = np.linspace(0, 1.5, 601)
    r = -np.expm1(-2 * d) / 2
    fig, ax = plt.subplots(figsize=(8.6, 5.6), facecolor="white")
    ax.set_facecolor("white")
    ax.plot(d, d, "--", color="#c06923", lw=2, label="Short-interval approximation: r = d")
    ax.plot(d, r, color="#246c94", lw=2.6, label="Haldane: r = (1 − exp(−2d)) / 2")
    ax.axhline(0.5, color="#555555", ls=":", lw=1.8, label="Model ceiling: r = 0.5")
    d_inverse = -np.log1p(-0.4) / 2
    r_at_point = -np.expm1(-0.4) / 2
    ax.scatter((0.2, d_inverse), (r_at_point, 0.2), color="#246c94", s=35, zorder=5)
    ax.annotate("d = 0.2 M → r = 0.164840", xy=(0.2, r_at_point), xytext=(0.47, 0.085),
                fontsize=11, arrowprops={"arrowstyle": "->", "color": "#246c94"})
    ax.annotate("r = 0.2 → d = 0.255413 M\n                         = 25.5413 cM",
                xy=(d_inverse, 0.2), xytext=(0.68, 0.27), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#246c94"})
    ax.text(0.81, 0.69, "The straight line is useful near zero;\nit is not a long-interval probability model.",
            fontsize=11, color="#804414")
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1.56)
    ax.set_xlabel("Map distance d (morgans; 1 M = 100 cM)", fontsize=12)
    ax.set_ylabel("Recombination fraction r", fontsize=12)
    ax.set_title("Map distance counts exchanges; recombination fraction scores parity", fontsize=14, pad=14)
    ax.legend(loc="upper left", fontsize=10, frameon=True, facecolor="white", framealpha=1)
    ax.grid(color="#e2e2e2", lw=0.7)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.035, "Toy model: Poisson(d) exchanges along the transmitted chromatid; independent disjoint counts.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.095, right=0.97, bottom=0.16, top=0.87)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
