"""Draw hydrostatic face forces and pressure versus depth; save PNG to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

rho, g, side = 1000.0, 9.81, 0.10
area, volume = side**2, side**3
top, bottom = 0.20, 0.30
pressures = rho * g * np.array([top, bottom])
forces = pressures * area
assert np.allclose(pressures, [1962, 2943])
assert np.allclose(forces, [19.62, 29.43])
assert np.isclose(forces[1] - forces[0], rho * g * volume)
assert np.isclose(rho * g * volume, 9.81)

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
blue, orange, ink = "#156a9c", "#b54720", "#223543"
fig, (ax, chart) = plt.subplots(1, 2, figsize=(10, 5.6), dpi=120,
                              gridspec_kw={"width_ratios": [1.4, 1]})
fig.subplots_adjust(left=0.03, right=0.97, top=0.77, bottom=0.25, wspace=0.25)
fig.suptitle("Buoyancy comes from a pressure difference", fontsize=18, y=0.96)
fig.text(0.5, 0.87, r"Resting water: $\rho_f=1000\ \mathrm{kg/m^3}$, $g=9.81\ \mathrm{m/s^2}$", ha="center", fontsize=13)
ax.set_title("Inward forces on an immersed cube", fontsize=13, pad=12)
ax.set_xlim(-0.27, 0.42)
ax.set_ylim(0.39, -0.045)
ax.axis("off")
ax.add_patch(Rectangle((-0.27, 0), 0.69, 0.39, facecolor="#edf6fb", edgecolor="none"))
ax.plot([-0.27, 0.42], [0, 0], color=blue, lw=2)
ax.text(-0.25, -0.017, "Surface: gauge pressure = 0 Pa", color=blue, fontsize=11)
x0 = 0.07
ax.add_patch(Rectangle((x0, top), side, side, facecolor="#f5d5a1", edgecolor=ink, lw=2, zorder=3))
ax.text(x0 + side/2, (top+bottom)/2, "0.10 m\ncube", ha="center", va="center", fontsize=11, color=ink, zorder=5)


def arrow(start, end, color):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "lw": 2.5, "color": color, "mutation_scale": 15}, zorder=4)


arrow((0.12, 0.12), (0.12, top), orange)
arrow((0.12, 0.375), (0.12, bottom), blue)
ax.text(0.16, 0.145, "19.62 N downward\n(top: 1962 Pa gauge)", va="center", color=orange, fontsize=11)
ax.text(0.14, 0.355, "29.43 N upward\n(bottom: 2943 Pa gauge)", va="center", color=blue, fontsize=11)
for h in [0.22, 0.275]:
    arrow((x0 - 0.06, h), (x0, h), ink)
    arrow((x0 + side + 0.06, h), (x0 + side, h), ink)
ax.text(-0.23, 0.25, "Side forces\ncancel", va="center", color=ink, fontsize=11)
for h, label in [(top, "0.20 m"), (bottom, "0.30 m")]:
    ax.plot([-0.245, -0.20], [h, h], color=blue, lw=1)
    ax.text(-0.195, h + (0.018 if h == bottom else -0.015), label, color=blue, fontsize=10)
ax.annotate("", xy=(-0.25, 0.30), xytext=(-0.25, 0.10),
            arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.5})
ax.text(-0.262, 0.10, "Depth", va="bottom", color=blue, rotation=90, fontsize=10)

h = np.linspace(0, 0.38, 250)
chart.plot(rho*g*h/1000, h, color=blue, lw=2.6)
chart.set_xlim(0, 4.2)
chart.set_ylim(0.38, 0)
chart.set_xlabel("Gauge pressure (kPa)")
chart.set_ylabel("Depth below surface (m)")
chart.set_title(r"$p_g=\rho_fgh$", fontsize=15, pad=12)
chart.grid(alpha=0.20)
for h, p, color, label in zip([top, bottom], pressures, [orange, blue], ["Top", "Bottom"]):
    chart.plot([0, p/1000], [h, h], color=color, lw=1.2, ls="--")
    chart.scatter(p/1000, h, color=color, s=40, zorder=4)
    chart.annotate(f"{label}: {p:.0f} Pa", (p/1000, h),
                   xytext=(10, 8) if label == "Top" else (-8, 10),
                   ha="left" if label == "Top" else "right",
                   textcoords="offset points", color=color, fontsize=11)
fig.text(0.5, 0.105, r"Face area $A=0.010\ \mathrm{m^2}$     |     Net upward force: $29.43-19.62=9.81\ \mathrm{N}$",
         ha="center", color=ink, fontsize=13)
fig.text(0.5, 0.045, "Face forces use gauge pressure. The common surface-pressure contribution cancels.",
         ha="center", fontsize=11)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
plt.close(fig)
