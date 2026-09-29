"""Draw local null-normal beam geometry; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python ../penrose-trapped-null-congruences.py
The drawing is schematic; the metric/sign checks below are independent of it.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def check_geometry():
    """Contract normals using the (v,r) metric, then differentiate sphere area."""
    rows = []
    for radius in (3.0, 2.0, 1.5):
        f = 1.0 - 2.0 / radius  # M=1
        metric = np.array([[-f, 1.0], [1.0, 0.0]])
        outgoing = np.array([1.0, f / 2.0])
        ingoing = np.array([0.0, -1.0])
        assert abs(outgoing @ metric @ outgoing) < 1e-14
        assert abs(ingoing @ metric @ ingoing) < 1e-14
        assert abs(outgoing @ metric @ ingoing + 1.0) < 1e-14
        expansions = []
        for normal in (outgoing, ingoing):
            h = 1e-5
            # Independent centered difference of log(area), not expansion formula.
            area_plus = 4.0 * np.pi * (radius + h * normal[1]) ** 2
            area_minus = 4.0 * np.pi * (radius - h * normal[1]) ** 2
            numeric = (np.log(area_plus) - np.log(area_minus)) / (2.0 * h)
            exact = 2.0 * normal[1] / radius
            assert abs(numeric - exact) < 2e-10
            for scale in (0.3, 2.0, 7.0):
                assert np.sign(scale * exact) == np.sign(exact)
            expansions.append(exact)
        rows.append({"r_over_M": radius, "theta_plus_times_M": expansions[0],
                     "theta_minus_times_M": expansions[1]})
    assert rows[0]["theta_plus_times_M"] > 0
    assert rows[1]["theta_plus_times_M"] == 0
    assert all(rows[2][key] < 0 for key in
               ("theta_plus_times_M", "theta_minus_times_M"))
    return {"null_normals_and_cross_normalization": "passed",
            "area_finite_difference": "passed", "positive_rescaling_signs": "passed",
            "spheres": rows}


def draw():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.7), dpi=120)
    colors = ("#1766a5", "#be4b16")
    u = np.linspace(0, 1, 100)
    for ax, trapped in zip(axes, (False, True)):
        widths = (1 - 0.30 * u if trapped else 1 + 0.45 * u,
                  1 - 0.60 * u)
        for width, color in zip(widths, colors):
            for sign in (-1, 1):
                x = sign * width
                ax.plot(x, 0.45 + 2.1 * u, color=color, lw=2.3)
                j, k = 52, 65
                ax.annotate("", (x[k], 0.45 + 2.1*u[k]),
                            (x[j], 0.45 + 2.1*u[j]),
                            arrowprops={"arrowstyle": "->", "color": color, "lw": 2.3})
            ax.add_patch(Ellipse((0, 2.55), 2*width[-1], 0.23,
                                 fill=False, edgecolor=color, lw=2.3))
        ax.add_patch(Ellipse((0, 0.45), 2, 0.26, facecolor="#eeeeee",
                             edgecolor="#333333", zorder=5))
        ax.text(0, 0.10, "initial closed surface S", ha="center")
        ax.text(0, 3.22, "Both future beams shrink" if trapped else
                "One future beam grows", ha="center", weight="bold")
        ax.text(0, 2.92, r"$\theta_+<0,\quad\theta_-<0$" if trapped else
                r"$\theta_+>0,\quad\theta_-<0$", ha="center", fontsize=15)
        ax.text(0, -0.25, "future trapped" if trapped else "ordinary exterior sphere",
                ha="center", weight="bold")
        ax.set(xlim=(-1.8, 1.8), ylim=(-0.40, 3.5))
        ax.axis("off")
    axes[0].annotate("future", xy=(-1.70, 2.4), xytext=(-1.70, 1.4),
                     ha="center", rotation=90,
                     arrowprops={"arrowstyle": "->", "color": "#333333"})
    fig.suptitle("Trapping concerns transverse area of both null families", fontsize=17)
    fig.text(0.5, 0.13, "Blue: outgoing null normals     Orange: ingoing null normals",
             ha="center", fontsize=12)
    fig.text(0.5, 0.065, "Schematic beam widths, not spacetime coordinates. Ellipses represent 2D sections.\n"
             "A shrinking outgoing beam can still follow a future-directed light ray.",
             ha="center", fontsize=11)
    fig.subplots_adjust(top=0.88, bottom=0.22, wspace=0.20, left=0.05, right=0.98)
    path = Path(__file__).with_suffix(".png").name
    fig.savefig(path, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    print(json.dumps(check_geometry(), indent=2))
    draw()
