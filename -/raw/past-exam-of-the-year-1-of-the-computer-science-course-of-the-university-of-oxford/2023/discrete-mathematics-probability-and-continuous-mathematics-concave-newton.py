"""Original illustrative Newton geometry, not a function supplied by the exam.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. Write the matching PNG to CWD.
f(x)=-1000+x-1000 log(cosh(x/2500)) has f'(0)=1, f'' in [-0.00016,0),
and f'>0.6 everywhere, so it satisfies the examination's stated bounds.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    u = np.asarray(x) / 2500
    return -1000 + np.asarray(x) - 1000 * (np.logaddexp(u, -u) - np.log(2))


def df(x):
    return 1 - 0.4 * np.tanh(np.asarray(x) / 2500)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    left, right = 1000.0, 2000.0
    for _ in range(60):
        midpoint = (left + right) / 2
        if f(midpoint) < 0:
            left = midpoint
        else:
            right = midpoint
    root = (left + right) / 2
    x0 = 0.0
    x1 = x0 - f(x0) / df(x0)
    x2 = x1 - f(x1) / df(x1)
    assert x0 < x1 < x2 < root < 2000
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.6), dpi=100)
    fig.patch.set_facecolor("white")
    for ax, interval in zip(axs, [(0, 2000), (980, 1150)]):
        x = np.linspace(*interval, 600)
        ax.set_facecolor("white")
        ax.axhline(0, color="#777777", lw=1)
        ax.plot(x, f(x), color="#235b82", lw=2.5, label="Strictly concave f")
        ax.plot(x, f(x0) + df(x0)*(x-x0), color="#bd8040", lw=1.6, ls="--", label="Tangent at x₀")
        ax.plot(x, f(x1) + df(x1)*(x-x1), color="#3f8657", lw=1.6, ls="-.", label="Tangent at x₁")
        ax.axvline(root, color="#9a3f50", lw=1, ls=":")
        ax.set(xlim=interval, xlabel="x")
        ax.grid(alpha=0.16)
    axs[0].set(ylim=(-1100, 1100), ylabel="Function / tangent value", title="Tangents cross before the root")
    axs[0].scatter([x0, x1], [f(x0), 0], c="#bd8040", s=28, zorder=4)
    axs[0].annotate("x₁ = 1000", (x1, 0), (700, -450), arrowprops={"arrowstyle": "->"})
    axs[0].legend(fontsize=8.5, loc="upper left")
    axs[1].set(ylim=(-110, 85), title="Next step stays on the same side")
    axs[1].scatter([x1, x2, root], [0, 0, 0], c=["#bd8040", "#3f8657", "#9a3f50"], s=28, zorder=4)
    axs[1].annotate("x₁", (x1, 0), (990, 30), arrowprops={"arrowstyle": "->"})
    axs[1].annotate("x₂", (x2, 0), (1065, -60), arrowprops={"arrowstyle": "->"})
    axs[1].annotate("root x*", (root, 0), (1117, 45), arrowprops={"arrowstyle": "->"})
    fig.suptitle("Newton iteration from below a strictly increasing concave curve", fontsize=12.5, y=0.98)
    fig.text(0.035, 0.025, "Illustration: f(x) = −1000 + x − 1000 log cosh(x/2500); not an extra assumption about the exam's f.", fontsize=9)
    fig.subplots_adjust(left=0.085, right=0.985, top=0.85, bottom=0.16, wspace=0.19)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
