"""Illustrative uniform gas model, not experimental data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Generate the matching PNG in CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def temperature_ratio(s, epsilon, capacity_ratio=2.5):
    """Exponential expansion to twice the volume, then a fixed-volume hold."""
    finish = np.log(2.0) / (capacity_ratio * epsilon)
    steady = 1.0 / (1.0 + epsilon)
    during = steady + (1.0 - steady) * np.exp(-(1.0 + epsilon) * s)
    at_finish = steady + (1.0 - steady) * np.exp(-(1.0 + epsilon) * finish)
    after = 1.0 + (at_finish - 1.0) * np.exp(-(s - finish))
    return np.where(s <= finish, during, after), finish


def main():
    plt.rcParams.update({"font.size": 10.5, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (apparatus, ax) = plt.subplots(1, 2, figsize=(11.4, 5.1), dpi=110,
                                      gridspec_kw={"width_ratios": [1.1, 1]})
    apparatus.set(xlim=(0, 6.8), ylim=(0, 5.1), aspect="equal")
    apparatus.axis("off")
    apparatus.set_title("Regulated bath and conducting cylinder", pad=15)
    apparatus.add_patch(Rectangle((0.25, 0.55), 6.05, 3.15,
                                  facecolor="#e5f3fb", edgecolor="#397999", lw=1.8))
    apparatus.text(0.55, 3.32, r"Stirred heat bath at $T_b$", color="#195e7e")
    apparatus.add_patch(Rectangle((1.0, 1.5), 2.4, 1.25,
                                  facecolor="#fff0d4", edgecolor="#515151", lw=2))
    apparatus.plot([3.4, 4.2], [1.5, 1.5], color="#515151", lw=2)
    apparatus.plot([3.4, 4.2], [2.75, 2.75], color="#515151", lw=2)
    apparatus.add_patch(Rectangle((3.3, 1.5), 0.2, 1.25,
                                  facecolor="#8c939a", edgecolor="#515151"))
    apparatus.plot([3.5, 5.8], [2.125, 2.125], color="#515151", lw=4)
    apparatus.plot([5.8, 5.8], [1.85, 2.4], color="#515151", lw=4)
    apparatus.text(2.13, 2.12, "Ideal gas\nT, p, V", ha="center", va="center")
    apparatus.annotate("", xy=(5.25, 3.03), xytext=(3.95, 3.03),
                       arrowprops={"arrowstyle": "-|>", "lw": 1.8})
    apparatus.text(4.75, 3.22, "Slow expansion", ha="center", fontsize=10)
    apparatus.annotate("", xy=(2.3, 1.5), xytext=(2.3, 1.0),
                       arrowprops={"arrowstyle": "-|>", "color": "#b44b1b", "lw": 2})
    apparatus.text(2.3, 0.76, r"Heat in: $\dot Q=G(T_b-T)$", ha="center", color="#a23d16")
    apparatus.plot([1.45, 1.45, 2.4], [2.75, 4.08, 4.08], color="#515151", lw=1.5)
    apparatus.add_patch(Rectangle((2.4, 3.88), 2.25, 0.62,
                                  facecolor="white", edgecolor="#515151"))
    apparatus.text(3.525, 4.19, "T and p readouts", ha="center", va="center", fontsize=10)
    apparatus.text(3.3, 0.15, "Schematic; small mechanical imbalance drives motion", ha="center",
                   fontsize=9)
    s = np.linspace(0, 65, 2000)
    for epsilon, color, label in [(0.05, "#b75224", "Faster"), (0.005, "#176e9e", "Slower")]:
        theta, finish = temperature_ratio(s, epsilon)
        ax.plot(s, theta - 1.0, color=color, lw=2.2,
                label=rf"{label}: $\epsilon={epsilon:g}$")
        endpoint, _ = temperature_ratio(np.array([finish]), epsilon)
        ax.scatter([finish], endpoint - 1, color=color, zorder=4)
        ax.annotate("Hold V fixed", xy=(finish, endpoint[0] - 1),
                    xytext=(finish + (5 if epsilon == 0.05 else -18),
                            -0.038 if epsilon == 0.05 else -0.016),
                    arrowprops={"arrowstyle": "->", "color": color},
                    color=color, fontsize=10)
    ax.axhline(0, color="0.4", ls="--", lw=1)
    ax.set(xlim=(0, 65), ylim=(-0.055, 0.003), xlabel=r"Time $s=t/\tau$,  $\tau=C_V/G$",
           ylabel=r"Temperature difference $(T-T_b)/T_b$",
           title="Calculated lag, then recovery")
    ax.legend(loc="lower right", frameon=True, facecolor="white", fontsize=10)
    ax.grid(alpha=0.2)
    fig.suptitle("Slower piston motion approaches an isotherm", fontsize=14)
    fig.text(0.5, 0.035, r"Uniform-temperature model: $C_V=\frac{5}{2}nR$, "
             r"$V=V_i e^{\lambda t}$ to $2V_i$, $\epsilon=nR\lambda/G$" +
             "   •   illustrative, not measured", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.97, bottom=0.19, top=0.81, wspace=0.32)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
