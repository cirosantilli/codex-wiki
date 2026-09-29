"""Original illustrative curve and synthetic fit, not measured data or transport.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
"""

from math import erf, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def cdf(values):
    return np.array([.5 * (1 + erf(float(v) / sqrt(2))) for v in values])


def collection(voltage, spacing=4.9, offset=1.2, retarder=1.0, sigma=.18):
    """Convolve the periodically extended accepted intervals with Gaussian jitter."""
    x = np.asarray(voltage) - offset
    total = np.zeros_like(x)
    for k in range(-5, 15):
        total += cdf((x - k * spacing - retarder) / sigma)
        total -= cdf((x - (k + 1) * spacing) / sigma)
    return total


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(11, 6))
    grid = fig.add_gridspec(2, 2, width_ratios=[1.23, 1], height_ratios=[2, 1],
                           left=.075, right=.975, bottom=.12, top=.84, wspace=.3, hspace=.13)
    curve = fig.add_subplot(grid[:, 0])
    fit = fig.add_subplot(grid[0, 1])
    residual = fig.add_subplot(grid[1, 1], sharex=fit)
    fig.suptitle("Repeated loss sets a spacing; collection and offsets set the phase", fontsize=15, y=.97)
    fig.text(.5, .9, "Chosen analytical curve and independent synthetic positions — no experimental data",
             ha="center", color="#555555", fontsize=11)
    voltage = np.linspace(4.5, 28, 3200)
    curve.plot(voltage, collection(voltage), color="#226b98", lw=2)
    centers = 1.2 + np.arange(1, 6) * 4.9 + .5
    for v in centers:
        curve.axvline(v, color="#b8c4cb", lw=.8, ls=":", zorder=0)
    curve.annotate("", (centers[2], .48), (centers[1], .48),
                   arrowprops={"arrowstyle": "<->", "color": "#943e6b", "lw": 1.8})
    curve.text((centers[1] + centers[2]) / 2, .53, "4.9 V", ha="center", color="#943e6b")
    curve.text(21.5, .24, "Trough center\n" + r"$V_c+nd+V_r/2$", ha="center",
               bbox={"facecolor": "white", "edgecolor": "none", "alpha": .93, "pad": 3})
    curve.set(xlim=(4.5, 28), ylim=(-.04, 1.08), xlabel="Accelerating voltage V (V)",
              ylabel=r"Collected fraction $I/I_0$", title="Gaussian-smoothed reset + retarder rule")
    curve.text(.02, .93, r"$V_r=1.0$ V; $\sigma=0.18$ V", transform=curve.transAxes, fontsize=10)
    n = np.arange(1, 6)
    positions = np.array([6.62, 11.46, 16.48, 21.30, 26.14])
    slope, intercept = np.polyfit(n, positions, 1)
    errors = positions - intercept - slope * n
    fit.plot(n, intercept + slope * n, color="#217349", lw=1.7, label="Least squares line")
    fit.scatter(n, positions, color="#943e6b", s=32, zorder=3, label="Synthetic troughs")
    fit.set(ylabel="Trough voltage (V)", title="Fit positions, retain an intercept")
    fit.legend(loc="upper left", frameon=False, fontsize=9)
    fit.text(.96, .12, f"d = {slope:.3f} V\nb = {intercept:.3f} V", ha="right",
             transform=fit.transAxes, color="#217349", fontsize=11)
    fit.tick_params(labelbottom=False)
    residual.axhline(0, color="#777777", lw=1)
    residual.vlines(n, 0, errors, color="#943e6b", lw=1.5)
    residual.scatter(n, errors, color="#943e6b", s=24, zorder=3)
    residual.set(xlim=(.7, 5.3), ylim=(-.1, .105), xticks=n,
                 xlabel="Successive trough index n", ylabel="Residual (V)")
    for ax in [curve, fit, residual]:
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
