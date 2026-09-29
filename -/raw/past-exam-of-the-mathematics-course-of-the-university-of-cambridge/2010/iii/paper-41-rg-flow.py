"""Draw a linear RG flow near a critical surface; output PNG to caller CWD.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7.6, 4.8), dpi=100)
    fig.set_facecolor("white")
    t, v = np.meshgrid(np.linspace(-1.0, 1.0, 9), np.linspace(-0.8, 0.8, 7))
    dt, dv = t, -v
    speed = np.hypot(dt, dv)
    keep = speed > 0
    ax.quiver(t[keep], v[keep], dt[keep] / speed[keep], dv[keep] / speed[keep],
              angles="xy", scale_units="xy", scale=6,
              color="#647787", width=0.0045, pivot="middle")
    ax.axvline(0, color="#176a9e", linestyle="--", linewidth=2,
               label="Critical surface t = 0: attraction toward the fixed point")
    ax.axhline(0, color="#bc5138", linewidth=1.6,
               label="Repulsive thermal trajectory: departure from the fixed point")
    ax.scatter([0], [0], color="black", s=45, zorder=4)
    ax.annotate("Critical fixed point", (0, 0), xytext=(25, 20),
                textcoords="offset points", arrowprops={"arrowstyle": "->"})
    ax.set(xlim=(-1.15, 1.15), ylim=(-0.94, 0.94),
           xlabel="Relevant thermal coordinate t",
           ylabel="Irrelevant coordinate v",
           title="Coarse-graining flow: dt/ds = t, dv/ds = −v")
    ax.set_aspect("equal")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.32), fontsize=9)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-41-rg-flow.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
