"""Generate stellar-parallax-geometry.png in the current working directory.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp python3 ../stellar-parallax-geometry.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The left panel exaggerates the angle; the right uses an ideal circular orbit,
an ecliptic-plane target, and no proper motion. No catalogue data are plotted.
"""

import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc


def main():
    plt.rcParams.update({"font.size": 13, "savefig.facecolor": "white"})
    fig, (geometry, sky) = plt.subplots(1, 2, figsize=(11, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.97, bottom=0.18, top=0.80, wspace=0.34)
    fig.suptitle("Stellar parallax: one angle, two observing positions", fontsize=20, y=0.97)
    fig.text(0.5, 0.90, "Ideal circular orbit; geometry schematic, angles exaggerated, not to scale",
             ha="center", fontsize=12)

    star_y, orbit_radius = 6.0, 2.0
    colors = ("#2368ac", "#cf6519")
    for x, color, name in zip((-orbit_radius, orbit_radius), colors, ("Earth: January", "Earth: July")):
        geometry.plot([x, 0], [0, star_y], color=color, lw=2.4)
        geometry.scatter([x], [0], s=85, color=color, zorder=4)
        geometry.text(x, 0.33, name, ha="center", fontsize=12,
                      bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    geometry.plot([0, 0], [0, star_y], ls="--", color="#727272", lw=1.5)
    geometry.plot([-orbit_radius, orbit_radius], [0, 0], color="#777777", lw=1.2)
    geometry.scatter([0], [0], s=125, color="#e8aa19", edgecolor="#8c650c", zorder=4)
    geometry.text(-0.2, -0.35, "Sun", ha="right")
    geometry.scatter([0], [star_y], marker="*", s=230, color="#453778", zorder=5)
    geometry.text(0, star_y + 0.48, "Star", ha="center", weight="bold")

    angle = math.degrees(math.atan(orbit_radius / star_y))
    geometry.add_patch(Arc((0, star_y), 3.7, 3.7, theta1=270 - angle, theta2=270,
                          color=colors[0], lw=2))
    geometry.text(-0.44, 3.79, r"$p$", color=colors[0], fontsize=19)
    geometry.annotate("", xy=(3.25, star_y), xytext=(3.25, 0),
                      arrowprops={"arrowstyle": "<->", "color": "#555555", "lw": 1.4})
    geometry.text(3.45, 3, r"$d$", fontsize=17, va="center")
    for left, right, y, label in ((0, 2, -0.55, "1 AU"), (-2, 2, -1.42, "2 AU: six months apart")):
        geometry.annotate("", xy=(right, y), xytext=(left, y),
                          arrowprops={"arrowstyle": "<->", "lw": 1.5, "color": "#333333"})
        geometry.text((left + right) / 2, y - 0.12, label, ha="center", va="top", fontsize=12)
    geometry.text(0, -2.95, r"$\tan p = (1\,\mathrm{AU})/d$", ha="center", fontsize=16)
    geometry.set(xlim=(-3.5, 3.95), ylim=(-3.6, 7.1), aspect="equal")
    geometry.axis("off")

    months = np.linspace(0, 12, 241)
    p_arcsec = 0.05
    displacement = -p_arcsec * np.cos(2 * np.pi * months / 12)
    sky.plot(months, displacement, lw=2.8, color="#453778")
    sky.axhline(0, color="#888888", ls="--", lw=1)
    sky.scatter([0, 6, 12], [-p_arcsec, p_arcsec, -p_arcsec],
                color=[colors[0], colors[1], colors[0]], s=65, zorder=4)
    sky.annotate("", xy=(6, p_arcsec), xytext=(6, -p_arcsec),
                 arrowprops={"arrowstyle": "<->", "lw": 1.8, "color": colors[1]})
    sky.text(6.55, -0.002, '2p = 0.10 arcsec', fontsize=12, va="center",
             bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    sky.set(xlim=(-0.5, 12.5), ylim=(-0.08, 0.08),
            xticks=[0, 3, 6, 9, 12], yticks=[-0.05, 0, 0.05],
            xlabel="Time since January (months)", ylabel="Angular displacement (arcsec)")
    sky.set_title('p = 0.05 arcsec  ⇒  d ≈ 20 pc', fontsize=16, pad=14)
    sky.spines[["top", "right"]].set_visible(False)
    fig.text(0.72, 0.05, "Ideal annual signal after proper motion is removed", ha="center", fontsize=11)
    fig.savefig("stellar-parallax-geometry.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print("Wrote stellar-parallax-geometry.png (1100 × 570); ideal p = 0.05 arcsec.")


if __name__ == "__main__":
    main()
