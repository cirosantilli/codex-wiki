"""Visualize integral_0^1 x exp(x) dx = e - (e - 1), tested on Python 3.14.4.

Run from the desired output directory; uses the root pyproject dependencies.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 1, 2001)
    desired = x * np.exp(x)
    remaining = np.exp(x)
    total = desired + remaining
    computed = np.trapezoid(desired, x)
    assert abs(computed - 1) < 1e-7
    assert abs(np.trapezoid(remaining, x) - np.expm1(1)) < 1e-7
    assert abs(np.trapezoid(total, x) - np.e) < 2e-7

    blue, green = "#277da8", "#3b8963"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.3), dpi=130,
                             constrained_layout=True, facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(0, 1), ylim=(0, 5.8), xlabel="x", ylabel="height")
        ax.set_xticks([0, .25, .5, .75, 1])
        ax.grid(alpha=.14)
    left, right = axes
    left.fill_between(x, 0, desired, color=blue, alpha=.27)
    left.plot(x, desired, color=blue, lw=2.3, label=r"$xe^x$")
    left.set_title("The integral we want")
    left.text(.53, .43, "Area = 1", ha="center", color=blue, weight="bold")
    left.text(.08, 4.3, r"$\int_0^1 xe^x\,dx=e-(e-1)=1$", fontsize=12)
    left.legend(loc="upper left", frameon=False)
    right.fill_between(x, 0, remaining, color=green, alpha=.25)
    right.fill_between(x, remaining, total, color=blue, alpha=.27)
    right.plot(x, total, color="#333333", lw=2.3,
               label=r"$(xe^x)'=(1+x)e^x$")
    right.plot(x, remaining, color=green, lw=2, label=r"$e^x$")
    right.set_title(r"Endpoint contribution: $[xe^x]_0^1=e$")
    right.text(.48, .7, r"Remaining area $=e-1$", ha="center", color=green)
    right.annotate("Upper band area = 1", xy=(.79, 3.1), xytext=(.12, 3.7),
                   color=blue, arrowprops={"arrowstyle": "->", "color": blue})
    right.legend(loc="upper left", frameon=False, fontsize=10)
    fig.savefig(Path.cwd() / "integration-by-parts-example.png",
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Integral x exp(x): {computed:.10f}; endpoint: {np.e:.10f}; "
          f"remaining: {np.expm1(1):.10f}")


if __name__ == "__main__":
    main()
