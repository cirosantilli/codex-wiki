"""Original analytical illustration; tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; the output filename follows this generator's stem.
No observations or external image assets are used.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.6), layout="constrained")
    fig.suptitle("Two-node Gauss–Legendre quadrature", fontsize=17)
    x = np.linspace(-1, 1, 601)
    nodes = np.array([-1, 1]) / np.sqrt(3)
    left.plot(x, (3*x*x - 1)/2, color="#2366a0", lw=2.5,
              label=r"$P_2(x)=(3x^2-1)/2$")
    left.axhline(0, color="0.45", lw=1)
    left.scatter(nodes, [0, 0], s=65, color="#b64b23", zorder=4,
                 label="Sampling nodes")
    for node, label in zip(nodes, [r"$-1/\sqrt{3}$", r"$1/\sqrt{3}$"]):
        left.annotate(label + "\nweight = 1", (node, 0), xytext=(0, 22),
                      textcoords="offset points", ha="center", color="#833617")
    left.set(xlim=(-1.05, 1.05), ylim=(-0.62, 1.2), xlabel="$x$",
             ylabel=r"$P_2(x)$", title="Nodes are orthogonal-polynomial roots")
    left.set_xticks([-1, 0, 1])
    left.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), frameon=False)

    powers = np.arange(5)
    exact = np.array([2, 0, 2/3, 0, 2/5])
    sampled = np.array([np.sum(nodes**int(k)) for k in powers])
    right.bar(powers - 0.16, exact, width=0.30, color="#2366a0", label="Integral I")
    right.bar(powers + 0.16, sampled, width=0.30, color="#b64b23", label="Rule Q")
    right.scatter([0.84, 1.16, 2.84, 3.16], [0, 0, 0, 0],
                  c=["#2366a0", "#b64b23"]*2, s=24, zorder=4)
    right.text(0, 2.08, "2 = 2", ha="center")
    right.text(1, 0.12, "0 = 0", ha="center")
    right.text(2, 0.77, "2/3 = 2/3", ha="center")
    right.text(3, 0.12, "0 = 0", ha="center")
    right.text(4, 0.53, "2/5 ≠ 2/9", ha="center", color="#833617")
    right.set(ylim=(0, 2.35), xlabel="Monomial degree k", ylabel="Value",
              title=r"Compare $I(x^k)$ with $Q(x^k)$")
    right.set_xticks(powers)
    right.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17),
                 frameon=False, ncol=2)
    fig.supxlabel("Analytical illustration: exact through degree 3; degree 4 fails.",
                  fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=100, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
