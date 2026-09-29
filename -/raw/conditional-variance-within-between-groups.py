"""Original exact within/between-group variance example; PNG to cwd."""
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), layout="constrained")
    for y, values, mean, color in [(1, [0, 4], 2, "#315f86"), (0, [6, 10], 8, "#b5702b")]:
        axes[0].plot(values, [y, y], color=color, lw=2)
        axes[0].scatter(values, [y, y], color=color, s=70, zorder=3)
        axes[0].scatter([mean], [y], color=color, marker="x", s=90, linewidths=2, zorder=4)
        for value in values:
            axes[0].text((value+mean)/2, y+.12, "−2" if value<mean else "+2", ha="center", fontsize=11)
        axes[0].text(mean, y-.17, f"group mean {mean}", ha="center", fontsize=10)
    axes[0].axvline(6.5, color="#a12a40", lw=1.5, ls="--", label="Overall mean = 6.5")
    axes[0].set(xlim=(-1, 11), ylim=(-.4, 1.45), xlabel="X", yticks=[0, 1],
                yticklabels=["Group B: probability 3/4", "Group A: probability 1/4"], title="Within each group: variance 4")
    axes[0].legend(loc="upper left", fontsize=9)
    axes[0].grid(axis="x", alpha=.2)
    axes[1].bar([0], [10.75], color="#6a8195", width=.55)
    axes[1].bar([1], [4], color="#315f86", width=.55, label="Remaining within-group variance")
    axes[1].bar([1], [6.75], bottom=[4], color="#20814e", width=.55, label="Variance of group means")
    axes[1].text(0, 11.0, "43/4 = 10.75", ha="center", fontsize=11)
    axes[1].text(1, 2, "4", ha="center", va="center", color="white", fontsize=14)
    axes[1].text(1, 7.375, "27/4 = 6.75", ha="center", va="center", color="white", fontsize=12)
    axes[1].set(xticks=[0, 1], xticklabels=["Total variance", "Conditioning decomposition"],
                ylim=(0, 13), ylabel="Variance / expected squared error", title="Total = within + between")
    axes[1].legend(loc="upper left", fontsize=8)
    axes[1].grid(axis="y", alpha=.2)
    fig.suptitle("Knowing the group removes variation of the conditional means from prediction error", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
