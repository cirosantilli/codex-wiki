"""Draw exact parabola traversals and a singular change of curve parameter.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Points mark equal parameter increments, not observations of an experiment.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, orange, gray = "#2468a0", "#b76b14", "#666666"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (route, clock) = plt.subplots(1, 2, figsize=(10.8, 5.6), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.97, top=0.78, bottom=0.32, wspace=0.34)
    fig.suptitle("The same parabola can have a nonzero or zero instantaneous velocity", fontsize=15, y=0.98)
    fig.text(0.5, 0.885, r"$\gamma(t)=(t,t^2)$ and $\beta(s)=\gamma(s^3)=(s^3,s^6)$", ha="center", fontsize=14)
    x = np.linspace(-1.15, 1.15, 300)
    route.plot(x, x*x, color=gray, lw=2, label=r"route: $y=x^2$")
    samples = np.linspace(-1, 1, 5)
    route.scatter(samples, samples**2, marker="o", s=65, facecolors="white", edgecolors=blue,
                  linewidths=1.8, zorder=3, label=r"equal increments of $t$")
    route.scatter(samples**3, samples**6, marker="x", s=48, color=orange, linewidths=1.8,
                  zorder=4, label=r"equal increments of $s$")
    route.axhline(0, color=gray, ls="--", lw=1)
    route.annotate("", (1, 0), (0, 0), arrowprops={"arrowstyle": "->", "lw": 3, "color": blue})
    route.scatter([0], [0], s=95, facecolors="white", edgecolors=orange, linewidths=2, zorder=5)
    route.annotate(r"$\beta'(0)=0$", (0, 0), xytext=(-1.1, -0.4), color=orange,
                   arrowprops={"arrowstyle": "->", "color": orange}, fontsize=12)
    route.text(0.38, -0.20, r"$\gamma'(0)=(1,0)$", color=blue)
    route.set(xlim=(-1.25, 1.35), ylim=(-0.55, 1.65), xlabel="x", ylabel="y")
    route.set_aspect("equal")
    route.set_title("Geometry: the horizontal tangent line survives", fontsize=11)
    route.legend(loc="upper center", frameon=False, fontsize=9)

    u = np.linspace(-1.05, 1.05, 301)
    clock.plot(u, u, color=blue, lw=2, label=r"$x=t$")
    clock.plot(u, u**3, color=orange, lw=2.4, label=r"$x=s^3$")
    clock.axhline(0, color=gray, ls="--", lw=1)
    clock.axvline(0, color="#dddddd", lw=0.8)
    clock.scatter([0], [0], color="black", s=30, zorder=5)
    clock.annotate("slope 1", (0.48, 0.48), xytext=(-0.95, 0.75), color=blue,
                   arrowprops={"arrowstyle": "->", "color": blue})
    clock.annotate("slope 0 at the origin", (0, 0), xytext=(-0.96, -0.68), color=orange,
                   arrowprops={"arrowstyle": "->", "color": orange})
    clock.set(xlim=(-1.1, 1.1), ylim=(-1.25, 1.25), xlabel="parameter (t or s)", ylabel="x-coordinate")
    clock.set_title("Traversal: the singular clock has zero derivative", fontsize=11)
    clock.legend(loc="lower right", frameon=False, fontsize=11)
    fig.text(0.26, 0.135, "The blue arrow is a velocity at the origin.\nThe orange ring represents the zero vector.", ha="center", va="center")
    fig.text(0.76, 0.135, r"$\beta'(s)=(3s^2,6s^5)$"+"\n"+r"$h(s)=s^3$ has no smooth inverse at zero.", ha="center", va="center")
    fig.text(0.5, 0.025, "Exact analytical curves; the marked points are parameter samples, not measured data.",
             ha="center", fontsize=10, color="#555555")
    assert np.allclose((samples**3)**2, samples**6)
    assert np.all(3*u[u != 0]**2 > 0)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
