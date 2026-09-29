"""Compare delayed solutions and blowup; Python 3.14/NumPy 2.3.5/Matplotlib 3.10.7.

Writes an opaque white ode-uniqueness-and-blowup.png to the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.9), dpi=120,
                             constrained_layout=True, facecolor="white")
    left, right = axes
    t = np.linspace(0, 3, 601)
    colors = ["#2378a6", "#d07b25", "#33865c"]
    for delay, color in zip([0, 1, 2], colors):
        left.plot(t, np.maximum(t - delay, 0) ** 2, color=color,
                  lw=2.5, label=f"delay c = {delay}")
    left.axhline(0, color="#555555", ls="--", lw=1.5, label="always zero")
    left.scatter([0], [0], color="#222222", s=34, zorder=5)
    left.set(title="Continuous rule, multiple futures\n"
                   r"$y'=2\sqrt{\max(y,0)},\quad y(0)=0$",
             xlabel="time t", ylabel="trajectory value y",
             xlim=(0, 3), ylim=(-0.3, 9.7), xticks=[0, 1, 2, 3])
    left.legend(loc="upper left", framealpha=1, fontsize=9)

    endpoint = np.pi / 2
    ceiling = 10.0
    # Never sample the singular endpoint or continue onto another tangent branch.
    t = np.linspace(0, endpoint - 0.005, 1001)
    right.plot(t, np.tan(t), color="#8555a5", lw=2.6, label=r"unique $y=\tan t$")
    right.axvline(endpoint, color="#b34335", ls="--", lw=1.6)
    right.text(endpoint - 0.025, 1.8, r"$T=\pi/2$", rotation=90,
               ha="right", va="center", color="#b34335")
    cutoff = np.arctan(ceiling)
    right.annotate("continues upward", xy=(cutoff, 9.8), xytext=(0.4, 8.8),
                   arrowprops={"arrowstyle": "->", "color": "#8555a5"},
                   color="#8555a5", fontsize=9)
    for time in [1.0, 1.4]:
        value = np.tan(time)
        right.scatter([time], [value], s=26, color="#8555a5", zorder=5)
        right.annotate(f"({time:g}, {value:.3f})", xy=(time, value),
                       xytext=(-8, 7), textcoords="offset points",
                       ha="right", fontsize=9)
    right.set(title="Smooth rule, finite lifetime\n"
                    r"$y'=1+y^2,\quad y(0)=0$",
              xlabel="time t", ylabel="trajectory value y",
              xlim=(0, endpoint + 0.075), ylim=(-0.3, ceiling),
              xticks=[0, 0.5, 1.0, endpoint],
              xticklabels=["0", "0.5", "1.0", r"$\pi/2$"])
    right.legend(loc="upper left", bbox_to_anchor=(0, 0.75),
                 framealpha=1, fontsize=9)
    fig.supxlabel("Right panel: vertical axis clipped at 10; no finite value exists at T.",
                  fontsize=10)
    for ax in axes:
        ax.grid(alpha=0.15)
        ax.set_facecolor("white")
    fig.savefig(Path.cwd() / "ode-uniqueness-and-blowup.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
