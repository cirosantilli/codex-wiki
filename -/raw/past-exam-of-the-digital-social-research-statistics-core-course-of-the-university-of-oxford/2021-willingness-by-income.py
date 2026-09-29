"""Derived comparisons from the 2021 Statistics Core printed survey counts.

Source: Oxford A14564W1, Figures 2--8, using the first two willingness
categories combined as agreement. These are aggregate survey summaries,
not individual observations or estimates of vaccine efficacy. Output goes
to the current working directory. Dependencies: root pyproject.toml.
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def wilson(successes, totals, z=1.959963984540054):
    """Individual, not simultaneous, 95% binomial score intervals."""
    p = successes / totals
    denominator = 1 + z * z / totals
    centre = (p + z * z / (2 * totals)) / denominator
    radius = z * np.sqrt(p * (1 - p) / totals + z * z / (4 * totals**2)) / denominator
    return centre - radius, centre + radius


def main():
    # Rows: six ordered income strata; groups: recorded Male, Female.
    # Columns: strongly agree, agree, neutral, disagree, strongly disagree.
    counts = np.array([
        [[8, 9, 12, 9, 6], [13, 12, 18, 10, 20]],
        [[9, 19, 23, 9, 18], [25, 22, 29, 17, 41]],
        [[25, 23, 21, 8, 15], [28, 32, 34, 24, 35]],
        [[30, 26, 16, 12, 18], [42, 24, 46, 29, 35]],
        [[28, 24, 18, 8, 17], [12, 20, 22, 9, 20]],
        [[264, 185, 92, 39, 51], [105, 133, 116, 45, 75]],
    ], dtype=float)
    n = counts.sum(axis=2)
    successes = counts[:, :, :2].sum(axis=2)
    p = successes / n
    pooled_weights = n.sum(axis=1) / n.sum()
    standardized = (p * pooled_weights[:, None]).sum(axis=0)
    crude = successes.sum(axis=0) / n.sum(axis=0)
    assert counts.sum() == 2135
    assert np.array_equal(counts.sum(axis=0), [[364, 286, 182, 85, 125], [225, 243, 265, 134, 226]])

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                         "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.6), dpi=100,
                             gridspec_kw={"width_ratios": [1.35, 1]}, layout="constrained")
    colours = ["#2964a0", "#c46c22"]
    for g, (label, colour, offset) in enumerate(zip(["Male", "Female"], colours, [-0.09, 0.09])):
        low, high = wilson(successes[:, g], n[:, g])
        axes[0].errorbar(np.arange(6) + offset, p[:, g] * 100,
                         yerr=np.array([p[:, g] - low, high - p[:, g]]) * 100,
                         fmt="o", color=colour, capsize=3, label=label)
    axes[0].set(xticks=np.arange(6), xticklabels=["<10k", "10–<20k", "20–<30k", "30–<40k", "40–<50k", "50k+"],
                xlabel="Household income (USD/year)", ylabel="Agree or strongly agree (%)",
                ylim=(15, 85), title="Within-income agreement\nIndividual 95% Wilson intervals")
    axes[0].grid(axis="y", alpha=0.22)
    axes[0].legend(loc="upper left", frameon=False)

    for g, (label, colour) in enumerate(zip(["Male", "Female"], colours)):
        values = np.array([crude[g], standardized[g]]) * 100
        bars = axes[1].bar(np.arange(2) + (g - 0.5) * 0.28, values, width=0.28, color=colour, label=label)
        axes[1].bar_label(bars, labels=[f"{value:.2f}%" for value in values], padding=3, fontsize=10)
    for i, gap in enumerate([crude[0] - crude[1], standardized[0] - standardized[1]]):
        axes[1].text(i, 73, f"Gap: {gap * 100:.2f} pp", ha="center", weight="bold")
    axes[1].set(xticks=[0, 1], xticklabels=["Observed\nincome mixes", "Same pooled\nincome mix"],
                ylabel="Agree or strongly agree (%)", ylim=(0, 83), title="Separate composition from\na common-weight comparison")
    axes[1].grid(axis="y", alpha=0.18)
    axes[1].set_axisbelow(True)
    fig.suptitle("Historical survey willingness: October 2020", fontsize=14)
    output = Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": output, "dimensions": [1240, 460], "n": int(n.sum()),
                      "crude_rates": crude.tolist(), "common_weight_rates": standardized.tolist(),
                      "common_income_weights": pooled_weights.tolist(), "within_income_rates": p.tolist()}))


if __name__ == "__main__":
    main()
