"""Show conditioning and resetting a geometric waiting count; PNG in CWD.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5 (pyproject.toml).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    p = 0.3
    q = 1 - p
    m = 5
    k = np.arange(1, 16)
    r = np.arange(1, 11)
    original = p * q ** (k - 1)
    residual = p * q ** (m + r - 1) / q ** m
    fresh = p * q ** (r - 1)
    assert np.allclose(residual, fresh)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.9), dpi=110,
                             sharey=True, facecolor="white")
    axes[0].bar(k[:m], original[:m], color="#d0d0d0", width=0.72,
                label="Excluded by T > 5")
    axes[0].bar(k[m:], original[m:], color="#256393", width=0.72,
                label="Original mass at k > 5")
    axes[0].axvline(m + 0.5, color="#555555", linestyle="--", linewidth=1)
    axes[0].set_xticks([1, 3, 5, 6, 8, 10, 12, 15])
    axes[0].set_xlabel("Original first-success attempt k")
    axes[0].set_ylabel("Probability mass")
    axes[0].set_title("Keep only outcomes after five failures", pad=12)
    axes[0].legend(loc="upper right", frameon=False, fontsize=9)
    axes[1].bar(r, residual, color="#ba6021", width=0.7,
                label="P(T − 5 = r | T > 5)")
    axes[1].plot(r, fresh, "o", markerfacecolor="white", markeredgecolor="#256393",
                 markeredgewidth=1.6, markersize=6, linestyle="none",
                 label="Fresh P(T = r)")
    axes[1].set_xticks(r)
    axes[1].set_xlabel("Additional attempts r = k − 5")
    axes[1].set_title("Divide by P(T > 5), then reset the count", pad=12)
    axes[1].legend(loc="upper right", frameon=False, fontsize=9)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_ylim(0, 0.40)
        ax.set_yticks(np.arange(0, 0.41, 0.1))
        ax.grid(axis="y", alpha=0.22)
        ax.set_axisbelow(True)
    fig.suptitle("Five failures leave the same remaining-count law  (p = 0.3)",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.12,
             "Conditioning event: P(T > 5) = 0.7⁵ = 0.16807 (includes all k > 5).",
             ha="center", fontsize=11)
    fig.text(0.5, 0.065,
             "At r = 1: 0.050421 ÷ 0.16807 = 0.30.   At r = 2: the mass is 0.21.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.017,
             "Panels truncate the infinite tails; the conditional law is normalized using the full tail.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.28, top=0.79, wspace=0.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
