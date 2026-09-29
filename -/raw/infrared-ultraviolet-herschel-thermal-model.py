"""Original Herschel-style schematic and illustrative lumped thermal model.

Run from _media with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The diagram is not a historical reconstruction or a measured spectral curve.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
import numpy as np


def excess_temperature(time, absorbed_power, capacity=0.020, loss=0.001,
                       shutter_time=60.0):
    """Kelvin above fixed ambient; a constant beam is blocked at shutter_time."""
    tau = capacity / loss
    illuminated = absorbed_power / loss * (-np.expm1(-time / tau))
    at_shutter = absorbed_power / loss * (-np.expm1(-shutter_time / tau))
    cooling = at_shutter * np.exp(-(time - shutter_time) / tau)
    return np.where(time <= shutter_time, illuminated, cooling)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(9.3, 7.4), layout="constrained")
    schematic, model = fig.subplots(2, 1, gridspec_kw={"height_ratios": [1.0, 1.05]})
    fig.suptitle("Beyond visible red: detection by heating", fontsize=17)
    schematic.set(xlim=(0, 10), ylim=(0, 5))
    schematic.axis("off")
    schematic.set_title("A. Experiment logic — schematic, not to scale", loc="left")
    schematic.add_patch(Polygon([(2.5, 3.5), (3.2, 4.4), (3.5, 3.1)],
                                facecolor="#e1edf3", edgecolor="#345466", lw=1.8))
    schematic.annotate("", (2.8, 3.7), (0.5, 3.7),
                       arrowprops={"arrowstyle": "->", "lw": 2, "color": "#61594e"})
    schematic.text(0.5, 4.05, "Sunlight")
    schematic.text(2.5, 4.63, "Glass prism")
    schematic.add_patch(Rectangle((4.1, 0.9), 5.5, 0.30,
                                  facecolor="white", edgecolor="#88949a", lw=1.5))
    for x, color in [(4.7, "#654aab"), (5.05, "#315da8"), (5.4, "#1a805b"),
                     (5.75, "#b89d10"), (6.1, "#cb7b23"), (6.45, "#b23638")]:
        schematic.plot([3.25, x], [3.45, 1.2], color=color, lw=2)
        schematic.add_patch(Rectangle((x - 0.17, 0.95), 0.34, 0.23,
                                      color=color, alpha=0.8))
    schematic.plot([3.25, 7.6], [3.45, 1.2], "--", color="#7b4d36", lw=2)
    schematic.text(5.25, 0.50, "Visible spectrum", ha="center")
    schematic.text(4.48, 1.45, "Violet", color="#654aab", fontsize=10)
    schematic.text(6.25, 1.45, "Red", color="#b23638", fontsize=10)
    schematic.text(7.4, 0.45, "Beyond red", ha="center", color="#7b4d36")
    schematic.text(6.2, 3.6, "Dashed ray: infrared\n(no visible color here)",
                   color="#7b4d36", ha="center")
    for x in [7.6, 9.1]:
        schematic.add_patch(Circle((x, 1.22), 0.13, color="#23272b"))
        schematic.plot([x, x], [1.32, 2.22], color="#23272b", lw=3)
    schematic.text(7.15, 2.35, "Blackened bulb\nmeasures warming", ha="center")
    schematic.text(9.12, 2.9, "Shaded ambient\nreference*", ha="center")
    schematic.annotate("", (9.1, 2.22), (9.1, 2.75),
                       arrowprops={"arrowstyle": "->", "color": "#54616a"})
    schematic.text(0.05, 0.04, "*Suggested modern control; not a claim about Herschel's layout.",
                   fontsize=10, color="#46545f")

    time = np.linspace(0, 120, 1201)
    for power, color in [(0.0010, "#784b2e"), (0.0005, "#176b88")]:
        model.plot(time, excess_temperature(time, power), color=color, lw=2.5,
                   label=f"Absorbed power = {power * 1000:.1f} mW")
    model.axvline(60, color="#65727a", linestyle="--", lw=1.4)
    model.text(63, 0.82, "Beam blocked\nCooling begins", color="#46545f")
    model.set(xlim=(0, 120), ylim=(0, 1.08), xlabel="Time (s)",
              ylabel="Bulb temperature above ambient (K)")
    model.set_title("B. Analytical model — illustrative parameters, no measured data", loc="left")
    model.grid(alpha=0.20)
    model.legend(loc="upper left", frameon=False)
    model.text(0.98, 0.06, "C = 0.020 J/K     G = 0.0010 W/K\n"
               r"$\tau=C/G=20$ s; $C\,d\theta/dt=P_{\rm abs}-G\theta$",
               transform=model.transAxes, ha="right", fontsize=10,
               bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.95})
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
