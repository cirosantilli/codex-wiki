"""Synthetic linear limb-darkening profiles; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes this script's basename as an opaque PNG in the CWD.
All coefficients are stipulated, with no measured solar data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.2), layout="constrained")
    q = np.linspace(-1.03, 1.03, 501)
    x, y = np.meshgrid(q, q)
    radius2 = x*x + y*y
    disk = np.ma.masked_where(radius2 > 1, 0.4 + 0.6*np.sqrt(np.maximum(0, 1-radius2)))
    cmap = plt.colormaps["gray"].copy()
    cmap.set_bad("white")
    ax = axes[0]
    ax.imshow(disk, origin="lower", extent=[q[0], q[-1], q[0], q[-1]],
              cmap=cmap, vmin=0, vmax=1, interpolation="nearest")
    ax.add_patch(Circle((0, 0), 1, fill=False, color="0.25", linewidth=1))
    ax.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), aspect="equal",
           title="Synthetic disk: u = 0.6", xlabel=r"$x/R_\star$", ylabel=r"$y/R_\star$")
    ax.text(0, 0, "1.00", ha="center", va="center")
    ax.text(0, -0.77, "darker toward the edge", ha="center", color="white", fontsize=10)
    mu = np.linspace(0, 1, 501)
    r = np.linspace(0, 1, 501)
    colors = ["#626262", "#0072b2", "#d55e00", "#009e73"]
    for u, color in zip([0, 0.3, 0.6, 0.9], colors):
        axes[1].plot(mu, 1-u+u*mu, color=color, label=f"u = {u:g}", lw=2)
        axes[2].plot(r, 1-u+u*np.sqrt(1-r*r), color=color, lw=2)
    axes[1].set(title="Angular profiles", xlabel=r"$\mu = \cos\theta$",
                ylabel=r"$I/I_c$", xlim=(0, 1), ylim=(0, 1.06))
    axes[1].legend(loc="lower right", frameon=False)
    axes[2].set(title="Projected radial profiles", xlabel=r"$r/R_\star$",
                ylabel=r"$I/I_c$", xlim=(0, 1), ylim=(0, 1.06))
    for ax in axes[1:]:
        ax.grid(alpha=0.2)
    fig.suptitle("Linear limb darkening: equal central intensity, stipulated coefficients", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
