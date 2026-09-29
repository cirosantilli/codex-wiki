"""Compare specular reflection with phase-conjugate return in a uniform medium.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from the output directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.3), sharex=True, sharey=True)
    blue, orange, green = "#2463a8", "#bb4d12", "#168064"
    L = 3.0
    z = np.linspace(0, L, 180)
    x = np.linspace(-1.65, 1.65, 400)
    for ax, conjugate in zip(axes, (False, True)):
        return_color = green if conjugate else orange
        ax.axvline(L, color="#343434", lw=4)
        for radius in (1.8, 2.3, 2.8):
            valid = np.abs(x) < radius
            zx = np.sqrt(radius**2 - x[valid] ** 2)
            ax.plot(zx, x[valid], color=blue, lw=1.2, alpha=0.5)
            if conjugate:
                ax.plot(zx, x[valid], color=green, ls="--", lw=1.2)
        if not conjugate:
            for radius in (3.4, 4.1, 4.8, 5.5):
                zx = 2 * L - np.sqrt(radius**2 - x**2)
                ax.plot(zx, x, color=orange, ls="--", lw=1.2, alpha=0.75)
        for slope in (-0.25, 0, 0.25):
            outward = slope * z
            returning = outward if conjugate else slope * (2 * L - z)
            ax.plot(z, outward, color=blue, lw=2)
            ax.plot(z, returning, color=return_color, lw=2, ls="--")
            ax.annotate("", (1.25, slope * 1.25), (0.85, slope * 0.85),
                        arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
            rz = (2.2, 1.8)
            rx = tuple(slope * q if conjugate else slope * (2 * L - q) for q in rz)
            ax.annotate("", (rz[1], rx[1]), (rz[0], rx[0]),
                        arrowprops={"arrowstyle": "->", "color": return_color, "lw": 2})
        ax.plot(0, 0, "o", color=blue, ms=7, zorder=5)
        if not conjugate:
            ax.scatter([0, 0], [-1.5, 1.5], color=orange, s=35, zorder=5)
        ax.text(L, 1.83, "return surface", ha="center", fontsize=10)
        ax.set(xlim=(-0.22, 3.32), ylim=(-1.8, 1.8), xlabel="z (geometric units)")
        ax.set_aspect("equal", adjustable="box")
        ax.set_title("Phase-conjugate mirror" if conjugate else "Ordinary flat mirror", pad=29)
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("x (geometric units)")
    fig.text(0.285, 0.12, "Return at z = 0: x = −1.5, 0, 1.5", ha="center")
    fig.text(0.775, 0.12, "Every ideal return ray reaches the source", ha="center")
    fig.suptitle("Reversing the entire wavevector retraces the ray", y=0.98, fontsize=15)
    fig.text(0.5, 0.035, "Blue solid: outward rays and wavefronts    •    Colored dashed: return rays and wavefronts",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.23, top=0.77, wspace=0.23)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
