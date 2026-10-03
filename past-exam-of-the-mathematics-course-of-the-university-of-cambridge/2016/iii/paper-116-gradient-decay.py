"""Generate paper-116-gradient-decay.png in the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7, using the
repository's existing pyproject.toml dependencies. No repository writes.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 6, 500)
    fig, ax = plt.subplots(figsize=(7.8, 4), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    ax.semilogy(t, np.exp(-2*t), color="#1765a1", linewidth=2.3,
                label=r"Morse minimum: $f(x)=x^2$, $x(t)=e^{-2t}$")
    ax.semilogy(t, (1+8*t)**(-0.5), color="#c26418", linewidth=2.3,
                label=r"Degenerate minimum: $f(x)=x^4$, $x(t)=(1+8t)^{-1/2}$")
    ax.set(xlabel="Time t", ylabel="Distance from the minimum (log scale)",
           title="A degenerate minimum can slow gradient convergence",
           xlim=(0, 6), ylim=(4e-6, 1.6))
    ax.legend(loc="lower left", fontsize=9, framealpha=1)
    ax.grid(True, which="major", color="#d9d9d9", linewidth=0.7)
    fig.tight_layout()
    fig.savefig(Path("paper-116-gradient-decay.png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
