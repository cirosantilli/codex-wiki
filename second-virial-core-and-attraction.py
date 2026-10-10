"""Hard-sphere exclusion and an exactly integrable square-well toy potential.

No experimental data. The plot uses range multiplier a = 3/2.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../second-virial-core-and-attraction.py
The PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12, "axes.labelsize": 11})
    fig = plt.figure(figsize=(9.8, 6.5), facecolor="white")
    grid = fig.add_gridspec(2, 2, left=0.09, right=0.96, bottom=0.23, top=0.85, hspace=0.58, wspace=0.36)
    geometry = fig.add_subplot(grid[0, 0])
    mayer = fig.add_subplot(grid[0, 1])
    coefficient = fig.add_subplot(grid[1, :])
    fig.suptitle("From excluded centres to temperature-dependent pressure", fontsize=14, y=0.97)
    fig.text(0.5, 0.92, "Three-dimensional hard-core geometry + square-well toy model (no measured data)", ha="center", fontsize=11)

    geometry.set_title("A. Diameter is the contact separation", pad=10)
    geometry.add_patch(Circle((0, 0), 1, facecolor="#fbeee1", edgecolor="#c36a20", ls="--", lw=1.8))
    geometry.add_patch(Circle((0, 0), 0.5, facecolor="#b5cfe3", edgecolor="#21669c", lw=1.6))
    geometry.add_patch(Circle((1, 0), 0.5, facecolor="#dce9f2", edgecolor="#21669c", lw=1.6))
    geometry.plot([0, 1], [0, 0], "o", color="#1c3c55", markersize=4)
    geometry.annotate("", xy=(1, -0.27), xytext=(0, -0.27), arrowprops={"arrowstyle": "<->", "color": "#1c3c55"})
    geometry.text(0.50, -0.43, r"$\sigma$", ha="center", fontsize=12)
    geometry.annotate("forbidden second centres\n" + r"inside radius $\sigma$", xy=(-0.78, 0.55), xytext=(-1.32, 1.1), fontsize=9, arrowprops={"arrowstyle": "->", "color": "#c36a20"})
    geometry.text(1, 0.65, r"radius $\sigma/2$", ha="center", fontsize=10)
    geometry.text(0.25, -1.22, "Cross-section: particles touch at separation r = σ", ha="center", fontsize=9)
    geometry.set(xlim=(-1.5, 1.9), ylim=(-1.4, 1.4), aspect="equal")
    geometry.axis("off")

    a = 1.5
    example_temperature = 2.0
    f_shell = np.expm1(1 / example_temperature)
    mayer.set_title("B. Mayer function at $T^*=2$", pad=10)
    mayer.axhline(0, color="#777777", lw=1)
    mayer.fill_between([0, 1], -1, 0, color="#c36a20", alpha=0.18)
    mayer.fill_between([1, a], 0, f_shell, color="#21669c", alpha=0.18)
    mayer.plot([0, 1], [-1, -1], color="#c36a20", lw=2.5)
    mayer.plot([1, a], [f_shell, f_shell], color="#21669c", lw=2.5)
    mayer.plot([a, 2.1], [0, 0], color="#444444", lw=2)
    mayer.vlines([1, a], [-1, 0], [f_shell, f_shell], color="#777777", ls=":", lw=1.2)
    mayer.text(0.38, -0.70, "core", color="#925018", ha="center")
    mayer.text(1.25, 0.28, "shell", color="#21669c", ha="center", fontsize=10)
    mayer.text(1.66, 0.78, "$f=0$\noutside", ha="center", fontsize=10)
    mayer.set(xlim=(0, 2.1), ylim=(-1.2, 1.15), xlabel=r"$r/\sigma$", ylabel="$f=e^{-u/(k_BT)}-1$")
    mayer.set_xticks([0, 1, a, 2], ["0", "1", "1.5", "2"])
    mayer.grid(alpha=0.15)

    temperatures = np.linspace(1, 8, 500)
    normalized_b2 = 1 - (a**3 - 1)*np.expm1(1/temperatures)
    zero_temperature = 1 / np.log1p(1 / (a**3 - 1))
    coefficient.set_title("C. Shell attraction weakens on heating: exact toy integral", pad=10)
    coefficient.plot(temperatures, normalized_b2, color="#21669c", lw=2.4, label="square well: $a=3/2$")
    coefficient.axhline(1, color="#c36a20", lw=1.8, ls="--", label=r"hard spheres: $B_2/b_{\mathrm{HS}}=1$")
    coefficient.axhline(0, color="#777777", lw=1)
    coefficient.plot([zero_temperature], [0], "o", color="#21669c", markersize=5)
    coefficient.annotate(f"zero at $T^*$ ≈ {zero_temperature:.3f}", xy=(zero_temperature, 0), xytext=(3.65, -1.30), arrowprops={"arrowstyle": "->", "color": "#21669c"}, fontsize=10)
    coefficient.set(xlim=(1, 8), ylim=(-3.5, 1.45), xlabel=r"$T^*=k_BT/\epsilon$", ylabel=r"$B_2/b_{\mathrm{HS}}$")
    coefficient.grid(alpha=0.18)
    coefficient.legend(loc="lower right", fontsize=10, facecolor="white", framealpha=1)
    fig.text(0.5, 0.055, r"$b_{\mathrm{HS}}=2\pi\sigma^3/3=4$ particle volumes.  $B_2=-2\pi\int_0^\infty f(r)r^2\,dr$ weights spherical shells.", ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
