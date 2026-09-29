"""Original spherical coordinate sketch; output to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7.0, 5.6), layout="constrained")
ax = fig.add_subplot(projection="3d")
theta, phi = np.meshgrid(np.linspace(0, np.pi, 15), np.linspace(0, 2*np.pi, 25))
ax.plot_wireframe(np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi),
                  np.cos(theta), color="0.78", linewidth=0.5, alpha=0.65)
t0, p0 = np.deg2rad([55, -33])
angles = np.linspace(0, 2*np.pi, 500)
ax.plot(np.sin(t0)*np.cos(angles), np.sin(t0)*np.sin(angles),
        np.full_like(angles, np.cos(t0)), color="tab:blue", lw=2.1,
        label=r"latitude: $\theta$ constant")
ts = np.linspace(0, np.pi, 400)
ax.plot(np.sin(ts)*np.cos(p0), np.sin(ts)*np.sin(p0), np.cos(ts),
        color="tab:orange", lw=2.1, label=r"meridian: $\phi$ constant")
er = np.array([np.sin(t0)*np.cos(p0), np.sin(t0)*np.sin(p0), np.cos(t0)])
et = np.array([np.cos(t0)*np.cos(p0), np.cos(t0)*np.sin(p0), -np.sin(t0)])
ep = np.array([-np.sin(p0), np.cos(p0), 0])
ax.scatter(*er, color="black", s=25, depthshade=False)
for vector, label, color in [(er, r"$\mathbf{e}_r$", "tab:red"),
                             (et, r"$\mathbf{e}_\theta$", "tab:green"),
                             (ep, r"$\mathbf{e}_\phi$", "tab:purple")]:
    ax.quiver(*er, *vector, length=0.48, arrow_length_ratio=0.22, color=color, lw=2)
    ax.text(*(er + 0.57*vector), label, color=color, fontsize=14)
ax.plot([0, 0], [0, 0], [-1.15, 1.2], color="0.3", lw=0.8)
ax.text(0, 0, 1.27, "$z$", fontsize=12)
ax.text(0.06, 0, -1.15, "south pole", fontsize=9)
ax.text(-0.05, 0, 1.05, "north pole", fontsize=9, ha="right")
ax.set(xlim=(-1.25, 1.6), ylim=(-1.25, 1.25), zlim=(-1.25, 1.3),
       title="Coordinate curves and basis on a sphere")
ax.set_box_aspect((2.85, 2.5, 2.55), zoom=1.3)
ax.view_init(elev=19, azim=-58)
ax.set_axis_off()
ax.legend(loc="lower left", fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
