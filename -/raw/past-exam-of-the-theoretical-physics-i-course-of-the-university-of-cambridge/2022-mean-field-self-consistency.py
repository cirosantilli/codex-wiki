"""Plot the spin-1 mean-field equation; write the PNG to the current directory.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from the matching _media directory, using the repository pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def response(spin, temperature_ratio):
    argument = 1.5 * spin / temperature_ratio
    return 2 * np.sinh(argument) / (1 + 2 * np.cosh(argument))


def positive_root(temperature_ratio):
    lower, upper = 1e-8, 1.0
    for _ in range(70):
        middle = (lower + upper) / 2
        if response(middle, temperature_ratio) > middle:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def main():
    spin = np.linspace(-1.0, 1.0, 801)
    ratios = (1.3, 1.0, 0.8)
    labels = ("Above the transition", "At the transition", "Below the transition")
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.5), sharex=True, sharey=True)
    fig.set_facecolor("white")
    for ax, ratio, label in zip(axes, ratios, labels):
        ax.plot(spin, spin, color="0.35", linestyle="--", linewidth=1.4, label=r"$S$")
        ax.plot(spin, response(spin, ratio), color="#1764ab", linewidth=2.1, label=r"$G_T(S)$")
        if ratio < 1:
            root = positive_root(ratio)
            ax.scatter([-root, root], [-root, root], color="#b44725", s=34, zorder=4)
            ax.scatter([0], [0], facecolor="white", edgecolor="#b44725", s=34, zorder=4)
        else:
            ax.scatter([0], [0], color="#b44725", s=34, zorder=4)
        ax.axhline(0, color="0.85", linewidth=0.7, zorder=0)
        ax.axvline(0, color="0.85", linewidth=0.7, zorder=0)
        ax.set_title(label + "\n" + rf"$T/T_c={ratio:g}$", fontsize=11)
        ax.set_xlabel(r"Assumed mean spin $S$")
        ax.set_xlim(-1.02, 1.02)
        ax.set_ylim(-1.02, 1.02)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.set_aspect("equal")
        ax.spines[["right", "top"]].set_visible(False)
    axes[0].set_ylabel("Single-site response")
    axes[0].legend(loc="upper left", frameon=False, fontsize=9)
    fig.suptitle(r"Spin-1 mean field: $G_T(S)=2\sinh[3S/(2T/T_c)]\,/\,\{1+2\cosh[3S/(2T/T_c)]\}$", fontsize=11)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.18, top=0.76, wspace=0.34)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
