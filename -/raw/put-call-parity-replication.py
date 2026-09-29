"""Draw the identical-cash-flow replication behind put-call parity.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from _media: python ../put-call-parity-replication.py
The PNG is written into the current working directory.
"""

from math import exp, isclose
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    stock, strike, maturity, rate, call_price = 100, 100, 1, 0.05, 10
    bond_price = strike * exp(-rate * maturity)
    put_price = call_price + bond_price - stock
    cost_a = call_price + bond_price
    cost_b = put_price + stock
    assert isclose(cost_a, cost_b, abs_tol=1e-12)
    prices = np.linspace(60, 140, 401)
    call = np.maximum(prices - strike, 0)
    put = np.maximum(strike - prices, 0)
    np.testing.assert_allclose(call + strike, put + prices, atol=1e-12)

    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.7), layout="constrained",
                             facecolor="white")
    fig.suptitle("Put-call parity: two ways to deliver the same cash flow", fontsize=15)
    blue, orange, green = "#2563a6", "#b76816", "#347456"
    ax = axes[0]
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.set_title("Today: S₀ = K = 100, T = 1, r = 0.05", fontsize=11, pad=12)
    ax.text(0.5, 0.95, "Illustrative call price C₀ = 10", ha="center", va="top")
    ax.text(0.5, 0.75,
            f"A: call + bond paying 100 at expiry\n"
            f"10 + 100 exp(−0.05)\n= {cost_a:.8f}",
            ha="center", va="center", linespacing=1.6, color=blue,
            bbox={"boxstyle": "round,pad=0.7", "facecolor": "#f1f6fc",
                  "edgecolor": blue})
    ax.text(0.5, 0.43,
            f"B: put + one stock share\n{put_price:.8f} + 100\n= {cost_b:.8f}",
            ha="center", va="center", linespacing=1.6, color=orange,
            bbox={"boxstyle": "round,pad=0.7", "facecolor": "#fdf6ed",
                  "edgecolor": orange})
    ax.text(0.5, 0.12, "Identical terminal cash flows\n⇒ equal initial costs without arbitrage",
            ha="center", va="center", linespacing=1.5)

    ax = axes[1]
    ax.plot(prices, call + strike, color=blue, linewidth=4,
            label=r"A: call + bond, $C_T+100$")
    ax.plot(prices, put + prices, color=orange, linewidth=2, linestyle="--",
            label=r"B: put + stock, $P_T+S_T$")
    scenarios = [80, 100, 120]
    values = [100, 100, 120]
    ax.scatter(scenarios, values, s=40, color=green, zorder=4)
    for price, value, offset in [(80, 100, (-28, -26)),
                                  (100, 100, (5, -26)),
                                  (120, 120, (5, 8))]:
        ax.annotate(f"({price}, {value})", (price, value), xytext=offset,
                    textcoords="offset points", fontsize=10)
    ax.axvline(strike, color="#777777", linestyle=":", linewidth=1)
    ax.set(xlim=(60, 140), ylim=(85, 145), xticks=[60, 80, 100, 120, 140],
           xlabel=r"Terminal stock price $S_T$", ylabel="Terminal portfolio amount",
           title=r"At expiry: $A_T=B_T=\max(S_T,100)$",)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / "put-call-parity-replication.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
