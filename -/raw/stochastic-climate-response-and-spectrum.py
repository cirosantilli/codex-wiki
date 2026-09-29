"""Original one-box climate curves; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Run from _media to write the matching PNG to the current working directory.
The curves are analytic illustrative calculations, not measured climate data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    heat_capacity = 2.0e8  # J m^-2 K^-1
    restoring = 2.0  # W m^-2 K^-1
    forcing = 4.0  # W m^-2
    noise_strength = 1.0e8  # (W m^-2)^2 s
    tau = heat_capacity / restoring
    variance = noise_strength / (heat_capacity * restoring)
    x = np.linspace(0.0, 5.0, 700)
    mean = forcing / restoring * (-np.expm1(-x))
    spread = np.sqrt(variance * (-np.expm1(-2 * x)))
    w_tau = np.geomspace(0.01, 100, 700)
    spectrum_ratio = 1.0 / (1.0 + w_tau**2)

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 5.5), dpi=100)
    fig.patch.set_facecolor("white")
    fig.suptitle("A slow climate response retains memory of fast forcing", fontsize=18, y=0.97)

    left.fill_between(x, mean - spread, mean + spread, color="#bad6eb", alpha=1,
                      label="Mean ± one standard deviation")
    left.plot(x, mean, color="#145d8a", linewidth=2.5, label="Step-forced mean")
    left.axhline(forcing / restoring, color="#9b5c16", linestyle="--", linewidth=1.4,
                 label="Equilibrium mean: 2 K")
    t_one = forcing / restoring * (1 - np.exp(-1))
    left.plot([1], [t_one], "o", color="#145d8a", markersize=6)
    left.annotate("At one response time:\nmean = 1.264 K", (1, t_one),
                  xytext=(1.48, 0.60), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": "#145d8a"})
    left.set(title="A. A step forcing, starting at exactly zero",
             xlabel=r"Time / response time, $t/\tau$", ylabel="Temperature anomaly (K)",
             xlim=(0, 5), ylim=(-0.15, 2.75))
    left.legend(loc="upper left", fontsize=9, frameon=False)
    left.grid(alpha=0.22)

    right.loglog(w_tau, spectrum_ratio, color="#8f3456", linewidth=2.5)
    right.axvline(1, color="#75808c", linestyle=":", linewidth=1.3)
    right.axhline(0.5, color="#75808c", linestyle=":", linewidth=1.3)
    right.plot([1], [0.5], "o", color="#8f3456")
    right.annotate("Half-power corner\nωτ = 1", (1, 0.5), xytext=(2.7, 0.6), fontsize=10,
                   arrowprops={"arrowstyle": "->", "color": "#8f3456"})
    right.text(0.022, 0.24, "Low-frequency\nplateau", fontsize=11)
    right.text(3.4, 0.0017, "Fast fluctuations\nare suppressed", fontsize=11)
    right.set(title="B. Stationary unforced temperature spectrum",
              xlabel=r"Angular frequency × response time, $|\omega|\tau$",
              ylabel=r"Normalized spectrum, $S_T(\omega)/S_T(0)$",
              xlim=(0.01, 100), ylim=(6e-5, 1.65))
    right.grid(which="both", alpha=0.18)
    fig.text(0.5, 0.075,
             f"Chosen model: τ = {tau / (365.25 * 86400):.2f} years; "
             f"stationary standard deviation = {np.sqrt(variance):.2f} K. "
             "The shaded spread grows from a fixed initial value.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025, "Analytic model curves, not observed climate data.",
             ha="center", fontsize=11, color="#405464")
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.22, top=0.84, wspace=0.30)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
