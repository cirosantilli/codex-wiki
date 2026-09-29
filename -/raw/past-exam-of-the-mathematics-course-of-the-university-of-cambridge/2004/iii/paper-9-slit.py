"""Open a slit into its two boundary sides. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-9-slit.png to the caller's current directory. Caller MPLCONFIGDIR
is honored; neither source paths nor repository configuration are modified.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.8), layout="constrained")
    fig.patch.set_facecolor("white")
    theta = np.linspace(0, np.pi, 400)
    axes[0].plot(2 * np.cos(theta), 2 * np.sin(theta), color="black", lw=1.7)
    axes[0].plot([-2, 2], [0, 0], color="black", lw=1.7)
    axes[0].plot([0, 0], [0, 1], color="black", lw=2.2)
    axes[0].plot(0, 0.5, "o", mfc="white", mec="black", ms=5)
    axes[0].annotate(r"$i/2$", (0, 0.5), (-0.35, 0.78))
    angles = np.linspace(0, 2 * np.pi, 500)
    axes[1].plot(np.cos(angles), np.sin(angles), color="black", lw=1.7)
    axes[1].plot([0, 1], [0, 0], color="black", lw=2.2)
    axes[1].plot(4 / 21, 0, "o", mfc="white", mec="black", ms=5)
    axes[1].annotate(r"$4/21$", (4 / 21, 0), (0.12, -0.26))
    axes[2].plot(np.cos(theta), np.sin(theta), color="black", lw=1.7)
    axes[2].plot([-1, 1], [0, 0], color="black", lw=1.7)
    c = 2 / np.sqrt(21)
    for sign, color in [(1, "#007f9b"), (-1, "#c65c00")]:
        t = np.linspace(0.42, 0.012, 90)
        z = sign * t + 0.5j
        v = 4 * (z * z + 1) / (z * z + 16)
        arg = np.mod(np.angle(v), 2 * np.pi)
        u = np.sqrt(np.abs(v)) * np.exp(0.5j * arg)
        for ax, points in zip(axes, [z, v, u]):
            ax.plot(points.real, points.imag, color=color, lw=2)
            ax.annotate("", (points[-1].real, points[-1].imag),
                        (points[-18].real, points[-18].imag),
                        arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        axes[2].plot(sign * c, 0, "o", mfc="white", mec=color, ms=6)
        axes[2].text(sign * c, -0.12, r"$+c$" if sign > 0 else r"$-c$",
                     color=color, ha="center", va="top")
    axes[0].set(xlim=(-2.16, 2.16), ylim=(-0.17, 2.16), title=r"Slit domain $D$")
    axes[1].set(xlim=(-1.16, 1.16), ylim=(-1.16, 1.16),
                title=r"$v=4(z^2+1)/(z^2+16)$")
    axes[2].set(xlim=(-1.16, 1.16), ylim=(-0.2, 1.16), title=r"$u=\sqrt{v}$, $0<\arg u<\pi$")
    for ax in axes:
        ax.set_aspect("equal", adjustable="box")
        ax.set_facecolor("white")
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.suptitle(r"Right (blue) and left (orange) approaches separate; $c=2/\sqrt{21}$", fontsize=12)
    fig.savefig(Path.cwd() / "paper-9-slit.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
