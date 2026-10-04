"""Generate paper-26-large-deviation-costs.png in the current directory.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The first two panels use exponential sample means; the third uses Poisson
moderate deviations. All parameters have lambda=1, with cap C=1.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def exponential_rate(x):
    return x - 1 - np.log(x)


def minimum_rate(x, copies):
    return np.where(x <= 1, exponential_rate(x), copies * exponential_rate(x))


def main():
    plt.rcParams.update({"font.size": 10, "axes.titlesize": 11})
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.75), dpi=160,
                             constrained_layout=True, facecolor="white")
    fig.suptitle(r"Rare-event costs and the effect of clipping ($\lambda=1$)")
    x = np.linspace(0.15, 2.2, 1800)
    axes[0].plot(x, exponential_rate(x), "--", color="0.45", label=r"One mean: $I(m)$")
    axes[0].plot(x, minimum_rate(x, 3), color="#1768ac", linewidth=2,
                 label=r"Minimum of three: $J(m)$")
    axes[0].axvline(1, color="0.55", linestyle=":")
    axes[0].set(xlabel=r"Mean or minimum $m$", ylabel="Rate function",
                title="A large minimum requires all means to rise", ylim=(0, 1.5))
    axes[0].legend(loc="upper center", fontsize=8)

    z = np.linspace(0.4, 2, 1800)
    for copies, color, offset in [(1, "#1768ac", (-43, 9)),
                                  (3, "#d17b0f", (9, 9)),
                                  (10, "#238b45", (-27, -31))]:
        objective = np.log(z) - minimum_rate(z, copies)
        optimum = (copies + 1) / copies
        value = np.log(optimum) - minimum_rate(np.array(optimum), copies)
        theory = (copies + 1) * np.log1p(1 / copies) - 1
        assert np.isclose(value, theory)
        assert np.max(objective) <= theory + 1e-12
        axes[1].plot(z, objective, color=color, label=f"k={copies}")
        axes[1].plot(optimum, value, "o", color=color, markersize=4)
        axes[1].annotate(f"z*={optimum:.2f}", (optimum, value),
                         xytext=offset, textcoords="offset points", fontsize=8,
                         color=color)
    axes[1].axvline(1, color="0.55", linestyle=":")
    axes[1].axhline(0, color="0.7", linewidth=0.6)
    axes[1].set(xlabel=r"Clipped minimum $z$ ($a=0.4$, $b=2$)",
                ylabel=r"Moment objective $\log z-J(z)$",
                title="High moments favor values above the mean", ylim=(-2.5, 0.65))
    axes[1].legend(loc="lower left", fontsize=8)

    fluctuations = np.linspace(-2.4, 2.2, 1600)
    axes[2].plot(fluctuations, fluctuations**2 / 2, "--", color="0.45",
                 label=r"Input: $x^2/2$")
    allowed = fluctuations[fluctuations <= 1]
    axes[2].plot(allowed, allowed**2 / 2, color="#1768ac", linewidth=2,
                 label="Clipped output")
    axes[2].plot(1, 0.5, "o", color="#1768ac", markersize=5)
    axes[2].axvline(1, color="0.55", linestyle=":")
    axes[2].axvspan(1, 2.2, color="0.9", zorder=-1)
    axes[2].text(1.6, 2.7, "Output cost\n= infinity", ha="center", fontsize=9)
    axes[2].set(xlabel="Scaled fluctuation", ylabel="Moderate-deviation rate",
                title="The output cannot exceed its cap", ylim=(0, 3.2))
    axes[2].legend(loc="upper center", fontsize=8)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / "paper-26-large-deviation-costs.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
