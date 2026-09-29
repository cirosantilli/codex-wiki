"""Draw Picard iterates; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes an opaque white picard-iteration-exponential.png to the current directory.
"""
from math import factorial
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0.0, 1.0, 501)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(7.6, 4.8), dpi=120,
                           constrained_layout=True, facecolor="white")
    colors = ["#777777", "#2378a6", "#d07b25", "#33865c", "#8555a5"]
    for n, color in enumerate(colors):
        values = sum(t ** k / factorial(k) for k in range(n + 1))
        endpoint = sum(1.0 / factorial(k) for k in range(n + 1))
        ax.plot(t, values, lw=2.2, color=color,
                label=rf"$y_{n}$: $y_{n}(1)={endpoint:.6f}$")
    ax.plot(t, np.exp(t), color="#222222", lw=2.2, ls="--",
            label=rf"$e^t$: $e={np.e:.6f}$")
    ax.set(title="Repeated integration builds the exponential\n"
                 r"$y'=y,\quad y(0)=1,\quad y_n(t)=\sum_{k=0}^n t^k/k!$",
           xlabel="time t", ylabel="trajectory value y",
           xlim=(0, 1.025), ylim=(0.9, 2.85))
    ax.text(0.49, 1.18, "At t = 1, the fourth iterate's error\n"
            f"is e − 65/24 = {np.e - 65 / 24:.8f}.", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 5})
    ax.legend(loc="upper left", framealpha=1, fontsize=10)
    ax.grid(alpha=0.15)
    ax.set_facecolor("white")
    fig.savefig(Path.cwd() / "picard-iteration-exponential.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
