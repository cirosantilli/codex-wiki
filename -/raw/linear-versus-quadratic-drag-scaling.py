"""Compare distinct normalized drag models; write an opaque PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    speed_ratio = np.linspace(0, 2.4, 301)
    fig, ax = plt.subplots(figsize=(7.4, 4.9), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(speed_ratio, speed_ratio, lw=2.5, color="#246a9b",
            label=r"Linear model: $F_D/F_D(U_0)=U/U_0$")
    ax.plot(speed_ratio, speed_ratio**2, lw=2.5, color="#ba5739",
            label=r"Constant-$C_D$ quadratic model: $(U/U_0)^2$")
    ax.axvline(2, color="#777777", ls="--", lw=1)
    ax.scatter([2, 2], [2, 4], color=["#246a9b", "#ba5739"], s=55, zorder=4)
    ax.annotate("ratio 2", (2, 2), xytext=(14, -12), textcoords="offset points",
                color="#246a9b", fontsize=11)
    ax.annotate("ratio 4", (2, 4), xytext=(14, -8), textcoords="offset points",
                color="#ba5739", fontsize=11)
    ax.set(xlim=(0, 2.4), ylim=(0, 6), xlabel=r"Relative speed ratio $U/U_0$",
           ylabel=r"Force ratio $F_D(U)/F_D(U_0)$",
           title="Linear and quadratic drag: distinct normalized models")
    ax.set_xticks([0, 0.5, 1, 1.5, 2, 2.4])
    ax.grid(True, alpha=0.18)
    ax.legend(loc="upper left", fontsize=10)
    fig.text(0.5, 0.075,
             "Linear: Stokes assumptions and small particle Re. Quadratic: fixed density, area and Cd.",
             ha="center", fontsize=9)
    fig.text(0.5, 0.03, "Each uses its own reference force; no exact transition or common all-speed parameters.",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.12, 1, 1))
    fig.savefig(Path.cwd() / "linear-versus-quadratic-drag-scaling.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
