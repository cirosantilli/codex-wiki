"""Plot known-unit-variance normal mean likelihoods; Python 3.14."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    original = np.array([-1.0, 0.0, 2.0, 3.0])
    mu = np.linspace(-0.6, 2.6, 1601)
    samples = (
        (original, "#007c83", "n = 4: [−1, 0, 2, 3]"),
        (np.tile(original, 4), "#c4511c", "n = 16: four repetitions of that array"),
    )
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.7), dpi=100,
                             facecolor="white")
    for data, color, label in samples:
        n = len(data)
        mean = data.mean()
        assert mean == 1
        direct = -n / 2 * np.log(2 * np.pi) - 0.5 * np.sum(
            (data[:, None] - mu[None, :])**2, axis=0)
        peak = -n / 2 * np.log(2 * np.pi) - 0.5 * np.sum((data - mean)**2)
        difference = -n / 2 * (mu - mean)**2
        assert np.allclose(direct - peak, difference, atol=1e-12)
        assert np.isclose(mu[np.argmax(direct)], 1)
        width = np.sqrt(4 / n)
        assert np.isclose(-n / 2 * width**2, -2)
        axes[0].plot(mu, np.exp(difference), lw=2.7, color=color, label=label)
        axes[1].plot(mu, difference, lw=2.7, color=color,
                     label=f"n = {n}: curvature −ℓ″ = {n}")
        for ax, height in zip(axes, (np.exp(-2), -2)):
            ax.plot([1 - width, 1 + width], [height, height], "o",
                    color=color, ms=5)
        axes[0].annotate("", xy=(1 - width, np.exp(-2)),
                         xytext=(1 + width, np.exp(-2)),
                         arrowprops={"arrowstyle": "<->", "color": color,
                                     "lw": 1.6})

    assert np.sum((original - 1)**2) == 10
    assert np.isclose((2 * np.pi)**-2 * np.exp(-5), 0.000170674231586843)
    assert np.isclose(np.exp(-2), 0.1353352832366127)
    # Check observed curvature from the direct sums of squares at three means.
    for data, _, _ in samples:
        step = 0.01
        values = np.array([-0.5 * np.sum((data - m)**2)
                           for m in (1 - step, 1, 1 + step)])
        assert np.isclose(-(values[0] - 2 * values[1] + values[2]) / step**2,
                          len(data), rtol=1e-8)

    axes[0].set(title="Relative likelihood: narrower for n = 16",
                ylabel="L(μ) / L(1)", ylim=(0, 1.08))
    axes[1].set(title="Log-likelihood difference: −n(μ − 1)² / 2",
                ylabel="ℓ(μ) − ℓ(1)", ylim=(-12, 0.8))
    axes[0].axhline(np.exp(-2), color="#777777", lw=1, linestyle="--")
    axes[1].axhline(-2, color="#777777", lw=1, linestyle="--")
    axes[0].text(2.56, np.exp(-2) + 0.025, "e⁻²", ha="right", fontsize=10)
    axes[1].text(2.56, -1.7, "−2", ha="right", fontsize=10)
    for ax in axes:
        ax.set(xlim=(-0.6, 2.6), xlabel="Candidate mean μ (known σ = 1)")
        ax.axvline(1, color="#555555", lw=1, linestyle=":")
        ax.set_xticks([0, 0.5, 1, 1.5, 2])
        ax.grid(color="#e7e7e7", linewidth=0.7)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
        ax.title.set_fontsize(11)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.91),
               ncol=2, fontsize=9.5, frameon=False)
    axes[1].legend(loc="lower center", fontsize=9, framealpha=1)
    fig.suptitle("Constructed normal samples: fitted mean = 1, known variance = 1",
                 fontsize=13, y=0.97)
    fig.text(0.5, 0.08,
             "At relative height e⁻²: distance from the peak is 1 for n = 4, "
             "and ½ for n = 16. Width scales as 1/√n.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.035,
             "Each sample is modeled as independent observations. "
             "Copying recorded data does not create independent evidence.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.23, top=0.77,
                        wspace=0.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
