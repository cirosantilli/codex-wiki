"""Equatorial shallow-water dispersion; write a PNG to the working directory."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k = np.linspace(-4, 4, 801)
    yanai = (k + np.sqrt(k * k + 4)) / 2
    fig, ax = plt.subplots(figsize=(9.5, 4.4), dpi=100, facecolor="white")
    for n, color in [(1, "#888888"), (2, "#bdbdbd")]:
        branches = np.full((3, len(k)), np.nan)
        for i, kk in enumerate(k):
            roots = np.sort(np.roots([1, 0, -(kk * kk + 2 * n + 1), -kk]).real)
            roots[roots <= 0] = np.nan
            branches[:, i] = roots
        for j, branch in enumerate(branches):
            ax.plot(k, branch, color=color, lw=1.4,
                    label=rf"Higher trapped modes $n={n}$" if j == 2 else None)
    ax.plot(k, yanai, color="#1766aa", lw=2.5, label="Yanai")
    kp = np.linspace(0, 4, 300)
    ax.plot(kp, kp, color="#d87922", lw=2.5, label="Kelvin")
    ax.axhline(0.5, color="#38966b", ls="--", lw=1.5, label=r"Forcing $W=1/2$")
    for point, label, offset in [(-1.5, "Yanai: energy eastward", (-110, 35)),
                                 (0.5, "Kelvin: energy eastward", (25, 35))]:
        ax.scatter([point], [0.5], color="black", zorder=5, s=30)
        ax.annotate(label, (point, .5), xytext=offset, textcoords="offset points",
                    fontsize=10, arrowprops={"arrowstyle": "->", "color": "black"})
    ax.set(xlim=(-4, 4), ylim=(0, 2.6), xlabel=r"Zonal wavenumber $K=k\sqrt{c/\beta}$",
           ylabel=r"Positive frequency $W=\omega/\sqrt{\beta c}$",
           title="A westward phase can carry wave energy eastward")
    ax.grid(alpha=.2)
    ax.legend(frameon=False, fontsize=9, loc="upper left")
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
