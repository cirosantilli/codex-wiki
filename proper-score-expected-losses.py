"""Compare expected scoring incentives; write the PNG basename to cwd.

Run from _media with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The positive, report-independent loss normalization preserves minimizers.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = 0.7
    near_zero = np.geomspace(1e-6, 0.02, 250)
    p = np.unique(np.r_[near_zero, np.linspace(0.02, 0.98, 1601), 1 - near_zero, q])
    brier = q * (1 - p) ** 2 + (1 - q) * p**2
    log_loss = -q * np.log(p) - (1 - q) * np.log1p(-p)
    brier_min = q * (1 - q)
    log_min = -q * np.log(q) - (1 - q) * np.log1p(-q)
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Expected scoring incentives when the true probability is q = 0.7", fontsize=14)
    loss_ax, reward_ax = axes
    loss_ax.plot(p, (brier - brier_min) / brier_min, color="#2369a5", lw=2.5, label="Brier loss")
    loss_ax.plot(p, (log_loss - log_min) / log_min, color="#b44d18", lw=2.5, label="Logarithmic loss")
    loss_ax.scatter([q], [0], color="black", zorder=5)
    loss_ax.set(title="Proper losses: LOWER is better", ylabel="Excess expected loss / truthful expected loss", ylim=(-0.12, 4))
    loss_ax.annotate("Both minima at p = 0.7", xy=(q, 0), xytext=(0.34, 1.05), arrowprops={"arrowstyle": "->", "color": "#444444"})
    loss_ax.text(0.03, 3.6, "Log loss diverges at p = 0 and p = 1", fontsize=10)
    loss_ax.legend(loc="upper right", bbox_to_anchor=(1, 0.80), frameon=False)
    loss_ax.text(0.5, -0.24, "Truthful expected losses: Brier 0.21; log 0.610864\nOnly the loss curves are normalized.", ha="center", va="top", transform=loss_ax.transAxes, fontsize=10)
    reward_p = np.linspace(0, 1, 501)
    reward_ax.plot(reward_p, 0.3 + 0.4 * reward_p, color="#6d4392", lw=2.5)
    reward_ax.scatter([q, 1], [0.58, 0.7], color=["#444444", "#6d4392"], zorder=5)
    reward_ax.set(title="Linear reward: HIGHER is better", ylabel="Expected reward (original units)", ylim=(0, 1))
    reward_ax.annotate("Honest: (0.7, 0.58)", xy=(q, 0.58), xytext=(0.10, 0.15), arrowprops={"arrowstyle": "->", "color": "#444444"})
    reward_ax.annotate("Maximum: (1, 0.7)", xy=(1, 0.7), xytext=(0.24, 0.87), arrowprops={"arrowstyle": "->", "color": "#6d4392"})
    reward_ax.text(0.5, -0.24, "Expected reward = 0.3 + 0.4p\nCertainty pays more than the honest report.", ha="center", va="top", transform=reward_ax.transAxes, fontsize=10)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlabel="Reported success probability p", xlim=(0, 1), xticks=[0, 0.2, 0.4, 0.6, 0.7, 0.8, 1])
        ax.axvline(q, color="#777777", linestyle=":", lw=1.2, zorder=0)
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig("proper-score-expected-losses.png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
