"""Plot exact quadratic quadrature errors with a log-log slope triangle.

Run from _media; outputs quadrature-quadratic-errors-and-slope.png to CWD.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    counts = 2 ** np.arange(7)
    midpoint, trapezoidal = [], []
    for n in counts:
        edges = np.linspace(0, 1, n + 1)
        midpoints = (edges[:-1] + edges[1:]) / 2
        midpoint.append(abs(np.sum(midpoints**2) / n - 1 / 3))
        trapezoidal.append(abs((np.sum(edges[1:-1]**2) + 0.5) / n - 1 / 3))
    np.testing.assert_allclose(midpoint, 1 / (12 * counts**2), rtol=1e-11)
    np.testing.assert_allclose(trapezoidal, 1 / (6 * counts**2), rtol=1e-11)
    np.testing.assert_allclose(np.array(midpoint[:-1]) / midpoint[1:], 4, rtol=1e-11)
    fig, ax = plt.subplots(figsize=(8.2, 5.2), layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_xscale("log", base=2)
    ax.set_yscale("log", base=2)
    ax.plot(counts, trapezoidal, "o-", color="#b65716", label=r"$|T_n-I|=1/(6n^2)$", lw=2)
    ax.plot(counts, midpoint, "s-", color="#2166a3", label=r"$|M_n-I|=1/(12n^2)$", lw=2)
    ax.set_xticks(counts, [str(n) for n in counts])
    ticks = 2.0 ** np.arange(-16, -1, 2)
    ax.set_yticks(ticks, [f"$2^{{{int(np.log2(t))}}}$" for t in ticks])
    ax.grid(which="major", color="#e3e6e9")
    ax.spines[["top", "right"]].set_visible(False)
    # The triangle has log2 horizontal displacement 1 and vertical displacement -2.
    x0, y0 = 8, 1 / 16
    ax.plot([x0, 2 * x0, 2 * x0, x0], [y0, y0, y0 / 4, y0], color="#434a53", lw=1.5)
    ax.text(11.3, y0 * 1.3, r"$n\times2$", ha="center", fontsize=12)
    ax.text(17.5, y0 / 2, "error ÷ 4", va="center", fontsize=12)
    ax.text(11, y0 / 6, r"slope $=-2/1=-2$", ha="center", fontsize=12)
    ax.set(xlim=(0.85, 80), ylim=(2**-16, 0.3), xlabel="Number of equal panels $n$", ylabel=r"Absolute error against $I=\int_0^1 x^2\,dx=1/3$")
    ax.legend(loc="lower left", fontsize=12, framealpha=1)
    ax.set_title("Exact samples of $x^2$ on $[0,1]$: order two", fontsize=15)
    fig.supxlabel("These are exact error laws for this polynomial; they do not certify an unknown integrand.", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
