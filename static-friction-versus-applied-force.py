"""Plot conditional friction states, without imposing a loading trajectory.

Writes an opaque white PNG to CWD. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (distribution build 3.10.7+dfsg1).
The numerical parameters are stipulated, not measured material properties.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    normal_force, mu_static, mu_kinetic = 10.0, 0.5, 0.3
    static_limit = mu_static * normal_force
    sliding_magnitude = mu_kinetic * normal_force
    resting_loads = np.linspace(0.0, static_limit, 251)
    sliding_loads = np.linspace(0.0, 8.0, 401)
    blue, orange = "#1768ac", "#bd5217"
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(9.0, 5.5), dpi=120)
    fig.subplots_adjust(left=.10, right=.97, bottom=.25, top=.78)
    ax.plot(resting_loads, resting_loads, color=blue, lw=3,
            label=r"At rest: $|f_s|=F$, only for $0\leq F\leq5$ N")
    ax.plot(sliding_loads, np.full_like(sliding_loads, sliding_magnitude),
            color=orange, lw=2.6, ls="--",
            label=r"Already sliding right: $|f_k|=3$ N while $v>0$")
    ax.scatter([4, 5], [4, 5], s=55, color=blue, zorder=5)
    ax.scatter([6], [3], s=55, color=orange, zorder=5)
    ax.annotate("F = 4 N, at rest\nf = −4 N; a = 0", (4, 4),
                xytext=(1.3, 4.6), fontsize=10, color=blue,
                arrowprops={"arrowstyle": "->", "color": blue},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    ax.annotate("F = 5 N: rest still allowed\nClosed endpoint: f = −5 N", (5, 5),
                xytext=(5.4, 5.1), fontsize=10, color=blue,
                arrowprops={"arrowstyle": "->", "color": blue},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    ax.annotate("F = 6 N, sliding right\nf = −3 N; a = +3 m/s²", (6, 3),
                xytext=(5.05, 1.0), fontsize=10, color=orange,
                arrowprops={"arrowstyle": "->", "color": orange},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    ax.set(xlim=(0, 8), ylim=(0, 6), xticks=np.arange(9),
           yticks=np.arange(7), xlabel="Applied force F to the right (N)",
           ylabel="Friction magnitude |f| (N)")
    ax.grid(alpha=.2)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.015), frameon=False,
              fontsize=10, borderaxespad=0)
    fig.suptitle("Friction depends on the contact state", fontsize=16, y=.97)
    fig.text(.5, .90, r"Stipulated model: $m=1$ kg, $N=10$ N, $\mu_s=0.5$, $\mu_k=0.3$",
             ha="center", fontsize=11)
    fig.text(.5, .125, "The dashed branch is conditional on existing rightward slip, even below 5 N.",
             ha="center", fontsize=10)
    fig.text(.5, .075, "At F = 5 N: rest gives a = 0; existing rightward slip gives a = +2 m/s².",
             ha="center", fontsize=10)
    fig.text(.5, .025, "Comparison of states, not a force-ramp trajectory. Both branches exert leftward friction.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
