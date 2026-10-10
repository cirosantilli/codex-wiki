"""Show absolute loss and the effect of replacing one chosen value.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the desired output directory; the PNG is written to the CWD.
The lists are chosen examples, not actual observations or a model check.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    blue, orange, green = "#176ca4", "#ce6010", "#267747"
    original = np.array([1, 2, 2, 5, 10])
    changed = np.array([1, 2, 2, 5, 100])
    a = np.sort(np.unique(np.r_[np.linspace(-1, 26, 1081), original, 2.0]))
    a = a[a <= 26]
    loss = np.abs(a[:, None] - original).sum(axis=1)
    changed_loss = np.abs(a[:, None] - changed).sum(axis=1)
    replacement = np.linspace(10, 100, 181)
    samples = np.tile(original.astype(float), (replacement.size, 1))
    samples[:, -1] = replacement
    means = samples.mean(axis=1)
    medians = np.median(samples, axis=1)

    fig, (objective, centers) = plt.subplots(1, 2, figsize=(10, 4.7), dpi=120)
    fig.patch.set_facecolor("white")
    fig.suptitle("One changed value: median stays, mean moves", fontsize=16, y=0.98)
    fig.text(0.5, 0.90, "Chosen illustration: [1, 2, 2, 5, 10] becomes [1, 2, 2, 5, 100]",
             ha="center", fontsize=11)
    for ax in (objective, centers):
        ax.set_facecolor("white")
        ax.grid(alpha=0.22)
        ax.spines[["top", "right"]].set_visible(False)

    objective.plot(a, loss - loss.min(), color=blue, lw=3,
                   label=r"Original: $\min S=12$")
    objective.plot(a, changed_loss - changed_loss.min(), color=orange, lw=2.2,
                   ls="--", label=r"After change: $\min S=102$")
    objective.scatter([2], [0], color=green, s=40, zorder=5)
    objective.annotate("Both minimized at 2", xy=(2, 0), xytext=(5, 23),
                       fontsize=10, arrowprops={"arrowstyle": "->", "color": green})
    objective.set(title="Absolute-loss objectives, aligned at minima",
                  xlabel=r"Candidate location $a$", ylabel=r"$S(a)-\min S$",
                  xlim=(-1, 26), ylim=(-4, 105))
    objective.set_xticks([0, 2, 10, 20, 26])
    objective.legend(loc="upper left", fontsize=10, frameon=False)

    centers.plot(replacement, means, color=orange, lw=2.5, label="Sample mean")
    centers.plot(replacement, medians, color=green, lw=2.5, label="Sample median")
    centers.scatter([10, 100], [4, 22], color=orange, s=35, zorder=5)
    centers.scatter([10, 100], [2, 2], color=green, marker="s", s=30, zorder=5)
    centers.text(12, 5.8, "Mean = 4", color=orange, fontsize=10)
    centers.text(97, 23, "Mean = 22", color=orange, ha="right", fontsize=10)
    centers.text(58, 3.3, "Median = 2 throughout", color=green, ha="center", fontsize=10)
    centers.set(title="Change only the largest value", xlabel="Replacement for 10",
                ylabel="Fitted center", xlim=(5, 105), ylim=(0, 26))
    centers.set_xticks([10, 25, 50, 75, 100])
    centers.legend(loc="upper left", frameon=False, fontsize=10)

    fig.text(0.5, 0.025,
             r"Not measured data. The fitted Laplace scale changes too: $12/5=2.4$ to $102/5=20.4$.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.19, top=0.79, wspace=0.32)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
