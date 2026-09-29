"""Plot the exact entropy budget for a symmetric four-symbol toy channel.

Save the PNG basename to cwd; run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib. Uses the repository's matplotlib/numpy
environment; tested with Python 3.14. No experimental data are used.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def binary_entropy(q):
    q = np.asarray(q, dtype=float)
    result = np.zeros_like(q)
    mask = (q > 0) & (q < 1)
    p = q[mask]
    result[mask] = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    return result


def main():
    q = np.linspace(0, 1, 1001)
    flag = binary_entropy(q)
    alternatives = q * np.log2(3)
    total = flag + alternatives
    assert np.isclose(total[750], 2)
    assert np.isclose(total[-1], np.log2(3))
    assert np.all(np.diff(total[:751]) > 0)
    assert np.all(np.diff(total[750:]) < 0)

    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9.0, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.21, top=0.85)
    ax.fill_between(q, 0, flag, color="#bfdcee", label=r"Error flag: $h_2(q)$")
    ax.fill_between(q, flag, total, color="#f8d494",
                    label=r"Wrong-symbol uncertainty: $q\log_2 3$")
    ax.plot(q, total, color="#163b61", linewidth=2.5,
            label=r"Total: $H(X\mid Y)=h_2(q)+q\log_2 3$")
    ax.plot(q, flag, color="#5790b4", linewidth=1.5)
    ax.axvline(0.75, color="#516275", linestyle="--", linewidth=1.3)
    for value in (0.3, 0.75, 1.0):
        height = float(binary_entropy([value])[0] + value * np.log2(3))
        ax.scatter([value], [height], color="#163b61", zorder=5, s=32)
    ax.annotate("q = 0.3\n1.3568 bits", (0.3, float(total[300])), (0.07, 1.65),
                arrowprops={"arrowstyle": "->", "color": "#516275"}, fontsize=11)
    ax.annotate("q = 3/4: independent\n2 bits (maximum)", (0.75, 2), (0.49, 2.14),
                arrowprops={"arrowstyle": "->", "color": "#516275"}, fontsize=11)
    ax.annotate("q = 1: always wrong\n1.5850 bits remain", (1, float(total[-1])), (0.69, 1.17),
                arrowprops={"arrowstyle": "->", "color": "#516275"}, fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9, "pad": 3})
    ax.set(xlim=(0, 1.01), ylim=(0, 2.42), xlabel="Error probability q of the identity decoder",
           ylabel="Conditional entropy (bits)", xticks=[0, 0.25, 0.5, 0.75, 1])
    ax.set_axisbelow(True)
    ax.grid(alpha=0.2)
    ax.legend(loc="lower left", fontsize=10, framealpha=0.95)
    fig.suptitle("Fano's bound is exact for this four-symbol toy model", fontsize=15, y=0.97)
    fig.text(0.5, 0.91, "Two uncertainties add; more raw errors need not mean more uncertainty",
             ha="center", fontsize=11, color="#516275")
    fig.text(0.5, 0.10,
             "Identity decoder minimizes error for 0 ≤ q ≤ 3/4; for q > 3/4, guess another symbol.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.045, "Uniform input; symmetric channel; theoretical probabilities, not measured data",
             ha="center", fontsize=10, color="#516275")
    fig.savefig(Path.cwd() / "fano-error-entropy-budget.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
