"""Two independent stipulated examples; no measured molecular values.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media; output
is the matching PNG basename in the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    avogadro = 6.02214076e23
    electronvolt = 1.602176634e-19
    boltzmann = 1.380649e-23
    conversion = avogadro * electronvolt / 1000
    gas_constant = avogadro * boltzmann
    depth, quantum, temperature = 2.0, 0.2, 300.0
    zero_point = quantum / 2 - quantum**2 / (16 * depth)
    values = np.array([depth * conversion, (depth - zero_point) * conversion,
                       (depth - zero_point) * conversion
                       + 1.5 * gas_constant * temperature / 1000])
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 5.8),
                                     layout="constrained", facecolor="white")
    colors = ["#215b87", "#b15b00", "#30784c"]
    left.set_facecolor("white")
    left.bar(np.arange(3), values, color=colors, width=0.65)
    for i, value in enumerate(values):
        left.text(i, value + 2.0, f"{value:.3f}", ha="center", fontsize=11)
    left.set_xticks(np.arange(3), [r"$N_A D_e$", r"$N_A D_0$",
                                 "$\\Delta_{\\rm diss}H^\\circ$\n300 K model"])
    left.set(ylim=(0, 218), ylabel="Molar energy or enthalpy (kJ/mol)",
             title="Same dissociation, different conventions")
    left.text(0.5, 0.58, f"Ground-state correction: −{zero_point * conversion:.3f}\n"
              "Thermal correction: +3.742 kJ/mol\n\n"
              "Ideal gas; active rotations;\nthermal vibration and electronic\n"
              "excitation neglected", transform=left.transAxes,
              ha="center", va="center", color="#222222", fontsize=10.5,
              bbox={"facecolor": "white", "edgecolor": "#cccccc", "pad": 8})
    right.set_facecolor("white")
    states = [r"$AB_2$", r"$AB+B$", r"$A+2B$"]
    levels = [0, 300, 700]
    for i, (level, label) in enumerate(zip(levels, states)):
        right.hlines(level, i - 0.26, i + 0.26, color="#215b87", linewidth=3)
        right.text(i, level + 22, label, ha="center")
    for i, step in enumerate([300, 400]):
        right.plot([i + 0.26, i + 0.75], [levels[i], levels[i]],
                   color="#999999", linestyle=":")
        right.annotate("", xy=(i + 0.75, levels[i + 1]),
                       xytext=(i + 0.75, levels[i]),
                       arrowprops={"arrowstyle": "->", "color": "#b15b00",
                                   "linewidth": 2})
        right.text(i + 0.84, (levels[i] + levels[i + 1]) / 2,
                   f"{step}", va="center", color="#9a5000")
    right.text(0.03, 0.84, "Total: 700 kJ/mol\nMean per bond: 350 kJ/mol",
               transform=right.transAxes, fontsize=11)
    right.set(xlim=(-0.4, 2.55), ylim=(-65, 850), xticks=[],
              ylabel="Cumulative enthalpy (kJ/mol of initial species)",
              xlabel="Two successive dissociations at one temperature",
              title="Different reactants, different step costs")
    fig.suptitle("Stipulated examples — separate hypothetical systems", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
