"""Plot likelihood comparisons for ten Bernoulli trials; Python 3.14."""

from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    p = np.linspace(0, 1, 2001)
    colors = {2: "#007c83", 5: "#7460a8", 8: "#c4511c"}
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.7), dpi=100,
                             facecolor="white")
    for k, color in colors.items():
        peak = k / 10
        raw = p**k * (1 - p)**(10 - k)
        peak_height = peak**k * (1 - peak)**(10 - k)
        relative = raw / peak_height
        with np.errstate(divide="ignore"):
            difference = k * np.log(p / peak) + (10 - k) * np.log(
                (1 - p) / (1 - peak))

        # Verify the plotted log comparison against the direct product, including
        # zero-height boundaries, rather than against another log formula.
        assert np.allclose(np.exp(difference), relative, rtol=1e-12, atol=1e-14)
        assert np.isclose(p[np.argmax(raw)], peak)
        assert raw[0] == raw[-1] == 0
        axes[0].plot(p, relative, color=color, lw=2.5,
                     label=f"k = {k}: fitted p = {peak:.1f}")
        axes[1].plot(p, difference, color=color, lw=2.5)
        for ax, height in zip(axes, (1, 0)):
            ax.plot(peak, height, "o", color=color, ms=5)
            ax.axvline(peak, color=color, lw=0.9, alpha=0.5, linestyle=":")

    assert comb(10, 8) == 45
    assert np.isclose(0.8**8 * 0.2**2, 0.0067108864)
    assert np.isclose(comb(10, 8) * 0.8**8 * 0.2**2, 0.301989888)
    assert np.isclose(np.trapezoid(p**8 * (1 - p)**2, p), 1 / 495,
                      rtol=1e-9, atol=1e-12)
    # All-failure/all-success samples have boundary maxima on the closed domain.
    assert p[np.argmax((1 - p)**10)] == 0
    assert p[np.argmax(p**10)] == 1

    axes[0].set(title="Relative likelihood: peak height = 1",
                ylabel="L(p) / L(fitted p)", ylim=(0, 1.08))
    axes[1].set(title="Log-likelihood difference: peak = 0",
                ylabel="ℓ(p) − ℓ(fitted p)", ylim=(-12, 0.8))
    axes[0].axhline(np.exp(-2), color="#777777", lw=1, linestyle="--")
    axes[1].axhline(-2, color="#777777", lw=1, linestyle="--")
    axes[0].text(0.98, np.exp(-2) + 0.02, "e⁻² ≈ 0.1353", ha="right",
                 fontsize=10, color="#555555")
    axes[1].text(0.98, -1.7, "−2 corresponds to e⁻²", ha="right",
                 fontsize=10, color="#555555")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.91),
               ncol=3, fontsize=9.5, frameon=False)
    for ax in axes:
        ax.set(xlim=(0, 1), xlabel="Unknown success probability p")
        ax.set_xticks(np.linspace(0, 1, 6))
        ax.grid(color="#e7e7e7", linewidth=0.7)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
        ax.title.set_fontsize(11)
    fig.suptitle("Ten independent Bernoulli trials: k = 2, 5, or 8 successes",
                 fontsize=13, y=0.97)
    fig.text(0.5, 0.08,
             "Neither vertical axis is a probability density over p. "
             "Ordered data and count data give the same rescaled curves.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.035,
             "At p = 0 and p = 1: L = 0 and ℓ = −∞ "
             "(outside the right panel's finite range).",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.23, top=0.77,
                        wspace=0.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
