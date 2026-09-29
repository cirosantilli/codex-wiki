"""Plot Gamma on the positive axis and its correctly shifted factorial values.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write an opaque white PNG to the current working directory.
"""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0.2, 6, 1000)
    y = np.array([math.gamma(float(value)) for value in x])
    integers = np.arange(1, 7)
    factorials = np.array([math.factorial(int(value) - 1) for value in integers])
    fig, ax = plt.subplots(figsize=(8.0, 4.8), dpi=130, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(x, y, color="#2866a3", lw=2.4, label=r"$\Gamma(x)$")
    ax.scatter(integers, factorials, color="#b84f24", s=45, zorder=3,
               label=r"$\Gamma(n)=(n-1)!$, integer $n\geq 1$")
    for n, value in zip(integers, factorials):
        offset = (-34, -20) if n == 6 else (5, 9 if n != 2 else 22)
        ax.annotate(f"{n-1}! = {value}", (n, value), xytext=offset,
                    textcoords="offset points", fontsize=9, color="#813718")
    ax.set(xlim=(0.2, 6.12), ylim=(-7, 133), xticks=integers,
           xlabel=r"Positive real argument $x$", ylabel=r"$\Gamma(x)$",
           title="Gamma interpolates factorials with a one-step shift")
    ax.legend(loc="upper left", frameon=False)
    ax.grid(alpha=0.17)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
