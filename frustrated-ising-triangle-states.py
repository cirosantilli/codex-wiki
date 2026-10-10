"""Draw an exactly enumerable Ising triangle; write the PNG to the cwd."""
from pathlib import Path
import itertools

import matplotlib.pyplot as plt
import numpy as np


def energy(spins):
    return sum(spins[i] * spins[(i + 1) % 3] for i in range(3))


def main():
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.4), layout="constrained")
    points = np.array([[0, 1], [-0.866, -0.5], [0.866, -0.5]])
    for ax, spins, title in zip(axes[:2], [(1, -1, 1), (1, 1, 1)],
                                 ["Ground state: one unsatisfied bond", "Aligned state: three unsatisfied bonds"]):
        for i in range(3):
            j = (i + 1) % 3
            bad = spins[i] == spins[j]
            ax.plot(*points[[i, j]].T, color="#d55e00" if bad else "#0072b2",
                    lw=4, ls="--" if bad else "-")
        for (x, y), spin in zip(points, spins):
            ax.scatter(x, y, s=850, c="white", edgecolors="#333333", zorder=3)
            ax.annotate("↑" if spin == 1 else "↓", (x, y), ha="center", va="center",
                        fontsize=29, zorder=4)
        ax.set_title(title, fontsize=12)
        ax.text(0, -0.91, f"Energy / J = {energy(spins):+d}", ha="center", fontsize=13)
        ax.set(xlim=(-1.3, 1.3), ylim=(-1.1, 1.5), aspect="equal")
        ax.axis("off")
    states = list(itertools.product((-1, 1), repeat=3))
    levels, counts = np.unique([energy(s) for s in states], return_counts=True)
    axes[2].bar(levels, counts, width=1.0, color=["#0072b2", "#d55e00"])
    axes[2].set(xticks=levels, yticks=range(7), ylim=(0, 7), xlabel="Energy / J",
                ylabel="Number of spin configurations", title="All eight configurations")
    for level, count in zip(levels, counts):
        axes[2].text(level, count + .12, str(count), ha="center", fontsize=13)
    fig.suptitle("Three antiferromagnetic Ising bonds cannot all be satisfied", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
