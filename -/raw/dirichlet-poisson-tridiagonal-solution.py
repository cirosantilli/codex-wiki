"""Plot an original quadratic Poisson solution and exact Thomas mesh values.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; the output basename matches this generator.
"""

from fractions import Fraction as F
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def mesh_solution():
    p, g = [F(2)], [F(9, 8)]
    for rhs in [F(1, 8), F(17, 8)]:
        m = -1 / p[-1]
        p.append(2 + m)
        g.append(rhs - m * g[-1])
    u = [F(0)] * 3
    u[-1] = g[-1] / p[-1]
    for i in range(1, -1, -1):
        u[i] = (g[i] + u[i + 1]) / p[i]
    assert p == [F(2), F(3, 2), F(4, 3)]
    assert u == [F(23, 16), F(7, 4), F(31, 16)]
    return [F(1), *u, F(2)]


def main():
    nodes = np.linspace(0, 1, 5)
    values = np.array([float(v) for v in mesh_solution()])
    x = np.linspace(0, 1, 301)
    fig, ax = plt.subplots(figsize=(8, 4.8), facecolor="white")
    ax.plot(x, 1 + 2*x - x*x, color="#27618c", lw=2.4, label="Exact solution: $u(x)=1+2x-x^2$")
    ax.plot(nodes, values, "--", color="#aaa", lw=1.3, label="Straight segments joining mesh values")
    ax.scatter(nodes[1:-1], values[1:-1], s=70, color="#c76a1b", zorder=4,
               label="Interior values from Thomas elimination")
    ax.scatter(nodes[[0, -1]], values[[0, -1]], s=65, facecolors="white", edgecolors="#27618c",
               linewidths=2, zorder=5, label="Prescribed Dirichlet endpoints")
    for i, text in enumerate([r"$1$", r"$23/16$", r"$7/4$", r"$31/16$", r"$2$"]):
        ax.annotate(text, (nodes[i], values[i]), xytext=(0, 12 if i != 3 else -23),
                    textcoords="offset points", ha="center", fontsize=12)
    ax.set(xlim=(-.045, 1.045), ylim=(.9, 2.36), xlabel="$x$", ylabel="$u$",
           xticks=nodes, title=r"$-u''=2$,  $u(0)=1$,  $u(1)=2$; mesh spacing $h=1/4$")
    ax.grid(alpha=.2)
    ax.legend(loc="upper left", fontsize=9, framealpha=1)
    fig.tight_layout(pad=1.1)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
