"""Original square-pulse Rabi model; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; writes rabi-square-pulse-detuning.png to the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def transition_probability(area, detuning_ratio):
    """area=Omega*t and detuning_ratio=delta/Omega; Omega > 0."""
    rate = np.sqrt(1 + np.asarray(detuning_ratio) ** 2)
    return np.sin(np.asarray(area) * rate / 2) ** 2 / rate ** 2


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=110, facecolor="white")
    times = np.linspace(0, 4, 1201)
    for d, color in [(0, "#2166ac"), (1, "#b83238")]:
        axes[0].plot(times, transition_probability(np.pi * times, d), color=color, lw=2, label=rf"$\delta/\Omega={d}$")
    axes[0].axvline(1, color="#777777", lw=1, ls=":")
    axes[0].plot([1], [1], "o", color="#2166ac")
    axes[0].set(xlabel=r"Duration $t/\tau_\pi$  ($\tau_\pi=\pi/\Omega$)", ylabel=r"Transfer probability $P_{g\to e}$", title="Coherent population exchange", xlim=(0, 4))
    axes[0].legend(loc="upper right", frameon=False)
    detunings = np.linspace(-4, 4, 1601)
    axes[1].plot(detunings, transition_probability(np.pi, detunings), color="#2166ac", lw=2, label=r"Fixed $\pi$ pulse")
    axes[1].plot(detunings, 1 / (1 + detunings ** 2), color="#777777", lw=1.4, ls=":", label=r"Upper bound $1/(1+x^2)$")
    axes[1].plot([0, 1, np.sqrt(3)], transition_probability(np.pi, np.array([0, 1, np.sqrt(3)])), "o", color="#b83238", ms=5)
    axes[1].annotate("0.3166", xy=(1, transition_probability(np.pi, 1)), xytext=(1.7, 0.5), arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    axes[1].set(xlabel=r"Detuning $x=\delta/\Omega$", title=r"Single-transit line: $\Omega\tau=\pi$", xlim=(-4, 4))
    axes[1].legend(loc="upper right", frameon=False, fontsize=9)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_ylim(-0.035, 1.10)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax.grid(alpha=0.20)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Ideal square-pulse Rabi model", fontsize=15)
    fig.text(0.5, 0.025, "Original calculation • identical two-level particles • constant drive • no measured data", ha="center", fontsize=10, color="#555555")
    fig.tight_layout(rect=(0, 0.07, 1, 0.93))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
