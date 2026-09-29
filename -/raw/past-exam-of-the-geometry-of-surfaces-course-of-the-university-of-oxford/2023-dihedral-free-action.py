"""Original drilled-torus figure; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Uses only the dependencies in the wiki's root pyproject.toml. Run from the
desired output directory; the PNG and mesh-check JSON are written there.
The mesh is a marching-tetrahedra approximation to a smooth maximum of a
solid-torus defining function and three cylindrical bore defining functions.
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


N = 3
R = 2.6
TUBE_RADIUS = 0.8
BORE_RADIUS = 0.35
SMOOTHNESS = 60.0
AXIS_ANGLES = np.arange(N) * np.pi / N


def field(x, y, z):
    """Negative inside the smoothed solid; positive on every rotation axis."""
    value = (np.hypot(x, y) - R) ** 2 + z * z - TUBE_RADIUS**2
    value = SMOOTHNESS * value
    for theta in AXIS_ANGLES:
        transverse = -x * np.sin(theta) + y * np.cos(theta)
        bore = BORE_RADIUS**2 - transverse**2 - z**2
        value = np.logaddexp(value, SMOOTHNESS * bore)
    return value / SMOOTHNESS


def extract_mesh():
    # A fixed diagonal in every cube makes adjacent tetrahedra conforming.
    nx, ny, nz = 137, 137, 49
    xs = np.linspace(-3.65, 3.65, nx)
    ys = np.linspace(-3.65, 3.65, ny)
    zs = np.linspace(-1.0, 1.0, nz)
    xx, yy, zz = np.meshgrid(xs, ys, zs, indexing="ij")
    xyz = np.column_stack((xx.ravel(), yy.ravel(), zz.ravel()))
    values = field(xx, yy, zz).ravel()
    ii, jj, kk = np.meshgrid(
        np.arange(nx - 1), np.arange(ny - 1), np.arange(nz - 1), indexing="ij"
    )
    bases = ((ii * ny + jj) * nz + kk).ravel()
    offsets = np.array([0, ny * nz, nz, ny * nz + nz,
                        1, ny * nz + 1, nz + 1, ny * nz + nz + 1])
    tetrahedra = [(0, 1, 3, 7), (0, 3, 2, 7), (0, 2, 6, 7),
                  (0, 6, 4, 7), (0, 4, 5, 7), (0, 5, 1, 7)]
    all_triangle_edges = []
    for tet in tetrahedra:
        ids = bases[:, None] + offsets[list(tet)]
        inside = values[ids] < 0
        patterns = inside @ np.array([1, 2, 4, 8])
        for pattern in range(1, 15):
            selected = ids[patterns == pattern]
            if not len(selected):
                continue
            inn = [i for i in range(4) if pattern & (1 << i)]
            out = [i for i in range(4) if not pattern & (1 << i)]
            if len(inn) in (1, 3):
                if len(inn) == 1:
                    local_edges = [(inn[0], j) for j in out]
                else:
                    local_edges = [(out[0], j) for j in inn]
                all_triangle_edges.append(selected[:, local_edges])
            else:
                a, b = inn
                c, d = out
                # Intersections a-c, a-d, b-d, b-c form the quadrilateral.
                for local_edges in [[(a, c), (a, d), (b, d)],
                                    [(a, c), (b, d), (b, c)]]:
                    all_triangle_edges.append(selected[:, local_edges])
    triangle_edges = np.concatenate(all_triangle_edges)
    triangle_edges.sort(axis=2)
    edges, inverse = np.unique(triangle_edges.reshape(-1, 2), axis=0,
                               return_inverse=True)
    weights = values[edges[:, 0]] / (values[edges[:, 0]] - values[edges[:, 1]])
    vertices = (xyz[edges[:, 0]] * (1 - weights[:, None])
                + xyz[edges[:, 1]] * weights[:, None])
    faces = inverse.reshape(-1, 3)
    return vertices, faces


def mesh_checks(vertices, faces):
    mesh_edges = np.concatenate((faces[:, [0, 1]], faces[:, [1, 2]],
                                 faces[:, [2, 0]]))
    mesh_edges.sort(axis=1)
    unique_edges, counts = np.unique(mesh_edges, axis=0, return_counts=True)
    parents = np.arange(len(vertices))

    def root(a):
        while parents[a] != a:
            parents[a] = parents[parents[a]]
            a = parents[a]
        return a

    for a, b in unique_edges:
        parents[root(a)] = root(b)
    components = len({root(i) for i in range(len(vertices))})
    chi = len(vertices) - len(unique_edges) + len(faces)
    # Check invariance analytically at numerical samples, not just on the mesh.
    rng = np.random.default_rng(2023)
    p = rng.uniform(-3.4, 3.4, (1000, 3))
    angle = 2 * np.pi / N
    beta = np.array([[np.cos(angle), np.sin(angle), 0],
                     [-np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    alpha = np.diag([1, -1, -1])
    errors = []
    for matrix in (alpha, beta):
        q = p @ matrix.T
        errors.append(float(np.max(np.abs(field(*p.T) - field(*q.T)))))
    t = np.linspace(-4, 4, 2001)
    axis_minima = [float(np.min(field(0 * t, 0 * t, t)))]
    for angle in AXIS_ANGLES:
        axis_minima.append(float(np.min(field(t * np.cos(angle),
                                              t * np.sin(angle), 0 * t))))
    checks = {"vertices": len(vertices), "edges": len(unique_edges),
              "faces": len(faces), "euler_characteristic": chi,
              "genus": (2 - chi) // 2, "components": components,
              "all_edges_have_two_incident_faces": bool(np.all(counts == 2)),
              "generator_invariance_errors": errors,
              "minimum_field_on_rotation_axes": axis_minima}
    assert components == 1 and chi == -12 and np.all(counts == 2), checks
    assert max(errors) < 1e-12 and min(axis_minima) > 0, checks
    return checks


def make_figure(vertices, faces):
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10.4, 5.1), layout="constrained")
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    triangles = vertices[faces]
    normals = np.cross(triangles[:, 1] - triangles[:, 0],
                       triangles[:, 2] - triangles[:, 0])
    normals /= np.linalg.norm(normals, axis=1)[:, None]
    light = np.array([0.3, -0.5, 0.8])
    light /= np.linalg.norm(light)
    shade = 0.42 + 0.58 * np.abs(normals @ light)
    colors = np.column_stack((0.28 * shade, 0.68 * shade, 0.85 * shade,
                              np.ones(len(shade))))
    mesh = Poly3DCollection(triangles, facecolors=colors, edgecolors="none",
                            linewidth=0, rasterized=True)
    ax.add_collection3d(mesh)
    colors_axes = ["#b4462e", "#7a4bab", "#277341"]
    for theta, color in zip(AXIS_ANGLES, colors_axes):
        t = np.linspace(-3.7, 3.7, 2)
        ax.plot(t * np.cos(theta), t * np.sin(theta), 0 * t,
                color=color, linestyle="--", linewidth=1.0)
    ax.plot([0, 0], [0, 0], [-1.6, 1.8], color="#333333",
            linestyle="--", linewidth=1.2)
    ax.text(0, 0, 1.92, "vertical rotation axis", ha="center", fontsize=9)
    ax.set(xlim=(-3.7, 3.7), ylim=(-3.7, 3.7), zlim=(-1.6, 2.0))
    ax.set_box_aspect((1, 1, 0.5))
    ax.view_init(elev=27, azim=-76)
    ax.set_axis_off()
    ax.set_title("Smooth drilled torus, n = 3\ngenus = 1 + 6 = 7", pad=1)

    plan = fig.add_subplot(1, 2, 2)
    q = np.linspace(-3.7, 3.7, 701)
    xx, yy = np.meshgrid(q, q)
    ff = field(xx, yy, 0 * xx)
    plan.contourf(xx, yy, ff, levels=[-100, 0], colors=["#55a1be"])
    plan.contour(xx, yy, ff, levels=[0], colors=["#1d556b"], linewidths=0.8)
    for j, (theta, color) in enumerate(zip(AXIS_ANGLES, colors_axes)):
        plan.plot(q * np.cos(theta), q * np.sin(theta), linestyle="--",
                  color=color, linewidth=1.1, label=f"half-turn axis {j+1}")
    plan.plot(0, 0, "o", color="#333333", markersize=4)
    plan.text(0.12, 0.14, "vertical axis", fontsize=9)
    plan.annotate("radial bore", xy=(R, 0), xytext=(3.65, -1.25),
                  arrowprops={"arrowstyle": "->", "color": "#333333"},
                  ha="right", fontsize=9)
    plan.set_aspect("equal")
    plan.set(xlim=(-3.85, 3.85), ylim=(-3.85, 3.85))
    plan.axis("off")
    plan.set_title("Horizontal section at z = 0\nall rotation axes avoid the surface")
    plan.legend(loc="lower center", fontsize=8, frameon=False,
                 bbox_to_anchor=(0.5, -0.04), ncol=1)
    fig.savefig("2023-dihedral-free-action.png", dpi=145, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    vertices, faces = extract_mesh()
    checks = mesh_checks(vertices, faces)
    make_figure(vertices, faces)
    Path("2023-dihedral-free-action-checks.json").write_text(
        json.dumps(checks, indent=2) + "\n"
    )
    print(json.dumps(checks))
