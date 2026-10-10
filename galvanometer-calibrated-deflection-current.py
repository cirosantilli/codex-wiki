"""Plot an illustrative calibration; Python 3.14, matplotlib 3.10.7, NumPy 2.3.5."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    turns, area, field, stiffness = 120, 3.00e-4, 0.250, 3.00e-6
    sensitivity = turns * area * field / stiffness
    current = np.linspace(-60, 60, 481)  # microamperes
    degrees = np.rad2deg(sensitivity * current * 1e-6)
    resolution = 0.10  # chosen readout tolerance, not measured noise
    unresolved_current = np.deg2rad(resolution) / sensitivity * 1e6
    fig, ax = plt.subplots(figsize=(8.6, 5.3))
    ax.plot(current, degrees, color="#2166ac", lw=2, label="Calculated linear calibration")
    selected = np.array([-40, -20, 0, 20, 40])
    ax.scatter(selected, np.rad2deg(sensitivity * selected * 1e-6), s=42,
               color="#2166ac", zorder=3, label="Illustrative settings (not measurements)")
    ax.axhspan(-resolution, resolution, color="#e5c565", alpha=0.65,
               label="Chosen ±0.10° zero tolerance")
    ax.axhline(0, color="#666666", linewidth=0.8)
    ax.axvline(0, color="#666666", linewidth=0.8)
    ax.axvline(-60, ls=":", color="#777777")
    ax.axvline(60, ls=":", color="#777777")
    ax.set(xlim=(-65, 65), ylim=(-11.4, 11.4),
           xlabel="Signed coil current I (µA)", ylabel="Settled deflection θ (degrees)",
           title="Moving-coil deflection: calibration and reversal")
    ax.set_xticks(np.arange(-60, 61, 20))
    ax.grid(alpha=0.18)
    ax.annotate("+40 µA → +6.88°", xy=(40, np.rad2deg(0.12)), xytext=(12, 9.5),
                arrowprops={"arrowstyle": "->", "color": "#2166ac"}, color="#2166ac")
    ax.annotate("−40 µA → −6.88°", xy=(-40, -np.rad2deg(0.12)), xytext=(-55, -10.2),
                arrowprops={"arrowstyle": "->", "color": "#2166ac"}, color="#2166ac")
    ax.legend(loc="upper left", fontsize=9, framealpha=1)
    inset = ax.inset_axes([0.63, 0.12, 0.33, 0.31])
    near_zero = np.linspace(-1.5, 1.5, 101)
    inset.axhspan(-resolution, resolution, color="#e5c565", alpha=0.65)
    inset.plot(near_zero, np.rad2deg(sensitivity * near_zero * 1e-6), color="#2166ac", lw=2)
    for value in [-unresolved_current, unresolved_current]:
        inset.axvline(value, color="#84691d", ls="--", lw=1)
    inset.axhline(0, color="#666666", lw=0.7)
    inset.axvline(0, color="#666666", lw=0.7)
    inset.set(xlim=(-1.5, 1.5), ylim=(-0.26, 0.26),
              title="Zero band: ±0.582 µA", xlabel="I (µA)", ylabel="θ (°)")
    inset.set_xticks([-1, 0, 1])
    inset.set_yticks([-0.2, 0, 0.2])
    inset.tick_params(labelsize=8)
    inset.xaxis.label.set_size(9)
    inset.yaxis.label.set_size(9)
    inset.title.set_size(10)
    fig.text(0.5, 0.048, "N = 120   A = 3.00 × 10⁻⁴ m²   B = 0.250 T   k = 3.00 × 10⁻⁶ N m/rad",
             ha="center", fontsize=10)
    fig.text(0.5, 0.014, "Sᵢ = 3000 rad/A • chosen full scale: ±0.180 rad at ±60 µA • model, not experimental data",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.10, right=0.98, top=0.89, bottom=0.19)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
