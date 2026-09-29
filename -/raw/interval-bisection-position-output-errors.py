"""Compare position certificates and output residuals for an analytic toy.

Write the matching PNG to the CWD; run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib. Tested with Python 3.14.4,
Matplotlib 3.10.7 and NumPy 2.3.5. Fractions drive every search decision.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, red, green = "#2166ac", "#bd4c32", "#28855d"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    a, b = Fraction(0), Fraction(3)
    bounds, errors, residuals = [], [], []
    for k in range(13):
        m = (a + b) / 2
        r = m**3 + m - 10
        bounds.append(float((b - a) / 2))
        errors.append(float(abs(m - 2)))
        residuals.append(float(abs(r)))
        assert b - a == Fraction(3, 2**k)
        assert abs(m - 2) <= (b - a) / 2
        if r < 0:
            a = m
        else:
            b = m

    fig, (decay, geometry) = plt.subplots(1, 2, figsize=(10.1, 4.7), layout="constrained")
    fig.suptitle("Position error and output residual are different quantities", fontsize=15)
    k = np.arange(13)
    decay.semilogy(k, bounds, color=blue, lw=2, label=r"Position bound $W_k/2$")
    decay.semilogy(k, errors, "o-", color=green, markersize=4, label=r"Position error $|m_k-2|$")
    decay.semilogy(k, residuals, "s--", color=red, markersize=4, label=r"Output residual $|f(m_k)-10|$")
    decay.axhline(1e-3, color="#777777", lw=1, ls=":")
    decay.text(0.3, 1.2e-3, "Position tolerance 0.001", fontsize=9, color="#555555")
    decay.set(xlabel="Completed halvings k", ylabel="Magnitude (log scale)",
              xticks=[0, 2, 4, 6, 8, 10, 12], title="Exact cubic toy; not measured data")
    decay.legend(fontsize=9, frameon=False, loc="upper right")
    decay.grid(alpha=0.17, which="both")

    m = Fraction(63, 32)
    fm = m**3 + m
    assert fm - 10 == -Fraction(13121, 32768)
    x = np.linspace(1.93, 2.05, 300)
    geometry.plot(x, x**3 + x, color=blue, lw=2.3)
    geometry.axhline(10, color="#bbbbbb", lw=1)
    geometry.scatter([float(m), 2], [float(fm), 10], color=[blue, green], zorder=5)
    geometry.plot([float(m), float(m)], [float(fm), 10], color=red, lw=1.4)
    geometry.annotate("", xy=(1.956, 10), xytext=(1.956, float(fm)),
                      arrowprops={"arrowstyle": "<->", "color": red, "lw": 1.7})
    geometry.text(1.951, float((fm + 10) / 2), "Output residual\n≈ 0.400421", color=red,
                  ha="right", va="center", fontsize=10)
    geometry.plot([2, 2], [9.25, 10], color=green, lw=1, ls=":")
    geometry.plot([float(m), float(m)], [9.25, float(fm)], color=blue, lw=1, ls=":")
    geometry.annotate("", xy=(2, 9.32), xytext=(float(m), 9.32),
                      arrowprops={"arrowstyle": "<->", "color": green, "lw": 1.7})
    geometry.text(float((m + 2) / 2), 9.24, "Position error = 1/32", ha="center",
                  va="top", fontsize=10, color=green)
    geometry.text(2.004, 10.02, "x* = 2", color=green, fontsize=10)
    geometry.text(float(m) + 0.002, float(fm) - 0.05, "m₄ = 63/32", fontsize=10, color=blue)
    geometry.set(xlim=(1.9, 2.058), ylim=(9.07, 10.8), xlabel="Input x", ylabel="Output f(x)",
                 title="After four halvings", xticks=[1.92, 1.96, 2.00, 2.04])
    geometry.grid(alpha=0.14)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
