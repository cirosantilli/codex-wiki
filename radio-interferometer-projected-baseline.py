"""Original schematic geometry, not historical measurements.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; writes the matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(11, 6.4), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[3.5, 1])
    ax = fig.add_subplot(grid[0, 0])
    track = fig.add_subplot(grid[0, 1])
    chain = fig.add_subplot(grid[1, :])
    blue, orange, green = "#185c9c", "#c55a16", "#267355"
    origin, baseline = np.array([0., 0.]), np.array([4., 0.])
    sight = np.array([0.5, np.sqrt(3)/2])
    parallel = np.dot(baseline, sight) * sight
    perpendicular = baseline - parallel
    assert np.isclose(np.dot(perpendicular, sight), 0)
    assert np.allclose(parallel + perpendicular, baseline)

    def arrow(start, end, color, text=None, offset=(0, 0)):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=14, lw=2, color=color))
        if text:
            middle = (np.asarray(start) + np.asarray(end))/2 + offset
            ax.text(*middle, text, color=color, ha="center", va="center",
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})

    arrow(origin, baseline, "#444444", r"$\mathbf{b}=\mathbf{r}_2-\mathbf{r}_1$", (0, -.24))
    arrow(origin, 3.2*sight, blue)
    ax.text(.8, 2.9, r"toward phase centre $\mathbf{s}_0$", color=blue)
    arrow(origin, parallel, orange, r"$(\mathbf{b}\cdot\mathbf{s}_0)\mathbf{s}_0$", (-.5, .07))
    arrow(parallel, baseline, green, r"$\mathbf{b}_\perp$", (.35, .22))
    tangent = perpendicular/np.linalg.norm(perpendicular)
    ax.plot(*np.stack([parallel-.4*tangent, baseline+.45*tangent]).T,
            color=green, ls=":", lw=1)
    corner = parallel + .14*tangent
    ax.plot(*np.stack([corner-.14*sight, corner, parallel+.14*sight]).T,
            color="#777777", lw=1)
    ax.scatter([0, 4], [0, 0], s=65, c="#444444", zorder=5)
    ax.text(-.1, -.55, "Antenna 1", ha="center")
    ax.text(4, -.55, "Antenna 2", ha="center")
    ax.text(.15, -1.03, r"Reference delay magnitude: $|\tau_g|=|\mathbf{b}\cdot\mathbf{s}_0|/c$")
    ax.set(xlim=(-1.3, 5), ylim=(-1.25, 3.4), aspect="equal")
    ax.set_title("Path delay and sky-plane projection", loc="left", weight="bold")
    ax.axis("off")

    hour = np.linspace(-np.pi/2, np.pi/2, 401)
    declination = np.deg2rad(45)
    for radius, color in [(1, blue), (.6, green)]:
        u = radius*np.cos(hour)
        v = radius*np.sin(declination)*np.sin(hour)
        track.plot(u, v, c=color, lw=2, label=f"Baseline {radius:g}" )
        track.plot(-u, -v, c=color, ls="--", lw=1.4)
    for degrees, label in [(-60, "−4 h"), (0, "0 h"), (60, "+4 h")]:
        h = np.deg2rad(degrees)
        xy = (np.cos(h), np.sin(declination)*np.sin(h))
        track.scatter(*xy, c=blue, s=25, zorder=5)
        track.annotate(label, xy, xytext=(7, 2), textcoords="offset points", fontsize=10)
    track.axhline(0, c=".8", lw=.7)
    track.axvline(0, c=".8", lw=.7)
    track.set(xlim=(-1.32, 1.38), ylim=(-.95, 1.0), aspect="equal",
              xlabel=r"$u$ / (longest baseline / $\lambda$)",
              ylabel=r"$v$ / (longest baseline / $\lambda$)")
    track.set_title("Earth rotation: east–west baselines", loc="left", weight="bold")
    track.text(-1.2, .83, r"$\delta=45^\circ$; solid: 12-hour track", fontsize=10)
    track.text(-1.2, -.88, "Dashed: Hermitian partners (inferred)", fontsize=10)
    track.legend(loc="upper center", bbox_to_anchor=(.5, -.22), ncol=2, frameon=False, fontsize=10)

    chain.set(xlim=(0, 10), ylim=(0, 1))
    chain.axis("off")
    blocks = [(.02, 1.9, "Two antenna\nvoltage signals"),
              (2.45, 2.1, "Reference delay +\nphase compensation"),
              (5.1, 2.25, "Complex correlation\n" + r"$\langle E_1 E_2^*\rangle$"),
              (7.9, 2, "Visibility at one\nprojected baseline")]
    for x, width, label in blocks:
        chain.add_patch(FancyBboxPatch((x, .2), width, .65, boxstyle="round,pad=0.02",
                                      ec="#aaaaaa", fc="#f4f7fa"))
        chain.text(x+width/2, .525, label, ha="center", va="center", fontsize=10)
    for start, end in [(1.95, 2.4), (4.6, 5.05), (7.4, 7.85)]:
        chain.annotate("", (end, .525), (start, .525), arrowprops={"arrowstyle": "->", "color": ".4"})
    fig.suptitle("Separated antennas measure spatial coherence", fontsize=16, weight="bold")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
