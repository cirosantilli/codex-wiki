"""Meridional second-order-fluid circulation; Python 3.14, NumPy/Matplotlib from root pyproject.
Writes only paper-49-sphere-secondary.png to the caller's current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    # a=1; divide velocities by the positive prefactor c*K**2/(4*mu*a**3).
    axis = np.linspace(-4.0, 4.0, 401)
    x, z = np.meshgrid(axis, axis)
    r = np.hypot(x, z)
    safe = np.maximum(r, 1.0)
    h = 1.0 - 3.0 / safe**2 + 2.0 / safe**3
    hp = 6.0 / safe**3 - 6.0 / safe**4
    vr = h * (3.0 * z**2 / safe**2 - 1.0) / safe**2
    vt = -hp * x * z / safe**3
    vx = np.ma.masked_where(r <= 1.01, vr * x / safe + vt * z / safe)
    vz = np.ma.masked_where(r <= 1.01, vr * z / safe - vt * x / safe)
    fig, ax = plt.subplots(figsize=(7.5, 6.0), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.streamplot(axis, axis, vx, vz, color="#2366a5", density=1.25,
                  linewidth=1.15, arrowsize=1.3, maxlength=8.0)
    ax.add_patch(Circle((0, 0), 1, facecolor="#e6e8eb", edgecolor="#222222", linewidth=1.6, zorder=5))
    ax.text(0, 0, "rotating\nsphere", ha="center", va="center", fontsize=11, zorder=6)
    ax.plot([0, 0], [-4, -1.02], ":", color="#777777", lw=.8)
    ax.plot([0, 0], [1.02, 4], ":", color="#777777", lw=.8)
    ax.annotate("outflow near poles", (0.12, 2.55), (1.35, 3.35),
                arrowprops={"arrowstyle": "->", "color": "#222222"}, fontsize=10)
    ax.annotate("equatorial inflow", (2.5, 0), (1.35, -.55),
                arrowprops={"arrowstyle": "->", "color": "#222222"}, fontsize=10)
    ax.set(xlim=(-4, 4), ylim=(-4, 4), xlabel=r"$x/a$", ylabel=r"$z/a$")
    ax.set_aspect("equal")
    ax.set_title("Elastic secondary flow around a rotating sphere\n"
                 r"$\psi_1+2\psi_2>0$; negligible inertia", fontsize=12)
    fig.subplots_adjust(left=.12, right=.96, bottom=.12, top=.86)
    fig.savefig(Path.cwd() / "paper-49-sphere-secondary.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
