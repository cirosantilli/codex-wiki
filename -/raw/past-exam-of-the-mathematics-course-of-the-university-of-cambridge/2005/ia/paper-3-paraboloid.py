"""Original annular-paraboloid sketch. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-3-paraboloid.png to caller CWD and preserves MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    fig = plt.figure(figsize=(6.3, 5.2), facecolor="white")
    ax = fig.add_subplot(projection="3d")
    ax.set_facecolor("white")
    r, angle = np.meshgrid(np.linspace(.5, 1, 31), np.linspace(0, 2*np.pi, 100))
    # A wire sketch exposes the inner hole, both boundary arrows and the normal.
    ax.plot_wireframe(r*np.cos(angle), r*np.sin(angle), r*r, color="#819fb4",
                     rstride=8, cstride=5, linewidth=.65)
    phi = np.linspace(0, 2*np.pi, 400)
    for radius, sign, color in [(1., 1., "#8a3f35"), (.5, -1., "#2c684d")]:
        ax.plot(radius*np.cos(phi), radius*np.sin(phi), np.full(phi.size, radius**2),
                color=color, lw=2.5)
        p = -np.pi/2
        point = np.array([radius*np.cos(p), radius*np.sin(p), radius**2])
        tangent = .25*sign*np.array([-np.sin(p), np.cos(p), 0])
        ax.quiver(*point, *tangent, color=color, arrow_length_ratio=.35, linewidth=2.5)
    point = np.array([.75, 0, .75**2])
    normal = np.array([-1.5, 0., 1.])
    normal = .40*normal/np.linalg.norm(normal)
    ax.quiver(*point, *normal, color="#202020", arrow_length_ratio=.25, linewidth=2)
    ax.text(*(point+1.1*normal), r"$n$", fontsize=13)
    ax.set_title(r"Paraboloid band: $1/2\leq r\leq1$, upward orientation")
    ax.set_xlabel("x");ax.set_ylabel("y");ax.set_zlabel("z")
    ax.set_xlim(-1.1, 1.1);ax.set_ylim(-1.1, 1.1);ax.set_zlim(0, 1.25)
    ax.set_box_aspect([2.2, 2.2, 1.25])
    ax.view_init(elev=25, azim=-55)
    fig.tight_layout()
    fig.text(.10, .09, "Outer boundary r = 1: CCW", color="#8a3f35", fontsize=10)
    fig.text(.10, .055, "Inner boundary r = 1/2: CW (viewed from above)", color="#2c684d", fontsize=10)
    fig.savefig(Path.cwd() / "paper-3-paraboloid.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
