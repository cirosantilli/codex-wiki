"""Original virtual-image and focal-plane ray diagrams; no measured data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the current directory with this script's basename.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def ray(ax, xs, ys, color):
    ax.plot(xs, ys, color=color, lw=2)
    for k in range(len(xs) - 1):
        start = np.array([xs[k], ys[k]])
        step = np.array([xs[k + 1], ys[k + 1]]) - start
        ax.annotate("", xy=start + 0.7 * step, xytext=start + 0.5 * step,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2})


def diagram(ax, u):
    f, h, end = 10.0, 0.3, 12.0
    virtual = u != f
    if virtual:
        v = f * u / (u - f)
        image_h = -v * h / u
        for intercept in np.linspace(-0.6, 0.6, 13):
            slope = (intercept - h) / u - intercept / f
            assert abs(intercept + v * slope - image_h) < 1e-12
        for intercept, slope, color in [(h, -h / f, "#006ca8"),
                                        (0, -h / u, "#c95a16")]:
            ax.plot([v, 0], [intercept + v * slope, intercept],
                    color=color, lw=1.8, ls=(0, (5, 3)))
        ax.annotate("", xy=(v, image_h), xytext=(v, 0),
                    arrowprops={"arrowstyle": "-|>", "color": "#19764b",
                                "lw": 2.5, "linestyle": "--", "mutation_scale": 17})
        ax.scatter([v], [image_h], color="#19764b", s=28, zorder=5)
        ax.text(v, image_h + 0.14, "virtual tip: (−30, +1.20) cm", ha="center",
                fontsize=10, color="#19764b")
        ax.text(-23, 0.22, "dashed = backward extensions", fontsize=10,
                ha="center", bbox={"facecolor": "white", "edgecolor": "none"})
        # The segment represents a receiving opening, not a focusing screen.
        ax.plot([5, 5], [-0.23, 0.18], color="#333333", lw=4)
        ax.annotate("eye receives\nactual rays", xy=(5, -0.02), xytext=(8, 0.75),
                    fontsize=10, ha="center", arrowprops={"arrowstyle": "->"})
        ax.set_title("A   u = 7.5 cm: v = −30 cm, m = +4", loc="left", fontsize=12,
                     pad=12)
    else:
        for intercept in np.linspace(-0.6, 0.6, 13):
            slope = (intercept - h) / u - intercept / f
            assert abs(slope + h / f) < 1e-12
        ax.text(-27, 1.15, "No finite intersection\nNo finite image height", fontsize=11,
                ha="center", color="#19764b")
        ax.text(8, 0.66, "parallel outgoing rays\nslope = −hₒ / f", fontsize=10,
                ha="center")
        ax.set_title("B   u = f = 10 cm: image conventionally at infinity",
                     loc="left", fontsize=12, pad=12)
    ax.axhline(0, color="#777777", lw=1)
    ax.plot([0, 0], [-0.65, 1.1], color="#25475c", lw=3)
    ax.text(0, 1.24, "thin lens", ha="center", fontsize=10)
    ax.scatter([-f, f], [0, 0], color="#222222", s=20, zorder=5)
    ax.text(-f, -0.14, "front F", ha="center", fontsize=9)
    ax.text(f, 0.08, "rear F", ha="center", fontsize=9)
    ray(ax, [-u, 0, end], [h, h, h * (1 - end / f)], "#006ca8")
    ray(ax, [-u, 0, end], [h, 0, -h * end / u], "#c95a16")
    ax.annotate("", xy=(-u, h), xytext=(-u, 0),
                arrowprops={"arrowstyle": "-|>", "color": "#813c98",
                            "lw": 3, "mutation_scale": 17})
    ax.text(-u - 1, 0.84, "object: +0.30 cm", ha="center", fontsize=10,
            color="#813c98")
    ax.set_xlim(-39, 15)
    ax.set_ylim(-0.8, 1.75)
    ax.set_xticks([-30, -20, -10, 0, 10])
    ax.set_yticks([0, 0.6, 1.2])
    ax.set_ylabel("height (cm)", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=9)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.6))
    diagram(axes[0], 7.5)
    diagram(axes[1], 10.0)
    axes[-1].set_xlabel("x (cm); solid light rays travel to the right →", fontsize=10)
    fig.suptitle("Virtual image and the u = f boundary", fontsize=15, y=0.98)
    fig.text(0.5, 0.018,
             "Ideal thin lens, f = 10 cm • same scales in both panels • vertical scale enlarged • no measured data",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.11, top=0.89, hspace=0.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Virtual-image extensions: 13 rays checked; focal-plane parallelism: 13 rays checked.")


if __name__ == "__main__":
    main()
