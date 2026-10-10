"""Exact three-dimensional sphere flow in a meridional plane.

Outputs basename PNG in CWD. Tested with Python 3.14.4,
numpy 2.3.5 and matplotlib 3.10.7 (repository dependencies).
Build: make _media/stokes-sphere-streamlines.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def velocity(x, y):
    """Sphere fixed, incident velocity +ex; a=U=1, exterior r>=1."""
    r = np.hypot(x, y)
    f = 1 - 3 / (4 * r) - 1 / (4 * r**3)
    h = -3 / (4 * r) + 3 / (4 * r**3)
    return f + h * x**2 / r**2, h * x * y / r**2


def stream_function(x, y):
    """Axisymmetric stream function, not a planar incompressible one."""
    r = np.hypot(x, y)
    # Factored form is well conditioned near the sphere surface.
    return y**2 * (r - 1)**2 * (2 * r + 1) / (4 * r**3)


theta = np.linspace(0, 2 * np.pi, 101)
u, v = velocity(np.cos(theta), np.sin(theta))
assert np.max(np.hypot(u, v)) < 1e-14
assert np.isclose(velocity(1e7, 0)[0], 1, atol=2e-7)
for x, y in [(1.5, 0.5), (-2.0, 1.0), (0.4, 1.6)]:
    # u_x = (1/y) dpsi/dy, u_y = -(1/y) dpsi/dx in y>0.
    eps = 1e-5
    expected = velocity(x, y)
    from_psi = (
        (stream_function(x, y + eps) - stream_function(x, y - eps)) / (2 * eps * y),
        -(stream_function(x + eps, y) - stream_function(x - eps, y)) / (2 * eps * y),
    )
    assert np.allclose(expected, from_psi, atol=2e-10)

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
fig, ax = plt.subplots(figsize=(9.5, 5.8), dpi=120)
fig.subplots_adjust(left=0.085, right=0.89, bottom=0.20, top=0.80)
xs = np.linspace(-4, 4, 641)
ys = np.linspace(-2.4, 2.4, 385)
x, y = np.meshgrid(xs, ys)
r = np.hypot(x, y)
safe_r = np.maximum(r, 1)
f = 1 - 3 / (4 * safe_r) - 1 / (4 * safe_r**3)
h = -3 / (4 * safe_r) + 3 / (4 * safe_r**3)
ux = f + h * x**2 / safe_r**2
uy = h * x * y / safe_r**2
speed = np.ma.masked_where(r <= 1, np.hypot(ux, uy))
background = ax.pcolormesh(x, y, speed, cmap="Blues", vmin=0, vmax=1,
                          shading="auto", rasterized=True)
psi = np.ma.masked_where(r <= 1, y**2 * (safe_r - 1)**2 * (2 * safe_r + 1) / (4 * safe_r**3))
# Each level corresponds to incident distance b at infinity; mirror symmetry
# is exact because contours depend on y squared and r.
impact = np.array([0.20, 0.40, 0.65, 0.90, 1.20, 1.50, 1.75])
levels = impact**2 / 2
ax.contour(x, y, psi, levels=levels, colors="#293e52", linewidths=1.05)
for level in levels:
    for xpos in (-2.6, 0.0, 2.6):
        lo, hi = max(0, np.sqrt(max(0, 1 - xpos**2))), 5.0
        for _ in range(55):
            mid = (lo + hi) / 2
            if stream_function(xpos, mid) < level:
                lo = mid
            else:
                hi = mid
        ypos = (lo + hi) / 2
        if ypos > 2.3:
            continue
        for sign in (-1, 1):
            vx, vy = velocity(xpos, sign * ypos)
            norm = np.hypot(vx, vy)
            dx, dy = 0.09 * vx / norm, 0.09 * vy / norm
            ax.annotate("", xy=(xpos + dx, sign * ypos + dy),
                        xytext=(xpos - dx, sign * ypos - dy),
                        arrowprops={"arrowstyle": "-|>", "color": "#293e52", "lw": 1,
                                    "mutation_scale": 9})
ax.add_patch(Circle((0, 0), 1, facecolor="#e8e8e8", edgecolor="#273847", lw=1.8, zorder=5))
ax.text(0, 0.45, "fixed sphere", ha="center", zorder=6, fontsize=11)
ax.text(0, 0.08, r"$\mathbf{u}=0$", ha="center", zorder=6, fontsize=14)
ax.annotate("", xy=(0, -1), xytext=(0, 0), zorder=6,
            arrowprops={"arrowstyle": "->", "color": "#273847"})
ax.text(0.10, -0.67, "$a$", fontsize=13, zorder=6)
ax.set(xlim=(-4, 4), ylim=(-2.4, 2.4), xlabel=r"$x/a$", ylabel=r"$y/a$ (meridional slice)")
ax.set_aspect("equal")
cb = fig.colorbar(background, ax=ax, fraction=0.035, pad=0.035)
cb.set_label(r"Speed $|\mathbf{u}|/U$")
fig.suptitle("Stokes flow past a no-slip sphere", y=0.97, fontsize=18)
fig.text(0.5, 0.88, r"Sphere frame: $\mathbf{u}_{\infty}=U\mathbf{e}_x$  →   |   $\mathrm{Re}\ll1$", ha="center", fontsize=13)
fig.text(0.5, 0.095, "Exact axisymmetric streamlines: symmetric before and after the sphere.", ha="center", fontsize=12)
fig.text(0.5, 0.045, "Reversing the incident flow reverses every arrow; both velocity components vanish at r = a.", ha="center", fontsize=10.5)
output = Path.cwd() / f"{Path(__file__).stem}.png"
fig.savefig(output, facecolor="white", transparent=False)
plt.close(fig)
print(f"{output.name}: no-slip, far-field and stream-function checks passed")
