"""Original functional stereo/reconstruction diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import numpy as np


def arrow(ax, a, b, color="#64748b", style="->", lw=1.5):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=12,
                               color=color, lw=lw))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11.4, 6.4), dpi=120, facecolor="white")
    fig.suptitle("Stereo photographs become a test of a reaction", fontsize=17, y=.97)
    left = fig.add_axes((.045, .37, .47, .49))
    left.set(xlim=(-1.1, 6.3), ylim=(-.8, 4.2))
    left.axis("off")
    left.set_title("Sensitive hydrogen target + two views", loc="left", fontsize=12)
    left.add_patch(FancyBboxPatch((.5, -.3), 4.5, 2.35, boxstyle="round,pad=.08",
                                 facecolor="#edf6fc", edgecolor="#527a96", lw=1.5))
    arrow(left, (-1, .5), (2.2, .5), color="#334155", lw=2)
    left.text(-.95, .15, "beam", fontsize=11)
    t = np.linspace(0, 1, 50)
    left.plot(2.2 + 2.0*t, .5 + 1.0*t - .7*t*t, color="#ba3c25", lw=2.3)
    left.plot(2.2 + 1.6*t, .5 - .7*t + .4*t*t, color="#266f48", lw=2.3)
    left.scatter([2.2], [.5], color="#1e293b", zorder=5, s=26)
    left.text(2.1, -.14, "interaction vertex", ha="center", fontsize=10)
    left.text(4.65, 1.5, r"$\odot\ B$", ha="right", fontsize=13)
    left.text(2.75, - .65, "bubbles mark charged daughter paths", ha="center", fontsize=10)
    for cx, label in [(1.05, "camera L"), (4.4, "camera R")]:
        left.add_patch(Rectangle((cx-.36, 3.1), .72, .5, facecolor="#e2e8f0", edgecolor="#475569"))
        left.plot([cx, cx], [2.94, 3.1], color="#475569", lw=5)
        left.text(cx, 3.77, label, ha="center", fontsize=10)
        left.plot([cx, 2.2], [2.94, .5], color="#8b6baf", ls="--", lw=1.1)
    left.text(5.22, 2.45, "matched\nvertex", ha="center", fontsize=10, color="#75539b")
    left.text(.6, 2.25, "illumination + calibrated windows", fontsize=10)

    right = fig.add_axes((.60, .37, .36, .49))
    right.set(xlim=(-.4, 2.8), ylim=(-.55, 3.9), aspect="equal")
    right.axis("off")
    right.set_title("Ideal ray geometry (no refraction)", fontsize=12)
    b, f = 2., .8
    point = np.array([.8, 3.])
    for x, label in [(0, "L"), (b, "R")]:
        right.plot([x, point[0]], [0, point[1]], color="#75539b", lw=1.5)
        right.plot([x, x], [0, 3.4], color="#94a3b8", ls=":", lw=1)
        right.scatter([x], [0], s=25, color="#334155")
        right.text(x, -.2, label, ha="center")
    right.plot([-.3, 2.4], [f, f], color="#94a3b8", lw=1.2)
    right.text(2.45, f, "virtual\nimage plane", fontsize=9, va="center")
    for x in [0, b]:
        u = x + (point[0]-x)*f/point[1]
        right.scatter([u], [f], s=26, color="#d97706", zorder=5)
    right.scatter([point[0]], [point[1]], color="#1e293b", s=30)
    right.text(point[0]+.1, point[1]+.08, "P = (X, Z)", fontsize=10)
    arrow(right, (0, -.45), (b, -.45), style="<->", lw=1)
    right.text(b/2, -.43, "baseline b", ha="center", va="bottom", fontsize=9)
    right.text(1., 3.65, r"$d = u_L-u_R\quad\Rightarrow\quad Z=fb/d$", ha="center", fontsize=12)

    flow = fig.add_axes((.03, .08, .94, .23))
    flow.set(xlim=(0, 10), ylim=(0, 1))
    flow.axis("off")
    labels = ["Match points\nin stereo views", "Calibrated rays\nto (x, y, z)",
              "Track curvature\nto momenta", "Reaction fits\n+ selection", "Mass histogram\nacross events"]
    for i, label in enumerate(labels):
        x = i*2 + .07
        flow.add_patch(FancyBboxPatch((x, .24), 1.68, .57, boxstyle="round,pad=.045",
                       facecolor="#f1f5f9" if i<4 else "#e6f3ec", edgecolor="#64748b"))
        flow.text(x+.84, .525, label, ha="center", va="center", fontsize=10)
        if i<4:
            arrow(flow, (x+1.74, .525), (x+1.97, .525), lw=1.4)
    fig.text(.5, .028, "Functional schematic: photographs record bubbles; resonance evidence comes from the event ensemble.",
             ha="center", fontsize=11, color="#334155")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
