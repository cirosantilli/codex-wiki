"""Generate 2017-sticky-column-markov-chain.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.5), dpi=100, facecolor="white", gridspec_kw={"width_ratios": [1.15, 0.85, 1.1]})
    ax = axes[0]
    for k in range(4):
        ax.add_patch(Circle((k, 0), 0.20, facecolor="#dbeafe", edgecolor="#2563eb", lw=1.4))
        ax.text(k, 0, str(k), ha="center", va="center", fontsize=12)
        end = k+1
        ax.add_patch(FancyArrowPatch((k+0.23, 0), (end-0.23 if end<4 else 3.85, 0), arrowstyle="-|>", mutation_scale=12, color="#2563eb"))
        ax.text(k+0.5, 0.18, "1" if k==0 else "1/2", ha="center", fontsize=10)
    ax.text(4.04, 0, "…", ha="center", va="center", fontsize=17)
    for k, radius in [(1, 0.55), (2, 0.45), (3, 0.40)]:
        ax.add_patch(FancyArrowPatch((k-0.04, -0.22), (0.04, -0.22), connectionstyle=f"arc3,rad=-{radius}", arrowstyle="-|>", mutation_scale=12, color="#b91c1c", lw=1.1))
    ax.text(1.8, -1.0, "Every positive state resets\nto 0 with probability 1/2", ha="center", va="top", fontsize=10, color="#b91c1c")
    ax.set(xlim=(-0.30, 4.35), ylim=(-1.7, 0.85))
    ax.set_title("The difference is Markov", fontsize=11)
    ax.axis("off")
    k = np.arange(8)
    masses = np.r_[1/3, (1/3)*2.0**(-np.arange(7))]
    axes[1].bar(k, masses, color="#2563eb", width=0.72)
    axes[1].set_title("Stationary probabilities", fontsize=11)
    axes[1].set_xlabel("Difference k")
    axes[1].set_ylabel(r"$\pi_k$")
    axes[1].set_xticks([0, 2, 4, 6])
    axes[1].set_ylim(0, 0.39)
    axes[1].text(3.4, 0.31, r"$\pi_0=1/3$", fontsize=11)
    for seed, color in [(7, "#2563eb"), (21, "#15803d"), (35, "#a16207")]:
        rng = np.random.default_rng(seed)
        heights = [0, 0]
        values = []
        for step in range(1, 4001):
            side = int(rng.integers(0, 2))
            heights[side] = max(heights[side]+1, heights[1-side])
            values.append(max(heights)/step)
        axes[2].plot(np.arange(20, 4001), values[19:], color=color, lw=0.9, alpha=0.8)
    axes[2].axhline(2/3, color="#111827", lw=1.5, ls="--", label=r"Proved limit $2/3$")
    axes[2].set(xlim=(20, 4000), ylim=(0.45, 0.87), xlabel="Number of blocks n", ylabel=r"$H_n/n$")
    axes[2].set_title("Growth averages along three paths", fontsize=11)
    axes[2].legend(fontsize=9, loc="upper right")
    for ax in axes[1:]:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.18)
    fig.suptitle("Sticky columns: a stationary difference controls the growth rate", fontsize=14, y=0.96)
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.16, top=0.80, wspace=0.32)
    fig.savefig("2017-sticky-column-markov-chain.png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
