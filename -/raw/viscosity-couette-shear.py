"""Draw Couette velocity and face tractions; write the PNG in the current directory.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Build from the repository root: make _media/viscosity-couette-shear.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


U = 0.020  # m/s
h = 0.0010  # m
mu = 0.10  # Pa s
shear_rate = U / h
stress = mu * shear_rate
area = 0.010  # m^2
densities = np.array([1000.0, 500.0])  # kg/m^3
nu = mu / densities
diffusion_times = h**2 / nu
assert np.isclose(shear_rate, 20.0)
assert np.isclose(stress, 2.0)
assert np.isclose(stress * area, 0.020)
assert np.allclose(nu, [1e-4, 2e-4])
assert np.allclose(diffusion_times, [0.010, 0.005])
assert np.isclose(mu * shear_rate**2 * h, stress * U)

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
blue = "#1766a0"
orange = "#b04d13"
ink = "#243341"
fig, axes = plt.subplots(1, 2, figsize=(10, 5.5), dpi=120)
fig.subplots_adjust(left=0.04, right=0.97, top=0.80, bottom=0.20, wspace=0.16)
fig.suptitle("Couette flow: velocity gradient and transmitted shear", y=0.96, fontsize=18)
fig.text(0.5, 0.88, r"$U=0.020\ \mathrm{m/s},\quad h=1.0\ \mathrm{mm},\quad\mu=0.10\ \mathrm{Pa\,s}$", ha="center", fontsize=14)


def arrow(ax, start, end, color, width=2.2):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color,
                            "lw": width, "mutation_scale": 14})


ax = axes[0]
ax.set_title("Velocity between the plates", fontsize=14, pad=14)
ax.set_xlim(-0.48, 3.25)
ax.set_ylim(-0.38, 1.46)
ax.axis("off")
ax.add_patch(Rectangle((0, 0), 2.7, 1, color="#f1f7fb", zorder=0))
for y in (0, 1):
    ax.add_patch(Rectangle((0, y - 0.035), 2.7, 0.07, color="#667380"))
ys = np.linspace(0.15, 0.90, 6)
for y in ys:
    arrow(ax, (0.40, y), (0.40 + 1.8 * y, y), blue)
ax.plot([0.40, 2.20], [0, 1], "--", color=blue, lw=1.5, alpha=0.6)
arrow(ax, (0.40, 1.23), (2.20, 1.23), blue)
ax.text(2.3, 1.23, "$U$", va="center", color=blue, fontsize=15)
ax.text(1.35, 1.08, "moving upper plate", ha="center", va="bottom", color=ink)
ax.text(1.35, -0.12, "fixed lower plate:  u = 0", ha="center", va="top", color=ink)
ax.annotate("", xy=(-0.23, 1), xytext=(-0.23, 0),
            arrowprops={"arrowstyle": "<->", "color": ink, "lw": 1.5})
ax.text(-0.31, 0.5, "$h$", ha="right", va="center", fontsize=15)
ax.text(2.75, 1, "$y=h$", va="center", fontsize=11)
ax.text(2.75, 0, "$y=0$", va="center", fontsize=11)
ax.text(1.35, -0.34, r"$u(y)=Uy/h\quad\Rightarrow\quad du/dy=20\ \mathrm{s^{-1}}$", ha="center", fontsize=13)

ax = axes[1]
ax.set_title("Viscous traction on a fluid slice", fontsize=14, pad=14)
ax.set_xlim(-0.48, 3.25)
ax.set_ylim(-0.38, 1.46)
ax.axis("off")
ax.add_patch(Rectangle((0.45, 0.27), 1.90, 0.50, facecolor="#f1f7fb", edgecolor=blue, lw=2))
ax.text(1.40, 0.52, "fluid slice", ha="center", va="center", color=ink)
arrow(ax, (0.85, 0.77), (2.15, 0.77), orange, 3)
arrow(ax, (2.15, 0.27), (0.85, 0.27), orange, 3)
ax.text(1.5, 1.11, r"top face: $+2\,\mathbf{e}_x\ \mathrm{Pa}$", ha="center", color=orange)
ax.text(1.5, -0.08, r"bottom face: $-2\,\mathbf{e}_x\ \mathrm{Pa}$", ha="center", color=orange)
arrow(ax, (0.45, 0.77), (0.45, 1.04), ink, 1.4)
arrow(ax, (0.45, 0.27), (0.45, 0.00), ink, 1.4)
ax.text(0.32, 1.05, r"$\mathbf{n}=+\mathbf{e}_y$", ha="right", fontsize=11)
ax.text(0.32, 0.00, r"$\mathbf{n}=-\mathbf{e}_y$", ha="right", fontsize=11)
ax.text(1.35, -0.34, r"$\tau_{xy}=\mu U/h=2.0\ \mathrm{Pa}$", ha="center", fontsize=14)

fig.text(0.5, 0.09, "Equal face areas give equal and opposite forces: net viscous force = 0.", ha="center", fontsize=13)
fig.text(0.5, 0.04, "The moving plate feels a backward force; its drive must supply an equal forward force.", ha="center", fontsize=11, color=ink)
output = Path.cwd() / f"{Path(__file__).stem}.png"
fig.savefig(output, facecolor="white", transparent=False)
plt.close(fig)
print(f"{output.name}: 1200 x 660; shear rate={shear_rate:g} s^-1; stress={stress:g} Pa; force={stress * area:g} N")
print(f"nu={nu.tolist()} m^2/s; h^2/nu={diffusion_times.tolist()} s; wall power={stress * U:g} W/m^2")
