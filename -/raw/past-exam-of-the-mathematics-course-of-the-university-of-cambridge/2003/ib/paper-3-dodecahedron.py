"""Draw a regular dodecahedron and its (2,3,5) spherical reflection chamber.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes paper-3-dodecahedron.png to the caller's current working directory.
The caller may supply MPLCONFIGDIR; this script leaves it unchanged.
"""
import itertools

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def main():
    phi = (1 + np.sqrt(5.0)) / 2
    vertices = list(itertools.product([-1.0, 1.0], repeat=3))
    normals = []
    for u, v in itertools.product([-1.0, 1.0], repeat=2):
        a = (0, u / phi, v * phi)
        vertices.extend([a, (a[1], a[2], 0), (a[2], 0, a[1])])
        n = (0, u * phi, v)
        normals.extend([n, (n[1], n[2], 0), (n[2], 0, n[1])])
    vertices = np.array(vertices)
    polygons = []
    for normal in normals:
        normal = np.array(normal)
        face = vertices[np.isclose(vertices @ normal, phi ** 2)]
        center = face.mean(axis=0)
        e1 = face[0] - center
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(normal / np.linalg.norm(normal), e1)
        angles = np.arctan2((face - center) @ e2, (face - center) @ e1)
        polygons.append(face[np.argsort(angles)])
    normal = np.array([0., phi, 1.])
    F = normal * phi ** 2 / np.dot(normal, normal)
    M = np.array([0., phi, 0.])
    V = np.array([1 / phi, phi, 0.])
    chamber = np.array([F, M, V])
    fig = plt.figure(figsize=(10, 5), facecolor="white", layout="constrained")
    ax = fig.add_subplot(121, projection="3d", computed_zorder=False)
    colors = ["#ffdf8d" if np.allclose(n, normal) else "#d9e7ed" for n in normals]
    ax.add_collection3d(Poly3DCollection(polygons, facecolors=colors, edgecolors="#405367", linewidths=.65, alpha=1, zorder=1))
    ax.add_collection3d(Poly3DCollection([chamber], facecolors="#d55339", edgecolors="#a63625", linewidths=2, alpha=1, zorder=2))
    ax.scatter(*chamber.T, color="#94271d", s=25, depthshade=False, zorder=3)
    for point, name, offset in zip(chamber, ["F", "M", "V"], [[0, 0, .09], [-.24, 0, -.10], [.22, 0, -.10]]):
        ax.text(*(point + offset), name, fontsize=12, weight="bold", zorder=4)
    ax.set_title("Regular dodecahedron\nFace center F, edge midpoint M, vertex V", fontsize=11)
    ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.8, 1.8); ax.set_zlim(-1.8, 1.8)
    ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=22, azim=55); ax.set_axis_off()
    bx = fig.add_subplot(122, projection="3d")
    unit = chamber / np.linalg.norm(chamber, axis=1)[:, None]
    for a, b in [(0, 1), (1, 2), (2, 0)]:
        angle = np.arccos(np.clip(np.dot(unit[a], unit[b]), -1, 1))
        s = np.linspace(0, 1, 100)
        arc = (np.sin((1 - s) * angle)[:, None] * unit[a] + np.sin(s * angle)[:, None] * unit[b]) / np.sin(angle)
        bx.plot(*arc.T, color="#b63624", linewidth=2.6)
    # A small patch of the sphere contains the entire chamber.
    longitude = np.linspace(0.48, 1.7, 20)
    latitude = np.linspace(-.1, .65, 16)
    lon, lat = np.meshgrid(longitude, latitude)
    bx.plot_wireframe(np.cos(lat)*np.cos(lon), np.cos(lat)*np.sin(lon), np.sin(lat), color="#bdcbd3", linewidth=.45, alpha=.65)
    bx.scatter(*unit.T, color="#94271d", s=30, depthshade=False)
    for point, name in zip(unit, [r"F: $\pi/5$", r"M: $\pi/2$", r"V: $\pi/3$"]):
        bx.text(*(point * 1.035), name, fontsize=11, weight="bold")
    bx.set_xlim(-.15, .65); bx.set_ylim(.6, 1.1); bx.set_zlim(-.08, .65)
    bx.set_box_aspect((.8, .5, .73)); bx.view_init(elev=22, azim=55); bx.set_axis_off()
    bx.set_title("Radial projection to the unit sphere\nReflection chamber of angles (π/2, π/3, π/5)", fontsize=11)
    fig.savefig("paper-3-dodecahedron.png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
