"""Original charge-lattice ambiguity; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; emits oil-drop-charge-lattice-identifiability.png in CWD.
All readings are simulated and expressed in an arbitrary reference charge.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    y = np.array([2.03, 2.96, 5.02, 3.99])
    sigma = 0.08
    n = np.array([2, 3, 5, 4])
    fit = np.dot(n, y) / np.dot(n, n)
    chi2 = np.sum(((y - n * fit) / sigma) ** 2)
    assert np.isclose(fit, 1.0) and np.isclose(chi2, 0.46875)
    assert np.allclose(n * fit, (2 * n) * (fit / 2))
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (ax, score) = plt.subplots(2, 1, figsize=(9, 6.8),
                                   gridspec_kw={"height_ratios": [1.4, 1.6]})
    for row, a, color in [(2, 1.0, "#1864ab"), (1, 0.5, "#087f5b")]:
        lattice = np.arange(0, 5.6, a)
        ax.plot(lattice, np.full_like(lattice, row), "|", ms=18,
                color=color, mew=1.5)
        ax.errorbar(y, np.full(4, row + 0.17), xerr=sigma, fmt="o",
                    capsize=4, color="#d9480f", ms=5)
        labels = np.rint(y / a).astype(int)
        for loc, label in zip(y, labels):
            ax.text(loc, row + 0.43, str(label), ha="center", color=color)
    ax.set(yticks=[1, 2], yticklabels=[r"$a=1/2$", r"$a=1$"],
           ylim=(0.35, 2.85), xlim=(0, 5.6), xlabel=r"Simulated $|q|/Q_*$")
    ax.set_title("Same fitted charges; doubled integer labels", fontsize=12)
    ax.text(0.5, 0.03, "Both: χ² = 0.46875; bars = one standard uncertainty",
            transform=ax.transAxes, ha="center", fontsize=10)
    candidates = np.linspace(0.35, 1.6, 12000)
    assignments = np.rint(y[:, None] / candidates)
    loss = np.sum(((y[:, None] - assignments * candidates) / sigma) ** 2, axis=0)
    score.plot(candidates, loss, color="#495057", lw=1)
    score.plot([0.5, 1], [chi2, chi2], "o", color="#d9480f", zorder=3)
    for a, label in [(0.5, "1/2"), (1.0, "1")]:
        score.annotate(label, (a, chi2), xytext=(a + 0.07, 13),
                       arrowprops={"arrowstyle": "->", "color": "#d9480f"},
                       color="#d9480f")
    score.set(xlim=(0.35, 1.6), ylim=(-1.5, 90),
              xlabel=r"Candidate spacing $a$ (in units of $Q_*$)",
              ylabel="Minimum χ² over integer counts")
    score.grid(alpha=0.18)
    fig.suptitle("A finite lattice fit does not identify a minimal charge", fontsize=15)
    fig.text(0.5, 0.018, "Simulation: a smaller candidate unit permits larger integer counts.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.045, 1, 0.95), h_pad=2)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
