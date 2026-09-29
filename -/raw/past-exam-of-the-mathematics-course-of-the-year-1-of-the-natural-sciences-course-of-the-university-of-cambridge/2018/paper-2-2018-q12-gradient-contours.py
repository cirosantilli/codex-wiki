"""Original gradient sketch; Python 3.14 with root NumPy/Matplotlib deps.

Write the PNG basename in the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    axis = np.linspace(0, 3.2, 500)
    x, y = np.meshgrid(axis, axis)
    samples = np.linspace(0.15, 2.9, 8)
    qx, qy = np.meshgrid(samples, samples)
    fig, ax = plt.subplots(figsize=(5.6, 5.2), layout="constrained")
    fig.set_facecolor("white")
    cs = ax.contour(x, y, 2*x*y, levels=[0.5, 1, 2, 4, 8, 12, 16], colors="#176b9b", linewidths=1.1)
    ax.clabel(cs, fmt=lambda v: f"$f={v:g}$", fontsize=9)
    ax.quiver(qx, qy, 2*qy, 2*qx, color="#343434", angles="xy", scale_units="xy", scale=19,
              width=0.0035, headwidth=4.2, pivot="mid")
    ax.axhline(0, color="0.35", lw=1.1)
    ax.axvline(0, color="0.35", lw=1.1)
    ax.set(xlim=(0, 3.2), ylim=(0, 3.2), aspect="equal", xlabel="$x$", ylabel="$y$",
           title="$f=2xy$, $\\nabla f=(2y,2x)$")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
