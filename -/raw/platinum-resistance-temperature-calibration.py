"""Original illustrative Pt100 response and two-point calibration; no measured data.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from the media directory; output uses this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained")
    temperature = np.linspace(0, 50, 201)
    ax = axes[0]
    ax.plot(temperature, 100 * (1 + 0.00385 * temperature), color="#226a9e", lw=2.5)
    for t, label, offset in [(0, "0 °C → 100 Ω", (9, 10)),
                             (25, "25 °C → 109.625 Ω", (-68, 20)),
                             (50, "50 °C → 119.25 Ω", (-130, -28))]:
        resistance = 100 * (1 + 0.00385 * t)
        ax.plot(t, resistance, "o", color="#226a9e", ms=6)
        ax.annotate(label, (t, resistance), xytext=offset,
                    textcoords="offset points", fontsize=10)
    ax.set(title="Chosen nominal local model", xlabel="Celsius temperature t (°C)",
           ylabel="Element resistance R (Ω)", xlim=(-3, 53), ylim=(98, 123))
    ax.text(0.04, 0.89, "R = 100 Ω (1 + αt)\nα = 0.00385 / °C",
            transform=ax.transAxes, fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "#d5d5d5", "pad": 7})
    ax.grid(alpha=0.2)

    ax = axes[1]
    nominal = 100 + 0.385 * temperature
    fitted = 100.20 + 0.388 * temperature
    # Residuals relative to the nominal model reveal small differences clearly.
    ax.plot(temperature, fitted - nominal, color="#8d4f96", lw=2,
            label="Line through two stipulated points")
    ax.axhline(0, color="#226a9e", ls="--", label="Chosen nominal model")
    ax.scatter([0, 50], [0.20, 0.35], color="#8d4f96", s=50, zorder=4,
               label="Fit points: 100.20 Ω, 119.60 Ω")
    check_t, check_r = 25, 110.10
    fit_at_check = 100.20 + 0.388 * check_t
    check_residual = check_r - (100 + 0.385 * check_t)
    fit_residual = fit_at_check - (100 + 0.385 * check_t)
    ax.scatter([check_t], [check_residual], marker="s", s=70,
               facecolors="white", edgecolors="#b45920", linewidths=2,
               zorder=5, label="Independent stipulated check: 110.10 Ω")
    ax.annotate("", (check_t, check_residual), (check_t, fit_residual),
                arrowprops={"arrowstyle": "<->", "color": "#b45920", "lw": 1.5})
    ax.text(27, 0.37, "+0.20 Ω\nfrom fitted line", color="#984813", fontsize=10)
    ax.set(title="Separate synthetic calibration", xlabel="Reference temperature (°C)",
           ylabel="R − chosen nominal model (Ω)", xlim=(-3, 53), ylim=(-0.07, 0.68))
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left", fontsize=8.5, framealpha=1)
    fig.suptitle("Resistance becomes temperature only through a stated response", fontsize=14)
    fig.supxlabel("All lines and points are illustrative calculations, not measurements.",
                  fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
