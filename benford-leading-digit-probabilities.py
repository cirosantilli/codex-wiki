"""Analytic digit probabilities; tested with Python 3.14.4, NumPy 2.3.5,
and Matplotlib 3.10.7. Write an opaque white PNG to the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    digits = np.arange(1, 10)
    benford = np.log10((digits + 1) / digits)
    uniform = np.full(9, 1 / 9)
    fig, ax = plt.subplots(figsize=(10, 4.6), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.bar(digits - 0.19, benford, width=0.36, color="#246a9b",
           label=r"Log-uniform $X$ on $[1,10)$: Benford law")
    ax.bar(digits + 0.19, uniform, width=0.36, color="#d38b38",
           label=r"Uniform $X$ on $[1,10)$: each digit has probability $1/9$")
    ax.annotate("0.30103", (0.81, benford[0]), xytext=(0, 7),
                textcoords="offset points", ha="center", fontsize=10)
    ax.annotate("0.04576", (8.81, benford[-1]), xytext=(0, 7),
                textcoords="offset points", ha="center", fontsize=10)
    ax.set(xlabel="First nonzero decimal digit d", ylabel="Probability",
           title="Two constructed laws give different leading-digit probabilities",
           xlim=(0.35, 9.65), ylim=(0, 0.36))
    ax.set_xticks(digits)
    ax.set_yticks(np.arange(0, 0.36, 0.05))
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(axis="y", alpha=0.18)
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    fig.text(0.5, 0.025, "Exact analytic probabilities; no sampled or observed dataset.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
