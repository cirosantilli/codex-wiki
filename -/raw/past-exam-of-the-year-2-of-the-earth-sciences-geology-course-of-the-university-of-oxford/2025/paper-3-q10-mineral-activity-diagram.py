"""Original activity diagram from mass-action relations; PNG in the CWD."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    fig, axis = plt.subplots(figsize=(8.6, 6.3), layout="constrained")
    fig.patch.set_facecolor("white")
    star_x, star_y = -5.515, 8.955
    x = np.linspace(-8, -3, 801)
    y = np.linspace(0, 19, 801)
    xx, yy = np.meshgrid(x, y)
    # Relative transformed potentials: corundum = 0; neph = -(y+x-3.44),
    # albite = -(y+3x+7.59), on a common two-Al formula normalization.
    potentials = np.stack([np.zeros_like(xx), -(yy + xx - 3.44), -(yy + 3 * xx + 7.59)])
    fields = np.argmin(potentials, axis=0)
    axis.pcolormesh(xx, yy, fields, shading="auto", cmap=ListedColormap(["#ece1ed", "#deedf6", "#fff1cf"]), vmin=-0.5, vmax=2.5, rasterized=True)
    first = 3.44 - x
    second = -7.59 - 3 * x
    for values, stable in [(first, x <= star_x), (second, x >= star_x)]:
        axis.plot(x[~stable], values[~stable], "--", color="0.5", lw=1.5)
        axis.plot(x[stable], values[stable], color="black", lw=2)
    axis.plot([star_x, star_x], [0, star_y], "--", color="0.5", lw=1.5)
    axis.plot([star_x, star_x], [star_y, 19], color="black", lw=2)
    axis.scatter([star_x], [star_y], color="black", s=28, zorder=4)
    axis.annotate("Three-phase intersection\n(−5.515, 8.955)", (star_x, star_y), xytext=(-7.8, 6.6), arrowprops={"arrowstyle": "->", "color": "0.2"}, fontsize=11)
    axis.text(-7.65, 16.5, "Nepheline", fontsize=16)
    axis.text(-4.8, 14, "Albite", fontsize=16)
    axis.text(-5.1, 2.5, "Corundum", fontsize=16)
    axis.text(-7.6, 11.4, "I", fontsize=13)
    axis.text(-3.9, 4.9, "II", fontsize=13)
    axis.text(star_x + 0.09, 17, "III", fontsize=13)
    axis.legend(handles=[Line2D([], [], color="black", lw=2, label="Stable coexistence boundary"), Line2D([], [], color="0.5", ls="--", lw=1.5, label="Metastable continuation")], loc="lower left", fontsize=10)
    axis.set(xlim=(-8, -3), ylim=(0, 19), xlabel=r"$\log_{10} a_{\mathrm{H_4SiO_4}}$", ylabel=r"$\log_{10}(a_{\mathrm{Na^+}}/a_{\mathrm{H^+}})$", title="Mineral activity diagram: stable fields and pairwise equilibria")
    fig.savefig(Path.cwd() / "paper-3-q10-mineral-activity-diagram.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
