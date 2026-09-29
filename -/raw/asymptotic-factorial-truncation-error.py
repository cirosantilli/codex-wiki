"""Original finite-parameter truncation errors of a divergent factorial series.

Reference integral computed by 96-node Gauss-Laguerre quadrature, independently
checked in work validation. No measured data. Tested with Python 3.14,
NumPy 2.3.5 and Matplotlib 3.10.7. Write basename.png to the CWD.
"""
from pathlib import Path
import math

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, ax = plt.subplots(figsize=(8.8, 4.9), dpi=120)
    fig.patch.set_facecolor("white")
    nodes, weights = np.polynomial.laguerre.laggauss(96)
    orders = np.arange(1, 27)
    colors = ["#c65102", "#2166ac", "#238b45", "#8e3c8f"]
    for z, color in zip([4, 8, 10, 16], colors):
        exact = float(weights @ (1/(1+nodes/z)))
        values = [sum((-1)**k*math.factorial(k)/z**k for k in range(n))
                  for n in orders]
        errors = np.abs(np.array(values)-exact)
        ax.semilogy(orders, errors, color=color, linewidth=2.4, label=f"z = {z}")
        minimum = int(np.argmin(errors))
        ax.scatter(orders[minimum], errors[minimum], color=color, s=55, zorder=5)
        ax.annotate(f"N = {orders[minimum]}", (orders[minimum], errors[minimum]),
                    xytext=(0, -24 if z == 8 else 12),
                    textcoords="offset points", ha="center", color=color, fontsize=10)
    ax.set(xlabel="Number N of retained terms", ylabel="Absolute error (log scale)",
           title="More terms help at first, then make the answer worse",
           xlim=(0.5, 26.5), xticks=[1, 4, 8, 10, 16, 20, 26])
    ax.grid(alpha=0.22)
    ax.legend(loc="upper left", fontsize=11)
    fig.suptitle(r"$S_N(z)=\sum_{k=0}^{N-1}(-1)^k k!/z^k$", fontsize=17)
    fig.subplots_adjust(left=0.11, right=0.975, bottom=0.15, top=0.79)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
