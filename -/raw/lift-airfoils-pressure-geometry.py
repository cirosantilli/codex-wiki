"""Original prescribed-pressure toy; not measured data or a solved flow.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes only the matching PNG basename to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon
import numpy as np


def rotate(points, alpha):
    """Positive incidence means a raised leading edge for left-to-right flow."""
    matrix = np.array([[np.cos(alpha), np.sin(alpha)],
                       [-np.sin(alpha), np.cos(alpha)]])
    return np.asarray(points) @ matrix.T


def prescribed_force(alpha):
    """Exact panel integration of piecewise linear pressure, in units q*c."""
    # Counterclockwise contour: lower surface first, then upper surface.
    body = np.array([[0., 0.], [.3, -.075], [1., 0.], [.3, .075], [0., 0.]])
    cp = np.array([.4, .28, 0., -.56, -.8])
    steps = np.diff(body, axis=0)
    normals_ds = np.column_stack((steps[:, 1], -steps[:, 0]))
    force = -(normals_ds * ((cp[:-1] + cp[1:]) / 2)[:, None]).sum(axis=0)
    # The leading edge has separate upper/lower limits; its single point has no area.
    return body, rotate(force, alpha)


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    alpha = np.deg2rad(10.)
    body, force = prescribed_force(alpha)
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=100,
                             gridspec_kw={"width_ratios": [1.5, 1.]})
    fig.patch.set_facecolor("white")
    ax, right = axes
    ax.add_patch(Polygon(rotate(body[:-1], alpha), facecolor="#edf1f5",
                         edgecolor="#273947", linewidth=1.7))
    chord = rotate([[0, 0], [1, 0]], alpha)
    ax.plot(*chord.T, color="#77838c", linestyle="--", linewidth=1.2)
    ax.plot([0, .38], [0, 0], color="#77838c", linestyle=":")
    ax.add_patch(Arc((0, 0), .52, .52, theta1=-10, theta2=0, color="#333333"))
    ax.text(.27, -.047, r"$\alpha=10^\circ$", fontsize=10)
    ax.text(-.04, -.11, "leading\nedge", ha="right", fontsize=10)
    ax.text(1., -.16, "trailing\nedge", ha="left", fontsize=10)
    ax.text(.52, -.21, "chord c (dashed)", fontsize=10, rotation=-10)
    for upper, color in [(True, "#1969aa"), (False, "#d66b22")]:
        for x in [.1, .23, .43, .65, .86]:
            thickness = .075 * (x / .3 if x <= .3 else (1-x) / .7)
            slope = .25 if x <= .3 else -.075/.7
            y = thickness if upper else -thickness
            if upper:
                normal = np.array([-slope, 1.])
                cp = -.8 * (1-x)
            else:
                normal = np.array([-slope, -1.])
                cp = .4 * (1-x)
            normal /= np.linalg.norm(normal)
            start = rotate([x, y], alpha)
            displacement = rotate(-.30 * cp * normal, alpha)
            ax.annotate("", xy=start+displacement, xytext=start,
                        arrowprops={"arrowstyle": "->", "color": color, "lw": 1.7})
    ax.text(.18, .26, r"upper: $C_p=-0.8(1-x/c)$", color="#1969aa")
    ax.text(.19, -.38, r"lower: $C_p=+0.4(1-x/c)$", color="#b2581b")
    ax.annotate("", xy=(-.05, .16), xytext=(-.37, .16),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#333333"})
    ax.text(-.35, .21, r"$U_\infty$", fontsize=12)
    ax.set(xlim=(-.40, 1.17), ylim=(-.46, .39), aspect="equal")
    ax.set_title("Surface normals differ from the lift axis", fontsize=12, pad=15)
    ax.axis("off")
    right.annotate("", xy=(.37, 0), xytext=(-.04, 0),
                   arrowprops={"arrowstyle": "->", "color": "#777777"})
    right.annotate("", xy=(0, .74), xytext=(0, -.04),
                   arrowprops={"arrowstyle": "->", "color": "#777777"})
    right.plot([0, force[0], force[0]], [force[1], force[1], 0],
               linestyle="--", color="#999999", linewidth=1)
    for end, color in [(force, "#6a3990"), ([force[0], 0], "#bb6823"),
                       ([0, force[1]], "#1969aa")]:
        right.annotate("", xy=end, xytext=(0, 0),
                       arrowprops={"arrowstyle": "->", "color": color, "lw": 2.1})
    right.text(.27, -.09, r"$\mathbf{e}_D$ (flow)", fontsize=10)
    right.text(-.035, .76, r"$\mathbf{e}_L$", fontsize=12)
    right.text(-.025, .34, "L", color="#1969aa", ha="right")
    right.text(force[0]/2, -.035, "D", color="#bb6823", ha="center")
    right.text(force[0]+.025, force[1]-.015, r"$\mathbf{F}'_p$", color="#6a3990")
    right.text(.12, -.19,
               f"Toy pressure resultant:\nL′/(qc) = {force[1]:.3f}\nD′/(qc) = {force[0]:.3f}",
               fontsize=11, linespacing=1.45, ha="center", va="top")
    right.set(xlim=(-.14, .42), ylim=(-.49, .86), aspect="equal")
    right.set_title("Resolve the resultant in flow axes", fontsize=12, pad=15)
    right.axis("off")
    fig.suptitle("Lift is perpendicular to the far-field relative flow", fontsize=16, y=.96)
    fig.text(.5, .035, "Prescribed toy pressures • no measured data • pressure contribution only",
             ha="center", color="#555555", fontsize=10)
    fig.subplots_adjust(left=.04, right=.96, top=.80, bottom=.16, wspace=.10)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
