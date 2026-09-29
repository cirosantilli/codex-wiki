"""Original fixed-order accuracy curves for a factorial asymptotic series.

F(z) = integral from zero to infinity of exp(-t)/(1+t/z) dt.
Numerical reference: 96-node Gauss-Laguerre quadrature, independently checked
against adaptive Simpson integration in the accompanying work validation.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Output basename.png to the current working directory.
"""
from pathlib import Path
import math

import matplotlib.pyplot as plt
import numpy as np


def integral_values(z):
    nodes, weights = np.polynomial.laguerre.laggauss(96)
    return np.array([weights @ (1/(1+nodes/value)) for value in z])


def partial_sum(z, n):
    return sum((-1)**k * math.factorial(k) / z**k for k in range(n))


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.6), dpi=120)
    fig.patch.set_facecolor("white")
    z = np.linspace(4, 32, 240)
    exact = integral_values(z)
    colors = {1: "#c65102", 3: "#2166ac", 5: "#238b45"}
    axes[0].plot(z, exact, color="#222222", linewidth=3, label="Integral F(z)")
    for n in [1, 3, 5]:
        approximation = partial_sum(z, n)
        axes[0].plot(z, approximation, color=colors[n], linewidth=2,
                     label=f"S{n}(z): {n} " + ("term" if n == 1 else "terms"))
        axes[1].semilogy(z, np.abs(approximation-exact), color=colors[n],
                         linewidth=2.5, label=f"N = {n}: actual error")
        axes[1].semilogy(z, math.factorial(n)/z**n, color=colors[n],
                         linestyle=":", linewidth=1.7)
    axes[0].set(xlabel="Positive parameter z", ylabel="Value",
                title="Hold the truncation order fixed", ylim=(0.80, 1.02))
    axes[1].set(xlabel="Positive parameter z", ylabel="Absolute error (log scale)",
                title=r"Dotted curves: proven bounds $N!/z^N$")
    for ax in axes:
        ax.set_xlim(4, 32)
        ax.grid(alpha=0.22)
        ax.legend(loc="lower right" if ax is axes[0] else "lower left", fontsize=10)
    fig.suptitle(r"$F(z)=\int_0^\infty e^{-t}/(1+t/z)\,dt$ and its factorial expansion",
                 fontsize=16)
    fig.subplots_adjust(left=0.07, right=0.985, bottom=0.15, top=0.80, wspace=0.31)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
