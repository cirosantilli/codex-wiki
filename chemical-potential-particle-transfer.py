"""Show ideal-gas redistribution as minimization of Helmholtz free energy.

Amounts are macroscopic moles, not a drawing of twelve individual particles.
Writes chemical-potential-particle-transfer.png in the current working directory.
Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def draw_compartments(ax, amounts, title, equilibrium=False):
    blue, orange = "#236a9e", "#b6532b"
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.set_title(title, fontsize=13, pad=8)
    for left, amount, name, color in zip([0.03, 0.55], amounts, ["A", "B"], [blue, orange]):
        ax.add_patch(Rectangle((left, 0.29), 0.42, 0.45,
                               facecolor="#eef4f8" if name == "A" else "#faf0e9",
                               edgecolor=color, lw=2))
        ax.text(left + 0.21, 0.56, f"{name}: {amount} mol", ha="center",
                fontsize=14, color=color)
        ax.text(left + 0.21, 0.38, "Volume V", ha="center", fontsize=11)
    ax.plot([0.45, 0.55], [0.51, 0.51], lw=5, color="#666666")
    ax.plot([0.50, 0.50], [0.51, 0.78], lw=1.5, color="#666666")
    ax.text(0.50, 0.88, "Open valve", ha="center", fontsize=11)
    if equilibrium:
        ax.text(0.5, 0.09, r"$p_A=p_B$ and $\mu_{{\rm m},A}=\mu_{{\rm m},B}$",
                ha="center", fontsize=12, color="#267747")
    else:
        ax.text(0.5, 0.09, r"Initially: A $\longrightarrow$ B   ($p_A=3p_B$)",
                ha="center", fontsize=12)


def main():
    blue, orange, green = "#236a9e", "#b6532b", "#267747"
    x = np.linspace(0.0, 1.0, 701)
    # The endpoint limit of y log(y) is zero; keep logarithms finite there.
    excess = (x * np.log(np.maximum(x, 1e-15))
              + (1 - x) * np.log(np.maximum(1 - x, 1e-15)) + np.log(2))
    slope_x = np.linspace(0.008, 0.992, 700)
    slope = np.log(slope_x / (1 - slope_x))
    initial = 0.75
    initial_excess = initial * np.log(initial) + (1 - initial) * np.log(1 - initial) + np.log(2)
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 7.0), dpi=120,
                             gridspec_kw={"height_ratios": [0.90, 1.25]})
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.15, top=0.82,
                        hspace=0.38, wspace=0.33)
    fig.suptitle("Matter exchange follows a free-energy slope", fontsize=16, y=0.97)
    fig.text(0.5, 0.90, "Same ideal gas • fixed temperature • equal rigid volumes • total amount 12 mol",
             ha="center", fontsize=12)
    draw_compartments(axes[0, 0], [9, 3], "Initial allocation")
    draw_compartments(axes[0, 1], [6, 6], "Final equilibrium", equilibrium=True)
    left, right = axes[1]
    left.plot(x, excess, color=blue, lw=2.4)
    left.scatter([0.5, initial], [0, initial_excess], s=50, color=[green, orange], zorder=5)
    left.annotate("6 mol / 6 mol", xy=(0.5, 0), xytext=(0.38, 0.27),
                  ha="center", color=green, fontsize=11,
                  arrowprops={"arrowstyle": "->", "color": green})
    left.annotate("9 mol / 3 mol", xy=(initial, initial_excess), xytext=(0.77, 0.44),
                  ha="center", color=orange, fontsize=11,
                  arrowprops={"arrowstyle": "->", "color": orange})
    left.set(title="Excess above the equal-allocation minimum",
             ylabel=r"$[F(x)-F(1/2)]/(n_{\rm tot}RT)$", ylim=(-0.04, 0.73))
    left.annotate("", xy=(0.58, 0.02), xytext=(0.71, 0.09),
                  arrowprops={"arrowstyle": "->", "color": orange, "lw": 1.8})
    right.plot(slope_x, slope, color=blue, lw=2.4)
    right.axhline(0, lw=1, color="#777777")
    right.axvline(0.5, lw=1, ls="--", color=green)
    right.scatter([0.5, initial], [0, np.log(3)], s=50, color=[green, orange], zorder=5)
    right.annotate(r"Initially: $\ln 3>0$" + "\nDecrease the amount in A",
                   xy=(initial, np.log(3)), xytext=(0.53, 3.5), ha="center", fontsize=11,
                   color=orange, arrowprops={"arrowstyle": "->", "color": orange},
                   bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    right.text(0.25, -3.4, "Increase the\namount in A", ha="center", color=blue, fontsize=11)
    right.set(title="Slope for increasing the amount in A",
              ylabel=r"$(dF/dn_A)/(RT)=\ln[x/(1-x)]$", ylim=(-5, 5))
    for ax in [left, right]:
        ax.set(xlim=(0, 1), xlabel=r"Fraction in A: $x=n_A/n_{\rm tot}$")
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
        ax.title.set_fontsize(11)
    fig.text(0.5, 0.035, "At the minimum, the free-energy slope and the chemical-potential difference both vanish.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
