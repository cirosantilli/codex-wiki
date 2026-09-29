"""Original spheroid/sphere intersections; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 4.8), layout="constrained", facecolor="white")
ax = fig.add_subplot(1, 2, 1, projection="3d")
section = fig.add_subplot(1, 2, 2)
t, phi = np.meshgrid(np.linspace(0, np.pi, 45), np.linspace(0, 2 * np.pi, 65))
ax.plot_surface(3 * np.cos(t), np.sin(t) * np.cos(phi), np.sin(t) * np.sin(phi), color="#4e98c7", alpha=0.3, linewidth=0)
ax.plot_wireframe(2 * np.cos(t), 2 * np.sin(t) * np.cos(phi), 2 * np.sin(t) * np.sin(phi), rstride=5, cstride=5, color="0.6", alpha=0.35, linewidth=0.7)
angle = np.linspace(0, 2 * np.pi, 401)
offset, radius = np.sqrt(27 / 8), np.sqrt(5 / 8)
for sign, color in [(-1, "#d37619"), (1, "#b73346")]:
    ax.plot(np.full_like(angle, sign * offset), radius * np.cos(angle), radius * np.sin(angle), color=color, lw=2.7)
    ax.scatter([sign * offset], [0], [0], color=color, s=20)
ax.set(xlim=(-3.2, 3.2), ylim=(-2.2, 2.2), zlim=(-2.2, 2.2), xlabel=r"$\xi$", ylabel=r"$\eta$", zlabel=r"$\zeta$", title="Two circles perpendicular to the long axis")
ax.set_box_aspect((6.4, 4.4, 4.4))
ax.view_init(elev=23, azim=-62)
section.plot(3 * np.cos(angle), np.sin(angle), color="#287cae", lw=2, label="Ellipsoid section")
section.plot(2 * np.cos(angle), 2 * np.sin(angle), color="0.5", lw=1.7, label="Sphere section")
for sign, color in [(-1, "#d37619"), (1, "#b73346")]:
    section.plot([sign * offset] * 2, [-radius, radius], "--", color=color, lw=1)
    section.scatter([sign * offset] * 2, [-radius, radius], color=color, s=26, zorder=3)
section.set(xlim=(-3.3, 3.3), ylim=(-2.3, 2.3), xlabel=r"$\xi$", ylabel=r"$\eta$", title=r"Meridional section $\zeta=0$")
section.set_aspect("equal")
section.grid(alpha=0.16)
section.legend(fontsize=9, loc="upper center")
fig.savefig("paper-1-q6-ellipsoid-circles.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
