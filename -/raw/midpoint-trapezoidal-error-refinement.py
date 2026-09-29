"""Plot exact quadratic quadrature errors and a controlled sample-bias model.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    panels = 2 ** np.arange(8)
    midpoint_errors, trapezoid_errors, biased_errors = [], [], []
    bias = 0.002
    for n in panels:
        x = np.linspace(0, 1, n + 1)
        midpoints = (x[:-1] + x[1:]) / 2
        m = np.sum(midpoints**2) / n
        t = (np.sum(x[1:-1]**2) + (x[0]**2 + x[-1]**2) / 2) / n
        observed = x**2 + bias
        biased_t = (np.sum(observed[1:-1]) + (observed[0] + observed[-1]) / 2) / n
        midpoint_errors.append(1 / 3 - m)
        trapezoid_errors.append(t - 1 / 3)
        biased_errors.append(biased_t - 1 / 3)
    midpoint_errors = np.asarray(midpoint_errors)
    trapezoid_errors = np.asarray(trapezoid_errors)
    biased_errors = np.asarray(biased_errors)
    np.testing.assert_allclose(midpoint_errors, 1 / (12 * panels**2), rtol=1e-10)
    np.testing.assert_allclose(trapezoid_errors, 1 / (6 * panels**2), rtol=1e-10)
    np.testing.assert_allclose(biased_errors, trapezoid_errors + bias, rtol=1e-10)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.4), layout="constrained")
    fig.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_xticks(panels, labels=[str(n) for n in panels])
        ax.set(xlabel="Number of panels $n$", ylabel="Absolute error against $I=1/3$")
        ax.grid(which="major", color="#e4e7eb")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].plot(panels, trapezoid_errors, "o-", color="#b75a16", label="$T_n-I=1/(6n^2)$")
    axes[0].plot(panels, midpoint_errors, "s-", color="#236aa0", label="$I-M_n=1/(12n^2)$")
    axes[0].set_title("Exact samples: errors fall by four\nwhen the panel count doubles", fontsize=12)
    axes[1].plot(panels, biased_errors, "o-", color="#b75a16", label="Samples $x_i^2+0.002$")
    axes[1].plot(panels, trapezoid_errors, "--", color="#757b83", label="Exact samples")
    axes[1].axhline(bias, color="#7b3e8c", lw=1.5, label="Common bias $\\delta=0.002$")
    axes[1].set_title("Biased samples: refinement leaves a floor\n$T_n^{\\mathrm{obs}}-I=1/(6n^2)+\\delta$", fontsize=12)
    for ax in axes:
        ax.legend(loc="lower left", fontsize=9, facecolor="white", framealpha=1)
    fig.suptitle("Composite quadrature for $f(x)=x^2$ on $[0,1]$", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
