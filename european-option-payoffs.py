"""Draw deterministic European option payoffs, with no pricing model.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from _media: python ../european-option-payoffs.py
The PNG is written into the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    strike = 100
    prices = np.linspace(60, 140, 401)
    call = np.maximum(prices - strike, 0)
    put = np.maximum(strike - prices, 0)
    np.testing.assert_allclose(call - put, prices - strike, atol=1e-12)

    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.4), layout="constrained",
                             facecolor="white")
    fig.suptitle("European options at expiry: strike K = 100", fontsize=15)
    ax = axes[0]
    ax.plot(prices, call, color="#2563a6", linewidth=2.5,
            label=r"Call: $(S_T-K)^+$")
    ax.plot(prices, put, color="#b76816", linewidth=2.5,
            label=r"Put: $(K-S_T)^+$")
    scenarios = np.array([80, 100, 120])
    ax.scatter(scenarios, np.maximum(scenarios - strike, 0),
               color="#2563a6", s=38, zorder=4)
    ax.scatter(scenarios, np.maximum(strike - scenarios, 0),
               color="#b76816", s=38, marker="s", zorder=3)
    ax.set(ylim=(-3, 43), ylabel="Terminal payoff per share",
           title="Each exercise right pays only its positive part")
    ax.legend(loc="upper center", fontsize=10)

    ax = axes[1]
    ax.axhline(0, color="#777777", linewidth=1)
    ax.plot(prices, call - put, color="#347456", linewidth=2.5,
            label=r"Difference: $C_T-P_T=S_T-K$")
    ax.scatter(scenarios, scenarios - strike, color="#347456", s=38, zorder=4)
    for price, offset in [(80, (10, -18)), (100, (10, -18)), (120, (-70, 12))]:
        ax.annotate(f"({price}, {price - strike})", (price, price - strike),
                    xytext=offset, textcoords="offset points", fontsize=10)
    ax.set(ylim=(-43, 43), ylabel="Difference of terminal payoffs",
           title="Subtracting cancels the corner")
    ax.legend(loc="upper left", fontsize=10)

    for ax in axes:
        ax.axvline(strike, color="#777777", linestyle="--", linewidth=1)
        ax.set(xlim=(60, 140), xlabel=r"Terminal stock price $S_T$",
               xticks=[60, 80, 100, 120, 140])
        ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / "european-option-payoffs.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
