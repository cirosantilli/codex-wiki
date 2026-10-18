"""Plot the published age fit and an algebraic residual consistency check.

Oxford A14564W1 (2021), Figure 9, prints the fitted coefficients, observed
age/response ranges, and residual minimum used here. No raw observations
are reconstructed. Output goes to CWD; dependencies: root pyproject.toml.
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    intercept, slope = 12.645291, 0.016489
    ages = np.linspace(19, 91, 250)
    fitted = intercept + slope * ages
    # A response of 1 is reported as attained, not merely a possible bound.
    # Its residual is at most 1 - min(fitted); every residual is at least
    # 1 - max(fitted), giving necessary bounds on the sample minimum.
    necessary = np.array([1 - fitted.max(), 1 - fitted.min()])
    printed_minimum = -10.014
    assert printed_minimum > necessary[1]
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                         "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.3), dpi=100,
                             gridspec_kw={"width_ratios": [1, 1.25]}, layout="constrained")
    axes[0].plot(ages, fitted, color="#2964a0", linewidth=2.5)
    axes[0].set(xlabel="Age (years)", ylabel="Fitted willingness score",
                xlim=(19, 91), ylim=(0, 21), title="Published straight-line fit\nObserved ages only")
    axes[0].grid(alpha=0.2)
    axes[0].text(21, 4, "72-year fitted contrast:\n1.187 score points", fontsize=11)
    axes[0].text(21, 18.2, "No individual observations shown", fontsize=10)

    axes[1].hlines(0, necessary[0], necessary[1], color="#2964a0", linewidth=5)
    axes[1].plot(necessary, [0, 0], "|", color="#2964a0", markersize=15, markeredgewidth=2)
    axes[1].plot(printed_minimum, 1, "o", color="#b33b32", markersize=9)
    axes[1].axvline(necessary[1], color="#2964a0", linestyle=":", alpha=0.6)
    axes[1].text(necessary.mean(), -0.18, f"[{necessary[0]:.3f}, {necessary[1]:.3f}]", ha="center", fontsize=10)
    axes[1].text(printed_minimum, 1.13, f"{printed_minimum:.3f}", ha="center", color="#b33b32")
    axes[1].set(yticks=[0, 1], yticklabels=["Any compatible\nresidual minimum", "Printed residual\nminimum"],
                xlabel="Residual (score points)", xlim=(-13.65, -9.35), ylim=(-0.42, 1.6),
                title="The attained response minimum gives\na necessary algebraic constraint")
    axes[1].spines["left"].set_visible(False)
    axes[1].tick_params(axis="y", length=0)
    axes[1].text(-13.5, 1.48, "The printed summaries cannot all describe the same fit.", fontsize=10)
    output = Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": output, "dimensions": [1180, 430], "fitted_range": [float(fitted.min()), float(fitted.max())],
                      "necessary_residual_minimum_interval": necessary.tolist(), "printed_residual_minimum": printed_minimum,
                      "72_year_fitted_contrast": float(72 * slope)}))


if __name__ == "__main__":
    main()
