"""Plot a calculated Boyle-law isotherm and its reciprocal-volume form.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    constant = 10_000.0  # kPa cm³; calculated example, not measured data
    ambient = 100.0  # kPa; stipulated reference for the gauge curve
    volume = np.linspace(30.0, 160.0, 500)
    reciprocal = np.linspace(0.0, 0.035, 500)
    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=100)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.18, top=0.78, wspace=0.29)
    fig.suptitle("Boyle's law: the same states in two coordinates", y=0.97, fontsize=16)
    fig.text(0.5, 0.89, "Fixed amount and absolute temperature  •  pV = 10 000 kPa cm³ = 10 J",
             ha="center", fontsize=12)
    blue, orange = "#17628c", "#b45b16"
    left.plot(volume, constant / volume, color=blue, lw=2.7)
    left.set(xlim=(0, 170), ylim=(0, 360), xlabel="Total gas volume V (cm³)",
             ylabel="Absolute pressure p (kPa)", title="Inverse relation: p = C / V")
    left.set_xticks([0, 50, 100, 150])
    left.set_yticks([0, 100, 200, 300])
    for v, label, xytext in [(100, "A: 100 cm³, 100 kPa", (76, 43)),
                             (50, "B: 50 cm³, 200 kPa", (66, 260))]:
        p = constant / v
        left.scatter([v], [p], color=blue, s=45, zorder=4)
        left.plot([0, v, v], [p, p, 0], color=blue, alpha=0.35, ls=":")
        left.annotate(label, (v, p), xytext=xytext, textcoords="data",
                      arrowprops={"arrowstyle": "->", "color": blue}, fontsize=10)
    right.plot(reciprocal, constant * reciprocal, color=blue, lw=2.7,
               label="Absolute p = C (1/V)")
    right.plot(reciprocal, constant * reciprocal - ambient, color=orange,
               lw=2, ls="--", label="Gauge p = C (1/V) − 100 kPa")
    right.scatter([0.01, 0.02], [100, 200], color=blue, s=45, zorder=4)
    right.annotate("A", (0.01, 100), xytext=(0.011, 125), color=blue)
    right.annotate("B", (0.02, 200), xytext=(0.021, 215), color=blue)
    right.scatter([0], [-100], color=orange, s=35, zorder=4, clip_on=False)
    right.set(xlim=(0, 0.035), ylim=(-120, 360), xlabel="Reciprocal total volume 1/V (cm⁻³)",
              ylabel="Pressure (kPa)", title="Straight lines: reference changes intercept")
    right.set_xticks([0, 0.01, 0.02, 0.03], ["0", "0.010", "0.020", "0.030"])
    right.set_yticks([-100, 0, 100, 200, 300])
    right.axhline(0, color="#777777", lw=0.8)
    right.legend(loc="upper left", fontsize=9, framealpha=1)
    for ax in (left, right):
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.04, "Calculated curves, not experimental data; the origin on the right is an extrapolation.",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
