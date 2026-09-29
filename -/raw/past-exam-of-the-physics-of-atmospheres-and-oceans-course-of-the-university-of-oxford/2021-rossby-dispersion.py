"""Original dimensionless Rossby isofrequency circles; Python 3.14, numpy, matplotlib."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7.5, 5.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    t = np.linspace(0.015, 2 * np.pi - 0.015, 900)
    for omega, color in zip((0.30, 0.50, 0.80, 1.20), ("#28639a", "#318472", "#ba613c", "#78579b")):
        radius = 1 / (2 * omega)
        k, ell = radius * (np.cos(t) - 1), radius * np.sin(t)
        ax.plot(k, ell, color=color, lw=2, label=fr"$\omega={omega:.2f}$")
        for angle in (np.pi / 3, np.pi, 5 * np.pi / 3):
            kk, ll = radius * (np.cos(angle) - 1), radius * np.sin(angle)
            vx, vy = kk * kk - ll * ll, 2 * kk * ll
            norm = np.hypot(vx, vy)
            dx, dy = 0.18 * vx / norm, 0.18 * vy / norm
            ax.annotate("", xy=(kk + dx / 2, ll + dy / 2), xytext=(kk - dx / 2, ll - dy / 2), arrowprops={"arrowstyle": "-|>", "color": color, "lw": 1.7, "mutation_scale": 14})
    kk = np.linspace(-3.6, 0, 100)
    ax.plot(kk, kk, "--", color="#888888", lw=1)
    ax.plot(kk, -kk, "--", color="#888888", lw=1, label="$|k|=|l|$")
    ax.axhline(0, color="#777777", lw=0.8)
    ax.axvline(0, color="#777777", lw=0.8)
    ax.plot(0, 0, "o", mfc="white", mec="black", ms=6, zorder=10)
    ax.text(-3.2, 0.16, "$c_{gx}>0$", fontsize=12)
    ax.text(-0.55, 1.65, "$c_{gx}<0$", fontsize=12)
    ax.set(xlim=(-3.65, 0.25), ylim=(-1.95, 1.95), xlabel="Zonal wavenumber $k$ (scaled)", ylabel="Meridional wavenumber $l$ (scaled)", title="Contours of positive frequency; arrows show group direction", aspect="equal")
    ax.legend(loc="lower left", framealpha=1, fontsize=10)
    ax.grid(alpha=0.15)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
