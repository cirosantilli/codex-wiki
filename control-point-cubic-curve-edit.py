"""Draw a cubic control-polygon edit; save the matching PNG in the CWD.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def curve(controls, t):
    t = np.asarray(t)
    weights = np.stack(((1-t)**3, 3*t*(1-t)**2,
                        3*t**2*(1-t), t**3), axis=-1)
    return weights @ controls


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    blue, orange = "#17689b", "#bb4f12"
    controls = np.array(((0., 0.), (1., 2.), (3., 2.), (4., 0.)))
    edited = controls.copy()
    edited[1] += (0, 1)
    t = np.linspace(0, 1, 601)
    before, after = curve(controls, t), curve(edited, t)
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.3), layout="constrained")
    for ax in axes:
        ax.set(xlim=(-.4, 4.4), ylim=(-.4, 3.65), xlabel="$x$", ylabel="$y$")
        ax.set_aspect("equal")
        ax.set_xticks(range(5))
        ax.set_yticks(range(4))
        ax.grid(alpha=.18)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
    left, right = axes
    left.set_title("Before: four handles define the curve", pad=12)
    left.plot(*controls.T, "o--", color=blue, lw=1.2, ms=7,
              mfc="white", label="Control polygon")
    left.plot(*before.T, color=blue, lw=2.6, label="Original curve")
    offsets = ((-13, -23), (-23, 12), (-16, 12), (-5, -23))
    for i, (p, offset) in enumerate(zip(controls, offsets)):
        left.annotate(f"$P_{i}$", p, xytext=offset, textcoords="offset points")
    mid = curve(controls, .5)
    left.plot(*mid, "o", color=blue, ms=5)
    left.annotate("$C(1/2)=(2,1.5)$", mid, xytext=(10, -35),
                  textcoords="offset points", arrowprops={"arrowstyle": "-"})
    left.legend(loc="upper right", frameon=False)
    right.set_title("After: move only $P_1$ by $h=(0,1)$", pad=12)
    right.plot(*before.T, color=blue, lw=2, alpha=.8, label="Original curve")
    right.plot(*after.T, color=orange, lw=2.6, label="Edited curve")
    right.plot(*edited.T, "o--", color=orange, lw=1.2, ms=7, mfc="white")
    right.plot(*controls[1], "o", color=blue, ms=6, mfc="white")
    right.annotate("", edited[1], controls[1],
                   arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.6})
    right.annotate("$h$", (.88, 2.5), ha="right")
    right.annotate("$P_1=(1,2)$", controls[1], xytext=(-38, 5),
                   textcoords="offset points", ha="right", fontsize=10)
    right.annotate(r"$\widetilde P_1=(1,3)$", edited[1], xytext=(-45, 14),
                   textcoords="offset points", fontsize=10)
    for i in (0, 2, 3):
        right.annotate(f"$P_{i}$", edited[i], xytext=offsets[i],
                       textcoords="offset points")
    a, b = curve(controls, 1/3), curve(edited, 1/3)
    right.plot(*np.array((a, b)).T, "o", color="#333333", ms=4)
    right.annotate("", b, a, arrowprops={"arrowstyle": "->", "lw": 1.6})
    right.annotate(r"$\Delta C(1/3)=(0,4/9)$", (a+b)/2,
                   xytext=(2.05, .65), fontsize=10,
                   arrowprops={"arrowstyle": "-", "color": "#666666"})
    right.legend(loc="upper right", frameon=False, fontsize=10)
    fig.suptitle("Moving a control point reshapes a curve", fontsize=16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
