"""Plot a constructed two-phase Gibbs free-energy difference.

Writes an opaque white PNG with this script's basename in the working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    temperature = np.linspace(260.0, 340.0, 321)
    difference = 12.0 - 0.040 * temperature
    samples = np.array([280.0, 300.0, 320.0])
    values = 12.0 - 0.040 * samples
    assert np.allclose(values, [0.8, 0.0, -0.8])
    assert np.isclose(12.0 / 0.040, 300.0)

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.0, 4.7), dpi=130)
    fig.subplots_adjust(left=0.13, right=0.96, bottom=0.22, top=0.80)
    fig.suptitle("Two phases: enthalpy favors A, entropy favors B", fontsize=15)
    fig.text(0.5, 0.865, "Fixed pressure; illustrative constants over a limited window",
             ha="center", fontsize=11, color="#444444")
    blue, orange = "#236a9e", "#b6532b"
    ax.axvspan(260, 300, color=blue, alpha=0.07)
    ax.axvspan(300, 340, color=orange, alpha=0.07)
    ax.axhline(0.0, color="#555555", lw=1.2)
    ax.axvline(300.0, color="#666666", ls="--", lw=1.0)
    ax.plot(temperature, difference, color="#324d73", lw=2.6)
    ax.scatter(samples, values, c=[blue, "#333333", orange], s=55, zorder=3)
    ax.annotate("280 K: +0.8", (280, 0.8), xytext=(268, 1.25), fontsize=11,
                arrowprops={"arrowstyle": "-", "color": blue}, color=blue)
    ax.annotate("300 K: equal", (300, 0), xytext=(304, 0.40), fontsize=11,
                arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.annotate("320 K: −0.8", (320, -0.8), xytext=(308, -1.35), fontsize=11,
                arrowprops={"arrowstyle": "-", "color": orange}, color=orange)
    ax.text(277, -1.10, "A has lower G", ha="center", color=blue)
    ax.text(324, 1.10, "B has lower G", ha="center", color=orange)
    ax.set(xlim=(260, 340), ylim=(-1.75, 1.75), xlabel="Temperature T (K)",
           ylabel=r"Molar difference $G_B-G_A$ (kJ mol$^{-1}$)")
    ax.set_xticks([260, 280, 300, 320, 340])
    ax.set_yticks([-1.6, -0.8, 0, 0.8, 1.6])
    fig.text(0.5, 0.04, "ΔH = 12 kJ/mol; ΔS = 0.040 kJ/(mol K)   •   ΔG = ΔH − TΔS\n"
             "Thermodynamic preference supplies no conversion timescale.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
