"""Generate survival-hazard-relationship.png in CWD; Python 3.14, NumPy, Matplotlib.

Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
The time coordinate is in years; hazard coefficients carry inverse-time units.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 10, 1001)
    models = [
        ("Constant: h(t) = 0.2 / year", "#007c83",
         np.full_like(t, 0.2), 0.2 * t),
        ("Increasing: h(t) = (0.04 / year²) × t", "#b35422",
         0.04 * t, 0.02 * t**2),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 4.4), dpi=110,
                             facecolor="white")
    for label, color, hazard, accumulated in models:
        survival = np.exp(-accumulated)
        # Check accumulation by trapezoidal integration and the density by
        # differentiating the survival curve, away from endpoint stencils.
        integrated = np.r_[0, np.cumsum((hazard[1:] + hazard[:-1])
                                       * np.diff(t) / 2)]
        assert np.allclose(integrated, accumulated, atol=1e-12)
        assert np.allclose(-np.gradient(survival, t)[1:-1],
                           (hazard * survival)[1:-1], atol=2e-6)
        assert np.isclose(survival[-1], np.exp(-2))
        for ax, values in zip(axes, (hazard, accumulated, survival)):
            ax.plot(t, values, color=color, lw=2.6, label=label)
            ax.plot(5, values[500], "o", color=color, ms=5)
    axes[0].set(title="Instantaneous rate h(t)", ylabel="Hazard (1 / year)",
                ylim=(0, 0.44))
    axes[1].set(title="Accumulated rate H(t)",
                ylabel="Cumulative hazard (dimensionless)", ylim=(0, 2.2))
    axes[2].set(title="Event-free probability S(t)",
                ylabel="Survival probability", ylim=(0, 1.08))
    axes[1].annotate("H(5) = 1", (5, 1), xytext=(1.3, 1.35),
                     color=models[0][1], fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": models[0][1]})
    axes[1].annotate("H(5) = 0.5", (5, 0.5), xytext=(5.2, 0.15),
                     color=models[1][1], fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": models[1][1]})
    axes[2].annotate("S(5) = 0.607", (5, np.exp(-0.5)), xytext=(5.5, 0.85),
                     color=models[1][1], fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": models[1][1]})
    axes[2].annotate("S(5) = 0.368", (5, np.exp(-1)), xytext=(0.4, 0.16),
                     color=models[0][1], fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": models[0][1]})
    for ax in axes:
        ax.set(xlim=(0, 10), xlabel="Time t (years)")
        ax.set_xticks([0, 2, 4, 6, 8, 10])
        ax.set_facecolor("white")
        ax.grid(color="#e6e6e6", lw=0.7)
        ax.spines[["top", "right"]].set_visible(False)
        ax.title.set_fontsize(11)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.92),
               ncol=2, frameon=False, fontsize=10)
    fig.suptitle("Integrate the rate, then exponentiate: S(t) = exp[−H(t)]",
                 fontsize=13, y=0.985)
    fig.text(0.5, 0.03,
             "Both survival curves decrease. At year 10 both reach exp(−2) ≈ 0.135, "
             "despite different hazard histories.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.76, bottom=0.18, wspace=0.36)
    fig.savefig(Path.cwd() / "survival-hazard-relationship.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
