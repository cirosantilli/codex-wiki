"""Generate the Q20 wave sketch; tested with Python 3.14, NumPy 2.3.5,
and Matplotlib 3.10.7, using the repository's pyproject.toml dependencies.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-6, 6, 1000)
    fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
    for a, color, style, label in [
        (0.6, "#176b9c", "--", r"$t_1$: $ct_1=0.6$"),
        (1.8, "#b63d39", "-", r"$t_2$: $ct_2=1.8$"),
    ]:
        psi = np.exp(-0.5 * (x - a) ** 2) - np.exp(-0.5 * (x + a) ** 2)
        ax.plot(x, psi, color=color, linestyle=style, linewidth=2.2, label=label)
    ax.axhline(0, color="0.6", linewidth=0.8)
    ax.axvline(0, color="0.6", linewidth=0.8)
    ax.set(xlabel=r"Position $x$", ylabel=r"$\psi(x,t)$", xlim=(-6, 6), ylim=(-1.1, 1.1))
    ax.set_title("Positive and negative Gaussian waves separate")
    ax.legend(loc="upper left", frameon=True)
    ax.grid(alpha=0.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
