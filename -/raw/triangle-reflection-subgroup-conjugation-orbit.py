"""Show reflection-subgroup and rotation-subgroup conjugation orbits.

Output PNG to CWD. Tested with Python 3.14, matplotlib 3.10.7,
and numpy 2.3.5. All arrows mean L -> r L r^{-1}.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig = plt.figure(figsize=(10, 6.8), facecolor="white")
    fig.suptitle("Conjugation moves reflection subgroups", fontsize=20, y=.965)
    fig.text(.5, .89, r"$G=S_3$, $r=(123)$; every blue arrow sends $L$ to $rLr^{-1}$",
             ha="center", fontsize=14)
    ax = fig.add_axes([.04, .32, .92, .52])
    ax.set(xlim=(-2.4, 2.4), ylim=(-.5, 2.2), aspect="equal")
    ax.axis("off")
    nodes = np.array([[-1.6, 1.55], [1.6, 1.55], [0, -.03]])
    labels = [r"$K=\{e,(12)\}$", r"$rKr^{-1}=\{e,(23)\}$",
              r"$r^2Kr^{-2}=\{e,(13)\}$"]
    fixed = ["reflection fixes vertex 3", "reflection fixes vertex 1",
             "reflection fixes vertex 2"]
    for (x, y), label, detail in zip(nodes, labels, fixed):
        ax.text(x, y, label, ha="center", va="center", fontsize=16,
                bbox={"boxstyle": "round,pad=.6", "facecolor": "#edf3f8", "edgecolor": "#1769a5"})
        ax.text(x, y - .39, detail, ha="center", fontsize=11, color="#536375")
    starts = [(-.7, 1.55), (1.3, 1.07), (-.5, .38)]
    ends = [(.48, 1.55), (.48, .38), (-1.3, 1.07)]
    for start, end in zip(starts, ends):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=21, lw=2, color="#1769a5"))
    ax.text(0, 1.13, r"$|\mathrm{Orb}_G(K)|=3$", ha="center", fontsize=15)
    ax.text(0, .85, r"$[G:N_G(K)]=6/2$", ha="center", fontsize=13)
    fig.text(.5, .26, r"Each node is a subgroup; the stabilizer is $N_G(K)=K$.", ha="center", fontsize=12)
    fig.text(.5, .18, r"Rotation subgroup: $H=\{e,(123),(132)\}$ has an orbit of size 1.",
             ha="center", fontsize=14,
             bbox={"boxstyle": "round,pad=.7", "facecolor": "#f0f7ee", "edgecolor": "#318445"})
    fig.text(.5, .075, r"$gHg^{-1}=H$ for every $g\in S_3$, although $(12)r(12)=r^{-1}$.",
             ha="center", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
