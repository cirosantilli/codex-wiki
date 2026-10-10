"""Show the joint mass and marginals of an explicit maximal coupling."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def main():
    joint = np.array([[0.1, 0.2, 0.1, 0.0], [0.0, 0.1, 0.0, 0.0],
                      [0.0, 0.0, 0.2, 0.0], [0.0, 0.0, 0.0, 0.3]])
    p, q = joint.sum(axis=1), joint.sum(axis=0)
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.6), layout="constrained",
                             gridspec_kw={"width_ratios": [1.25, 1]})
    fig.set_facecolor("white")
    ax = axes[0]
    ax.imshow(joint, cmap="Blues", vmin=0, vmax=0.35)
    labels = ["A", "B", "C", "D"]
    ax.set(xticks=range(4), xticklabels=labels, yticks=range(4),
           yticklabels=labels, xlabel="Y (law Q)", ylabel="X (law P)")
    ax.set_title("Joint probability mass")
    for row in range(4):
        for col in range(4):
            ax.text(col, row, f"{joint[row, col]:.1f}", ha="center", va="center",
                    color="white" if joint[row, col] >= 0.2 else "#163548", fontsize=13)
        ax.add_patch(Rectangle((row - 0.49, row - 0.49), 0.98, 0.98,
                               fill=False, edgecolor="#d4880b", linewidth=2.5))
    ax.set_xticks(np.arange(-0.5, 4), minor=True)
    ax.set_yticks(np.arange(-0.5, 4), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", bottom=False, left=False)
    right = axes[1]
    right.axis("off")
    statements = [
        "Row sums = P", "   (0.4, 0.1, 0.2, 0.3)",
        "Column sums = Q", "   (0.1, 0.3, 0.3, 0.3)",
        "Outlined diagonal: agreement", "   Pr(X = Y) = 0.7",
        "Off diagonal: mismatch", "   Pr(X ≠ Y) = 0.3",
        "This is the smallest possible", "mismatch for these two laws.",
    ]
    for i, line in enumerate(statements):
        right.text(0.04, 0.94 - i * 0.09, line, va="top", fontsize=12,
                   weight="bold" if i in [0, 2, 4, 6] else "normal")
    assert np.allclose(p, [0.4, 0.1, 0.2, 0.3])
    assert np.allclose(q, [0.1, 0.3, 0.3, 0.3])
    fig.suptitle("A maximal coupling retains all common probability mass", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
