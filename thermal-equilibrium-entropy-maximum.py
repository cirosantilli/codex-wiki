"""Plot the total entropy change along a fixed-energy temperature constraint.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes the matching PNG into the current working directory.
Entropy is relative to the initial 300 K, 400 K state; values are stipulated.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    c1, c2 = 1.0, 3.0  # whole-body constant-volume heat capacities, kJ/K
    initial1, initial2 = 300.0, 400.0  # K
    energy = c1 * initial1 + c2 * initial2  # relative internal energy, kJ
    temp1 = np.linspace(250.0, 500.0, 1001)
    temp2 = (energy - c1 * temp1) / c2
    entropy = c1 * np.log(temp1 / initial1) + c2 * np.log(temp2 / initial2)
    final = energy / (c1 + c2)
    maximum = c1 * np.log(final / initial1) + c2 * np.log(final / initial2)
    assert np.all(temp1 > 0) and np.all(temp2 > 0)
    assert np.allclose(c1 * temp1 + c2 * temp2, energy)
    assert temp1[np.argmax(entropy)] == final

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.2, 5.0), dpi=120)
    fig.subplots_adjust(left=0.13, right=0.96, bottom=0.24, top=0.82)
    fig.suptitle("Thermal equilibrium maximizes total entropy", fontsize=15)
    ax.plot(temp1, entropy, color="#216a99", lw=2.7)
    ax.axhline(0, color="#777777", lw=1, linestyle=":")
    ax.axvline(final, color="#24765c", lw=1, linestyle="--")
    ax.scatter([initial1, final], [0, maximum], c=["#b8531c", "#24765c"], s=35, zorder=4)
    ax.annotate("Initial state\nT₁ = 300 K, T₂ = 400 K", (initial1, 0),
                xytext=(272, -0.039), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#b8531c"})
    ax.annotate("Maximum: T₁ = T₂ = 375 K\nΔS = 0.02952799 kJ/K", (final, maximum),
                xytext=(385, -0.012), fontsize=10, color="#24765c",
                arrowprops={"arrowstyle": "->", "color": "#24765c"})
    start, end = 321.0, 350.0
    def curve(t):
        return c1 * np.log(t / initial1) + c2 * np.log(((energy - c1 * t) / c2) / initial2)
    ax.annotate("", (end, curve(end)), xytext=(start, curve(start)),
                arrowprops={"arrowstyle": "->", "color": "#b8531c", "lw": 2,
                            "connectionstyle": "arc3,rad=-0.1"})
    ax.set(xlim=(250, 500), ylim=(-0.075, 0.045),
           xlabel="Body 1 temperature T₁ (K)", ylabel="Total entropy change ΔS (kJ/K)")
    ax.set_xticks([250, 300, 350, 375, 400, 450, 500])
    ax.grid(alpha=0.18)
    fig.text(0.5, 0.125, "Fixed relative energy: T₂ = (1500 − T₁)/3 (temperatures in K)",
             ha="center", fontsize=10)
    fig.text(0.5, 0.07, "C₁ = 1 kJ/K; C₂ = 3 kJ/K; orange arrow follows the relaxation",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025, "Only 250–500 K shown; positive-temperature model domain: 0 < T₁ < 1500 K",
             ha="center", fontsize=9, color="#555555")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Entropy maximum at T1=T2={final:g} K; delta S={maximum:.12f} kJ/K")


if __name__ == "__main__":
    main()
