"""Plot two constant-parameter Arrhenius models and their linear transforms.

Writes its PNG to the current working directory. Curves are exact teaching
models, not experimental observations. Each is anchored at k(300 K)=0.1/s,
so the two pre-exponential factors are different.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

R = 8.31446261815324
REFERENCE_TEMPERATURE = 300.0
REFERENCE_RATE = 0.1


def log_relative_rate(temperature, activation_energy):
    return activation_energy / R * (
        1 / REFERENCE_TEMPERATURE - 1 / np.asarray(temperature)
    )


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    temperature = np.linspace(280, 350, 1401)
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.3), dpi=100)
    for energy, color in [(40000.0, "#2867a0"), (80000.0, "#bd5f21")]:
        log_ratio = log_relative_rate(temperature, energy)
        label = f"Eₐ = {energy / 1000:g} kJ/mol"
        axes[0].semilogy(temperature, REFERENCE_RATE * np.exp(log_ratio),
                         color=color, linewidth=2.5, label=label)
        axes[1].plot(1000 / temperature, log_ratio, color=color,
                     linewidth=2.5, label=label)
        rate310 = REFERENCE_RATE * np.exp(log_relative_rate(310, energy))
        axes[0].scatter([310], [rate310], s=38, color=color, zorder=4)
    axes[0].set_title("A 10 K rise gives different rate multipliers")
    axes[0].set_xlabel("Absolute temperature T (K)")
    axes[0].set_ylabel("First-order rate constant k (s⁻¹), logarithmic scale")
    axes[0].set_xlim(280, 350)
    axes[0].axvline(300, color="#666666", linestyle=":", linewidth=1.2)
    axes[0].annotate("Common k(300 K) = 0.100 s⁻¹",
                     xy=(300, 0.1), xytext=(284, 1.4),
                     arrowprops={"arrowstyle": "->", "color": "#555555"},
                     fontsize=10, color="#333333")
    axes[0].text(316, 0.036, "At 310 K:\n40 kJ/mol → 0.167749 s⁻¹\n"
                 "80 kJ/mol → 0.281398 s⁻¹",
                 fontsize=10, bbox={"facecolor": "white", "edgecolor": "#dddddd"})
    axes[1].set_title("Inverse temperature makes each model linear")
    axes[1].set_xlabel("Inverse temperature 1/T (10⁻³ K⁻¹)")
    axes[1].set_ylabel("ln[k(T) / k(300 K)]")
    axes[1].axhline(0, color="#777777", linewidth=1, alpha=0.45)
    axes[1].axvline(1000 / 300, color="#666666", linestyle=":", linewidth=1.2)
    for ax in axes:
        ax.grid(alpha=0.18)
        ax.legend(loc="upper left", fontsize=10, framealpha=0.96)
    axes[0].legend(loc="lower right", fontsize=10, framealpha=0.96)
    fig.suptitle("Arrhenius temperature sensitivity and its straight-line representation",
                 fontsize=15, y=0.98)
    fig.text(0.5, 0.035,
             "Chosen constant-parameter models, not measured data. "
             "Equal reference rates imply different prefactors.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.085, right=0.975, top=0.82, bottom=0.19, wspace=0.24)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
