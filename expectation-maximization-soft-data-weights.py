"""Plot an original first E-step. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def responsibilities(x, means):
    log_joint = -0.5 * (x[:, None] - means[None, :]) ** 2 - np.log(2.0)
    maximum = log_joint.max(axis=1, keepdims=True)
    log_sum = maximum + np.log(np.exp(log_joint - maximum).sum(axis=1, keepdims=True))
    return np.exp(log_joint - log_sum)


def main():
    x = np.array([-2.2, -1.8, -1.0, 1.0, 1.8, 2.2])
    means = np.array([-1.0, 1.0])
    r = responsibilities(x, means)
    colors = ["#2467a1", "#d06b22"]
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    fig, (data_ax, weight_ax) = plt.subplots(
        2, 1, figsize=(9, 6.2), gridspec_kw={"height_ratios": [1, 3.1]}
    )
    fig.patch.set_facecolor("white")
    fig.suptitle("EM keeps both label probabilities for every observation", fontsize=16)
    data_ax.scatter(x, np.zeros_like(x), s=64, color="#333333", zorder=3)
    for value in x:
        data_ax.annotate(f"{value:g}", (value, 0), xytext=(0, 9), textcoords="offset points", ha="center")
    for j, mean in enumerate(means):
        data_ax.plot([mean, mean], [-0.35, -0.1], color=colors[j], lw=2)
        data_ax.text(mean, -0.48, rf"$\mu_{j+1}^{{(0)}}={mean:g}$", ha="center", color=colors[j])
    data_ax.set(xlim=(-2.7, 2.7), ylim=(-0.7, 0.45), yticks=[], xlabel="Chosen data values x")
    data_ax.spines["left"].set_visible(False)
    rows = np.arange(len(x))
    weight_ax.barh(rows, r[:, 0], color=colors[0], height=0.66, label=r"$r_{i1}$: component 1")
    weight_ax.barh(rows, r[:, 1], left=r[:, 0], color=colors[1], height=0.66, label=r"$r_{i2}$: component 2")
    for row, probabilities in enumerate(r):
        for j, probability in enumerate(probabilities):
            if probability >= 0.08:
                center = probability / 2 + (probabilities[0] if j else 0)
                weight_ax.text(center, row, f"{probability:.3f}", ha="center", va="center", color="white")
        weight_ax.text(1.025, row, f"({probabilities[0]:.4f}, {probabilities[1]:.4f})", va="center", fontsize=11)
    weight_ax.set(yticks=rows, yticklabels=[f"x = {value:g}" for value in x], xlim=(0, 1), xlabel="Conditional label probability (each row sums to 1)")
    weight_ax.invert_yaxis()
    weight_ax.legend(loc="upper center", bbox_to_anchor=(0.55, -0.2), ncol=2, frameon=False)
    fig.text(0.5, 0.035, r"Fixed weights 1/2, known $\sigma=1$; weighted counts $N_1=N_2=3$", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.13, right=0.72, top=0.89, bottom=0.2, hspace=0.63)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
