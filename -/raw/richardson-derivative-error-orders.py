"""Plot Richardson errors; run from _media with Python 3.14, NumPy, Matplotlib.

Outputs richardson-derivative-error-orders.png in the current directory.
Uses 70-digit Decimal Taylor sums to avoid a binary64 cancellation floor.
"""

from decimal import Decimal, localcontext
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def sinc(h):
    term = total = Decimal(1)
    for k in range(1, 60):
        term *= -h * h / Decimal(2 * k * (2 * k + 1))
        total += term
    return total


def main():
    h_values = np.geomspace(1e-3, 0.5, 130)
    raw, extrapolated = [], []
    with localcontext() as context:
        context.prec = 70
        for value in h_values:
            h = Decimal(str(value))
            a = sinc(h)
            r = (4 * sinc(h / 2) - a) / 3
            raw.append(float(abs(a - 1)))
            extrapolated.append(float(abs(r - 1)))
    assert min(raw) > 0 and min(extrapolated) > 0
    plt.rcParams.update({"font.size": 11})
    fig, ax = plt.subplots(figsize=(7.5, 5), layout="constrained")
    ax.loglog(h_values, raw, color="#24679b", lw=2.4, label=r"Centered: $|A(h)-1|$")
    ax.loglog(h_values, extrapolated, color="#c35724", lw=2.4,
              label=r"Extrapolated: $|R(h)-1|$")
    ax.loglog(h_values, h_values**2 / 6, "--", color="#163e5d", lw=1.2,
              label=r"Second-order guide: $h^2/6$")
    ax.loglog(h_values, h_values**4 / 480, "--", color="#71351b", lw=1.2,
              label=r"Fourth-order guide: $h^4/480$")
    ax.set(xlabel="Coarse step h (fine step h/2)", ylabel="Absolute error",
           title=r"Sine derivative at zero: $A(h)=\sin(h)/h$, exact value 1")
    ax.set_xlim(1e-3, 0.5)
    ax.grid(which="major", color="#dce1e5", lw=0.8)
    ax.legend(loc="upper left", fontsize=10, framealpha=1)
    ax.text(0.97, 0.04, "70-digit arithmetic\nNo artificial error floor",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=9,
            bbox={"facecolor": "white", "edgecolor": "#dce1e5", "pad": 5})
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
