"""Original Borsuk-Ulam circle diagram; output PNG basename to CWD.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media: python ../borsuk-ulam-circle-antipodal-values.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    blue, orange, purple = "#2166ac", "#b95319", "#754399"
    theta = np.linspace(0, 2 * np.pi, 601)
    fig, (circle, graph) = plt.subplots(
        1, 2, figsize=(10, 4.3), gridspec_kw={"width_ratios": [1, 1.7]},
        layout="constrained", facecolor="white"
    )
    fig.suptitle(r"Circle example: $F(\theta)=\cos\theta$", fontsize=15)
    circle.plot(np.cos(theta), np.sin(theta), color="#66717b", lw=2)
    circle.axhline(0, color="#c7cdd2", lw=1)
    circle.axvline(0, color="#c7cdd2", lw=1)
    circle.plot([0, 0], [-1, 1], "--", color="#90979e", lw=1)
    circle.scatter([0, 0], [1, -1], color=[blue, orange], s=65, zorder=5)
    circle.text(0.12, 1.13, r"$\theta=\pi/2$" + "\n" + r"$F=0$",
                color=blue, va="center")
    circle.text(0.12, -1.13, r"$\theta=3\pi/2$" + "\n" + r"$F=0$",
                color=orange, va="center")
    circle.text(1.07, 0.08, "$x$")
    circle.text(-0.15, 1.28, "$y$")
    circle.set(xlim=(-1.45, 1.65), ylim=(-1.5, 1.5), aspect="equal")
    circle.set_title(r"Domain $S^1$: opposite points")
    circle.axis("off")

    graph.plot(theta, np.cos(theta), color=blue, lw=2.2,
               label=r"$F(\theta)=\cos\theta$")
    graph.plot(theta, np.cos(theta + np.pi), color=orange, ls="--", lw=2,
               label=r"$F(\theta+\pi)=-\cos\theta$")
    graph.plot(theta, 2 * np.cos(theta), color=purple, lw=2.2,
               label=r"$g(\theta)=F(\theta)-F(\theta+\pi)$")
    graph.axhline(0, color="#555555", lw=1)
    for t in (np.pi / 2, 3 * np.pi / 2):
        graph.axvline(t, color="#b4bac0", ls=":", lw=1)
        graph.scatter(t, 0, s=65, color=purple, zorder=6)
    graph.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                    ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    graph.set(xlim=(0, 2 * np.pi), ylim=(-2.35, 2.35),
              xlabel=r"Angle $\theta$ (radians)", ylabel="Value",
              title=r"Outputs and difference: $g(\theta+\pi)=-g(\theta)$")
    graph.grid(axis="y", color="#e6e8eb", lw=0.7)
    graph.legend(loc="upper center", fontsize=9, framealpha=1,
                 facecolor="white", edgecolor="#dddddd")
    for spine in ("top", "right"):
        graph.spines[spine].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
