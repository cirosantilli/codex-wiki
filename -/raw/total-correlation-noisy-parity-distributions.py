"""Plot exact stipulated noisy-parity laws; output matching PNG to CWD."""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    patterns = list(product((0, 1), repeat=3))
    labels = ["".join(map(str, p)) for p in patterns]
    colors = ["#28628e" if sum(p) % 2 == 0 else "#d0872e" for p in patterns]
    fig, axes = plt.subplots(3, 1, figsize=(9.5, 6.4), dpi=120,
        sharex=True, sharey=True, facecolor="white")
    for ax, epsilon in zip(axes, (0, 0.25, 0.5)):
        masses = [(1 - epsilon) / 4 if sum(p) % 2 == 0 else epsilon / 4
            for p in patterns]
        assert sum(masses) == 1
        ax.bar(range(8), masses, color=colors, width=0.66)
        ax.axhline(1 / 8, linestyle="--", color="#757575", linewidth=1)
        ax.set(ylim=(0, 0.30), yticks=(0, 0.125, 0.25), ylabel="Probability")
        ax.set_title(f"Parity-flip probability ε = {epsilon:g}", fontsize=11, loc="left")
        ax.grid(axis="y", alpha=0.15)
    axes[-1].set_xticks(range(8), labels, family="monospace", fontsize=11)
    axes[-1].set_xlabel("Joint outcome XYZ")
    fig.suptitle("Joint structure changes while every pair stays independent", fontsize=16)
    fig.text(0.5, 0.017,
        "Blue: even parity; orange: odd parity. Dashed line: independent three-bit law (1/8 per outcome).",
        ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.05, 1, 0.96))
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
