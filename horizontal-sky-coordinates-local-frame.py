"""Original analytical diagram of a synthetic local sky direction.

Run from _media; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The plan view shows the horizontal projection, not a second sky position.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


BLUE = "#186caa"
ORANGE = "#b85817"
GRAY = "#65717a"
eta, gamma = np.deg2rad([60.0, 30.0])
east = np.cos(gamma) * np.sin(eta)
north = np.cos(gamma) * np.cos(eta)
up = np.sin(gamma)
horizontal = np.hypot(east, north)
assert np.isclose(east**2 + north**2 + up**2, 1)

plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
fig, (plan, side) = plt.subplots(1, 2, figsize=(10.4, 5.2), facecolor="white")
fig.subplots_adjust(left=0.04, right=0.97, bottom=0.17, top=0.81, wspace=0.22)
fig.suptitle("One direction, two views of the local frame", fontsize=17, y=0.97)
fig.text(0.5, 0.89, r"Analytical illustration: $\eta=60^\circ$, $\gamma=30^\circ$; unit sky sphere", ha="center")

for ax in (plan, side):
    ax.set_aspect("equal")
    ax.axis("off")

az = np.linspace(0, 2 * np.pi, 361)
plan.plot(np.sin(az), np.cos(az), color=GRAY, lw=1.4)
for end in [(1.08, 0), (-1.08, 0), (0, 1.08), (0, -1.08)]:
    plan.annotate("", xy=end, xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": GRAY})
for x, y, text in [(0, 1.18, "N · 0°"), (1.26, 0, "E · 90°"),
                   (0, -1.18, "S · 180°"), (-1.28, 0, "W · 270°")]:
    plan.text(x, y, text, ha="center", va="center")
plan.annotate("", xy=(east, north), xytext=(0, 0),
              arrowprops={"arrowstyle": "->", "lw": 2.7, "color": BLUE})
plan.plot([east, east, 0], [0, north, north], "--", color=GRAY, lw=1)
plan.scatter([east], [north], color=BLUE, s=35, zorder=4)
plan.text(east + 0.09, north + 0.12, "Horizontal\nprojection", color=BLUE, ha="left", fontsize=10)
arc = np.linspace(0, eta, 80)
plan.plot(0.38 * np.sin(arc), 0.38 * np.cos(arc), color=ORANGE, lw=2)
plan.annotate("", xy=(0.38 * np.sin(eta), 0.38 * np.cos(eta)),
              xytext=(0.38 * np.sin(eta - 0.15), 0.38 * np.cos(eta - 0.15)),
              arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 1.7})
plan.text(0.18, 0.52, r"$\eta=60^\circ$", color=ORANGE)
plan.text(0.40, -0.10, r"$E=3/4$", ha="center", color=BLUE)
plan.text(-0.12, 0.22, r"$N=\sqrt{3}/4$", ha="right", color=BLUE, fontsize=10)
plan.scatter([0], [0], color="black", s=18, zorder=5)
plan.set_xlim(-1.6, 1.65)
plan.set_ylim(-1.35, 1.45)
plan.set_title("Plan view · looking downward", fontsize=12, pad=12)

elev = np.linspace(0, np.pi, 181)
side.plot(np.cos(elev), np.sin(elev), color=GRAY, lw=1.4)
side.axhline(0, color=GRAY, lw=1)
side.annotate("", xy=(0, 1.16), xytext=(0, 0),
              arrowprops={"arrowstyle": "->", "color": GRAY})
side.annotate("", xy=(horizontal, up), xytext=(0, 0),
              arrowprops={"arrowstyle": "->", "lw": 2.7, "color": BLUE})
side.plot([horizontal, horizontal], [0, up], "--", color=GRAY, lw=1.2)
side.plot([0, horizontal], [0, 0], color=BLUE, lw=2.5)
side.scatter([horizontal], [up], color=BLUE, s=40, zorder=4)
side.text(horizontal + 0.06, up + 0.07, "Sky direction", color=BLUE, fontsize=10)
side.text(horizontal + 0.05, up / 2, r"$U=1/2$", color=BLUE, fontsize=10)
alt_arc = np.linspace(0, gamma, 80)
side.plot(0.40 * np.cos(alt_arc), 0.40 * np.sin(alt_arc), color=ORANGE, lw=2)
side.text(0.47, 0.10, r"$\gamma=30^\circ$", color=ORANGE)
zen_arc = np.linspace(gamma, np.pi / 2, 80)
side.plot(0.65 * np.cos(zen_arc), 0.65 * np.sin(zen_arc), color="#36815a", lw=2)
side.text(0.17, 0.74, r"$z=60^\circ$", color="#36815a")
side.text(-0.09, 1.20, "Zenith · up", ha="center")
side.text(horizontal / 2, -0.16, r"$\sqrt{E^2+N^2}=\sqrt{3}/2$", ha="center", color=BLUE, fontsize=10)
side.text(0, -0.36, "Horizontal plane in this vertical section", ha="center", color=GRAY, fontsize=10)
side.scatter([0], [0], color="black", s=18, zorder=5)
side.text(-0.10, -0.13, "O", ha="right")
side.set_xlim(-1.22, 1.49)
side.set_ylim(-0.42, 1.35)
side.set_title("Vertical section through the direction", fontsize=12, pad=12)

fig.text(0.5, 0.06, "O is the observer. Azimuth turns from north through east; altitude rises from the horizontal plane.", ha="center", fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
