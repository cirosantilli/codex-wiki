"""Compare exact material-patch extension and rotation; output to the current directory.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Build from the repository root: make _media/viscosity-strain-versus-rotation.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


a = omega = 1.0  # s^-1
mu = 0.10  # Pa s
time = 0.65  # s
extension_gradient = np.diag([a, -a])
rotation_gradient = np.array([[0.0, -omega], [omega, 0.0]])
extension_D = 0.5 * (extension_gradient + extension_gradient.T)
rotation_D = 0.5 * (rotation_gradient + rotation_gradient.T)
extension_map = np.diag([np.exp(a * time), np.exp(-a * time)])
angle = omega * time
rotation_map = np.array([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle), np.cos(angle)]])
square = 0.55 * np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])
assert np.allclose(rotation_D, 0.0)
assert np.allclose(2 * mu * extension_D, np.diag([0.20, -0.20]))
assert np.isclose(np.linalg.norm(extension_gradient), np.linalg.norm(rotation_gradient))
assert np.isclose(np.linalg.det(extension_map), 1.0)
assert np.isclose(np.linalg.det(rotation_map), 1.0)
assert np.allclose(rotation_map.T @ rotation_map, np.eye(2))
rotated = square @ rotation_map.T
assert np.allclose(np.linalg.norm(np.diff(rotated, axis=0), axis=1), 1.10)

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
blue = "#1766a0"
orange = "#b04d13"
fig, axes = plt.subplots(1, 2, figsize=(10, 6), dpi=120)
fig.subplots_adjust(left=0.08, right=0.96, top=0.78, bottom=0.33, wspace=0.32)
fig.suptitle("Viscous stress responds to strain, not rigid rotation", y=0.97, fontsize=17)
fig.text(0.5, 0.90, r"$a=\Omega=1\ \mathrm{s^{-1}},\quad \mu=0.10\ \mathrm{Pa\,s},\quad t=0.65\ \mathrm{s}$", ha="center", fontsize=14)
x, y = np.meshgrid(np.linspace(-1.20, 1.20, 7), np.linspace(-1.20, 1.20, 7))

for ax, gradient, mapping, title in zip(
        axes, [extension_gradient, rotation_gradient], [extension_map, rotation_map],
        [r"Planar extension: $\mathbf{u}=(ax,-ay,0)$", r"Rigid rotation: $\mathbf{u}=(-\Omega y,\Omega x,0)$"]):
    ax.set_title(title, fontsize=13, pad=12)
    ax.set_aspect("equal")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_xlabel("x (m)", labelpad=3)
    ax.set_ylabel("y (m)", labelpad=3)
    ax.spines[["top", "right"]].set_visible(False)
    ax.axhline(0, color="#e0e5e9", lw=0.8, zorder=0)
    ax.axvline(0, color="#e0e5e9", lw=0.8, zorder=0)
    vx = gradient[0, 0] * x + gradient[0, 1] * y
    vy = gradient[1, 0] * x + gradient[1, 1] * y
    ax.quiver(x, y, vx, vy, color=blue, alpha=0.65, angles="xy", scale_units="xy", scale=5,
              width=0.007, headwidth=4, zorder=1)
    transformed = square @ mapping.T
    ax.plot(square[:, 0], square[:, 1], "--", lw=2, color="#67737f", zorder=3)
    ax.plot(transformed[:, 0], transformed[:, 1], color=orange, lw=2.8, zorder=4)
    ax.plot(*square[2], "o", color="#67737f", ms=6, zorder=5)
    ax.plot(*transformed[2], "o", color=orange, ms=7, zorder=5)

fig.text(0.29, 0.19, r"$D=\mathrm{diag}(1,-1,0)\ \mathrm{s^{-1}}$", ha="center", fontsize=13)
fig.text(0.29, 0.14, r"$\sigma_{\mathrm{visc}}=\mathrm{diag}(0.20,-0.20,0)\ \mathrm{Pa}$", ha="center", fontsize=12)
fig.text(0.73, 0.19, r"$\nabla\mathbf{u}\ne0,\quad D=0$", ha="center", fontsize=14)
fig.text(0.73, 0.14, r"$\sigma_{\mathrm{visc}}=0$", ha="center", fontsize=14)
handles = [Line2D([0], [0], color=blue, lw=2, label="instantaneous velocity"),
           Line2D([0], [0], color="#67737f", lw=2, ls="--", label="patch at t = 0"),
           Line2D([0], [0], color=orange, lw=2.8, label="patch at t = 0.65 s")]
fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.055), ncol=3, frameon=False, fontsize=11)
fig.text(0.5, 0.025, "Both preserve area. Extension changes shape; rotation preserves all distances.", ha="center", fontsize=12)
output = Path.cwd() / f"{Path(__file__).stem}.png"
fig.savefig(output, facecolor="white", transparent=False)
plt.close(fig)
print(f"{output.name}: 1200 x 720; |grad u|_F={np.linalg.norm(extension_gradient):.8f} s^-1 for both")
print(f"det(extension map)={np.linalg.det(extension_map):.8f}; det(rotation map)={np.linalg.det(rotation_map):.8f}")
print(f"extension stress diagonal={(2 * mu * extension_D).diagonal().tolist()} Pa; rotation D={rotation_D.tolist()}")
