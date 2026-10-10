"""Original analytic Möbius-band model; output the matching PNG to the CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
R, a = 2., .55

def surface(theta, w):
    return ((R + w * np.cos(theta / 2)) * np.cos(theta),
            (R + w * np.cos(theta / 2)) * np.sin(theta),
            w * np.sin(theta / 2))

def normal(theta):
    return (np.cos(theta) * np.sin(theta / 2),
            np.sin(theta) * np.sin(theta / 2),
            -np.cos(theta / 2))

fig = plt.figure(figsize=(10.6, 5.3), layout="constrained")
left = fig.add_subplot(1, 2, 1, projection="3d")
right = fig.add_subplot(1, 2, 2)
t, w = np.meshgrid(np.linspace(0, 2 * np.pi, 160), np.linspace(-a, a, 22))
left.plot_surface(*surface(t, w), color="#d7e4ee", alpha=.65, linewidth=0,
                  antialiased=True, shade=True)
boundary = np.linspace(0, 4 * np.pi, 801)
left.plot(*surface(boundary, a), color="#087e8b", lw=2.4, label="Single boundary")
core = np.linspace(0, 2 * np.pi, 401)
left.plot(*surface(core, 0), color="#303030", lw=1.6, ls=":", label="Core circle")
for theta in np.linspace(.45, 5.75, 7):
    left.quiver(*surface(theta, 0), *normal(theta), length=.65, color="#747474",
                linewidth=1.4, arrow_length_ratio=.23)
for theta, color, label in [(0., "#c45b12", r"$n(0)$"),
                             (2 * np.pi, "#2855a6", r"$n(2\pi)$")]:
    left.quiver(*surface(theta, 0), *normal(theta), length=1.15, color=color,
                linewidth=3, arrow_length_ratio=.19)
    x, y, z = surface(theta, 0)
    nx, ny, nz = normal(theta)
    left.text(x + 1.25 * nx, y + 1.25 * ny, z + 1.25 * nz, label, color=color,
              fontsize=13)
left.set(xlim=(-2.7, 2.7), ylim=(-2.7, 2.7), zlim=(-1.45, 1.45),
         title="Opposite normals at the same point")
left.set_box_aspect((1, 1, .55), zoom=1.35)
left.view_init(elev=26, azim=-57)
left.set_axis_off()
left.legend(loc="lower left", frameon=False, fontsize=11)
theta = np.linspace(0, 4 * np.pi, 601)
right.plot(theta, np.cos(theta / 2), color="#333333", lw=2.6)
right.axhline(0, color="#aaaaaa", lw=.8)
for x, y, color in [(0, 1, "#c45b12"), (2 * np.pi, -1, "#2855a6"),
                     (4 * np.pi, 1, "#087e8b")]:
    right.scatter([x], [y], color=color, s=65, zorder=3)
right.set(xticks=[0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi],
          xticklabels=["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"],
          xlim=(-.25, 4*np.pi + .25), ylim=(-1.28, 1.28),
          xlabel=r"Travel parameter $\theta$",
          ylabel=r"Ambient comparison $n(\theta)\cdot n(0)$",
          title=r"$n(\theta)\cdot n(0)=\cos(\theta/2)$")
right.text(2*np.pi, -.93, "One circuit:\nreversed at starting point",
           ha="center", va="bottom", fontsize=11, color="#2855a6")
right.text(4*np.pi-.18, .91, "Two circuits:\noriginal direction", ha="right",
           va="top", fontsize=11, color="#087e8b")
right.grid(alpha=.18)
fig.suptitle("Möbius band: normal reversal after one circuit", fontsize=17)
fig.supxlabel("Mathematical model, not measured data; the graph is not parallel transport",
              fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
