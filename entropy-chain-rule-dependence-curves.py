"""Plot exact entropy and information curves for B = A xor N.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    p = np.linspace(0, 1, 1001)
    h = np.zeros_like(p)
    inner = (p > 0) & (p < 1)
    q = p[inner]
    h[inner] = -q * np.log2(q) - (1 - q) * np.log2(1 - q)
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.4, 5.8))
    fig.suptitle("Dependence changes joint uncertainty, not the fair marginals", fontsize=15, y=0.97)
    ax.plot(p, 1 + h, color="#2166ac", lw=2.7, label=r"Joint: $H(A,B)=1+h_2(p)$")
    ax.plot(p, h, color="#e69028", lw=2.7, label=r"Remaining: $H(B\mid A)=h_2(p)$")
    ax.plot(p, 1 - h, color="#21845b", lw=2.7, label=r"Revealed: $I(A;B)=1-h_2(p)$")
    ax.axhline(1, color="#777e86", linestyle=":", lw=1.5, label=r"Marginals: $H(A)=H(B)=1$")
    ax.axvline(0.5, color="#b9bec5", linestyle="--", lw=1, zorder=0)
    for x in [0, 0.5, 1]:
        entropy = 1 if x == 0.5 else 0
        ax.scatter([x] * 3, [1 + entropy, entropy, 1 - entropy], c=["#2166ac", "#e69028", "#21845b"], s=35, zorder=4, clip_on=False)
    ax.set(xlim=(0, 1), ylim=(-0.07, 2.12), xlabel=r"Flip probability $p=\mathbb{P}(N=1)$", ylabel="Uncertainty or information (bits)")
    ax.set_xticks(np.linspace(0, 1, 6))
    ax.set_yticks(np.linspace(0, 2, 5))
    ax.grid(color="#e4e7eb", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.27), ncol=2, frameon=False, fontsize=11)
    for x, text, align in [(0, "Identical\nB = A\nOne bit revealed", "left"), (0.5, "Independent\nAll four pairs equally likely\nZero information revealed", "center"), (1, "Complementary\nB = 1 − A\nOne bit revealed", "right")]:
        ax.text(x, -0.28, text, ha=align, va="top", transform=ax.transAxes, fontsize=11, linespacing=1.45)
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.29, top=0.73)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
