"""Generate interference-intensity-versus-phase.png in CWD on white.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Scalar electric-field intensity; phase angles are in radians.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    phase = np.linspace(0, 2 * np.pi, 1001)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.4, 5.1), dpi=110)
    fig.subplots_adjust(left=.10, right=.97, bottom=.19, top=.78)
    for i2, colour, label in [(1., "#1768ac", r"$I_1=I_2=1$: visibility 1"),
                               (.25, "#cb6418", r"$I_1=1,\ I_2=0.25$: visibility 0.8")]:
        intensity = 1 + i2 + 2 * np.sqrt(i2) * np.cos(phase)
        ax.plot(phase, intensity, color=colour, lw=2.5, label=label)
        ax.axhline(1 + i2, color=colour, lw=1.2, ls="--", alpha=.7)
        ax.scatter([0, np.pi, 2 * np.pi],
                   [(1 + np.sqrt(i2)) ** 2, (1 - np.sqrt(i2)) ** 2,
                    (1 + np.sqrt(i2)) ** 2], color=colour, s=28, zorder=3)
    ax.annotate("4", (0, 4), xytext=(8, -1), textcoords="offset points", color="#1768ac")
    ax.annotate("2.25", (0, 2.25), xytext=(8, 8), textcoords="offset points", color="#cb6418")
    ax.annotate("0.25", (np.pi, .25), xytext=(8, 7), textcoords="offset points", color="#cb6418")
    ax.annotate("0", (np.pi, 0), xytext=(8, -12), textcoords="offset points", color="#1768ac")
    ax.set(xlim=(0, 2 * np.pi), ylim=(-.12, 4.18),
           xlabel=r"Phase difference $\delta$ (radians)",
           ylabel="Scalar electric-field intensity (common unit)")
    ax.set_xticks(np.arange(5) * np.pi / 2,
                  ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax.grid(alpha=.18)
    ax.legend(loc="upper center", bbox_to_anchor=(.5, 1.24), frameon=False, fontsize=10)
    fig.suptitle("Coherent beams: add fields, then square", y=.98, fontsize=15)
    fig.text(.5, .035, "Dashed: full-phase averages 2 and 1.25. Equal-beam curve uses I₀ = 1.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "interference-intensity-versus-phase.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
