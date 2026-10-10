"""Compare Jacobian area scaling and orientation, tested on Python 3.14.4.

Run from the desired output directory; uses the root pyproject dependencies.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def signed_area(points):
    following = np.roll(points, -1, axis=0)
    return .5 * np.sum(points[:, 0] * following[:, 1]
                       - points[:, 1] * following[:, 0])


def main():
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
    maps = [np.eye(2), np.array([[2, 1], [0, 1]]),
            np.array([[2, 1], [0, -1]])]
    colors = ["#3b8963", "#277da8", "#b37028"]
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.4), dpi=130,
                             constrained_layout=True, facecolor="white")
    titles = ["Original unit square", r"$T(u,v)=(2u+v,v)$",
              r"$\widetilde T(u,v)=(2u+v,-v)$"]
    for ax, matrix, color, title in zip(axes, maps, colors, titles):
        points = square @ matrix.T
        determinant = np.linalg.det(matrix)
        area = signed_area(points)
        assert np.isclose(area, determinant)
        ax.set_facecolor("white")
        ax.add_patch(Polygon(points, facecolor=color, alpha=.18,
                             edgecolor=color, linewidth=2))
        for value in np.linspace(0, 1, 5):
            for line in (np.array([[value, 0], [value, 1]]),
                         np.array([[0, value], [1, value]])):
                image = line @ matrix.T
                ax.plot(image[:, 0], image[:, 1], color=color, alpha=.55, lw=1)
        # Follow the same ordered vertices: reflection reverses the arrows.
        for start, end in zip(points, np.roll(points, -1, axis=0)):
            ax.annotate("", xy=start + .66 * (end - start),
                        xytext=start + .35 * (end - start),
                        arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        ax.scatter(points[:, 0], points[:, 1], color=color, s=18, zorder=3)
        ax.set(xlim=(-.3, 3.3), ylim=(-1.9, 1.4), title=title,
               xlabel="u" if ax is axes[0] else "x",
               ylabel="v" if ax is axes[0] else "y")
        ax.set_aspect("equal", adjustable="box")
        ax.set_xticks([0, 1, 2, 3])
        ax.set_yticks([-1, 0, 1])
        ax.grid(alpha=.15)
        ax.text(.5, .07, f"determinant = {determinant:g}\n"
                f"geometric area = {abs(area):g}", ha="center",
                transform=ax.transAxes, color=color, fontsize=11)
    # Check the two worked integrals independently by quadrature.
    nodes, weights = np.polynomial.legendre.leggauss(24)
    nodes, weights = (nodes + 1) / 2, weights / 2
    log_integral = np.sum(weights * 2 * nodes / (1 + nodes**2))
    weighted_area = np.sum(weights[:, None] * weights[None, :]
                           * 2 * (2 * nodes[:, None] + nodes[None, :]))
    assert abs(log_integral - np.log(2)) < 1e-14
    assert abs(weighted_area - 3) < 1e-14
    fig.suptitle("Area uses the absolute determinant; arrows record orientation", fontsize=12)
    fig.savefig(Path.cwd() / "change-of-variables-area.png",
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Signed polygon areas: {[signed_area(square @ m.T) for m in maps]}; "
          f"substitution: {log_integral:.10f}; integral of x over T(S): {weighted_area:.10f}")


if __name__ == "__main__":
    main()
