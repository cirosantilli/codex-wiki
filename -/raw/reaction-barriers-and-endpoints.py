"""Draw schematic potential-energy profiles with separately stated barriers.

The smooth teaching curves are not measured reaction paths or catalytic
cycles. The horizontal coordinate describes configurations, not time.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def smoothstep(u):
    return u * u * (3 - 2 * u)


def profile(coordinate, peak):
    coordinate = np.asarray(coordinate)
    return np.where(coordinate <= 0.5,
                    peak * smoothstep(2 * coordinate),
                    peak + (-20 - peak) * smoothstep(2 * coordinate - 1))


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    q = np.linspace(0, 1, 1601)
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.3), dpi=100, sharey=True)
    for ax, peak, color in zip(axes, [80, 50], ["#bd5f21", "#2867a0"], strict=True):
        ax.plot(q, profile(q, peak), color=color, linewidth=2.8)
        ax.hlines([0, -20, peak], 0, 1, color="#777777",
                   linestyle=":", linewidth=1.1)
        ax.scatter([0, 0.5, 1], [0, peak, -20], s=30, color=color, zorder=3)
        ax.annotate("", xy=(0.16, peak), xytext=(0.16, 0),
                     arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.7})
        ax.text(0.03, peak * 0.44, f"Forward barrier\n{peak} kJ/mol",
                color=color, fontsize=10, ha="left",
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.92})
        ax.annotate("", xy=(0.84, peak), xytext=(0.84, -20),
                     arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.7})
        ax.text(0.69, (peak - 20) / 2, f"Reverse barrier\n{peak + 20} kJ/mol",
                color=color, fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.92})
        ax.text(0.01, -8, "Reactants: 0", fontsize=10)
        ax.text(0.72, -31, "Products: −20", fontsize=10)
        ax.text(0.5, peak + 5, f"Peak: {peak}", fontsize=10, ha="center", color=color)
        ax.set_title(f"Illustrative route with peak {peak} kJ/mol")
        ax.set_xlim(-0.03, 1.03)
        ax.set_ylim(-38, 102)
        ax.set_xlabel("Reaction coordinate q (arbitrary scale)")
        ax.grid(axis="y", alpha=0.12)
    axes[0].set_ylabel("Potential energy relative to reactants (kJ/mol)")
    fig.suptitle("The endpoint difference stays −20 kJ/mol while the barriers change",
                 fontsize=15, y=0.98)
    fig.text(0.5, 0.045,
             "Schematic curves, not measured surfaces or a complete catalytic cycle. "
             "The reaction coordinate is not time.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.81, bottom=0.19, wspace=0.16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
