"""Original first-success cost model; write the matching opaque PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    p = 0.25
    n = np.arange(1, 15)
    survive = (1 - p) ** (n - 1)
    pmf = p * survive
    mean_cost = 3 - 2 * p
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 6), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[0.85, 1.6], hspace=0.5)
    trace = fig.add_subplot(grid[0, :])
    for i, (outcome, cost) in enumerate(zip(["failure"] * 3 + ["success"], [3, 3, 3, 1]), 1):
        color = "#f2dbce" if i < 4 else "#c7e8d7"
        trace.text(i, 0.5, f"Attempt {i}\n{outcome}\ncost {cost}", ha="center", va="center",
                   bbox={"boxstyle": "round,pad=0.5", "fc": color, "ec": "#606060"})
        if i < 4:
            trace.annotate("", xy=(i + 0.71, 0.5), xytext=(i + 0.3, 0.5),
                           arrowprops={"arrowstyle": "->", "color": "#606060"})
    trace.set(xlim=(0.55, 4.55), ylim=(-0.15, 1.05))
    trace.set_axis_off()
    trace.set_title("One illustrative sequence: N = 4, total cost = 10", pad=5)
    ax = fig.add_subplot(grid[1, 0])
    ax.bar(n, pmf, color="#287a9d", label=r"$P(N=i)$")
    ax.plot(n, survive, "o-", color="#b85831", label=r"$P(N\geq i)$")
    ax.set(xlabel="Trial index i", ylabel="Probability", ylim=(0, 1.08), xticks=[1, 4, 7, 10, 14])
    ax.legend(fontsize=10)
    ax.grid(axis="y", alpha=0.2)
    ax = fig.add_subplot(grid[1, 1])
    contributions = mean_cost * survive
    ax.bar(n, contributions, color="#3f8e72")
    ax.set(xlabel="Trial index i", ylabel="Expected cost contribution", xticks=[1, 4, 7, 10, 14])
    ax.text(0.96, 0.92, r"$E[X_i1_{\{N\geq i\}}]=2.5(3/4)^{i-1}$" + "\nSum over all i = 10",
            transform=ax.transAxes, ha="right", va="top", fontsize=10)
    ax.grid(axis="y", alpha=0.2)
    fig.suptitle("Stopping on success: p = 1/4, costs 3 and 1", fontsize=16, y=0.985)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.09, top=0.85, wspace=0.3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
