"""Draw an exact unit sphere, affine tangent plane, and displacement plane.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All geometry is analytical; no measurements or external images are used.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, orange, red, green = "#2468a0", "#b76b14", "#b63846", "#278353"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(11, 5.6), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.96, top=0.81, bottom=0.32, wspace=0.24)
    fig.suptitle("A tangent plane consists of points; a tangent space consists of velocities",
                 fontsize=15, y=0.98)
    fig.text(0.5, 0.90, r"Unit sphere at $p=(0,0,1)$: $p+T_pS^2$ is $z=1$; $T_pS^2$ is $v_z=0$",
             ha="center", fontsize=13)
    ax = fig.add_subplot(121, projection="3d", computed_zorder=False)
    theta, phi = np.meshgrid(np.linspace(0, np.pi, 25), np.linspace(0, 2*np.pi, 37))
    sx, sy, sz = np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)
    ax.plot_wireframe(sx, sy, sz, color=blue, linewidth=0.6, alpha=0.45, zorder=1)
    u, v = np.meshgrid(np.linspace(-1.1, 1.1, 7), np.linspace(-1.1, 1.1, 7))
    ax.plot_surface(u, v, np.ones_like(u), color=orange, alpha=0.16, shade=False, zorder=2)
    ax.plot_wireframe(u, v, np.ones_like(u), color=orange, alpha=0.35, linewidth=0.5, zorder=2)
    t = np.linspace(-1.2, 1.2, 160)
    ax.plot(np.sin(t), np.zeros_like(t), np.cos(t), color=red, lw=2.4, zorder=3)
    ax.plot(np.zeros_like(t), np.sin(t), np.cos(t), color=green, lw=2.4, zorder=3)
    p = np.array([0., 0., 1.])
    ax.scatter(*p, s=40, color="black", depthshade=False, zorder=5)
    ax.text(0.02, -0.08, 1.14, "$p$", fontsize=13, zorder=6)
    ax.quiver(*p, 0.75, 0, 0, color=red, arrow_length_ratio=0.15, lw=2.2, zorder=5)
    ax.quiver(*p, 0, 0.75, 0, color=green, arrow_length_ratio=0.15, lw=2.2, zorder=5)
    ax.text(0.87, 0, 1.08, "$e_1$", color=red, zorder=6)
    ax.text(0, 0.87, 1.08, "$e_2$", color=green, zorder=6)
    ax.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), zlim=(-1.05, 1.35))
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=23, azim=-55)
    ax.set_axis_off()
    ax.set_title("Two sphere curves supply two independent velocities", fontsize=11, pad=5)

    section = fig.add_subplot(122)
    angle = np.linspace(0, 2*np.pi, 361)
    section.plot(np.cos(angle), np.sin(angle), color=blue, lw=2, label="sphere section (y = 0)")
    section.axhline(1, color=orange, lw=2.4)
    section.axhline(0, color="#765195", lw=2, ls="--")
    section.scatter([0, 0], [1, 0], c=["black", "#765195"], s=35, zorder=5)
    section.annotate("$p$", (0, 1), xytext=(-0.18, 1.12), fontsize=13)
    section.annotate("$O$", (0, 0), xytext=(-0.18, -0.21), color="#765195")
    section.annotate("", (0.75, 1), (0, 1), arrowprops={"arrowstyle": "->", "color": red, "lw": 2.5})
    section.annotate("", (0.75, 0), (0, 0), arrowprops={"arrowstyle": "->", "color": "#765195", "lw": 2.5})
    section.text(-1.25, 1.32, r"Affine tangent plane: $z=1$", color=orange)
    section.text(-1.25, -0.43, r"Displacement plane: $v_z=0$", color="#765195")
    section.text(0.86, 0.71, "same direction,\ndifferent origins", fontsize=10, color="#444444")
    section.set(xlim=(-1.35, 1.7), ylim=(-1.15, 1.5), xlabel="x", ylabel="z")
    section.set_aspect("equal")
    section.set_title("Vertical cross-section: translating by p", fontsize=11)
    section.set_xticks([-1, 0, 1])
    section.set_yticks([-1, 0, 1])
    section.legend(loc="lower right", fontsize=9, frameon=False)
    fig.text(0.27, 0.135, r"$\gamma_1(t)=(\sin t,0,\cos t)$"+"\n"+r"$\gamma_2(t)=(0,\sin t,\cos t)$",
             ha="center", va="center", color="#333333")
    fig.text(0.76, 0.135, "Arrows show displacements. Their endpoints\nneed not remain on the sphere.", ha="center", va="center")
    fig.text(0.5, 0.025, "Analytical geometry illustration; the colored plane is a finite piece of an infinite plane.",
             ha="center", fontsize=10, color="#555555")
    assert np.allclose(sx*sx + sy*sy + sz*sz, 1)
    assert np.allclose(np.cross([1, 0, 0], [0, 1, 0]), p)
    assert np.allclose(np.sin(t)**2 + np.cos(t)**2, 1)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
