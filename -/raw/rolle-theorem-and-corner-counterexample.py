"""Compare a smooth Rolle example with a nondifferentiable corner.

Run from _media to save the opaque PNG there. Python 3.14; NumPy/Matplotlib.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.4), dpi=120,
                             constrained_layout=True)
    x = np.linspace(0, 2, 450)
    left = axes[0]
    left.plot(x, x*(x-2), color="#235789", linewidth=2.8,
              label=r"$f(x)=x(x-2)$")
    left.plot([0, 2], [0, 0], color="#287a51", linestyle="--",
              linewidth=2, label=r"secant: $y=0$")
    left.plot([0.3, 1.7], [-1, -1], color="#b63c45", linewidth=2.2,
              label=r"tangent: $y=-1$")
    left.scatter([0, 2], [0, 0], color="#287a51", s=50, zorder=5)
    left.scatter([1], [-1], color="#b63c45", s=50, zorder=5)
    left.annotate(r"$c=1$, $f'(1)=0$", (1, -1), xytext=(0.28, -0.65),
                  arrowprops={"arrowstyle": "->", "color": "#555555"})
    left.set(xlim=(-0.15, 2.15), ylim=(-1.25, 0.85),
             title="Smooth: Rolle's theorem applies", xlabel=r"$x$", ylabel=r"$y$")
    left.set_xticks([0, 1, 2])
    left.legend(loc="upper center", fontsize=10)

    right = axes[1]
    x = np.linspace(-1, 1, 451)
    right.plot(x, np.abs(x), color="#235789", linewidth=2.8,
               label=r"$f(x)=|x|$")
    right.plot([-1, 1], [1, 1], color="#287a51", linestyle="--",
               linewidth=2, label=r"secant: $y=1$")
    right.scatter([-1, 1], [1, 1], color="#287a51", s=50, zorder=5)
    right.scatter([0], [0], color="#b63c45", s=50, zorder=5)
    right.text(-0.89, 0.28, r"$f'=-1$", color="#235789")
    right.text(0.37, 0.28, r"$f'=1$", color="#235789")
    right.annotate("No derivative at 0", (0, 0), xytext=(-0.78, -0.29),
                   arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=11)
    right.set(xlim=(-1.15, 1.15), ylim=(-0.42, 1.65),
              title="Corner: differentiability fails", xlabel=r"$x$", ylabel=r"$y$")
    right.set_xticks([-1, 0, 1])
    right.legend(loc="upper center", fontsize=10)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / "rolle-theorem-and-corner-counterexample.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
