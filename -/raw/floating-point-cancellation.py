"""Compare two evaluations of sqrt(1+x)-1; write an opaque PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Run via Makefile: make _media/floating-point-cancellation.png
References use Decimal.from_float(x), so both algorithms solve the same input.
"""

from decimal import Decimal, localcontext
from math import sqrt
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


def reference(x, precision=100):
    with localcontext() as context:
        context.prec = precision
        d = Decimal.from_float(float(x))
        return d / ((1 + d).sqrt() + 1)


def measurements(xs):
    direct, rearranged, ratios, errors = [], [], [], []
    with localcontext() as context:
        context.prec = 100
        for x in xs:
            x = float(x)
            r = reference(x)
            values = [sqrt(1.0 + x) - 1.0,
                      x / (sqrt(1.0 + x) + 1.0)]
            direct.append(values[0])
            rearranged.append(values[1])
            ratios.append([float(Decimal.from_float(v) / r) for v in values])
            errors.append([float(abs(Decimal.from_float(v) - r) / r)
                           for v in values])
            # Higher precision checks the reference beyond plot resolution.
            r160 = reference(x, 160)
            assert abs(r - r160) / r160 < Decimal("1e-95")
    return np.array(direct), np.array(rearranged), np.array(ratios), np.array(errors)


def main():
    assert sys.float_info.radix == 2 and sys.float_info.mant_dig == 53
    assert sys.float_info.rounds == 1
    xs = np.unique(np.r_[np.logspace(-16, -1, 301),
                         [1e-16, 1e-12, 1e-8, 1e-4, 1e-1]])
    direct, rearranged, ratios, errors = measurements(xs)
    assert direct[0] == 0.0 and errors[0, 0] == 1.0
    assert np.all(rearranged > 0) and np.max(errors[:, 1]) < 4e-16

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9), layout="constrained")
    fig.patch.set_facecolor("white")
    labels = [r"Direct: $\sqrt{1+x}-1$",
              r"Rearranged: $x/(\sqrt{1+x}+1)$"]
    colors = ["#b43b35", "#2166ac"]
    for column, (label, color) in enumerate(zip(labels, colors)):
        axes[0].semilogx(xs, ratios[:, column], color=color, lw=1.5,
                        label=label)
        positive = errors[:, column] > 0
        axes[1].loglog(xs[positive], errors[positive, column], color=color,
                      lw=1.3, label=label)
        # Never disguise a zero error as a small positive error on a log axis.
        if np.any(~positive):
            axes[1].plot(xs[~positive], np.full(np.count_nonzero(~positive), 0.02),
                         "v", color=color, transform=axes[1].get_xaxis_transform(),
                         label=f"Zero error: {['direct', 'rearranged'][column]}")
    axes[0].axhline(1, color="0.4", ls=":", lw=1)
    axes[0].set(ylim=(-0.08, max(1.5, float(ratios.max()) + 0.1)),
                ylabel="Computed value / high-precision reference",
                title="The direct formula can return zero")
    axes[0].annotate("x = 10⁻¹⁶: direct result = 0", (xs[0], 0),
                     xytext=(1e-13, 0.24), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": colors[0]})
    axes[1].axhline(2.0**-53, color="0.4", ls=":", lw=1,
                    label=r"Unit roundoff $u=2^{-53}$")
    axes[1].set(ylim=(1e-20, 3), ylabel="Relative error (log scale)",
                title="Rearrangement preserves small results")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(1e-16, 1e-1), xlabel="Positive input x (log scale)")
        ax.set_xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e-1])
        ax.grid(which="major", alpha=0.16)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(loc="upper right", fontsize=9)
    axes[1].legend(loc="upper right", fontsize=9)
    fig.suptitle("Same real function, same binary64 input, different arithmetic\n"
                 "Reference: 100-digit Decimal, verified at 160 digits", fontsize=14)
    fig.savefig(Path.cwd() / "floating-point-cancellation.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
