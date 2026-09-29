"""Original Q20 cap orientations; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a, b, c = 1.7, 1.2, 1
    radial, phi = np.meshgrid(np.linspace(0, 1, 38), np.linspace(0, 2*np.pi, 90))
    fig = plt.figure(figsize=(9.6, 4.3), layout="constrained", facecolor="white")
    for index, power in enumerate([2, 8], 1):
        ax = fig.add_subplot(1, 2, index, projection="3d")
        ax.set_facecolor("white")
        x = a*radial*np.cos(phi)
        y = b*radial*np.sin(phi)
        z = c*np.maximum(1-radial**2, 0)**(1/power)
        ax.plot_surface(x, y, z, color="#70a7c5", alpha=0.35, edgecolor="#c0d0d8", linewidth=0.18, rcount=45, ccount=30)
        angle = np.linspace(0, 2*np.pi, 400)
        ax.plot(a*np.cos(angle), b*np.sin(angle), np.zeros_like(angle), color="#8d3c68", linewidth=2.6)
        ph = -1.0
        tangent = np.array([-a*np.sin(ph), b*np.cos(ph), 0])
        tangent /= np.linalg.norm(tangent)
        ax.quiver(a*np.cos(ph), b*np.sin(ph), 0, *tangent, color="#8d3c68", length=0.48, arrow_length_ratio=0.35, linewidth=2)
        rr, ph = 0.55, 0.85
        point = np.array([a*rr*np.cos(ph), b*rr*np.sin(ph), c*(1-rr**2)**(1/power)])
        normal = np.array([2*point[0]/a**2, 2*point[1]/b**2, power*point[2]**(power-1)/c**power])
        normal /= np.linalg.norm(normal)
        ax.quiver(*point, *normal, length=0.52, color="#ad412f", linewidth=2, arrow_length_ratio=0.28)
        ax.text(*(point+0.58*normal), "$n$", color="#ad412f", fontsize=12)
        ax.text(-a-0.04, 0, 0, "$C$", color="#8d3c68", fontsize=13)
        ax.text2D(0.08, 0.03, "Boundary is counterclockwise from +z", transform=ax.transAxes, fontsize=9)
        ax.set(xlim=(-2, 2), ylim=(-1.5, 1.5), zlim=(0, 1.5), title="Ellipsoidal cap" if power == 2 else "Cap with an eighth-power height term")
        ax.set_box_aspect((4, 3, 1.5))
        ax.view_init(elev=25, azim=-65)
        ax.set_axis_off()
    fig.savefig(Path("paper-1-stokes-orientation.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
