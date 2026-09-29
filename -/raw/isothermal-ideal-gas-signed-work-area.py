"""Illustrate reversible isothermal work. Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    n, gas_constant, temperature = 1.0, 8.31446261815324, 300.0
    volume = np.linspace(8.5, 23.0, 600)
    selected_volume = np.linspace(10.0, 20.0, 600)
    # A kilopascal litre is one joule.
    pressure = n * gas_constant * temperature / volume
    selected_pressure = n * gas_constant * temperature / selected_volume
    work_kj = n * gas_constant * temperature * np.log(2.0) / 1000
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=110, sharey=True)
    for ax, expansion, color in zip(axes, [True, False], ["#176e9e", "#b75224"]):
        ax.plot(volume, pressure, color=color, lw=2.5)
        ax.fill_between(selected_volume, 0, selected_pressure, color=color, alpha=0.18)
        ax.vlines([10, 20], 0, n * gas_constant * temperature / np.array([10, 20]),
                  color=color, ls="--", lw=1)
        ax.scatter([10, 20], n * gas_constant * temperature / np.array([10, 20]),
                   color=color, zorder=4)
        ax.text(10.2, 260, "A: 10 L", fontsize=10)
        ax.text(20.2, 136, "B: 20 L", fontsize=10)
        start, end = (12.0, 15.0) if expansion else (17.0, 14.0)
        ax.annotate("", xy=(end, n * gas_constant * temperature / end),
                    xytext=(start, n * gas_constant * temperature / start),
                    arrowprops={"arrowstyle": "-|>", "color": color,
                                "lw": 2.2, "mutation_scale": 17})
        sign = "+" if expansion else "−"
        ax.text(15, 75, f"$W_{{\\rm by}}=Q$\n{sign}{work_kj:.3f} kJ", ha="center",
                va="center", color=color, fontsize=13)
        ax.set(xlim=(8, 24), ylim=(0, 320), xlabel="Gas volume V (L)",
               title="Expansion: A → B" if expansion else "Compression: B → A")
        ax.set_xticks([10, 15, 20])
        ax.grid(alpha=0.18)
    axes[0].set_ylabel("Gas pressure p (kPa)")
    fig.suptitle("Reversible isotherm: 1 mol of ideal gas at 300 K", fontsize=14)
    fig.text(0.5, 0.035, r"$W_{\rm by}=\int_{V_i}^{V_f}p\,dV$   •   "
             "shading shows magnitude; traversal sets sign   •   ΔU = 0", ha="center")
    fig.subplots_adjust(left=0.08, right=0.97, top=0.82, bottom=0.18, wspace=0.14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
