"""Draw lens-image-formation.png in cwd with checked paraxial ray geometry.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
From _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp python3 ../lens-image-formation.py
All lengths are in metres; the vertical scale is enlarged for readability.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


COLORS = ("#1769aa", "#d26a15", "#23834c")
FOCAL_LENGTH = 0.1


def rays(u, height):
    """Return (height at lens, incident slope, outgoing slope) for three rays."""
    f = FOCAL_LENGTH
    lens_heights = [height, 0.0]
    # At the focus the third principal ray is undefined; use another aperture ray.
    lens_heights.append(-height * f / (u - f) if not np.isclose(u, f) else -height / 2)
    lens_heights = np.asarray(lens_heights)
    incident = (lens_heights - height) / u
    outgoing = incident - lens_heights / f
    assert np.max(np.abs(incident)) < 0.1
    assert np.max(np.abs(outgoing)) < 0.1
    if np.isclose(u, f):
        np.testing.assert_allclose(outgoing, -height / f, atol=1e-14)
    else:
        v = 1 / (1 / f - 1 / u)
        image_height = -v * height / u
        np.testing.assert_allclose(lens_heights + outgoing * v, image_height, atol=1e-14)
        # Check every pair independently rather than inserting a desired image point.
        for a, b in ((0, 1), (0, 2), (1, 2)):
            crossing = (lens_heights[b] - lens_heights[a]) / (outgoing[a] - outgoing[b])
            np.testing.assert_allclose(crossing, v, atol=1e-14)
    return lens_heights, incident, outgoing


def directed_segment(ax, xs, ys, color, dashed=False):
    ax.plot(xs, ys, color=color, lw=2.5, ls="--" if dashed else "-", zorder=3)
    if not dashed:
        start = 0.62
        end = 0.74
        x0, x1 = xs[0], xs[-1]
        y0, y1 = ys[0], ys[-1]
        ax.annotate("", xy=(x0 + end * (x1 - x0), y0 + end * (y1 - y0)),
                    xytext=(x0 + start * (x1 - x0), y0 + start * (y1 - y0)),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2.4}, zorder=4)


def draw_case(ax, u, height, title, xlim, ylim, ticks):
    f = FOCAL_LENGTH
    lens_heights, incident, outgoing = rays(u, height)
    ax.set_facecolor("white")
    ax.axhline(0, color="#66717c", lw=1.2, zorder=1)
    ax.annotate("", xy=(0, ylim[1] * 0.83), xytext=(0, ylim[0] * 0.83),
                arrowprops={"arrowstyle": "<->", "lw": 3.0, "color": "#333333"}, zorder=2)
    ax.scatter([-f, f], [0, 0], s=45, c="#333333", zorder=6)
    for x, label in ((-f, r"$F_{\mathrm{front}}$"), (f, r"$F_{\mathrm{rear}}$")):
        ax.annotate(label, (x, 0), xytext=(0, -20), textcoords="offset points",
                    ha="center", fontsize=14, bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.5}, zorder=7)
    ax.text(0.005, ylim[1] * 0.88, "Lens", fontsize=15, weight="bold")
    ax.annotate("", xy=(-u, height), xytext=(-u, 0),
                arrowprops={"arrowstyle": "-|>", "lw": 3.2, "color": "#222222"}, zorder=6)
    if u < f:
        ax.annotate("Object", (-u, 0), xytext=(0, -36), textcoords="offset points", ha="center", fontsize=16)
    else:
        ax.annotate("Object", (-u, height), xytext=(-5, 10), textcoords="offset points", ha="right", fontsize=16)
    if np.isclose(u, f):
        v = None
    else:
        v = 1 / (1 / f - 1 / u)
        image_height = -v * height / u
        ax.annotate("", xy=(v, image_height), xytext=(v, 0),
                    arrowprops={"arrowstyle": "-|>", "lw": 3.2, "ls": "--" if v < 0 else "-", "color": "#7b2d8d"}, zorder=6)
        ax.scatter([v], [image_height], s=38, color="#7b2d8d", zorder=7)
        ax.annotate("Virtual image" if v < 0 else "Real image", (v, image_height),
                    xytext=(-8 if v < 0 else 0, 10 if v < 0 else -28), textcoords="offset points",
                    ha="right" if v < 0 else "center", fontsize=16, color="#7b2d8d")
    for lens_y, in_slope, out_slope, color in zip(lens_heights, incident, outgoing, COLORS):
        directed_segment(ax, [-u, 0], [height, lens_y], color)
        right = xlim[1] - 0.008
        directed_segment(ax, [0, right], [lens_y, lens_y + out_slope * right], color)
        if v is not None and v < 0:
            directed_segment(ax, [v, 0], [lens_y + out_slope * v, lens_y], color, dashed=True)
    ax.set(xlim=xlim, ylim=ylim)
    ax.set_title(title, loc="left", fontsize=18, pad=15, weight="bold")
    ax.set_xticks(np.asarray(ticks) / 100, [str(t) for t in ticks])
    ax.set_xlabel("Position along optical axis (cm)", fontsize=15, labelpad=5)
    ax.set_yticks([])
    ax.tick_params(axis="x", labelsize=14)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)


def main():
    np.testing.assert_allclose(1 / (1 / 0.1 - 1 / 0.3), 0.15)
    np.testing.assert_allclose(-0.15 / 0.3, -0.5)
    np.testing.assert_allclose(1 / (1 / 0.1 - 1 / 0.05), -0.1)
    np.testing.assert_allclose(-(-0.1) / 0.05, 2)
    plt.rcParams.update({"font.size": 16, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(3, 1, figsize=(11, 11.5), facecolor="white")
    fig.subplots_adjust(left=0.06, right=0.98, top=0.865, bottom=0.14, hspace=0.78)
    fig.suptitle("One converging thin lens, three object positions", fontsize=23, y=0.985)
    fig.text(0.5, 0.947, "f = 10 cm   |   Heights enlarged; all drawn ray slopes satisfy the paraxial model",
             ha="center", fontsize=15)
    draw_case(axes[0], 0.3, 0.005, "u = 30 cm:  v = +15 cm,  m = −0.5",
              (-0.35, 0.24), (-0.012, 0.009), [-30, -20, -10, 0, 10, 15, 20])
    draw_case(axes[1], 0.1, 0.005, "u = 10 cm:  outgoing rays parallel; no finite image",
              (-0.19, 0.19), (-0.014, 0.009), [-10, 0, 10])
    draw_case(axes[2], 0.05, 0.003, "u = 5 cm:  v = −10 cm,  m = +2",
              (-0.19, 0.19), (-0.012, 0.011), [-10, -5, 0, 10])
    fig.legend([Line2D([0], [0], lw=2.5, color=COLORS[0]),
                Line2D([0], [0], lw=2.5, ls="--", color=COLORS[0])],
               ["Actual light paths →", "Backward extensions"],
               loc="lower center", ncol=2, frameon=False, fontsize=16, bbox_to_anchor=(0.5, 0.025))
    fig.savefig("lens-image-formation.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified all ray intersections, focal-case parallelism, lens distances and magnifications.")


if __name__ == "__main__":
    main()
