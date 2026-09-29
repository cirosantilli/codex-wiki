"""Plot forward waiting solutions; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write an opaque white PNG with this script's basename to the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(7.6, 4.7), dpi=120,
                           constrained_layout=True, facecolor="white")
    colors = ["#1671a3", "#cf7023", "#238758", "#8852a1"]
    for c, color in enumerate(colors):
        t = np.unique(np.r_[np.linspace(0.0, 4.0, 801), float(c)])
        ax.plot(t, np.maximum(t - c, 0.0) ** 2, color=color, lw=2.3,
                label=rf"wait $c={c}$")
        ax.scatter([c], [0], color=color, s=48, zorder=5, clip_on=False)
    ax.plot([0, 4], [0, 0], color="#333333", ls="--", lw=1.7,
            label="stay zero forever", zorder=6)
    ax.set(title="One starting value, many possible departures\n"
                 r"$y'=2\sqrt{|y|},\quad y(0)=0,\quad t\geq 0$",
           xlabel="time t", ylabel="state y", xlim=(0, 4.05), ylim=(-0.65, 16.7))
    ax.text(0.15, 5.2, "Each join has derivative zero.\n"
            "The equation supplies no departure time.", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 6})
    ax.legend(loc="upper left", fontsize=10, framealpha=1)
    ax.grid(alpha=0.16)
    ax.set_facecolor("white")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
