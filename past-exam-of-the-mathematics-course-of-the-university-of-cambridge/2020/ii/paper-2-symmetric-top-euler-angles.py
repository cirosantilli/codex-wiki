#!/usr/bin/env python3
"""Draw the Euler angles of the symmetric top in 2020 Part II Paper 2."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


OUTPUT = Path(__file__).with_suffix(".svg")
plt.rcParams["svg.hashsalt"] = "codex-wiki"

phi = np.deg2rad(38.0)
theta = np.deg2rad(34.0)
line = np.array([np.cos(phi), np.sin(phi), 0.0])
e3 = np.array([-np.sin(theta) * np.sin(phi), np.sin(theta) * np.cos(phi), np.cos(theta)])
perp = np.cross(e3, line)
perp /= np.linalg.norm(perp)

fig = plt.figure(figsize=(7.0, 6.0))
ax = fig.add_subplot(111, projection="3d")


def arrow(vector, label, color, width=1.8, scale=1.0):
    vector = scale * vector
    ax.quiver(0, 0, 0, *vector, color=color, linewidth=width, arrow_length_ratio=0.08)
    ax.text(*(1.08 * vector), label, color=color, fontsize=12)


arrow(np.array([1.0, 0.0, 0.0]), "$x$", "#555555", scale=0.95)
arrow(np.array([0.0, 0.0, 1.0]), "$z$", "#555555", scale=1.15)
arrow(line, "line of nodes", "#7b4ab5", scale=1.0)
arrow(e3, "$\\mathbf{e}_3$", "#176b87", width=2.4, scale=1.2)

# A small disk perpendicular to the symmetry axis represents the top.
angles = np.linspace(0.0, 2.0 * np.pi, 90)
radius = 0.42
center = 0.60 * e3
rim = center + radius * (np.cos(angles)[:, None] * line + np.sin(angles)[:, None] * perp)
ax.add_collection3d(Poly3DCollection([rim], facecolor="#8ec6d4", edgecolor="#176b87", alpha=0.35))
ax.plot(rim[:, 0], rim[:, 1], rim[:, 2], color="#176b87", linewidth=1.2)

# phi in the fixed horizontal plane.
phis = np.linspace(0.0, phi, 80)
phi_arc = 0.43 * np.column_stack((np.cos(phis), np.sin(phis), np.zeros_like(phis)))
ax.plot(*phi_arc.T, color="#c75146", linewidth=1.8)
ax.text(0.42 * np.cos(phi / 2), 0.42 * np.sin(phi / 2), 0.02, "$\\phi$", color="#c75146", fontsize=13)

# theta in the plane spanned by z and e3.
thetas = np.linspace(0.0, theta, 80)
theta_arc = 0.52 * np.column_stack((-np.sin(thetas) * np.sin(phi), np.sin(thetas) * np.cos(phi), np.cos(thetas)))
ax.plot(*theta_arc.T, color="#d18c00", linewidth=1.8)
mid = theta_arc[len(theta_arc) // 2]
ax.text(*(1.10 * mid), "$\\theta$", color="#a76f00", fontsize=13)

# psi is rotation about e3 from the line of nodes in the body plane.
psis = np.linspace(0.0, np.deg2rad(58.0), 70)
psi_arc = center + 0.29 * (np.cos(psis)[:, None] * line + np.sin(psis)[:, None] * perp)
ax.plot(*psi_arc.T, color="#2a8c55", linewidth=1.8)
label = psi_arc[len(psi_arc) // 2]
ax.text(*(1.07 * label), "$\\psi$", color="#2a8c55", fontsize=13)

ax.set_xlim(-1.0, 1.1)
ax.set_ylim(-0.75, 1.15)
ax.set_zlim(0.0, 1.25)
ax.set_box_aspect((1.25, 1.15, 1.0))
ax.view_init(elev=22, azim=-115)
ax.set_axis_off()
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"Date": None}, transparent=True)
