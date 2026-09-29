"""Draw original WKB mountain-wave sketches; output PNG to caller CWD.

The illustrations use kH=12; crest geometry and ray paths
are the geometrical-optics construction, not a quantitative amplitude fit.
Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def integral_samples(f, z):
    values = f(z)
    return np.r_[0.0, np.cumsum((values[1:] + values[:-1]) * np.diff(z) / 2)]


def ray_arrow(ax, x, z, fraction, color="#176a9e"):
    i = min(int(fraction * len(x)), len(x) - 5)
    j = min(i + max(4, len(x) // 15), len(x) - 1)
    ax.annotate("", (x[j], z[j]), (x[i], z[i]),
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2})


def main():
    q0 = 0.55
    kH = 12
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.9), dpi=100)
    fig.set_facecolor("white")

    z = np.linspace(0, 1.6, 1500)
    m = lambda zz: np.sqrt(((1 + zz) / q0)**2 - 1)
    phase = integral_samples(m, z)
    xgrid = np.linspace(-0.3, 3.3, 350)
    xx, zz = np.meshgrid(xgrid, z)
    axes[0].contour(xx, zz, kH * (xx + phase[:, None]),
                    levels=np.arange(-12, 150, 2 * np.pi),
                    colors="#a7b5c1", linewidths=0.8)
    rayx = q0 * (np.arccosh((1 + z) / q0) - np.arccosh(1 / q0))
    axes[0].plot(rayx, z, color="#176a9e", lw=2)
    ray_arrow(axes[0], rayx, z, 0.4)
    axes[0].set(title="N increases; U fixed", xlim=(-0.15, 2.1), ylim=(0, 1.6))
    axes[0].text(0.8, 0.3, "Upward energy ray", fontsize=9, color="#176a9e")

    zt = 1 - q0
    z = np.linspace(0, zt, 1500)
    phase = integral_samples(lambda zz: np.sqrt(np.maximum(((1 - zz) / q0)**2 - 1, 0)), z)
    xx, zz = np.meshgrid(xgrid, z)
    axes[1].contour(xx, zz, kH * (xx + phase[:, None]),
                    levels=np.arange(-12, 65, 2 * np.pi),
                    colors="#a7b5c1", linewidths=0.8)
    axes[1].contour(xx, zz, kH * (xx - phase[:, None] + 2 * phase[-1]),
                    levels=np.arange(-12, 65, 2 * np.pi),
                    colors="#c7adb2", linestyles="--", linewidths=0.8)
    rayx = q0 * (np.arccosh(1 / q0) - np.arccosh(np.maximum((1 - z) / q0, 1)))
    axes[1].plot(rayx, z, color="#176a9e", lw=2)
    axes[1].plot(2 * rayx[-1] - rayx[::-1], z[::-1], color="#bc5138", lw=2)
    ray_arrow(axes[1], rayx, z, 0.25)
    ray_arrow(axes[1], 2 * rayx[-1] - rayx[::-1], z[::-1], 0.4, "#bc5138")
    axes[1].axhspan(zt, 0.85, color="#eceef1")
    axes[1].axhline(zt, color="black", ls="--", lw=1)
    axes[1].text(0.75, 0.67, "Evanescent above", ha="center", fontsize=9)
    axes[1].text(0.77, zt + 0.035, "Turning level", ha="center", fontsize=9)
    axes[1].set(title="N decreases; U fixed", xlim=(-0.15, 1.5), ylim=(0, 0.85))

    zt = 1 / q0 - 1
    z = np.linspace(0, zt, 1500)
    q = q0 * (1 + z)
    root = np.sqrt(np.maximum(1 - q*q, 0))
    xt = np.sqrt(1 - q0*q0) / q0
    rayx = xt - root / q0
    axes[2].plot(rayx, z, color="#176a9e", lw=2)
    axes[2].plot(xt + root[::-1] / q0, z[::-1], color="#bc5138", lw=2)
    ray_arrow(axes[2], rayx, z, 0.3)
    ray_arrow(axes[2], xt + root[::-1] / q0, z[::-1], 0.35, "#bc5138")
    axes[2].axhspan(zt, 1.05, color="#eceef1")
    axes[2].axhline(zt, color="black", ls="--", lw=1)
    axes[2].text(xt, zt + 0.1, "Turning level", ha="center", fontsize=9)
    axes[2].text(xt, 0.35, "Circular energy ray", ha="center", fontsize=9)
    axes[2].set(title="N fixed; U increases linearly",
                xlim=(-0.1, 2 * xt + 0.1), ylim=(0, 1.05))

    for ax in axes:
        ax.set(xlabel="Downwind distance x/H", ylabel="Height z/H")
        ax.grid(alpha=0.15)
    fig.suptitle("Ground-frame energy rays (blue incident, red reflected); thin lines are wave crests",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-71-mountain-wkb.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
