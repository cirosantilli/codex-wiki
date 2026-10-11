#!/usr/bin/env python3
"""Original even-ring mode sketches; writes its PNG basename to cwd.

Tested: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7 (+dfsg1).
Dependencies are listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    count = 8
    theta = 2*np.pi*(np.arange(count)+.5)/count
    xy = np.column_stack((np.cos(theta), np.sin(theta)))
    tangents = np.column_stack((-np.sin(theta), np.cos(theta)))
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 4.0), dpi=120, facecolor="white")
    for ax, alternating, title in zip(axes, [False, True], [
            r"Uniform: $\omega_{\min}^2=g/L$",
            r"Alternating: $\omega_{\max}^2\simeq g/L+4k/m$"]):
        ax.set_facecolor("white")
        closed = np.vstack((xy, xy[0]))
        ax.plot(closed[:, 0], closed[:, 1], color=".75", lw=1)
        for j, pos in enumerate(xy):
            amplitude = (-1)**j if alternating else 1
            color = "#d55e00" if amplitude < 0 else "#0072b2"
            end = pos+.32*amplitude*tangents[j]
            ax.scatter(*pos, s=28, color=".25")
            ax.annotate("", xy=end, xytext=pos,
                        arrowprops={"arrowstyle": "-|>", "lw": 1.8, "color": color})
            ax.text(*(1.25*pos), "+1" if amplitude>0 else "−1",
                    ha="center", va="center", fontsize=10, color=color)
        ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), aspect="equal", title=title)
        ax.axis("off")
    fig.suptitle("Even ring: tangential normal-mode amplitudes (N = 8)", fontsize=12)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
