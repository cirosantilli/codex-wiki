"""Plot the distinct parallel secant and tangent promised by the MVT.

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
    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=120, constrained_layout=True)
    x = np.linspace(0.85, 3.15, 450)
    ax.plot(x, x**2, color="#235789", linewidth=2.8, label=r"$f(x)=x^2$")
    ax.plot(x, 4*x-3, color="#287a51", linewidth=2.2,
            linestyle="--", label=r"secant: $y=4x-3$")
    ax.plot(x, 4*x-4, color="#b63c45", linewidth=2.2,
            label=r"tangent: $y=4x-4$")
    ax.scatter([1, 3], [1, 9], color="#287a51", s=55, zorder=5)
    ax.scatter([2], [4], color="#b63c45", s=55, zorder=5)
    ax.annotate(r"$(1,1)$", (1, 1), xytext=(1.10, 0.35))
    ax.annotate(r"$(3,9)$", (3, 9), xytext=(2.60, 9.35))
    ax.annotate(r"$c=2$: $f'(2)=4$", (2, 4), xytext=(2.20, 2.05),
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.text(0.045, 0.63, "Both lines have slope 4\nTheir heights differ by 1",
            transform=ax.transAxes, fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "#cccccc", "pad": 6})
    ax.set(xlim=(0.85, 3.15), ylim=(-0.9, 10), xlabel=r"$x$", ylabel=r"$y$",
           title="Mean value theorem: matching slopes")
    ax.set_xticks([1, 2, 3])
    ax.grid(alpha=0.16)
    ax.legend(loc="upper left", fontsize=11)
    ax.set_facecolor("white")
    fig.savefig(Path.cwd() / "mean-value-theorem-secant-and-tangent.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
