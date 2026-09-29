"""Generate dulong-petit-classical-energy.png in the current working directory.

Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The bars show an ideal classical harmonic model, not material measurements.
Energy units are k_B times 300 K; the common energy origin is omitted.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    temperatures = np.array([300.0, 600.0])
    positions = np.arange(temperatures.size)
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.8))
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.27, top=0.76, wspace=0.32)
    fig.suptitle("Classical harmonic energy: doubling temperature doubles energy",
                 fontsize=13, y=0.96)
    for ax, directions, heading in zip(
            axes, [1, 3], ["One oscillator direction", "One atom: three directions"]):
        kinetic = directions * temperatures / (2 * 300.0)
        potential = kinetic.copy()
        ax.bar(positions, kinetic, width=0.56, color="#247aa6",
               label="Mean kinetic energy")
        ax.bar(positions, potential, bottom=kinetic, width=0.56,
               color="#e5aa49", label="Mean potential energy")
        for pos, kin, pot in zip(positions, kinetic, potential):
            ax.text(pos, kin / 2, f"{kin:g}", ha="center", va="center", color="white")
            ax.text(pos, kin + pot / 2, f"{pot:g}", ha="center", va="center")
            ax.text(pos, kin + pot + 0.10 * directions, f"total {kin + pot:g}",
                    ha="center", va="bottom", fontsize=10)
        ax.set_xticks(positions, ["300 K", "600 K"])
        ax.set(ylim=(0, 2.65 * directions), xlabel="Temperature",
               ylabel=r"Mean energy / $[k_B(300\,\mathrm{K})]$")
        ax.set_title(heading + "\n" +
                     (r"$\langle E\rangle=k_BT$, $C_V=k_B$" if directions == 1
                      else r"$\langle E\rangle=3k_BT$, $C_V=3k_B$"), fontsize=11)
        ax.set_yticks(np.arange(0, 2.65 * directions, directions))
        ax.set_axisbelow(True)
        ax.grid(axis="y", alpha=0.2)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.08),
               ncol=2, frameon=False)
    fig.text(0.5, 0.02, r"Equipartition: each quadratic term stores $k_BT/2$; "
             "six terms per atom.", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "dulong-petit-classical-energy.png", dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
