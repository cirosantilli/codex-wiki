"""Constructed choice probabilities; not clinical measurements or fitted data.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output is written to CWD.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    reward = np.linspace(0, 4, 161)
    effort = np.linspace(0, 3, 121)
    r_grid, e_grid = np.meshgrid(reward, effort)
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 4.2), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.85, bottom=0.31, top=0.77, wspace=0.22)
    fig.suptitle("One offer can hide different reward–effort mechanisms", fontsize=13, y=0.97)
    cases = ((0.6, 0.2, "Lower reward gain"), (1.0, 1.0, "Higher effort cost"))
    for ax, (alpha, kappa, title) in zip(axes, cases):
        probability = 1 / (1 + np.exp(-(alpha * r_grid - kappa * e_grid)))
        im = ax.imshow(probability, origin="lower", extent=(0, 4, 0, 3), aspect="auto", cmap="viridis", vmin=0, vmax=1)
        ax.plot(2, 1, marker="o", color="white", markeredgecolor="black", markersize=7)
        ax.annotate("Same P ≈ 0.731", xy=(2, 1), xytext=(0.15, 2.65), color="white", fontsize=9, arrowprops={"arrowstyle": "->", "color": "white", "lw": 1.2})
        ax.set_title(f"{title}\nα = {alpha:g}, κ = {kappa:g}", fontsize=10)
        ax.set_xlabel("Reward R (constructed units)", fontsize=10)
        ax.set_xticks(range(5))
        ax.set_yticks(range(4))
    axes[0].set_ylabel("Effort E (constructed units)", fontsize=10)
    cax = fig.add_axes((0.88, 0.31, 0.018, 0.46))
    fig.colorbar(im, cax=cax, label="P(accept)")
    fig.text(0.49, 0.075, "P(accept) = logistic(αR − κE); choice-noise scale fixed.\nConstructed model predictions, not patient data or clinical parameter fits.", fontsize=9, ha="center")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
