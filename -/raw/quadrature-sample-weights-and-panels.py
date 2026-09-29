"""Compare quadrature panels and the weights of their actual samples.

Run from _media; outputs quadrature-sample-weights-and-panels.png to CWD.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.8), layout="constrained")
    fig.set_facecolor("white")
    curve = np.linspace(0, 1, 501)
    for row, n in enumerate((1, 2)):
        edges = np.linspace(0, 1, n + 1)
        for col, method in enumerate(("Midpoint", "Trapezoidal")):
            ax = axes[row, col]
            color = "#2166a3" if col == 0 else "#b65716"
            ax.set_facecolor("white")
            if col == 0:
                nodes = (edges[:-1] + edges[1:]) / 2
                weights = np.full(n, 1 / n)
                for left, right, node in zip(edges[:-1], edges[1:], nodes):
                    ax.fill_between([left, right], node**2, color=color, alpha=0.16)
                    ax.plot([left, left, right, right], [0, node**2, node**2, 0], color=color)
                value = np.dot(weights, nodes**2)
                np.testing.assert_allclose(value, 1 / 3 - 1 / (12 * n**2))
                answer = "1/4" if n == 1 else "5/16"
                weight_labels = ["1" if n == 1 else "1/2"] * n
            else:
                nodes = edges
                weights = np.full(n + 1, 1 / n)
                weights[[0, -1]] /= 2
                ax.fill_between(nodes, nodes**2, color=color, alpha=0.16)
                ax.plot(nodes, nodes**2, color=color)
                for node in nodes:
                    ax.plot([node, node], [0, node**2], color=color, lw=1)
                value = np.dot(weights, nodes**2)
                np.testing.assert_allclose(value, 1 / 3 + 1 / (6 * n**2))
                answer = "1/2" if n == 1 else "3/8"
                weight_labels = ["1/2", "1/2"] if n == 1 else ["1/4", "1/2", "1/4"]
            np.testing.assert_allclose(weights.sum(), 1)
            ax.plot(curve, curve**2, color="#252b32", lw=2, label=r"$f(x)=x^2$")
            ax.scatter(nodes, nodes**2, s=38, color=color, zorder=4, clip_on=False)
            ax.axhline(0, color="#49525c", lw=0.8)
            # A separate strip records nodes and weights, not extra function values.
            ax.axhline(-0.18, color="#b9c0c7", lw=0.8)
            ax.scatter(nodes, np.full_like(nodes, -0.18), color=color, s=25, clip_on=False)
            for node, label in zip(nodes, weight_labels):
                ax.text(node, -0.27, "$" + label + "$", ha="center", va="center", fontsize=11)
            symbol = "M" if col == 0 else "T"
            ax.set_title(f"{method}, {n} panel{'s' if n > 1 else ''}: ${symbol}_{n}={answer}$", fontsize=12)
            ax.set(xlim=(-0.06, 1.06), ylim=(-0.34, 1.09), xlabel="$x$", ylabel="Height")
            ax.set_xticks([0, 0.25, 0.5, 0.75, 1], ["0", "1/4", "1/2", "3/4", "1"])
            ax.set_yticks([0, 0.5, 1])
            ax.spines[["top", "right", "bottom"]].set_visible(False)
            ax.grid(axis="y", color="#e3e6e9", zorder=0)
            if row == 0 and col == 0:
                ax.legend(loc="upper left", fontsize=10, framealpha=1)
    fig.suptitle(r"Same exact integral $I=1/3$, different samples and weights", fontsize=15)
    fig.supxlabel("Dots below each graph show sample locations; fractions give quadrature weights.", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
