"""Plot nested-grid exponential quadrature; run from _media with Python 3.14.

Requires NumPy and Matplotlib; writes the matching PNG basename to cwd.
Decimal quadrature sums at 70 digits keep the convergence plot free of floors.
"""

from decimal import Decimal, localcontext
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def trapezoid(n):
    step = Decimal(1) / n
    return step * ((Decimal(1) + Decimal(1).exp()) / 2
                   + sum((Decimal(j) * step).exp() for j in range(1, n)))


def main():
    n_values = np.array([1, 2, 4, 8, 16, 32, 64, 128])
    coarse_errors, fine_errors, combined_errors = [], [], []
    with localcontext() as context:
        context.prec = 70
        exact = Decimal(1).exp() - 1
        for n in n_values:
            coarse = trapezoid(int(n))
            fine = trapezoid(int(2 * n))
            combined = (4 * fine - coarse) / 3
            coarse_errors.append(float(abs(coarse - exact)))
            fine_errors.append(float(abs(fine - exact)))
            combined_errors.append(float(abs(combined - exact)))
    assert min(combined_errors) > 0
    plt.rcParams.update({"font.size": 10})
    fig, (area, error) = plt.subplots(1, 2, figsize=(9.6, 4.5), layout="constrained")
    x = np.linspace(0, 1, 401)
    coarse_x = np.linspace(0, 1, 3)
    fine_x = np.linspace(0, 1, 5)
    area.fill_between(fine_x, np.exp(fine_x), color="#cddfea", alpha=1,
                      label=r"Fine trapezoids ($T_4$)")
    area.plot(fine_x, np.exp(fine_x), color="#24679b", lw=1.6)
    area.plot(coarse_x, np.exp(coarse_x), "--", color="#586c7a", lw=1.4,
              label=r"Coarse panels ($T_2$)")
    area.plot(x, np.exp(x), color="#212121", lw=2, label=r"Exact curve $e^x$")
    for node in fine_x:
        area.plot([node, node], [0, np.exp(node)], color="#8ea6b8", lw=0.8)
    area.scatter(coarse_x, np.exp(coarse_x), color="#24679b", s=45, zorder=4,
                 label="Reused coarse nodes")
    area.scatter(fine_x[1::2], np.exp(fine_x[1::2]), color="#c35724", s=45,
                 zorder=4, label="Added midpoints")
    area.set(xlabel="x", ylabel="Function value", xlim=(-0.04, 1.04), ylim=(0, 3.65),
             title="Nested grids: n = 2 and 2n = 4")
    area.legend(loc="upper left", fontsize=8, framealpha=1)
    error.loglog(n_values, coarse_errors, "o-", color="#24679b", ms=4,
                  label=r"Coarse $T_n$: order 2")
    error.loglog(n_values, fine_errors, "s--", color="#587c94", ms=4,
                  label=r"Fine $T_{2n}$: order 2")
    error.loglog(n_values, combined_errors, "o-", color="#c35724", ms=4,
                  label=r"$S_{2n}=(4T_{2n}-T_n)/3$: order 4")
    error.set(xlabel="Coarse panel count n (fine count 2n)", ylabel="Absolute integral error",
              title=r"Exact integral: $e-1$")
    error.set_xticks(n_values, [str(n) for n in n_values])
    error.grid(which="major", color="#dce1e5", lw=0.8)
    error.legend(loc="lower left", fontsize=8, framealpha=1)
    fig.suptitle("Richardson cancellation turns trapezoidal quadrature into Simpson's rule", fontsize=12)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
