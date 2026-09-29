"""Illustrate a field sampled along a moving curve; output a PNG to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    reference = np.pi / 4
    point = np.array([np.cos(reference), np.sin(reference)])
    velocity = np.array([-np.sin(reference), np.cos(reference)])
    gradient = np.array([2 * point[0], 4 * point[1]])
    value = point[0]**2 + 2 * point[1]**2
    rate = gradient @ velocity
    assert np.isclose(value, 1.5)
    assert np.isclose(rate, 1)
    t = np.linspace(0, np.pi / 2, 500)
    assert np.allclose(np.cos(t)**2 + 2 * np.sin(t)**2, 1 + np.sin(t)**2)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, (spatial, sampled) = plt.subplots(1, 2, figsize=(11, 5.9), dpi=120, facecolor="white")
    grid = np.linspace(-1.35, 1.45, 400)
    x, y = np.meshgrid(grid, grid)
    contours = spatial.contour(x, y, x*x + 2*y*y, levels=[.5, 1, 1.5, 2, 3, 4],
                               colors="#aebac2", linewidths=1.2)
    spatial.clabel(contours, fmt="%g", fontsize=10)
    circle = np.linspace(0, 2 * np.pi, 600)
    spatial.plot(np.cos(circle), np.sin(circle), color="#206a9d", lw=2.8, label="Unit-circle path")
    spatial.scatter(*point, color="#202e38", s=55, zorder=5)
    for direction, scale, color in [(velocity, .58, "#b83242"), (gradient, .20, "#318468")]:
        spatial.annotate("", xy=point + scale * direction, xytext=point,
                         arrowprops={"arrowstyle": "->", "color": color, "lw": 2.6})
    spatial.text(.03, .95, r"$F(x,y)=x^2+2y^2$", transform=spatial.transAxes, va="top",
                 bbox={"facecolor": "white", "edgecolor": "none"})
    spatial.annotate("Velocity", xy=point + .58 * velocity, xytext=(-1.23, .75), color="#b83242",
                     arrowprops={"arrowstyle": "-", "color": "#b83242"}, fontsize=11)
    spatial.text(-1.18, -1.24, "Green arrow: gradient × 0.20", color="#318468", fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    spatial.text(.78, .46, r"$t=\pi/4$", fontsize=11)
    spatial.set(aspect="equal", xlim=(-1.35, 1.45), ylim=(-1.35, 1.45), xlabel="x", ylabel="y",
                title="Local field geometry and motion")
    sampled.plot(t, 1 + np.sin(t)**2, color="#206a9d", lw=3,
                 label=r"Sampled field: $1+\sin^2t$")
    tangent_domain = np.linspace(.15, 1.42, 250)
    sampled.plot(tangent_domain, value + rate * (tangent_domain - reference),
                 color="#bc7323", lw=2, linestyle="--", label="Tangent at π/4")
    sampled.scatter([reference], [value], color="#202e38", s=60, zorder=5)
    sampled.annotate("Value = 1.5\nRate = 1", xy=(reference, value), xytext=(.15, 1.86),
                     arrowprops={"arrowstyle": "->", "color": "#202e38"}, fontsize=12)
    sampled.set(xlim=(0, np.pi / 2), ylim=(.95, 2.05), xlabel="Path parameter t (radians)",
                ylabel="Field value along the path", title="Observed change along the curve")
    sampled.set_xticks([0, np.pi/4, np.pi/2], ["0", "π/4", "π/2"])
    for ax in (spatial, sampled):
        ax.grid(color="#e5e9eb")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Rate along a curve = gradient · velocity", fontsize=16, y=.975)
    fig.text(.5, .10, r"At $t=\pi/4$: $(\sqrt{2},2\sqrt{2})\cdot(-1/\sqrt{2},1/\sqrt{2})=1$",
             ha="center", fontsize=14)
    fig.legend(*sampled.get_legend_handles_labels(), loc="lower center", ncol=2,
               frameon=False, bbox_to_anchor=(.5, .018), fontsize=11)
    fig.subplots_adjust(left=.07, right=.98, top=.84, bottom=.23, wspace=.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
