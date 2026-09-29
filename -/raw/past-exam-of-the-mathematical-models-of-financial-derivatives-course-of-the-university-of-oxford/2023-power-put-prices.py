"""Draw European power-put prices; write the PNG to the working directory."""

from math import comb, erfc, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def normal_lower_tail(value):
    return np.fromiter((0.5 * erfc(float(x) / sqrt(2)) for x in value), float)


def power_put(spot, power, strike=1.0, rate=0.05, volatility=0.30, time=1.0):
    result = np.zeros_like(spot)
    for j in range(power + 1):
        d = (np.log(spot / strike) + (rate + (j - 0.5) * volatility**2) * time) / (
            volatility * sqrt(time)
        )
        result += (
            (-1) ** j
            * comb(power, j)
            * strike ** (power - j)
            * spot**j
            * np.exp(j * rate * time + j * (j - 1) * volatility**2 * time / 2)
            * normal_lower_tail(d)
        )
    return np.exp(-rate * time) * result


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13, "savefig.facecolor": "white"})
    spot = np.linspace(0.002, 1.9, 600)
    figure, axes = plt.subplots(1, 3, figsize=(11.4, 3.7), sharex=True, sharey=True)
    for power, ax in enumerate(axes, 1):
        ax.plot(spot, power_put(spot, power), color="#1367aa", linewidth=2.3, label="Price before expiry")
        ax.plot(spot, np.maximum(1 - spot, 0) ** power, "--", color="#666666", linewidth=1.5, label="Terminal payoff")
        ax.plot(0, np.exp(-0.05), "o", color="#1367aa", markersize=4)
        ax.axvline(1, color="#aaaaaa", linewidth=0.8, linestyle=":")
        ax.set(title=rf"Power $n={power}$", xlabel=r"Spot price $S/K$", xlim=(0, 1.9), ylim=(-0.015, 1.04))
        ax.grid(alpha=0.20)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel(r"Value in units of $K^n$")
    axes[0].legend(loc="upper right", fontsize=8.7, frameon=False)
    figure.suptitle(r"European power puts: $r=0.05$, $\sigma=0.30$, $T-t=1$", y=0.98, fontsize=14)
    figure.tight_layout(rect=(0, 0, 1, 0.92), w_pad=1.7)
    figure.savefig(Path.cwd() / "2023-power-put-prices.png", dpi=100)
    plt.close(figure)


if __name__ == "__main__":
    main()
