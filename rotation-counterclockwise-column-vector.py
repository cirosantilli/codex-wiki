"""Draw an active planar rotation; write the matching PNG to the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(6.8, 5.2), layout="constrained")
    fig.get_layout_engine().set(rect=(0, 0.07, 1, 0.93))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    theta = np.pi / 3
    before = np.array([2.0, 0.0])
    after = 2 * np.array([np.cos(theta), np.sin(theta)])
    t = np.linspace(0, 2 * np.pi, 361)
    ax.plot(2 * np.cos(t), 2 * np.sin(t), color="#d5dbe1", lw=1.5)
    ax.axhline(0, color="#73808d", lw=1)
    ax.axvline(0, color="#73808d", lw=1)
    for point, color in [(before, "#196ba1"), (after, "#c14b23")]:
        ax.annotate("", xy=point, xytext=(0, 0),
                    arrowprops={"arrowstyle": "-|>", "color": color,
                                "lw": 3, "mutation_scale": 20})
    t = np.linspace(0, theta, 100)
    radius = 0.72
    ax.plot(radius * np.cos(t), radius * np.sin(t), color="#4d5258", lw=1.7)
    ax.annotate("", xy=(radius * np.cos(t[-1]), radius * np.sin(t[-1])),
                xytext=(radius * np.cos(t[-8]), radius * np.sin(t[-8])),
                arrowprops={"arrowstyle": "-|>", "color": "#4d5258", "lw": 1.7})
    ax.text(0.82, 0.48, r"$\theta=\pi/3$", fontsize=13)
    ax.plot([after[0], after[0]], [0, after[1]], "--", color="#c14b23", lw=1)
    ax.plot([0, after[0]], [after[1], after[1]], "--", color="#c14b23", lw=1)
    ax.text(1.15, 1.85, r"$v'=(1,\sqrt{3})^T$", color="#c14b23", fontsize=13)
    ax.text(1.28, -0.32, r"$v=(2,0)^T$", color="#196ba1", fontsize=13)
    ax.text(-0.17, 1.8, r"$\sqrt{3}$", ha="right", color="#c14b23")
    ax.text(2.34, -0.16, "$x$", ha="center")
    ax.text(-0.15, 2.24, "$y$", ha="right")
    ax.set(xlim=(-2.25, 2.6), ylim=(-2.25, 2.4), aspect="equal")
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_yticks([-2, -1, 0, 1, 2])
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("Active counterclockwise rotation", fontsize=17, pad=14)
    fig.text(0.5, 0.02, "Column vectors · fixed Cartesian axes · length stays 2",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
