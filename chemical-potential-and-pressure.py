"""Plot an ideal gas's molar chemical-potential difference and exchange direction.

Writes chemical-potential-and-pressure.png in the current working directory.
Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    gas_constant = 8.314462618  # Stipulated J / (mol K).
    temperature = 300.0  # K.
    ratio = np.linspace(0.18, 4.0, 700)
    blue, orange, green = "#236a9e", "#b6532b", "#267747"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.6, 5.6), dpi=120)
    fig.subplots_adjust(left=0.13, right=0.96, bottom=0.35, top=0.80)
    fig.suptitle("Chemical potential responds to a pressure ratio", fontsize=16, y=0.96)
    fig.text(0.5, 0.875, r"Same ideal gas at a common temperature:  $\Delta\mu_{\rm m}/(RT)=\ln(p_B/p_A)$",
             ha="center", fontsize=12)
    ax.axvspan(0.18, 1.0, color=blue, alpha=0.07)
    ax.axvspan(1.0, 4.0, color=orange, alpha=0.07)
    ax.axhline(0, color="#777777", lw=1)
    ax.axvline(1, color=green, lw=1, ls="--")
    ax.plot(ratio, np.log(ratio), color=blue, lw=2.5)
    ax.scatter([0.5, 1.0], [np.log(0.5), 0], color=[orange, green], s=55, zorder=5)
    delta = -gas_constant * temperature * np.log(2)
    ax.annotate(f"Half the pressure\nAt 300 K: {delta:,.3f} J/mol",
                xy=(0.5, np.log(0.5)), xytext=(1.55, -1.25), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": orange, "lw": 1.4},
                bbox={"boxstyle": "round,pad=0.4", "fc": "white", "ec": orange})
    ax.annotate("Equal chemical potentials", xy=(1, 0), xytext=(1.5, 0.15),
                fontsize=11, color=green,
                arrowprops={"arrowstyle": "->", "color": green})
    ax.set(xlim=(0.18, 4), ylim=(-1.85, 1.55),
           xlabel=r"Pressure ratio $p_B/p_A$",
           ylabel=r"$(\mu_{{\rm m},B}-\mu_{{\rm m},A})/(RT)$")
    ax.set_xticks([0.25, 0.5, 1, 2, 3, 4], ["0.25", "0.5", "1", "2", "3", "4"])
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.215, "Initial transfer through an open valve between rigid compartments",
             ha="center", fontsize=12)
    fig.text(0.27, 0.135, r"$p_B<p_A$:  A $\longrightarrow$ B", ha="center", color=blue, fontsize=14)
    fig.text(0.74, 0.135, r"$p_B>p_A$:  B $\longrightarrow$ A", ha="center", color=orange, fontsize=14)
    fig.text(0.5, 0.055, "At fixed T and compartment volumes, transfer lowers total Helmholtz free energy.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
