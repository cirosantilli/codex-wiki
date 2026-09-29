"""Generate thin-lens-virtual-image.png in CWD; tested with Python 3.14.4.

Uses the repository's numpy and matplotlib dependencies. Exact coordinates in
an ideal paraxial thin-lens model; vertical scale enlarged for visibility.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def direction_arrow(ax, x0, x1, height, color):
    """Add a rightward arrow on a physically transmitted ray segment."""
    assert x1 > x0
    ax.annotate("", xy=(x1, height(x1)), xytext=(x0, height(x0)),
                arrowprops={"arrowstyle": "->", "lw": 2.0, "color": color},
                zorder=6)


def main():
    focal, distance, object_height = 1.0, 0.5, 0.1
    image = focal * distance / (distance - focal)
    magnification = -image / distance
    image_height = magnification * object_height
    parallel = lambda x: object_height * (1 - x / focal)
    centre = lambda x: -object_height * x / distance
    assert np.allclose([image, magnification, image_height], [-1.0, 2.0, 0.2],
                       atol=1e-14, rtol=0)
    assert np.isclose(parallel(focal), 0)
    assert np.isclose(centre(-distance), object_height)
    assert np.isclose(parallel(image), image_height)
    assert np.isclose(centre(image), image_height)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=110)
    fig.subplots_adjust(left=.10, right=.98, top=.80, bottom=.32)
    ax.axhline(0, color="0.4", lw=1.1)
    ax.add_patch(Ellipse((0, 0), .075, .54, facecolor="#e5f1fa",
                         edgecolor="#6d90a8", lw=1.4, zorder=1))
    ax.axvline(0, color="#6d90a8", lw=.8, linestyle=":")
    blue, orange = "#1768ac", "#cb6418"
    incoming = np.linspace(-distance, 0, 100)
    outgoing = np.linspace(0, 1.25, 200)
    ax.plot(incoming, np.full_like(incoming, object_height), color=blue, lw=2)
    ax.plot(incoming, centre(incoming), color=orange, lw=2)
    ax.plot(outgoing, parallel(outgoing), color=blue, lw=2,
            label="Parallel in; through rear focus out")
    ax.plot(outgoing, centre(outgoing), color=orange, lw=2,
            label="Through centre; undeviated")
    direction_arrow(ax, -.72 * distance, -.46 * distance,
                    lambda x: object_height, blue)
    direction_arrow(ax, -.72 * distance, -.46 * distance, centre, orange)
    direction_arrow(ax, .55, .78, parallel, blue)
    direction_arrow(ax, .55, .78, centre, orange)
    if image < 0:
        backwards = np.linspace(image, 0, 100)
        ax.plot(backwards, parallel(backwards), "--", color=blue, lw=1.5, zorder=1.5,
                label="Dashed: backward extensions only")
        ax.plot(backwards, centre(backwards), "--", color=orange, lw=1.5, zorder=1.5)
    ax.annotate("", xy=(-distance, object_height), xytext=(-distance, 0),
                arrowprops={"arrowstyle": "-|>", "color": "#237a48", "lw": 2.6},
                zorder=7)
    ax.annotate("", xy=(image, image_height), xytext=(image, 0),
                arrowprops={"arrowstyle": "-|>", "color": "#943d7c", "lw": 2.6},
                zorder=7)
    ax.scatter([-distance, image], [object_height, image_height],
               color=["#237a48", "#943d7c"], s=25, zorder=8)
    ax.scatter([-focal, focal], [0, 0], color="0.25", s=25, zorder=8)
    ax.annotate("Front focus (−1, 0)", xy=(-focal, 0), xytext=(0, -23),
                textcoords="offset points", ha="center", fontsize=10)
    ax.annotate("Rear focus (1, 0)", xy=(focal, 0), xytext=(0, -23),
                textcoords="offset points", ha="center", fontsize=10)
    ax.annotate("Object: (−0.5, 0.1)", xy=(-distance, object_height),
                xytext=(0, 18), textcoords="offset points",
                ha="center", color="#237a48", fontsize=11)
    ax.annotate("Virtual image: (−1, 0.2)", xy=(image, image_height),
                xytext=(-30, 18), textcoords="offset points",
                ha="center", color="#943d7c", fontsize=11)
    ax.text(0, .29, "Ideal lens at x = 0", ha="center", fontsize=10,
            color="#456b84")
    ax.set(xlim=(-1.4, 1.4), ylim=(-.30, .35), xticks=[-1, -.5, 0, .5, 1],
           xlabel="Position x (m)", ylabel="Height y (m)")
    ax.grid(alpha=.15)
    fig.suptitle("Virtual image: only backward extensions meet", fontsize=16, y=.97)
    fig.text(.5, .875, r"$f=1$ m, $u=0.5$ m, $v=-1$ m, $m=2$;  $h_o=0.1$ m, $h_i=0.2$ m", ha="center", fontsize=12)
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(.5, .08),
               ncol=1, frameon=False, fontsize=10)
    fig.text(.5, .025, "Ideal paraxial model in air. Vertical scale enlarged; arrows on solid rays show travel to the right.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
