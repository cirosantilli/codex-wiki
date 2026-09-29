"""Draw plane normals and the intersection line; output a PNG in the cwd."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
fig = plt.figure(figsize=(12, 5.2), layout="constrained")
ax = fig.add_subplot(121, projection="3d")
x, y = np.meshgrid(np.linspace(-1, 1.4, 5), np.linspace(-1, 1.4, 5))
ax.plot_surface(x, y, 2 + 0*x, color="#bed6e5", alpha=.65, edgecolor="none")
ax.quiver(0, 0, 0, 1, .9, 2, color="#a83245", arrow_length_ratio=.08, linewidth=2)
ax.plot([0, 0], [0, 0], [0, 2], color="#354c60", linewidth=2)
ax.plot([0, 1], [0, .9], [2, 2], "--", color="#555555")
ax.quiver(0, 0, 2, 0, 0, .8, color="#176b68", arrow_length_ratio=.2, linewidth=2)
ax.scatter([0, 0, 1], [0, 0, .9], [0, 2, 2], c=["#354c60", "#176b68", "#a83245"], s=24)
ax.text(.03, -.12, -.15, "O")
ax.text(.1, -.1, 1, r"$d$")
ax.text(.04, .05, 2.85, r"$\hat n$")
ax.text(1.05, .95, 2.12, r"$r$")
ax.text(.65, -.15, 1.15, r"$r\cdot\hat n=d$")
ax.set(xlim=(-1.15, 1.7), ylim=(-1.15, 1.7), zlim=(0, 3.1), title="A plane and its unit normal")
ax.set_axis_off()
ax.view_init(elev=18, azim=-65)

ax = fig.add_subplot(122, projection="3d")
x, y = np.meshgrid(np.linspace(.5, 3.5, 25), np.linspace(-.2, 2.2, 25))
z1 = (2*x+6*y-10)/3
z2 = 5*x+2*y-12
z1 = np.ma.masked_outside(z1, -3.5, 3.5)
z2 = np.ma.masked_outside(z2, -3.5, 3.5)
ax.plot_surface(x, y, z1, color="#6fa4c4", alpha=.4, edgecolor="none")
ax.plot_surface(x, y, z2, color="#cf8f5c", alpha=.4, edgecolor="none")
t = np.linspace(-.2, 2.2, 100)
ax.plot(2+0*t, t, 2*t-2, color="#202b39", linewidth=3)
ax.scatter([2], [0], [-2], color="#202b39", s=25)
ax.text(2.07, .06, -2.4, "(2, 0, −2)", fontsize=10)
ax.text2D(.02, .94, r"$2x+6y-3z=10$", transform=ax.transAxes, color="#346482")
ax.text2D(.02, .87, r"$5x+2y-z=12$", transform=ax.transAxes, color="#975e30")
ax.text2D(.02, .01, r"$r=(2,0,-2)+t(0,1,2)$", transform=ax.transAxes)
ax.set(xlabel="x", ylabel="y", zlabel="z", xlim=(.5, 3.5), ylim=(-.2, 2.2), zlim=(-3.5, 3.5), title="The common line")
ax.view_init(elev=20, azim=-35)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
