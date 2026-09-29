"""Draw synthetic potential-energy paths; output the matching PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
The chosen functions are illustrations, not measured molecular surfaces.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def potential(q, peak):
    """Join flat endpoint/peak tangents at q=0, 1/2, 1."""
    return np.where(
        q <= 0.5,
        peak * np.sin(np.pi * q) ** 2,
        -20.0 + (peak + 20.0) * np.sin(np.pi * q) ** 2,
    )


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    q = np.linspace(0, 1, 601)
    fig, ax = plt.subplots(figsize=(9.6, 5.1), dpi=110)
    fig.subplots_adjust(left=0.105, right=0.975, bottom=0.22, top=0.86)
    colors = ["#275f9e", "#bd6719"]
    for peak, color in zip([80.0, 50.0], colors):
        ax.plot(q, potential(q, peak), color=color, lw=3,
                label=f"Chosen path: peak {peak:.0f} kJ/mol")
    ax.axhline(0, color="#777777", lw=1, ls="--")
    ax.axhline(-20, color="#777777", lw=1, ls="--")
    for x, peak, color in [(0.2, 80, colors[0]), (0.35, 50, colors[1])]:
        ax.annotate("", (x, peak), (x, 0),
                    arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.6})
        ax.text(x - 0.018, peak / 2, f"{peak}", color=color, ha="right",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    for x, peak, color in [(0.72, 80, colors[0]), (0.85, 50, colors[1])]:
        ax.annotate("", (x, peak), (x, -20),
                    arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.6})
        ax.text(x + 0.02, (peak - 20) / 2, f"{peak + 20}", color=color,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.text(0.03, -10, "Reactants: 0", fontsize=11)
    ax.text(0.98, -30, "Products: −20", ha="right", fontsize=11)
    ax.set(xlim=(0, 1), ylim=(-37, 108),
           xlabel="Reaction coordinate q (arbitrary units; not time)",
           ylabel="Molar potential energy (kJ/mol)")
    ax.legend(loc="upper center", fontsize=11, frameon=False)
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks([-20, 0, 20, 40, 60, 80, 100])
    fig.suptitle("Synthetic reaction-coordinate profiles", fontsize=16, y=0.97)
    fig.text(0.5, 0.075,
             "Arrows: forward barriers 80 / 50; reverse barriers 100 / 70 kJ/mol.\n"
             "Potential-energy barriers alone do not determine fitted Arrhenius energies or equilibrium.",
             ha="center", va="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
