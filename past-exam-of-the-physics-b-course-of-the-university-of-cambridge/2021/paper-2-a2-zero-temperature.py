"""Original entropy/cooling sketch; write the PNG basename in the cwd.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Dependencies are declared in the repository's top-level pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7.4, 4.8), layout="constrained")
    fig.patch.set_facecolor("white")
    temperature = np.linspace(0, 1.04, 200)
    ax.plot(temperature, temperature, color="#2463a5", lw=2,
            label=r"Setting $X_1$: $S-S_0=a_1T$")
    ax.plot(temperature, 2 * temperature, color="#a33d46", lw=2,
            label=r"Setting $X_2$: $S-S_0=a_2T$, $a_2=2a_1$")
    current = 0.90
    for stage in range(5):
        next_temperature = current / 2
        ax.annotate("", xy=(current, current), xytext=(current, 2 * current),
                    arrowprops={"arrowstyle": "-|>", "lw": 1.5,
                                "color": "#bd6c20", "mutation_scale": 11})
        ax.annotate("", xy=(next_temperature, current), xytext=(current, current),
                    arrowprops={"arrowstyle": "-|>", "lw": 1.5,
                                "color": "#26735c", "mutation_scale": 11})
        if stage < 3:
            ax.plot([current, current], [0, current], ":", color="#aaaaaa", lw=0.7)
            ax.text(current, -0.12, rf"$T_{stage}$", ha="center", fontsize=10)
        current = next_temperature
    ax.text(0.94, 1.34, "Heat rejected\nisothermally", fontsize=9,
            ha="right", color="#955013")
    ax.text(0.53, 1.00, "Reversible adiabat", fontsize=9, color="#26735c")
    ax.text(0.48, 1.64, r"$T_n=T_0\,2^{-n}>0$ for finite $n$", fontsize=11)
    ax.plot(0, 0, "o", color="black", ms=4)
    ax.annotate("Common limiting entropy", xy=(0, 0), xytext=(0.37, 0.13),
                fontsize=9, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(xlabel=r"Temperature $T$ (schematic units)",
           ylabel=r"Entropy $S-S_0$ (schematic units)",
           title="Cooling approaches the common zero-temperature limit",
           xlim=(-0.025, 1.08), ylim=(-0.18, 2.25))
    ax.set_xticks([0])
    ax.set_yticks([0])
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=145,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
