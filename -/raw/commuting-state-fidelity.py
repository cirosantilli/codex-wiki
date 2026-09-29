"""Compare commuting mixed-state probabilities, overlap contributions, and distances.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Build with: make _media/commuting-state-fidelity.png
Writes an opaque white PNG with this script's basename to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    p, q = np.array([0.9, 0.1]), np.array([0.6, 0.4])
    contributions = np.sqrt(p * q)
    fidelity = contributions.sum()
    squared = fidelity**2
    distance = np.abs(p - q).sum() / 2
    assert np.isclose(fidelity, np.sqrt(0.54) + 0.2)
    assert np.isclose(distance, 0.3)
    assert 1 - fidelity <= distance <= np.sqrt(1 - squared)

    fig, axes = plt.subplots(1, 3, figsize=(11, 4.7),
                             gridspec_kw={"width_ratios": [1, 1, 1.1]})
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.24, top=0.71, wspace=0.4)
    fig.suptitle("Commuting mixed states: classical probabilities and quantum fidelity",
                 fontsize=14, y=0.98)
    fig.text(0.5, 0.87, r"$\rho=\mathrm{diag}(0.9,0.1),\quad\sigma=\mathrm{diag}(0.6,0.4)$",
             ha="center", fontsize=13)
    for ax in axes:
        ax.set_axisbelow(True)
        ax.grid(axis="y", color="#e5e5e5", lw=0.7)
        ax.set_ylim(0, 1.06)
        ax.set_yticks([0, 0.5, 1])

    positions = np.arange(2)
    for offset, values, color, label in (
        (-0.18, p, "#2171a5", r"$p_i$ from $\rho$"),
        (0.18, q, "#d17a15", r"$q_i$ from $\sigma$"),
    ):
        bars = axes[0].bar(positions + offset, values, width=0.34, color=color, label=label)
        axes[0].bar_label(bars, fmt="%.1f", padding=3)
    axes[0].set_xticks(positions, ["0", "1"])
    axes[0].set(xlabel="Common-basis outcome i", ylabel="Probability")
    axes[0].set_title("Outcome distributions", pad=12, fontsize=12)
    axes[0].legend(loc="upper center", bbox_to_anchor=(0.5, -0.25), frameon=False,
                   ncol=2, fontsize=9)

    bars = axes[1].bar(positions, contributions, width=0.55, color=["#388357", "#81ad8f"])
    axes[1].bar_label(bars, fmt="%.4f", padding=3)
    axes[1].set_xticks(positions, [r"$\sqrt{0.9\cdot0.6}$", r"$\sqrt{0.1\cdot0.4}$"])
    axes[1].set(ylabel=r"Contribution $\sqrt{p_iq_i}$", xlabel="Sum = unsquared F ≈ 0.9348")
    axes[1].set_title("Square-root overlaps", pad=12, fontsize=12)

    values = [fidelity, squared, distance]
    bars = axes[2].bar(np.arange(3), values, width=0.6,
                       color=["#2171a5", "#d17a15", "#388357"])
    axes[2].bar_label(bars, fmt="%.4f", padding=3)
    axes[2].set_xticks(np.arange(3), ["F\nunsquared", r"$F_{\mathrm{sq}}$" + "\nsquared", "D\ntrace dist."])
    axes[2].set_title("Comparison values", pad=12, fontsize=12)
    fig.text(0.65, 0.04,
             r"$1-F\approx0.0652\ \leq\ D=0.3\ \leq\ \sqrt{1-F^2}\approx0.3551$",
             ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
