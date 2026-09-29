"""Original cumulative-weight tests for entanglement catalysis; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

source = np.array([0.4, 0.4, 0.1, 0.1])
target = np.array([0.5, 0.25, 0.25, 0])
cases = [(source, target, "No auxiliary pair"),
         (np.kron(source, [0.6, 0.4]), np.kron(target, [0.6, 0.4]), "Returned nonmaximal catalyst"),
         (np.kron(source, [0.5, 0.5]), np.kron(target, [0.5, 0.5]), "Returned maximally entangled pair")]
fig, axes = plt.subplots(1, 3, figsize=(12, 4.3), dpi=100, facecolor="white", sharey=True)
for ax, (x, y, title) in zip(axes, cases):
    xx = np.r_[0, np.cumsum(np.sort(x)[::-1])]
    yy = np.r_[0, np.cumsum(np.sort(y)[::-1])]
    k = np.arange(len(xx))
    ax.plot(k, xx, "o-", lw=2, ms=4, label="Input cumulative weights")
    ax.plot(k, yy, "s--", lw=2, ms=4, label="Output cumulative weights")
    bad = xx > yy + 1e-12
    ax.scatter(k[bad], xx[bad], s=115, facecolor="none", edgecolor="tab:red", lw=1.8, zorder=5)
    ax.set(title=title, xlabel="Number of largest weights included", ylim=(-0.02, 1.07))
    ax.set_xticks(k[::1 if len(k) < 6 else 2])
    ax.grid(alpha=0.22)
axes[0].set_ylabel("Sum of largest squared Schmidt coefficients")
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, ncol=2, loc="lower center", bbox_to_anchor=(0.5, 0.04), fontsize=10)
fig.text(0.5, 0.015, "Deterministic LOCC requires input ≤ output at every partial sum; red circles mark failures.",
         ha="center", fontsize=10)
fig.subplots_adjust(left=0.06, right=0.99, top=0.87, bottom=0.25, wspace=0.15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
