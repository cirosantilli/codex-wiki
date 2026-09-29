"""Plot original EM likelihood and mean iterates, with the identical-means trap.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def evaluate(x, means):
    log_joint = -0.5 * (x[:, None] - means[None, :]) ** 2 - np.log(2.0) - 0.5 * np.log(2 * np.pi)
    maximum = log_joint.max(axis=1, keepdims=True)
    log_density = maximum + np.log(np.exp(log_joint - maximum).sum(axis=1, keepdims=True))
    r = np.exp(log_joint - log_density)
    return r, float(log_density.sum())


def main():
    x = np.array([-2.2, -1.8, -1.0, 1.0, 1.8, 2.2])
    means = np.array([-1.0, 1.0])
    history, likelihood = [], []
    for _ in range(7):
        r, value = evaluate(x, means)
        history.append(means.copy())
        likelihood.append(value)
        means = (r * x[:, None]).sum(axis=0) / r.sum(axis=0)
    history = np.array(history)
    iterations = np.arange(len(history))
    trap_likelihood = evaluate(x, np.zeros(2))[1]
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    fig, (ll_ax, mean_ax) = plt.subplots(1, 2, figsize=(9.6, 6))
    fig.patch.set_facecolor("white")
    fig.suptitle("EM improves the likelihood, but initialization matters", fontsize=16)
    ll_ax.plot(iterations, likelihood, "o-", color="#28794a", lw=2, label="Initial means (−1, 1)")
    ll_ax.axhline(trap_likelihood, color="#666666", ls="--", label="Initial means (0, 0): trapped")
    ll_ax.annotate(f"{likelihood[0]:.6f}", (0, likelihood[0]), xytext=(8, -25), textcoords="offset points")
    ll_ax.annotate(f"{likelihood[-1]:.6f}", (6, likelihood[-1]), xytext=(-5, 12), textcoords="offset points", ha="right")
    ll_ax.text(3, trap_likelihood + 0.14, f"{trap_likelihood:.6f}", ha="center", color="#555555")
    ll_ax.set(xlabel="Completed E/M iterations t", ylabel="Observed-data log-likelihood", ylim=(-15.1, -9.75), xticks=iterations)
    ll_ax.legend(loc="center right", fontsize=10, frameon=False)
    for j, color in enumerate(["#2467a1", "#d06b22"]):
        mean_ax.plot(iterations, history[:, j], "o-", color=color, lw=2, label=rf"$\mu_{j+1}^{{(t)}}$")
        mean_ax.text(5.9, history[-1, j] + (0.13 if j else -0.22), f"{history[-1, j]:.6f}", ha="right", color=color)
    mean_ax.axhline(0, color="#666666", ls="--", label="Both means: trapped at 0")
    mean_ax.set(xlabel="Completed E/M iterations t", ylabel="Component mean", ylim=(-2.15, 2.15), xticks=iterations)
    mean_ax.legend(loc="upper right", bbox_to_anchor=(1, 0.73), fontsize=10, frameon=False)
    for ax in (ll_ax, mean_ax):
        ax.grid(axis="y", color="#e5e5e5", lw=0.7)
        ax.set_axisbelow(True)
    fig.text(0.5, 0.055, r"Chosen data: −2.2, −1.8, −1, 1, 1.8, 2.2; fixed weights 1/2 and known $\sigma=1$", ha="center", fontsize=11)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.85, bottom=0.17, wspace=0.33)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
