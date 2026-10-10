"""Original arithmetic progression and its quadratic partial sums, written to CWD."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
k = np.arange(1, 13)
terms = 7 + 3*(k-1)
n = np.arange(13)
sums = np.concatenate(([0], np.cumsum(terms)))
axes[0].plot(k, terms, "o-", color="#2563eb", lw=1.5)
axes[0].set(xlabel="Term index k", ylabel="Term value", xlim=(0.5, 12.5), ylim=(0, 43), title="Equal differences: each new term adds 3")
axes[0].text(0.04, 0.94, r"$a_k=7+3(k-1)$", transform=axes[0].transAxes, va="top")
axes[0].annotate("7", (1, 7), xytext=(1.25, 4), color="#2563eb")
axes[0].annotate("28", (8, 28), xytext=(8.1, 24), color="#2563eb")
curve = np.linspace(0, 12, 200)
axes[1].plot(curve, (3*curve*curve+11*curve)/2, color="#c2410c", alpha=0.55, lw=1.5)
axes[1].scatter(n, sums, color="#c2410c", s=30, zorder=3)
axes[1].set(xlabel="Number of terms n", ylabel="Partial sum", xlim=(-0.3, 12.5), ylim=(-8, 308), title="Growing increments: partial sums are quadratic")
axes[1].text(0.04, 0.94, r"$S_n=\frac{3n^2+11n}{2}$", transform=axes[1].transAxes, va="top")
axes[1].annotate(r"$S_8=140$", (8, 140), xytext=(4.8, 185), arrowprops={"arrowstyle": "->", "color": "#c2410c"}, color="#c2410c")
for ax in axes:
    ax.set_xticks([0, 2, 4, 6, 8, 10, 12] if ax is axes[1] else [1, 2, 4, 6, 8, 10, 12])
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.25)
fig.suptitle("Constant increments in terms become constant second differences in sums", fontsize=14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
