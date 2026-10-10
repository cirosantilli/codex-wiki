"""Exact absorbed-walk laws, not simulated measurements; PNG goes to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def survival_law(horizon, barriers):
    """P(T>n) from live-position probabilities, starting at zero."""
    live = {0: 1.0}
    survival = [1.0]
    for _ in range(horizon):
        next_live = {}
        for position, probability in live.items():
            for step in (-1, 1):
                destination = position + step
                if destination not in barriers:
                    next_live[destination] = next_live.get(destination, 0.0) + probability / 2
        live = next_live
        survival.append(sum(live.values()))
    return np.array(survival)


def main():
    horizon = 400
    single = survival_law(horizon, {1})
    double = survival_law(horizon, {-2, 2})
    n = np.arange(horizon + 1)
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), dpi=120, facecolor="white")
    for law, color, label in [(single, "#287a9d", "First hit of +1"),
                               (double, "#b85831", "First hit of either −2 or +2")]:
        axes[0].semilogy(n[:61], law[:61], color=color, lw=2, label=label)
        capped = np.r_[0, np.cumsum(law[:-1])]
        axes[1].plot(n, capped, color=color, lw=2, label=label)
    axes[0].set(xlabel="Number of steps n", ylabel=r"Survival probability $P(T>n)$",
                xlim=(0, 60), ylim=(1e-9, 1.2))
    axes[1].axhline(4, color="#555555", linestyle=":", lw=1.4)
    axes[1].text(395, 4.6, "two barriers: mean 4", ha="right", fontsize=10)
    axes[1].set(xlabel="Cap n", ylabel=r"Capped mean $E[\min(T,n)]$", xlim=(0, horizon), ylim=(0, 34))
    for ax in axes:
        ax.grid(alpha=0.2)
    axes[0].legend(fontsize=9, loc="lower left")
    axes[1].text(0.04, 0.93, "One-barrier mean keeps growing", transform=axes[1].transAxes,
                 color="#287a9d", fontsize=10)
    fig.suptitle("Fair nearest-neighbour walk: finite stopping is not finite mean", fontsize=15)
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.13, top=0.84, wspace=0.3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
