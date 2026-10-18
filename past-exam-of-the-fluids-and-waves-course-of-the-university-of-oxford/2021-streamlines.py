"""Draw the instantaneous streamlines in Oxford A10 (2021), question 1(a).

Run from the desired output directory. Tested with Python 3.14.4 and the
NumPy/Matplotlib versions in the repository's root pyproject.toml.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = 0.35
    x = np.linspace(-2.1, 2.1, 501)
    y = np.linspace(-2.6, 2.6, 541)
    xx, yy = np.meshgrid(x, y)
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 4.4), facecolor="white")
    for ax, omega, caption in zip(
        axes,
        (1.8, 0.6),
        (r"$\Omega=1.8$: ellipses", r"$\Omega=0.6$: hyperbolas"),
    ):
        psi = omega * (np.exp(2 * t) * xx**2 + np.exp(-2 * t) * yy**2) / 2 - xx * yy
        if omega > 1:
            ax.contour(xx, yy, psi, levels=(0.12, 0.3, 0.6, 1.0, 1.5), colors="#176b93", linewidths=1.5)
        else:
            ax.contour(xx, yy, psi, levels=(-0.9, -0.4, -0.12), colors="#b4591c", linestyles="solid", linewidths=1.5)
            ax.contour(xx, yy, psi, levels=(0.12, 0.4, 0.9), colors="#176b93", linewidths=1.5)
            ax.contour(xx, yy, psi, levels=(0,), colors="#5a476f", linewidths=1.8)
        # Arrows tangent to the same frozen velocity field, of equal drawn length.
        for px, py in ((0.0, 1.2), (0.0, -1.2), (0.75, 0.0), (-0.75, 0.0)):
            vx = -px + omega * np.exp(-2 * t) * py
            vy = py - omega * np.exp(2 * t) * px
            norm = np.hypot(vx, vy)
            vx, vy = 0.29 * vx / norm, 0.29 * vy / norm
            ax.annotate("", xy=(px + vx / 2, py + vy / 2), xytext=(px - vx / 2, py - vy / 2), arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.5})
        ax.plot(0, 0, "o", color="black", ms=4)
        ax.axhline(0, color="0.8", lw=0.6, zorder=0)
        ax.axvline(0, color="0.8", lw=0.6, zorder=0)
        ax.set(xlim=(-2.1, 2.1), ylim=(-2.6, 2.6), xlabel="$x$", ylabel="$y$", title=caption)
        ax.set_aspect("equal")
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
    axes[1].text(0.03, 0.03, "Purple: straight separatrices", transform=axes[1].transAxes, fontsize=9, color="#5a476f", bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    fig.suptitle(r"Instantaneous streamlines at $t=0.35$", fontsize=13)
    fig.tight_layout()
    fig.savefig("2021-streamlines.png", dpi=150, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
