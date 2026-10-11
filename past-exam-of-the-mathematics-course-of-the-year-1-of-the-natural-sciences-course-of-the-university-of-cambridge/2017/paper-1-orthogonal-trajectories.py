"""Original Q20 parabolas and an orthogonal ellipse; PNG goes to cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1.8, 1.8, 1000)
    fig, ax = plt.subplots(figsize=(7, 5.2), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    colours = ["#206b96", "#168f9b", "#4e9c54", "#777777", "#b67c13", "#bc4939", "#a44b94"]
    for c, colour in zip(range(-3, 4), colours):
        ax.plot(x, c * x * x, color=colour, linewidth=1.6, label=f"$c={c}$")
    theta = np.linspace(0, 2 * np.pi, 1000)
    ax.plot(np.sqrt(2) * np.cos(theta), np.sin(theta), "k--", linewidth=2.5, label=r"$x^2+2y^2=2$")
    ax.axvline(0, color="#999999", linewidth=0.7)
    ax.set(xlim=(-1.75, 1.75), ylim=(-2.3, 2.3), xlabel="$x$", ylabel="$y$", title=r"$y=cx^2$ and an orthogonal trajectory")
    ax.set_aspect("equal")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path("paper-1-orthogonal-trajectories.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
