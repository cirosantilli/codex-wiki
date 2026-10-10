"""Original tail-sum example; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (mass, tail) = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
    blue, orange = "#287b9e", "#d58932"
    values = np.arange(4)
    probabilities = np.array([0.2, 0.3, 0.0, 0.5])
    mass.bar(values, probabilities, width=0.55,
             color=["#8d97a2", orange, "white", blue])
    for x, p in zip(values, probabilities):
        mass.text(x, p + 0.025, f"{p:.1f}", ha="center")
    mass.set(title="Probability mass", xlabel=r"Outcome $n$",
             ylabel=r"$\mathbb{P}(N=n)$", ylim=(0, 1.06),
             xticks=values, xlim=(-0.5, 3.65))
    mass.text(0.03, 0.90, r"$\mathbb{E}[N]=0(0.2)+1(0.3)+3(0.5)$",
              transform=mass.transAxes, fontsize=11)
    mass.text(0.03, 0.79, r"$=1.8$", transform=mass.transAxes, fontsize=14)
    tail.bar([0, 1, 2], [0.5, 0.5, 0.5], width=1, align="edge",
             color=blue, alpha=0.72, edgecolor="white")
    tail.bar([0], [0.3], bottom=0.5, width=1, align="edge",
             color=orange, alpha=0.8, edgecolor="white")
    tail.plot([0, 1, 1, 3, 3, 3.6], [0.8, 0.8, 0.5, 0.5, 0, 0],
              color="#253845", lw=1.8)
    tail.scatter([0, 1, 2, 3], [0.8, 0.5, 0.5, 0],
                 color="#253845", s=35, zorder=5)
    tail.scatter([1, 3], [0.8, 0.5], facecolor="white",
                 edgecolor="#253845", s=35, zorder=6)
    for x, height in zip([0.5, 1.5, 2.5], [0.8, 0.5, 0.5]):
        tail.text(x, height + 0.035, f"{height:.1f}", ha="center")
    tail.text(0.5, 0.65, "0.3", ha="center", va="center")
    for x in [0.5, 1.5, 2.5]:
        tail.text(x, 0.25, "0.5", ha="center", va="center")
    tail.set(title="Survival columns of width one", xlabel=r"Threshold $t$",
             ylabel=r"$S(t)=\mathbb{P}(N>t)$", ylim=(0, 1.06),
             xlim=(-0.1, 3.65), xticks=values)
    tail.text(0.04, 0.93, "Area = 0.8 + 0.5 + 0.5 = 1.8",
              transform=tail.transAxes, fontsize=11)
    fig.suptitle("Count each outcome's layers, then average", fontsize=15)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
