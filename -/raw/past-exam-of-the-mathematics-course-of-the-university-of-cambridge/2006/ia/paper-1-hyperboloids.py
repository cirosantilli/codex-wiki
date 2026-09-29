"""Coordinate hyperboloids; writes the opaque PNG to the caller's CWD.

Uses the repository's Python 3.14 NumPy/Matplotlib environment.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 4.6), facecolor="white", layout="constrained")
theta = np.linspace(0, 2*np.pi, 45)
ax1 = fig.add_subplot(121, projection="3d")
ax2 = fig.add_subplot(122, projection="3d")
angle, radius = np.meshgrid(theta, np.linspace(0, 2, 30))
for sign in [-1, 1]:
    ax1.plot_surface(radius*np.cos(angle), radius*np.sin(angle),
                     sign*np.sqrt(1+radius**2), color="#77a9c6",
                     edgecolor="#ecf3f8", linewidth=.18, alpha=.95)
angle, height = np.meshgrid(theta, np.linspace(-2, 2, 45))
radius = np.sqrt(1+height**2)
ax2.plot_surface(radius*np.cos(angle), radius*np.sin(angle), height,
                 color="#ce9976", edgecolor="#f7efe9", linewidth=.18, alpha=.95)
ax2.plot(np.cos(theta), np.sin(theta), np.zeros_like(theta),
         color="#964521", lw=1.5)
for ax in [ax1, ax2]:
    ax.set(xlim=(-2.5, 2.5), ylim=(-2.5, 2.5), zlim=(-2.5, 2.5),
           xlabel=r"$x$", ylabel=r"$y$", zlabel=r"$z$",
           xticks=[-2, 0, 2], yticks=[-2, 0, 2], zticks=[-2, 0, 2])
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=23, azim=-55)
    ax.tick_params(labelsize=8)
ax1.set_title(r"$a=1$: two sheets", fontsize=12)
ax2.set_title(r"$a=-1$: one sheet", fontsize=12)
fig.suptitle(r"$z^2-x^2-y^2=a$", fontsize=15)
fig.savefig("paper-1-hyperboloids.png", dpi=120, facecolor="white")
plt.close(fig)
