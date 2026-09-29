"""Plane internal-wave fields and phase/group-velocity geometry.

Write paper-49-internal-wave.png to the current working directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k, m, buoyancy_frequency = 1.0, 1.5, 1.0
    magnitude = np.hypot(k, m)
    omega = buoyancy_frequency * k / magnitude
    phase_velocity = omega * np.array([k, m]) / magnitude**2
    group_velocity = buoyancy_frequency * np.array([m * m, -k * m]) / magnitude**3
    assert np.isclose(phase_velocity @ group_velocity, 0.0)
    assert np.allclose(phase_velocity + group_velocity, [buoyancy_frequency / magnitude, 0])

    fig, axes = plt.subplots(1, 3, figsize=(12, 4.7), layout="constrained", facecolor="white")
    x = np.linspace(0, 2 * np.pi, 160)
    z = np.linspace(0, 2 * np.pi, 160)
    xx, zz = np.meshgrid(x, z)
    phase = k * xx + m * zz
    qx, qz = np.meshgrid(np.linspace(0.4, 5.9, 10), np.linspace(0.4, 5.9, 10))
    qphase = k * qx + m * qz

    for ax, scalar, arrow_phase, title, bar_title in [
        (axes[0], np.cos(phase), np.cos(qphase), "Buoyancy and displacement", r"$\sigma/A=\cos\phi$"),
        (axes[1], np.sin(phase), np.sin(qphase), "Pressure and velocity", r"$pK^2/(mA)=\sin\phi$"),
    ]:
        field = ax.pcolormesh(xx, zz, scalar, cmap="RdBu_r", vmin=-1, vmax=1, shading="auto")
        ax.contour(xx, zz, phase, levels=np.arange(0, 6 * np.pi, np.pi), colors="#666666", linewidths=0.55, alpha=0.45)
        ax.quiver(qx, qz, m * arrow_phase / k, -arrow_phase, angles="xy", scale_units="xy", scale=4.5, width=0.006, color="#222222")
        ax.set(xlabel=r"$x$", ylabel=r"$z$", title=title, xlim=(0, 2 * np.pi), ylim=(0, 2 * np.pi))
        ax.set_aspect("equal")
        colorbar = fig.colorbar(field, ax=ax, orientation="horizontal", shrink=0.88, pad=0.03, ticks=[-1, 0, 1])
        colorbar.set_label(bar_title)

    axes[0].text(0.03, 0.96, r"Arrows: $(\xi,\zeta)\propto(m/k,-1)\cos\phi$", transform=axes[0].transAxes, va="top", fontsize=8, bbox={"facecolor": "white", "alpha": 0.92, "edgecolor": "none"})
    axes[1].text(0.03, 0.96, r"Arrows: $(u,w)\propto(m/k,-1)\sin\phi$", transform=axes[1].transAxes, va="top", fontsize=8, bbox={"facecolor": "white", "alpha": 0.92, "edgecolor": "none"})
    for vector, label, color, origin in [
        (phase_velocity, r"$\mathbf{c}_p$", "#17633c", (0.7, 2.6)),
        (group_velocity, r"$\mathbf{c}_g$", "#61388d", (0.7, 2.6)),
    ]:
        end = np.array(origin) + 4 * vector
        axes[0].annotate("", xy=end, xytext=origin, arrowprops={"arrowstyle": "->", "color": color, "lw": 2.3})
        axes[0].text(*(end + [0.05, 0.03]), label, color=color, fontsize=12, bbox={"facecolor": "white", "alpha": 0.88, "edgecolor": "none"})

    ax = axes[2]
    tip = phase_velocity
    end = phase_velocity + group_velocity
    for start, finish, color in [(np.zeros(2), tip, "#17633c"), (tip, end, "#61388d")]:
        ax.annotate("", xy=finish, xytext=start, arrowprops={"arrowstyle": "->", "lw": 2.8, "color": color})
    ax.plot([0, end[0]], [0, 0], color="#333333", lw=1.5)
    back = -phase_velocity / np.linalg.norm(phase_velocity)
    onward = group_velocity / np.linalg.norm(group_velocity)
    corner = np.array([tip + 0.035 * back, tip + 0.035 * (back + onward), tip + 0.035 * onward])
    ax.plot(corner[:, 0], corner[:, 1], color="#333333", lw=1)
    ax.text(*(tip / 2 + [-0.08, 0.015]), r"$\mathbf{c}_p$", color="#17633c", fontsize=15)
    ax.text(*((tip + end) / 2 + [0.015, 0.035]), r"$\mathbf{c}_g$", color="#61388d", fontsize=15)
    ax.text(end[0] / 2, -0.055, r"$N/K$", ha="center", fontsize=13)
    ax.text(end[0] / 2, -0.18, r"$\mathbf{c}_p\cdot\mathbf{c}_g=0$" + "\n" + r"$\mathbf{c}_p+\mathbf{c}_g=(N/K,0)$", ha="center", va="center", fontsize=11)
    ax.set(title="Phase/group right triangle", xlim=(-0.12, 0.69), ylim=(-0.25, 0.40))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.suptitle(r"Upward/rightward phase; downward/rightward energy ($k=1$, $m=1.5$, $N=1$, $t=0$)", fontsize=12)
    output = Path("paper-49-internal-wave.png")
    fig.savefig(output, dpi=150, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
