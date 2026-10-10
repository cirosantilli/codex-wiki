"""Matched monochromatic phase at a planar air/water boundary.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; coordinates use lambda_0 as their length unit.
This stipulated n_air=1, n_water=4/3 model is not measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 6.2), layout="constrained")
    colors = ["#176b92", "#bd5125", "#65791b", "#843b91"]
    for ax, qx, title in zip(
        axes, [0.5, 0.0], ["Oblique incidence", "Normal incidence: no bending"]
    ):
        ax.axhspan(0, 2.9, color="#edf6fb")
        ax.axhline(0, color="#333333", lw=1.8)
        ax.axvline(0, color="#666666", ls=":", lw=1.4)
        x = np.linspace(-2.65, 2.65, 1001)
        qs = []
        for n, lo, hi in [(1, -2.9, 0), (4 / 3, 0, 2.9)]:
            qz = np.sqrt(n * n - qx * qx)
            qs.append(qz)
            for m in range(-6, 7):
                z = (m - qx * x) / qz
                mask = (z >= lo) & (z <= hi)
                ax.plot(x[mask], z[mask], color=colors[m % 4], lw=1.5)
            start, end = ((-2.3, -0.6) if lo < 0 else (0.5, 2.5))
            ray = lambda z: (qx * z / qz, z)
            ax.annotate("", xy=ray(end), xytext=ray(start),
                        arrowprops={"arrowstyle": "-|>", "lw": 3, "color": "#111111"})
        if qx:
            crossings = np.arange(-1, 2) / qx
            ax.scatter(crossings, np.zeros_like(crossings), color="#111111", s=25, zorder=5)
            for qz, side in zip(qs, [-1, 1]):
                theta = np.degrees(np.arctan2(qx, qz))
                angles = (270 - theta, 270) if side < 0 else (90 - theta, 90)
                ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=angles[0], theta2=angles[1],
                                 color="#111111", lw=1.5))
            ax.text(-0.73, -0.58, r"$30^\circ$", ha="right", bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
            ax.text(0.75, 0.64, r"$22.0243^\circ$", bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
            ax.text(0, 3.25, r"Same interface crossings: $\Delta x=2\lambda_0$", ha="center", fontsize=11)
        else:
            ax.text(0, 3.25, "No phase variation along the interface", ha="center", fontsize=11)
        for y, label in [(-2.68, r"Air: $n=1$, $\lambda_{\rm a}=\lambda_0$"),
                         (2.70, r"Water: $n=4/3$, $\lambda_{\rm w}=3\lambda_0/4$")]:
            ax.text(-2.48, y, label, va="center", fontsize=11,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
        ax.set(xlim=(-2.65, 2.65), ylim=(3.55, -3.12), title=title,
               xlabel=r"Along interface $x/\lambda_0$", ylabel=r"Into water $z/\lambda_0$")
        ax.set_aspect("equal")
        ax.set_yticks([-2, -1, 0, 1, 2])
    fig.suptitle("Refraction: matched phase, changed wavefront spacing", fontsize=17)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
