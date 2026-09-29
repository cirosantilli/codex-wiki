"""Spectral domains for cubic dispersion and drift diffusion.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes an opaque paper-71-contours.png to the caller's CWD.
"""
import os
import tempfile

if "MPLCONFIGDIR" not in os.environ:
    os.environ["MPLCONFIGDIR"] = tempfile.mkdtemp(prefix="paper-71-mpl-")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5), layout="constrained")
    x = np.linspace(-2.1, 2.1, 1400)
    blue = "#2168ad"
    red = "#b53436"
    cubic = np.sqrt(np.maximum(3*x*x-1, 0))
    drift = (1+np.sqrt(1+4*x*x))/2
    for ax, boundary in zip(axes, [cubic, drift]):
        ax.fill_between(x, boundary, 3.5, color="#dcebf5")
        ax.axhline(0, color="#777777", lw=.7)
        ax.axvline(0, color="#777777", lw=.7)
        ax.set(xlim=(-2.1, 2.1), ylim=(-.18, 3.5), xlabel=r"$\operatorname{Re}k$", ylabel=r"$\operatorname{Im}k$")
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([0, 1, 2, 3])
        ax.spines[["top", "right"]].set_visible(False)
        ax.text(.1, 2.95, r"$D_+$", fontsize=15, color=blue)
        ax.plot(x, boundary, color=blue, lw=1.7)
    axes[0].set_title(r"Cubic dispersion: $\omega=i(k-k^3)$", fontsize=11)
    b = np.sqrt(3)
    axes[0].scatter([-1/b, 1/b], [0, 0], color=blue, s=20, zorder=5)
    axes[0].annotate(r"$-1/\sqrt{3}$", (-1/b, 0), (-1.3, .25), fontsize=10)
    axes[0].annotate(r"$1/\sqrt{3}$", (1/b, 0), (.7, .25), fontsize=10)
    axes[0].annotate("", xy=(-1.1, np.sqrt(3*1.1**2-1)), xytext=(-1.25, np.sqrt(3*1.25**2-1)), arrowprops={"arrowstyle":"->", "color":blue})
    axes[0].annotate("", xy=(1.25, np.sqrt(3*1.25**2-1)), xytext=(1.1, np.sqrt(3*1.1**2-1)), arrowprops={"arrowstyle":"->", "color":blue})
    axes[0].annotate("", xy=(.3, 0), xytext=(-.25, 0), arrowprops={"arrowstyle":"->", "color":blue})
    axes[1].set_title(r"Drift diffusion: $\omega=k^2-ik$", fontsize=11)
    gamma = 1+np.abs(x)*np.tan(np.pi/8)
    axes[1].plot(x, gamma, color=red, lw=1.8, label=r"$\Gamma$, $\theta=\pi/8$")
    axes[1].scatter([0], [.4], color="#333333", marker="x", s=35, zorder=5)
    axes[1].annotate("initial-data pole\n($a=0.6$)", (0, .4), (.55, .48), fontsize=8.5,
                     arrowprops={"arrowstyle":"->", "color":"#555555"})
    axes[1].annotate(r"$i\alpha$", (0, 1), (.15, 1.05), fontsize=11)
    axes[1].annotate("", xy=(-.8, 1+.8*np.tan(np.pi/8)), xytext=(-1.3, 1+1.3*np.tan(np.pi/8)), arrowprops={"arrowstyle":"->", "color":red})
    axes[1].annotate("", xy=(1.3, 1+1.3*np.tan(np.pi/8)), xytext=(.8, 1+.8*np.tan(np.pi/8)), arrowprops={"arrowstyle":"->", "color":red})
    axes[1].legend(loc="upper left", frameon=False, fontsize=9)
    fig.suptitle("Upper spectral domains and oriented integration contours", fontsize=12)
    fig.savefig("paper-71-contours.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
