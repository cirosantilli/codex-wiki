"""Illustrate signed curvature; write signed-curvature-orientation.png to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def circle_curvature(radius, phi, phi_prime, phi_second):
    """Compute the determinant formula after an arbitrary regular reparametrization."""
    radial = np.array([np.cos(phi), np.sin(phi)])
    angular = np.array([-np.sin(phi), np.cos(phi)])
    velocity = radius * phi_prime * angular
    acceleration = radius * (phi_second * angular - phi_prime ** 2 * radial)
    determinant = velocity[0] * acceleration[1] - velocity[1] * acceleration[0]
    return determinant / np.linalg.norm(velocity, axis=0) ** 3


def main():
    u = np.linspace(-2.0, 2.0, 41)
    errors = []
    for radius in (1.0, 2.0):
        for direction in (1.0, -1.0):
            # Includes constant and nonconstant traversal speeds, with phi'' != 0.
            for phi, phi_prime, phi_second in [
                (direction * u, direction * np.ones_like(u), np.zeros_like(u)),
                (direction * 3 * u, direction * 3 * np.ones_like(u), np.zeros_like(u)),
                (direction * (u + 0.2 * np.sin(u)),
                 direction * (1 + 0.2 * np.cos(u)), direction * (-0.2 * np.sin(u)))
            ]:
                actual = circle_curvature(radius, phi, phi_prime, phi_second)
                errors.append(np.max(abs(actual - direction / radius)))
                np.testing.assert_allclose(actual, direction / radius, atol=1e-14, rtol=0)
    print(f"Circles: R=1 gives signed curvature +/-1; R=2 gives +/-0.5; "
          f"three reparametrizations in both directions; max error={max(errors):.3g}")

    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.25, top=0.74, wspace=0.25)
    curve_color, tangent_color, normal_color = "#5d3b83", "#1d68a6", "#23845b"
    angle = np.linspace(0, 2 * np.pi, 361)
    for ax, direction in zip(axes, (1, -1)):
        ax.plot(np.cos(angle), np.sin(angle), color=curve_color, lw=2.6)
        for theta in (np.pi / 6, 5 * np.pi / 6, 3 * np.pi / 2):
            point = np.array([np.cos(theta), np.sin(theta)])
            tangent = direction * np.array([-np.sin(theta), np.cos(theta)])
            left_normal = np.array([-tangent[1], tangent[0]])
            # Both traversals give the same inward curvature vector k N_L.
            np.testing.assert_allclose(direction * left_normal, -point, atol=1e-14)
            ax.plot(*point, "o", color=curve_color, ms=5, zorder=5)
            for vector, color in [(tangent, tangent_color), (left_normal, normal_color)]:
                ax.annotate("", xy=point + 0.43 * vector, xytext=point,
                            arrowprops={"arrowstyle": "-|>", "color": color,
                                        "lw": 2.3, "mutation_scale": 16})
        ax.plot(0, 0, "+", color="#777777", ms=9)
        ax.text(0, 0.18, r"$R=1$", ha="center", color="#555555")
        ax.set(xlim=(-1.65, 1.65), ylim=(-1.6, 1.6))
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.set_axis_off()
        if direction == 1:
            ax.set_title("Anticlockwise: left normal points inward\n" +
                         r"$r(t)=(\cos t,\sin t)$", fontsize=12, pad=12)
            ax.text(0.5, -0.11, r"$k=+1,\quad\kappa=1$", transform=ax.transAxes,
                    ha="center", fontsize=15)
        else:
            ax.set_title("Clockwise: left normal points outward\n" +
                         r"$q(t)=(\cos t,-\sin t)$", fontsize=12, pad=12)
            ax.text(0.5, -0.11, r"$k=-1,\quad\kappa=1$", transform=ax.transAxes,
                    ha="center", fontsize=15)
    fig.suptitle("Same circle, opposite signed curvature", fontsize=17, y=0.97)
    fig.text(0.5, 0.88, r"$N_L$ is the tangent rotated anticlockwise by $90^{\circ}$ in both panels.",
             ha="center", fontsize=12)
    fig.legend(handles=[Line2D([], [], color=tangent_color, lw=2.3, label="Unit tangent T (traversal)"),
                        Line2D([], [], color=normal_color, lw=2.3, label=r"Left unit normal $N_L$")],
               loc="lower center", bbox_to_anchor=(0.5, 0.075), ncol=2, frameon=False,
               fontsize=11)
    fig.text(0.5, 0.035, r"The curvature vector $dT/ds=kN_L$ points inward in both panels. Reversing traversal preserves $\kappa$.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
