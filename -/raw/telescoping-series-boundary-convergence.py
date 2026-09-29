"""Original partial sums showing a convergent boundary and an oscillating boundary."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes = plt.subplots(2, 1, figsize=(9, 6), layout="constrained")
n = np.arange(0, 31)
s = n/(3*n+1)
axes[0].plot(n, s, "o-", color="#2563eb", markersize=3.5, lw=1.5)
axes[0].axhline(1/3, color="#c2410c", linestyle="--", label=r"Limit $1/3$")
axes[0].set(xlim=(-0.4, 30.5), ylim=(-0.015, 0.37), ylabel="Partial sum", title=r"Convergent: $S_N=\frac{N}{3N+1}$")
axes[0].text(0.25, 0.12, r"$\frac{1}{3}-S_N=\frac{1}{3(3N+1)}$", transform=axes[0].transAxes, fontsize=12)
axes[0].annotate(r"$S_6=6/19$", (6, s[6]), xytext=(7.8, 0.235), arrowprops={"arrowstyle": "->", "color": "#2563eb"}, color="#2563eb")
axes[0].legend(loc="lower right", frameon=False)
m = np.arange(13)
alternating = (-1.)**m-1
axes[1].plot(m, alternating, "o", color="#7c3aed", markersize=5)
axes[1].set(xlim=(-0.4, 12.4), ylim=(-2.6, 0.6), yticks=[-2, 0], xticks=m, xlabel="Number of summed terms", ylabel="Partial sum", title=r"Divergent: $S_N=(-1)^N-1$ has no single limit")
axes[1].axhline(0, color="#7c3aed", alpha=0.2)
axes[1].axhline(-2, color="#7c3aed", alpha=0.2)
axes[1].text(0.03, 0.05, "Finite cancellation is exact in both cases", transform=axes[1].transAxes, fontsize=11)
for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.25)
fig.suptitle("The uncancelled boundary controls the infinite sum", fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
