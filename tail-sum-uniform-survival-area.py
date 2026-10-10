"""Original uniform survival-area example; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (density, tail) = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
    blue, orange = "#287b9e", "#d58932"
    density.fill_between([0, 4], [0.25, 0.25], color=blue, alpha=0.35)
    density.plot([0, 0, 4, 4, 4.6], [0, 0.25, 0.25, 0, 0], color=blue, lw=2)
    density.text(2, 0.13, "Area = 1", ha="center", fontsize=14)
    density.text(0.07, 0.84, r"$f(y)=1/4$ on $[0,4]$", transform=density.transAxes)
    density.text(0.07, 0.72, r"Mean: $\int_0^4 y f(y)\,dy=2$",
                 transform=density.transAxes)
    density.set(title="Density: probability per unit length", xlabel=r"Value $y$",
                ylabel=r"$f(y)$", xlim=(-0.1, 4.6), ylim=(0, 0.55),
                xticks=[0, 1, 2, 3, 4], yticks=[0, 0.25, 0.5])
    first = np.linspace(0, 2, 101)
    last = np.linspace(2, 4, 101)
    tail.fill_between(first, 1 - first / 4, color=blue, alpha=0.45)
    tail.fill_between(last, 1 - last / 4, color=orange, alpha=0.55)
    tail.plot([0, 4, 4.6], [1, 0, 0], color="#253845", lw=2)
    tail.plot([2, 2], [0, 0.5], color="#253845", ls="--", lw=1.3)
    tail.text(0.9, 0.3, "Area = 1.5", ha="center", fontsize=13)
    tail.text(2.95, 0.1, "0.5", ha="center", fontsize=13)
    tail.text(2.1, 0.57, "Cap at 2", fontsize=11)
    tail.text(0.17, 1.04, r"$S(t)=1-t/4$ on $[0,4]$", fontsize=12)
    tail.set(title="Survival: probability beyond a threshold", xlabel=r"Threshold $t$",
             ylabel=r"$S(t)=\mathbb{P}(Y>t)$", xlim=(-0.1, 4.6),
             ylim=(0, 1.2), xticks=[0, 1, 2, 3, 4], yticks=[0, 0.5, 1])
    fig.suptitle("Uniform on [0, 4]: survival triangle has area 2", fontsize=15)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
