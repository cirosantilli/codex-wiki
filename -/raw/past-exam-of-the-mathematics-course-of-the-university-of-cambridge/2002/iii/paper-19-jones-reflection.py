"""Compare the computed Jones polynomial with its reflection; output to CWD."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    coefficients = {2: 1, 7: 1, 8: -1, 9: 1, 10: -1}
    fig, axes = plt.subplots(2, 1, figsize=(10, 4.8), sharex=True)
    for ax, data, name, color in (
        (axes[0], coefficients, "Knot: $V_K(t)$", "#2563a6"),
        (axes[1], {-k: v for k, v in coefficients.items()}, "Mirror: $V_K(t^{-1})$", "#ae4b32"),
    ):
        powers = np.array(sorted(data))
        ax.bar(powers, [data[k] for k in powers], width=0.55, color=color)
        ax.axhline(0, color="#4a4a4a", linewidth=0.8)
        ax.set_ylim(-1.35, 1.35)
        ax.set_yticks([-1, 0, 1])
        ax.set_ylabel("Coefficient")
        ax.set_title(name, loc="left", fontsize=11)
        ax.grid(axis="x", color="#dddddd", linewidth=0.6)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[1].set_xticks(range(-10, 11, 2))
    axes[1].set_xlabel("Exponent of $t$")
    axes[1].set_xlim(-11, 11)
    fig.suptitle("Different Jones polynomials distinguish the knot from its mirror", fontsize=13)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-19-jones-reflection.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
