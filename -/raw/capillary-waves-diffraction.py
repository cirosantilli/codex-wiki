"""Original schematic and stipulated prediction for capillary-wave metrology.

Apparatus ingredients are documented by Zhu et al., AJP 75 (2007), 896–898,
doi:10.1119/1.2750379. This is not a tracing, data reproduction, or fitted curve.
Run from _media:
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../capillary-waves-diffraction.py
Tested: Python 3.14.4, matplotlib 3.10.7+dfsg1, numpy 2.3.5.
The matching opaque white PNG basename is written to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import ScalarFormatter
import numpy as np


def arrow(ax, start, end, color="#45505a", width=1.6):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": width})


def main():
    gamma, rho, g, depth = 0.072, 1000.0, 9.81, 0.030
    wavelength_mm = np.geomspace(1, 30, 700)
    k = 2 * np.pi / (wavelength_mm / 1000)
    f_deep = np.sqrt(g * k + gamma * k**3 / rho) / (2 * np.pi)
    f_capillary = np.sqrt(gamma * k**3 / rho) / (2 * np.pi)
    f_depth = f_deep * np.sqrt(np.tanh(k * depth))
    assert np.max(abs(f_depth / f_deep - 1)) < 4e-6

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (setup, prediction) = plt.subplots(1, 2, figsize=(10.8, 5.3),
                                           gridspec_kw={"width_ratios": [1.5, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Measure a ripple without touching the observed wave", fontsize=17,
                 weight="bold", y=0.97)
    fig.text(0.5, 0.90, "Original apparatus schematic + ideal prediction • no experimental points or fitted results",
             ha="center", fontsize=10)
    setup.set_xlim(0, 7.1)
    setup.set_ylim(-0.65, 5.05)
    setup.axis("off")
    setup.set_title("Drive frequency in; optical wavelength out", fontsize=12, pad=12)

    setup.add_patch(Rectangle((0.25, 0.25), 6.2, 1.42, facecolor="#eaf3fa", edgecolor="none"))
    setup.plot([0.25, 0.25, 6.45, 6.45], [1.7, 0.25, 0.25, 1.7], color="#45505a", lw=2)
    x = np.linspace(0.25, 6.45, 700)
    y = 1.67 + 0.07 * np.sin(2 * np.pi * (x - 0.3) / 0.55)
    setup.plot(x, y, color="#1765a8", lw=1.7)
    setup.text(3.4, 0.84, "Temperature-controlled liquid bath", ha="center", fontsize=10)
    setup.annotate("", xy=(0.62, 1.65), xytext=(0.62, 0.3),
                   arrowprops={"arrowstyle": "<->", "color": "#45505a"})
    setup.text(0.85, 0.97, "h = 30 mm", fontsize=9)
    setup.text(3.4, -0.12, "Isolation from ambient vibration", ha="center", fontsize=10)
    setup.text(3.4, -0.48, "Not to scale; ray angles and wave height exaggerated", ha="center", fontsize=9,
               color="#53616e")

    setup.add_patch(Rectangle((0.18, 3.7), 1.65, 0.65, facecolor="white", edgecolor="#45505a"))
    setup.text(1.005, 4.025, "Sinusoidal drive\nfrequency f", ha="center", va="center", fontsize=10)
    arrow(setup, (1.0, 3.67), (1.0, 2.90))
    setup.plot([1.0, 1.0], [2.18, 1.67], color="#45505a", lw=1.8)
    setup.plot([0.72, 1.28], [1.67, 1.67], color="#45505a", lw=4)
    setup.text(0.95, 2.53, "Oscillating frame\nseen edge-on", fontsize=10, ha="center")
    arrow(setup, (1.35, 1.98), (2.4, 1.98), color="#1765a8")
    setup.text(2.12, 1.46, "ripples →", fontsize=9, color="#1765a8")

    setup.text(2.7, 3.80, "Laser", fontsize=11, ha="center", color="#b32d35")
    setup.text(2.7, 3.45, r"$\lambda_L$ = 632.8 nm", fontsize=10, ha="center", color="#b32d35")
    spot = (3.6, 1.67)
    arrow(setup, (1.85, 2.70), spot, color="#b32d35", width=2)
    setup.text(3.18, 2.45, "grazing\nincidence", fontsize=9, color="#b32d35", ha="center")
    setup.plot([6.35, 6.35], [2.66, 4.0], color="#45505a", lw=3)
    for order, screen_y in [(1, 3.80), (0, 3.30), (-1, 2.80)]:
        arrow(setup, spot, (6.35, screen_y), color="#b32d35", width=1.2)
        setup.plot(6.35, screen_y, "o", color="#b32d35", ms=5)
        setup.text(6.57, screen_y, f"{order:+d}" if order else "0", fontsize=10, va="center")
    setup.text(5.77, 4.24, "Screen / camera", fontsize=10, ha="center")
    setup.text(5.25, 4.65, "Spot angles determine λ", fontsize=10, ha="center")
    setup.text(4.1, 0.48, "Moving surface acts as a grating", fontsize=9, ha="center")

    prediction.set_facecolor("white")
    prediction.axhspan(100, 290, color="#eaf3fa")
    prediction.loglog(wavelength_mm, f_deep, color="#1765a8", lw=2.5,
                      label="Gravity + surface tension")
    prediction.loglog(wavelength_mm, f_capillary, color="#bf5b13", ls="--", lw=1.8,
                      label="Capillary-only limit")
    prediction.set_xlim(1, 30)
    prediction.set_ylim(5, 900)
    prediction.set_xticks([1, 2, 5, 10, 20, 30])
    prediction.set_yticks([10, 30, 100, 300, 900])
    prediction.xaxis.set_major_formatter(ScalarFormatter())
    prediction.yaxis.set_major_formatter(ScalarFormatter())
    prediction.set_xlabel("Surface wavelength λ (mm)")
    prediction.set_ylabel("Drive frequency f (Hz)")
    prediction.set_title("Prediction to test by sweeping f", fontsize=12, pad=12)
    prediction.text(7.5, 145, "100–290 Hz\ndrive window", fontsize=9, color="#1765a8")
    prediction.grid(alpha=0.18, which="major")
    prediction.legend(loc="upper right", frameon=False, fontsize=9)
    fig.text(0.72, 0.045, "Stipulated: γ = 0.072 N/m, ρ = 1000 kg/m³, g = 9.81 m/s²", ha="center", fontsize=9)
    fig.subplots_adjust(left=0.025, right=0.97, bottom=0.15, top=0.79, wspace=0.22)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
