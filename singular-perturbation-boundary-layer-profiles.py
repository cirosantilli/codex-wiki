"""Plot exact boundary-layer profiles; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media: the opaque PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def exact_profile(x, epsilon):
    """Normalize with expm1, including when epsilon is not asymptotically small."""
    return np.expm1(-np.asarray(x) / epsilon) / np.expm1(-1.0 / epsilon)


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9, 5.4), layout="constrained")
    x = np.unique(np.concatenate((np.linspace(0, 1, 1801),
                                  np.geomspace(1e-6, 1, 1200))))
    colors = ("#0072B2", "#D55E00", "#009E73")
    for epsilon, color in zip((0.2, 0.05, 0.01), colors):
        ax.plot(x, exact_profile(x, epsilon), color=color, linewidth=2.6,
                label=rf"Exact, $\epsilon={epsilon:g}$")
        ax.scatter([epsilon], [exact_profile(epsilon, epsilon)],
                   color=color, s=42, zorder=4)
    ax.axhline(1, color="#333333", linestyle="--", linewidth=1.6,
               label=r"Outer approximation $y_0=1$")
    ax.scatter([0], [0], color="black", s=36, zorder=5)
    ax.annotate("All exact profiles satisfy y(0) = 0", xy=(0, 0),
                xytext=(0.26, 0.17), arrowprops={"arrowstyle": "->", "color": "#555555"},
                fontsize=11)
    ax.text(0.33, 0.39, r"Dots mark $x=\epsilon$: about 63% of the rise." + "\n"
            + r"Smaller $\epsilon$ compresses the transition toward $x=0$.",
            fontsize=11)
    ax.set(xlim=(-0.008, 1.01), ylim=(-0.035, 1.07), xlabel=r"Outer coordinate $x$",
           ylabel=r"Solution $y_\epsilon(x)$",
           title=r"A thin boundary layer repairs the left boundary condition")
    ax.grid(alpha=0.18)
    ax.legend(loc="center right", bbox_to_anchor=(0.99, 0.62), frameon=False,
              fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
