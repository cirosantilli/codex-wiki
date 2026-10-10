"""Compare floating, neutral and sinking cubes; save an opaque PNG to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

rho_water, g, side = 1000.0, 9.81, 0.10
volume = side**3
rho_body = np.array([600.0, 1000.0, 1200.0])
mass = rho_body * volume
weight = mass * g
fraction = rho_body[0] / rho_water
floating_depth = fraction * side
fully_immersed_buoyancy = rho_water * g * volume
buoyancy = np.array([weight[0], fully_immersed_buoyancy, fully_immersed_buoyancy])
assert np.allclose(mass, [0.6, 1.0, 1.2])
assert np.allclose(weight, [5.886, 9.81, 11.772])
assert np.isclose(fraction, 0.6) and np.isclose(floating_depth, 0.06)
assert np.allclose(weight-buoyancy, [0, 0, 1.962])
assert np.isclose(fully_immersed_buoyancy-weight[0], 3.924)

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
blue, orange, ink = "#156a9c", "#b54720", "#223543"
fig, axes = plt.subplots(1, 3, figsize=(10, 5.6), dpi=120)
fig.subplots_adjust(left=0.03, right=0.97, top=0.74, bottom=0.36, wspace=0.24)
fig.suptitle("Equal-size cubes: floating, neutral, sinking", fontsize=18, y=0.96)
fig.text(0.5, 0.875, r"Each side = 0.10 m; water $\rho_f=1000\ \mathrm{kg/m^3}$; $g=9.81\ \mathrm{m/s^2}$",
         ha="center", fontsize=13)
fig.text(0.5, 0.84, "Blue arrows: buoyancy upward     Orange arrows: weight downward", ha="center", fontsize=11)

for i, (ax, density, fb, mg, title) in enumerate(zip(axes, rho_body, buoyancy, weight,
                                                  ["Floating at rest", "Fully immersed, neutral", "Fully immersed, released"])):
    ax.set_xlim(-0.08, 0.24)
    ax.set_ylim(-0.22, 0.10)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=12, pad=24)
    ax.text(0.5, 1.03, rf"$\rho_{{\mathrm{{body}}}}={density:.0f}\ \mathrm{{kg/m^3}}$",
            transform=ax.transAxes, ha="center", fontsize=12, color=ink)
    ax.add_patch(Rectangle((-0.08, -0.22), 0.32, 0.22, facecolor="#edf6fb", edgecolor="none"))
    ax.plot([-0.08, 0.24], [0, 0], color=blue, lw=2)
    bottom = -floating_depth if i == 0 else -0.15
    ax.add_patch(Rectangle((0.03, bottom), side, side, facecolor="#f5d5a1", edgecolor=ink, lw=2, zorder=3))
    center = bottom + side/2
    for x, signed_length, color in [(-0.005, fb*0.009, blue), (0.165, -mg*0.009, orange)]:
        ax.annotate("", xy=(x, center+signed_length/2), xytext=(x, center-signed_length/2),
                    arrowprops={"arrowstyle": "-|>", "lw": 2.8, "color": color, "mutation_scale": 16}, zorder=4)
    if i == 0:
        ax.annotate("", xy=(0.215, bottom), xytext=(0.215, 0),
                    arrowprops={"arrowstyle": "|-|", "color": ink, "lw": 1.2})
        ax.text(0.228, bottom/2, "0.060 m", fontsize=10, va="center", rotation=90)
        ax.text(0.08, -0.16, "60% of volume\nbelow the surface", ha="center", va="center", fontsize=11, color=ink)
    else:
        ax.text(0.08, -0.205, "Entire volume immersed", ha="center", va="center", fontsize=10, color=ink)
    xpos = [0.173, 0.50, 0.827][i]
    fig.text(xpos, 0.29, f"Buoyancy: {fb:.3f} N upward", color=blue, fontsize=11, ha="center")
    fig.text(xpos, 0.245, f"Weight: {mg:.3f} N downward", color=orange, fontsize=11, ha="center")
    result = "Net force = 0" if i < 2 else "Initial net: 1.962 N down"
    fig.text(xpos, 0.193, result, color=ink, fontsize=12, ha="center", weight="bold")
fig.text(0.5, 0.115, "A neutral, rigid cube has no vertical restoring force at any fully immersed depth in uniform water.",
         ha="center", fontsize=11)
fig.text(0.5, 0.053, "The floating cube, if held fully immersed, needs an extra 3.924 N downward holding force.",
         ha="center", fontsize=11)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
plt.close(fig)
