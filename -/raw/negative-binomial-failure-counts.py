"""Plot exact negative binomial PMFs for r=1,2,5 at p=1/2.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Write an opaque white PNG with this script's basename to CWD.
"""

from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    x = np.arange(26)
    fig, axes = plt.subplots(3, 1, figsize=(9.6, 7.5), dpi=100, sharex=True)
    for ax, r, color in zip(axes, (1, 2, 5), ("#246b9c", "#19705b", "#985285")):
        # At p=1/2 these are integer binomial coefficients divided by powers of two.
        masses = np.array([comb(int(k) + r - 1, int(k)) / 2 ** (int(k) + r) for k in x])
        ax.bar(x, masses, width=0.70, color=color, alpha=0.85)
        ax.axvline(r, color="#a54800", linestyle="--", linewidth=1.7,
                   label=rf"Mean failures $\mathbb{{E}}X={r}$")
        ax.set(ylim=(0, masses.max() * 1.28), ylabel=r"$P(X=x)$", xlim=(-0.65, 25.65))
        ax.text(0.98, 0.91, rf"$r={r}$ successes; variance $={2*r}$", ha="right",
                va="top", transform=ax.transAxes, fontsize=12)
        ax.legend(frameon=False, loc="upper right", bbox_to_anchor=(1, 0.76))
        if r == 2:
            ax.annotate("Two modes: 0 and 1 (mass 1/4)", xy=(0.5, 0.25),
                        xytext=(4.1, 0.285), fontsize=10.5,
                        arrowprops={"arrowstyle": "->", "color": "#333333"})
        ax.grid(axis="y", alpha=0.16)
        ax.spines[["top", "right"]].set_visible(False)
    axes[-1].set(xlabel="Failures x before the r-th success", xticks=np.arange(0, 26, 1))
    fig.suptitle("Negative binomial counts: the target changes, p = 1/2", fontsize=16,
                 weight="bold", y=0.97)
    fig.text(0.5, 0.025, "Exact masses for x = 0,...,25; the distribution continues beyond the plot. Vertical scales differ.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.12, top=0.88, hspace=0.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
