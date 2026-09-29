"""Plot the Huber criterion and its derivative; emit PNG in the working directory."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k = 2.0
    u = np.linspace(-6, 6, 1201)
    loss = np.where(np.abs(u) <= k, u**2 / 2, k * np.abs(u) - k**2 / 2)
    score = np.clip(u, -k, k)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), layout="constrained")
    axes[0].plot(u, u**2 / 2, color="#c47a19", linestyle="--", label=r"Squared: $u^2/2$")
    axes[0].plot(u, k * np.abs(u), color="#777777", linestyle=":", label=r"Absolute: $2|u|$")
    axes[0].plot(u, loss, color="#176c9c", linewidth=2.6, label=r"Huber: $\rho_2(u)$")
    axes[0].set(title="Quadratic center, linear tails", ylabel="Criterion value", ylim=(-0.4, 19))
    axes[1].plot(u, u, color="#c47a19", linestyle="--", label=r"Linear score: $u$")
    negative, positive = u < 0, u > 0
    axes[1].plot(u[negative], -k * np.ones(negative.sum()), color="#777777", linestyle=":", label=r"Sign score: $2\,\mathrm{sgn}(u)$")
    axes[1].plot(u[positive], k * np.ones(positive.sum()), color="#777777", linestyle=":")
    axes[1].scatter([0], [0], color="#777777", s=16, zorder=4)
    axes[1].plot(u, score, color="#176c9c", linewidth=2.6, label=r"Huber: $\psi_2(u)$")
    axes[1].set(title="Each score is clipped at ±2", ylabel="Score", ylim=(-6.3, 6.3))
    for ax in axes:
        ax.set(xlabel=r"Standardized difference $u=(x-\theta)/s$", xlim=(-6, 6))
        ax.axhline(0, color="#bbbbbb", linewidth=0.7, zorder=0)
        for cutoff in (-k, k):
            ax.axvline(cutoff, color="#aaaaaa", linewidth=0.8, linestyle="--", zorder=0)
        ax.grid(alpha=0.18)
        ax.legend(loc="upper center", fontsize=9)
        ax.set_facecolor("white")
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
