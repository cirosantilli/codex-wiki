"""Generate pauli-antisymmetric-state-pairs.png in the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
The grid is a labelled finite-state model, not an experimental readout.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    swap = np.zeros((16, 16))
    for i in range(4):
        for j in range(4):
            swap[4 * j + i, 4 * i + j] = 1
    projector = (np.eye(16) - swap) / 2
    assert np.linalg.matrix_rank(projector) == 6
    assert np.allclose(projector @ projector, projector)
    fig, (grid, explanation) = plt.subplots(
        1, 2, figsize=(10.0, 5.6), dpi=130, facecolor="white",
        gridspec_kw={"width_ratios": [1.08, 1]},
    )
    fig.suptitle("Antisymmetrization: 16 ordered products become 6 states",
                 fontsize=16, weight="bold", y=0.97)
    labels = [r"$A\uparrow$", r"$A\downarrow$", r"$B\uparrow$", r"$B\downarrow$"]
    grid.set(xlim=(-0.5, 3.5), ylim=(3.5, -0.5), aspect="equal")
    grid.set_xticks(range(4), labels=labels, fontsize=13)
    grid.set_yticks(range(4), labels=labels, fontsize=13)
    grid.xaxis.tick_top()
    grid.xaxis.set_label_position("top")
    grid.set_xlabel("Complete state in particle slot 2", fontsize=11, labelpad=12)
    grid.set_ylabel("Complete state in particle slot 1", fontsize=11, labelpad=10)
    grid.tick_params(length=0, pad=9)
    for spine in grid.spines.values():
        spine.set_visible(False)
    for i in range(4):
        for j in range(4):
            face = "#f2f2f2" if i == j else ("#dfedf9" if i < j else "#fbe7de")
            grid.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1,
                                     facecolor=face, edgecolor="white", lw=2))
            text = "0" if i == j else f"{min(i,j)+1}{max(i,j)+1}"
            if i != j:
                text = ("+" if i < j else "−") + text
            grid.text(j, i, text, ha="center", va="center", fontsize=17,
                      color="#222222" if i == j else ("#245b99" if i < j else "#a74924"))
    explanation.axis("off")
    explanation.text(0.02, 0.91, "Equal complete states cancel", fontsize=13, weight="bold")
    explanation.text(0.02, 0.82, r"$|u,u\rangle-|u,u\rangle=0$", fontsize=17)
    explanation.text(0.02, 0.71, "Zero is not a normalizable quantum state.", fontsize=11)
    explanation.text(0.02, 0.57, "Each off-diagonal pair\ngives one state", fontsize=12, weight="bold", linespacing=1.4)
    explanation.text(0.02, 0.42, r"$|i\wedge j\rangle=(|i,j\rangle-|j,i\rangle)/\sqrt{2}$", fontsize=13)
    explanation.text(0.02, 0.30, "Numbers name pairs; signs show orientation.\n1, 2, 3, 4 label the complete states at left.", fontsize=10.5, linespacing=1.7)
    explanation.text(0.02, 0.12, "Pair 12 uses opposite spins in orbital A:\nits complete states differ, so it survives.", fontsize=10.5, linespacing=1.7, color="#137b67")
    fig.text(0.51, 0.052, "4 equal-state products vanish; 12 unequal ordered products form 6 independent antisymmetric pairs.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.10, right=0.985, bottom=0.16, top=0.79, wspace=0.24)
    fig.savefig(Path.cwd() / "pauli-antisymmetric-state-pairs.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
