"""Toy analytic number-average chain counts, not measured distributions.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
The matching PNG basename is written to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

NAVY, TEAL, ORANGE = "#18364b", "#007f82", "#c75f18"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "text.color": NAVY, "axes.labelcolor": NAVY,
                     "axes.edgecolor": NAVY, "figure.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(11.2, 6.3), dpi=100)
fig.subplots_adjust(left=.085, right=.96, bottom=.31, top=.77, wspace=.30)
fig.suptitle("Conversion controls two different ideal chain counts", y=.965, fontsize=17, weight="bold")
fig.text(.5, .885, "TOY ANALYTIC MODELS • no experimental points or measured chain-length distributions", ha="center", fontsize=10)
ax = axes[0]
p = np.linspace(0, .999, 1600)
ax.semilogy(p, 1/(1-p), lw=2.6, color=TEAL, label="Balanced groups: r = 1")
ax.semilogy(p, 1.98/(1.98-1.96*p), lw=2.6, color=ORANGE, label="Group ratio: r = 0.98")
ax.scatter([1], [99], color=ORANGE, s=30, zorder=4)
ax.annotate("At p = 1: Xₙ = 99", xy=(1, 99), xytext=(.37, 165),
            fontsize=10, arrowprops={"arrowstyle": "->", "color": ORANGE})
ax.set(xlim=(0, 1.01), ylim=(1, 1300), xlabel="p: fraction of limiting reactive groups consumed",
       ylabel="Xₙ: monomeric units per chain (log scale)", title="Step growth: imbalance limits the mean")
ax.legend(loc="upper left", fontsize=10, frameon=False)
ax.set_yticks([1, 10, 100, 1000], ["1", "10", "100", "1000"])
ax.text(.03, .08, r"$X_n=(1+r)/(1+r-2rp)$", transform=ax.transAxes, fontsize=13)
ax = axes[1]
for ratio, color in [(200, TEAL), (100, ORANGE)]:
    # A stipulated one-monomer initiation per chain sets the fixed-chain
    # interval's lower endpoint: q = 1/R, X_n = 1.
    q = np.linspace(1/ratio, 1, 501)
    ax.plot(q, q*ratio, lw=2.6, color=color, label=f"R = {ratio} feed molecules / chain")
ax.scatter([.5], [100], color=TEAL, s=30, zorder=4)
ax.annotate("Half the feed; mean = 100", xy=(.5, 100), xytext=(.10, 146),
            fontsize=10, arrowprops={"arrowstyle": "->", "color": TEAL})
ax.set(xlim=(0, 1), ylim=(0, 210), xlabel="q: fraction of feed monomer molecules incorporated",
       ylabel="Xₙ: monomeric units per initiated chain", title="Ideal living growth: fixed chain count")
ax.legend(loc="lower right", fontsize=9.5, frameon=False)
ax.text(.04, .87, r"$X_n=qR,\quad R=M_0/C$", transform=ax.transAxes, fontsize=13)
for ax in axes:
    ax.grid(alpha=.17)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(colors=NAVY)
fig.text(.085, .135, "Linear chains, two groups per feed molecule;\nno rings, branches, or chain-material loss.\nResidual monomers count among chains.", fontsize=10)
fig.text(.575, .135, "One unit initiates each chain (curves start at Xₙ = 1);\nno termination, irreversible transfer, or new chains.\nThe mean does not imply equal chain lengths.", fontsize=10)
fig.text(.5, .037, "p and q count different entities. The straight line is not a prediction for every chain-growth process.",
         ha="center", fontsize=10, color="#526773")
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
plt.close(fig)
