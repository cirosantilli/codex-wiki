"""Plot Question 6's Fourier partial sums; write the PNG to the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository's top-level pyproject.toml.
Run from any output directory: python /absolute/path/to/this/script.py
"""
import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "discrete-resit-2015-mpl"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def partial_sum(x, terms):
    odd = 2 * np.arange(terms) + 1
    return (4 / np.pi) * np.sum(np.sin(np.pi * x[:, None] * odd) / odd, axis=1)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    x = np.linspace(-2.1, 2.1, 3001)
    fig, ax = plt.subplots(figsize=(9, 4.7), facecolor="white")
    ax.set_facecolor("white")
    for left, right, value in [(-2.1, -2, -1), (-2, -1, 1), (-1, 0, -1), (0, 1, 1), (1, 2, -1), (2, 2.1, 1)]:
        ax.plot([left, right], [value, value], color="0.2", linewidth=2.3,
                label="Square wave between jumps" if left == -2.1 else None)
    for terms, color in [(1, "#d95f02"), (5, "#1b9e77"), (25, "#3768b1")]:
        ax.plot(x, partial_sum(x, terms), color=color, linewidth=1.35,
                label=f"{terms} odd harmonic" + ("s" if terms != 1 else ""))
    jumps = np.arange(-2, 3)
    ax.scatter(jumps, np.zeros(5), s=36, color="black", zorder=5,
               label="Series value at jumps: 0")
    ax.axhline(0, color="0.75", linewidth=0.7)
    ax.set(xlim=(-2.1, 2.1), ylim=(-1.65, 1.9), xlabel="$x$", ylabel="Value",
           title="Period-two square wave: odd Fourier harmonics")
    ax.set_xticks(jumps)
    ax.grid(alpha=0.17)
    ax.legend(loc="upper center", ncol=2, fontsize=9, framealpha=1)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "discrete-resit-2015-square-wave.png", dpi=140,
                facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
