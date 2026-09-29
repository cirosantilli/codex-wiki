"""Original synthetic calibration and skyline diagrams, not observing data.

Run from _media; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The invented skyline is piecewise linear. R=0.2 degrees is imposed for two
algebraic examples only; it is not an atmospheric refraction law or fit.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


BLUE = "#186caa"
ORANGE = "#b85817"
GRAY = "#65717a"
rise, separation = 3.0, 5.0
calibration_angle = np.arctan2(rise, separation)
assert np.isclose(np.tan(calibration_angle), rise / separation)

plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
fig, (cal, sky) = plt.subplots(1, 2, figsize=(10.5, 5.5), facecolor="white")
fig.subplots_adjust(left=0.04, right=0.97, bottom=0.21, top=0.79, wspace=0.30)
fig.suptitle("A level reference is different from a visible skyline", fontsize=16, y=0.97)
fig.text(0.5, 0.88, "Synthetic geometry and invented angular boundary · no measured sky positions", ha="center", fontsize=11)

cal.set_aspect("equal")
cal.axis("off")
cal.plot([0, separation], [0, 0], "--", color=GRAY, lw=1.5)
cal.plot([separation, separation], [0, rise], color=GRAY, lw=1.5)
cal.plot([0, separation], [0, rise], color=BLUE, lw=2)
cal.scatter([0, separation, separation], [0, 0, rise], color=["black", GRAY, BLUE], s=30, zorder=5)
# Sighting tube and its gravity reference are shown schematically at O.
direction = np.array([np.cos(calibration_angle), np.sin(calibration_angle)])
tube = np.array([-0.45 * direction, 0.85 * direction])
cal.plot(tube[:, 0], tube[:, 1], color=BLUE, lw=8, solid_capstyle="round")
cal.plot([0, 0], [0, -1.15], color=ORANGE, lw=1.8)
cal.scatter([0], [-1.15], color=ORANGE, s=80, marker="o")
cal.text(-0.22, -0.62, "Free\nweight", ha="right", color=ORANGE, fontsize=10)
cal.text(-0.12, 0.55, "Sighting tube\n(schematic)", ha="right", color=BLUE, fontsize=10)
arc = np.linspace(0, calibration_angle, 100)
cal.plot(1.15 * np.cos(arc), 1.15 * np.sin(arc), color=ORANGE, lw=2)
cal.text(1.30, 0.22, r"$\gamma_{\rm ref}=30.964^\circ$", color=ORANGE)
cal.text(separation / 2, -0.36, r"Horizontal separation $d=5$ m", ha="center", fontsize=10)
cal.text(separation + 0.16, rise / 2, "$q=3$ m\nrise", va="center", fontsize=10)
cal.text(separation + 0.13, rise + 0.22, "Reference\nmark", ha="center", color=BLUE, fontsize=10)
cal.text(2.4, -0.94, "Level sight gives the angular zero", ha="center", color=GRAY, fontsize=10)
cal.plot([4.75, 4.75, 5], [0, 0.25, 0.25], color=GRAY, lw=1)
cal.set_xlim(-1.45, 6.15)
cal.set_ylim(-1.62, 3.68)
cal.set_title("Calibration triangle · vertical section", fontsize=12, pad=15)

eta = np.array([0, 20, 45, 70, 95, 120, 145, 180])
terrain = np.array([1.0, 2.0, 4.0, 2.5, 1.5, 2.0, 3.5, 1.0])
sky.fill_between(eta, -1, terrain, color="#e9e3d7")
sky.plot(eta, terrain, color="#796246", lw=2)
sky.axhline(0, color=GRAY, lw=1.7, linestyle="--")
sky.text(93, 0.25, "Geometric horizon · 0°", color=GRAY, fontsize=9, ha="center")
sky.text(106, 4.1, "Invented terrain boundary", color="#796246", fontsize=10, ha="center")
for bearing, geom, label in [(45, 3.0, "Blocked"), (120, 7.0, "Clears boundary")]:
    apparent = geom + 0.2
    sky.scatter([bearing], [geom], s=60, marker="o", facecolors="white", edgecolors=BLUE, zorder=5)
    sky.scatter([bearing], [apparent], s=75, marker="*", color=ORANGE, zorder=6)
    sky.plot([bearing, bearing], [geom, apparent], color=ORANGE, lw=2)
    sky.annotate(label, xy=(bearing, apparent), xytext=(bearing, apparent + 0.7),
                 ha="center", color=BLUE, fontsize=10,
                 arrowprops={"arrowstyle": "-", "color": BLUE})
    assert (apparent > np.interp(bearing, eta, terrain)) == (bearing == 120)
sky.scatter([], [], facecolors="white", edgecolors=BLUE, marker="o", label="Geometric direction")
sky.scatter([], [], color=ORANGE, marker="*", label="Apparent direction")
sky.legend(loc="upper center", bbox_to_anchor=(0.5, -0.27), frameon=False, fontsize=9, ncol=2)
sky.set_xlim(0, 180)
sky.set_ylim(-1, 9)
sky.set_xticks([0, 45, 90, 135, 180])
sky.set_xlabel(r"Azimuth $\eta$ (degrees from north through east)", fontsize=10)
sky.set_ylabel(r"Altitude $\gamma$ (degrees)", fontsize=10)
sky.spines[["top", "right"]].set_visible(False)
sky.set_title("Apparent clearance · angular chart", fontsize=12, pad=15)
sky.text(92, -0.8, r"Imposed example: $\gamma_{\rm app}=\gamma_{\rm geom}+0.2^\circ$", ha="center", fontsize=9)

fig.text(0.5, 0.055, "The triangle sets the scale; skyline height is a separate function of azimuth. Refraction shift here is illustrative.", ha="center", fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
