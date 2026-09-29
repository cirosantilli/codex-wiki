"""Original Q16 mixed delay law; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = 0.4  # Illustrative r/R; axis labels keep the general parameters visible.
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(-0.12, 1.05), ylim=(-0.04, 1.14), xlabel="$s/R$")
        ax.set_xticks([0, q, 1], ["0", "$r/R$", "1"])
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].plot([0, q], [1, 1], color="#17638d", linewidth=2.4)
    axes[0].plot([q, 1], [0, 0], color="#17638d", linewidth=2.4)
    axes[0].fill_between([0, q], 0, 1, color="#17638d", alpha=0.12)
    axes[0].scatter([0, q], [1, 0], facecolor="white", edgecolor="#17638d", s=35, zorder=5)
    axes[0].scatter(q, 1, color="#17638d", s=35, zorder=5)
    axes[0].set(ylabel="$Rp(s)$", title="Density for strictly positive delays")
    axes[0].text(0.51, 0.65, "Area = $r/R$\nZero-delay atom\nis separate", fontsize=10)
    axes[1].plot([-0.12, 0], [0, 0], color="#17638d", linewidth=2.4)
    axes[1].plot([0, q, 1.05], [1-q, 1, 1], color="#17638d", linewidth=2.4)
    axes[1].plot([0, 0], [0, 1-q], "--", color="#b34332", linewidth=1.6)
    axes[1].scatter(0, 0, facecolor="white", edgecolor="#17638d", s=35, zorder=5)
    axes[1].scatter(0, 1-q, color="#17638d", s=35, zorder=5)
    axes[1].text(0.18, 0.23, r"$P(S=0)=1-r/R$", fontsize=10)
    axes[1].set(ylabel="$F_S(s)$", title="Full cumulative distribution")
    fig.savefig(Path("paper-1-delay-distribution.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
