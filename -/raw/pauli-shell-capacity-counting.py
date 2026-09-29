"""Original shell-counting diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; writes this script's basename with a PNG extension to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    colors = ["#286a9f", "#2f8877", "#d18a30", "#9860a1"]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.6), facecolor="white")
    fig.subplots_adjust(left=0.065, right=0.97, top=0.79, bottom=0.23, wspace=0.34)
    fig.suptitle("Shell capacity counts complete states", fontsize=17, y=0.97)
    ax = axes[0]
    for n in range(1, 5):
        left = 0
        for ell in range(n):
            capacity = 2 * (2 * ell + 1)
            ax.barh(n, capacity, left=left, color=colors[ell], height=0.62)
            ax.text(left + capacity / 2, n, str(capacity), ha="center", va="center", color="white", fontsize=12)
            left += capacity
        ax.text(left + 0.6, n, str(2 * n * n), va="center", weight="bold", fontsize=12)
    ax.set(xlim=(0, 35), ylim=(0.4, 4.6), yticks=range(1, 5), yticklabels=[f"n = {n}" for n in range(1, 5)], xlabel="Maximum electrons in a shell", title=r"Sum the subshell capacities: $2n^2$")
    ax.invert_yaxis()
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([0, 8, 18, 32])
    ax = axes[1]
    for ell in range(3):
        y = 2 - ell
        for m in range(-ell, ell + 1):
            for spin, dx in [(1, -0.18), (-1, 0.18)]:
                ax.add_patch(Rectangle((m + dx - 0.16, y - 0.26), 0.32, 0.52, edgecolor=colors[ell], facecolor="#f0f5f7", linewidth=1.5))
                ax.text(m + dx, y, "↑" if spin == 1 else "↓", ha="center", va="center", fontsize=14, color=colors[ell])
        ax.text(2.53, y, f"{2 * (2 * ell + 1)} states", va="center", fontsize=11)
    ax.set(xlim=(-2.6, 3.45), ylim=(-0.65, 2.65), xticks=range(-2, 3), yticks=[2, 1, 0], yticklabels=["s: ℓ = 0", "p: ℓ = 1", "d: ℓ = 2"], xlabel=r"Magnetic quantum number $m_\ell$", title="Resolve the n = 3 shell: 2 + 6 + 10 = 18")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.text(0.5, 0.085, "Each small cell is one spin orbital (one electron maximum); paired cells share a spatial orbital.", ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Labels describe wavefunctions and spin projections, not electron trajectories or spatial boxes.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
