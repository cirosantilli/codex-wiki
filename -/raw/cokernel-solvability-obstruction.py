"""A nonzero cokernel class prevents solving a rank-one linear system.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; opaque PNG to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1, 5, 200)
    fig, ax = plt.subplots(figsize=(8.3, 4.8), dpi=125)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(x, np.zeros_like(x), color="#238367", lw=3,
            label=r"Image: all $(b_1,0)$")
    ax.plot(x, np.ones_like(x), color="#80519d", ls="--", lw=2,
            label=r"Cokernel class $[b]=b+\mathrm{im}\,T$: all $(b_1,1)$")
    ax.scatter([3, 3], [0, 1], color=["#238367", "#80519d"], s=70, zorder=4)
    ax.annotate("Attainable (3, 0)", (3, 0), (0.4, -0.7),
                arrowprops={"arrowstyle": "->", "color": "#238367"},
                color="#238367", fontsize=11)
    ax.annotate("Unattainable b = (3, 1)", (3, 1), (0.1, 1.7),
                arrowprops={"arrowstyle": "->", "color": "#80519d"},
                color="#80519d", fontsize=11)
    ax.annotate("", (3, 1), (3, 0),
                arrowprops={"arrowstyle": "<->", "color": "#555555"})
    ax.text(3.12, 0.4, "Obstruction:\nsecond coordinate 1", fontsize=11,
            color="#555555", bbox={"facecolor": "white", "edgecolor": "none"})
    ax.axvline(0, color="#bbbbbb", lw=1)
    ax.set(xlim=(-1, 5), ylim=(-1, 2.25), xlabel="Output coordinate 1",
           ylabel="Output coordinate 2",
           title=r"$T(x,y)=(x+2y,0)$ cannot change the second output coordinate")
    ax.set_aspect("equal")
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.grid(alpha=0.12)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
