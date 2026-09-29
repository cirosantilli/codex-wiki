"""Plot a stipulated arithmetic-baseline Pauling model; no experimental data.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the current directory with this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    conversion = 96.485  # Rounded kJ/mol corresponding to 1 eV per particle.
    daa, dbb = 200.0, 450.0
    baseline = (daa + dbb) / 2
    dab = baseline + conversion
    excess = dab - baseline
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Bond-energy excess: a stipulated Pauling model", fontsize=15)
    left.bar([0, 1, 2], [daa, dbb, dab], width=0.55,
             color=["#7899af", "#7899af", "#276c9a"])
    left.set_xticks([0, 1, 2], ["A–A", "B–B", "A–B"])
    left.set_ylabel("Dissociation energy (kJ/mol)")
    left.set_ylim(0, 525)
    left.set_xlim(-0.6, 3.05)
    for x, value in enumerate([daa, dbb, dab]):
        left.text(x, value + 10, f"{value:g}", ha="center")
    left.axhline(baseline, color="#b34827", linestyle="--", linewidth=1.5)
    left.text(-0.45, baseline - 25, "Arithmetic baseline = 325", color="#b34827")
    left.annotate("", xy=(2.6, dab), xytext=(2.6, baseline),
                  arrowprops={"arrowstyle": "<->", "color": "#b34827", "lw": 1.8})
    left.text(2.61, (dab + baseline) / 2, "96.485", va="center", rotation=90,
              color="#b34827")
    left.set_title(r"$\Delta_D=D_{AB}-(D_{AA}+D_{BB})/2$")
    delta = np.linspace(0, 200, 401)
    right.plot(delta, np.sqrt(delta / conversion), color="#276c9a", linewidth=2.5)
    right.plot(excess, 1, "o", color="#b34827", markersize=7)
    right.axvline(excess, ymax=1/1.55, color="#b34827", linestyle=":")
    right.axhline(1, xmax=excess/200, color="#b34827", linestyle=":")
    right.annotate("96.485 kJ/mol → difference 1", xy=(excess, 1),
                   xytext=(17, 1.35), arrowprops={"arrowstyle": "->"})
    right.set(xlim=(0, 200), ylim=(0, 1.55), xlabel=r"Excess $\Delta_D$ (kJ/mol)",
              ylabel=r"$|\chi_P(A)-\chi_P(B)|$ (dimensionless)")
    right.set_title(r"$|\Delta\chi_P|=\sqrt{\Delta_D/96.485}$  (stated units)")
    right.grid(alpha=0.2)
    fig.supxlabel("Invented energies, consistent dissociation convention; no named substances", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
