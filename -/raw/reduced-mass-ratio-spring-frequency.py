"""Draw reduced mass and free-spring frequency versus partner mass ratio.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes the matching PNG basename to the current directory.
The mass and frequency scales are dimensionless model predictions.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    q = np.geomspace(0.1, 100, 600)
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.3), layout="constrained")
    mass, frequency = axes
    mass.plot(q, q / (1 + q), lw=2.5, color="#1765a0")
    mass.set(title=r"Reduced mass: $\mu/m_1=q/(1+q)$",
             ylabel=r"Reduced mass $\mu/m_1$", ylim=(0, 1.15))
    mass.axhline(1, color="#666666", ls="--", lw=1.3)
    mass.text(0.13, 1.035, r"Heavy-partner limit: $\mu\to m_1$", fontsize=10)
    mass.scatter([1, 100], [0.5, 100 / 101], color="#1765a0", s=45, zorder=4)
    mass.annotate(r"Equal masses: $1/2$", (1, 0.5), xytext=(1.8, 0.28),
                  arrowprops={"arrowstyle": "->", "color": "#1765a0"}, fontsize=10)
    mass.annotate(r"$100/101\approx0.9901$", (100, 100 / 101), xytext=(4, 0.77),
                  arrowprops={"arrowstyle": "->", "color": "#1765a0"}, fontsize=10)
    frequency.plot(q, np.sqrt(1 + 1 / q), lw=2.5, color="#b84b17")
    frequency.set(title=r"Free spring: $\omega/\sqrt{k/m_1}=\sqrt{1+1/q}$",
                  ylabel=r"Frequency / fixed-end value $\sqrt{k/m_1}$", ylim=(0.83, 3.55))
    frequency.axhline(1, color="#666666", ls="--", lw=1.3)
    frequency.scatter([1, 100], [np.sqrt(2), np.sqrt(1.01)],
                      color="#b84b17", s=45, zorder=4)
    frequency.annotate(r"Equal masses: $\sqrt{2}$", (1, np.sqrt(2)), xytext=(2.5, 2.22),
                       arrowprops={"arrowstyle": "->", "color": "#b84b17"}, fontsize=10)
    frequency.annotate(r"$q=100$: 0.499% above limit", (100, np.sqrt(1.01)), xytext=(1.5, 1.7),
                       arrowprops={"arrowstyle": "->", "color": "#b84b17"}, fontsize=10)
    frequency.text(0.13, 0.88, "Fixed-end limit = 1", fontsize=10)
    for ax in axes:
        ax.set(xscale="log", xlim=(0.1, 145), xlabel=r"Partner mass ratio $q=m_2/m_1$")
        ax.set_xticks([0.1, 1, 10, 100], ["0.1", "1", "10", "100"])
        ax.grid(alpha=0.2)
    fig.suptitle(r"Hold the first mass $m_1$ and spring constant $k$ fixed", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
