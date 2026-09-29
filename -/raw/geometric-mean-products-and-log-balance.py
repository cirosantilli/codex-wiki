"""Original toy compounding and fixed-product mean comparisons.

Write a PNG named after this script into the current working directory.
Python and dependency versions are documented in pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=120, facecolor="white")
for ax in axes:
    ax.set_facecolor("white")
    ax.grid(alpha=0.17)
steps = np.arange(3)
actual = np.array([1000, 1500, 1000])
arithmetic_repeated = 1000 * (13 / 12) ** steps
axes[0].plot(steps, actual, "o-", color="#286f99", linewidth=2.2,
             label="Specified factors: 3/2 then 2/3")
axes[0].plot(steps, np.full(3, 1000), "s--", color="#36916a", linewidth=2,
             label="Repeated geometric factor: 1")
axes[0].plot(steps, arithmetic_repeated, "^:", color="#bc7331", linewidth=2,
             label="Repeated arithmetic factor: 13/12")
axes[0].annotate("1500", (1, 1500), xytext=(0, 11), textcoords="offset points", ha="center")
axes[0].annotate("1173.61", (2, arithmetic_repeated[-1]), xytext=(-5, 12),
                 textcoords="offset points", ha="right", color="#98521b")
axes[0].set(xlim=(-0.1, 2.1), ylim=(930, 1610), xticks=[0, 1, 2],
            xlabel="Step (joining lines are guides)", ylabel="Hypothetical positive quantity",
            title="Preserve the product of successive factors")
axes[0].legend(loc="upper left", bbox_to_anchor=(0.0, 0.81), fontsize=8.6, framealpha=0.96)
t = np.linspace(0, 1.5, 301)
axes[1].plot(t, np.cosh(t), color="#bc7331", linewidth=2.2, label="A = cosh(t)")
axes[1].plot(t, np.ones_like(t), color="#36916a", linewidth=2.2, label="G = 1")
axes[1].plot(t, 1 / np.cosh(t), color="#286f99", linewidth=2.2, label="H = 1/cosh(t)")
axes[1].set(xlim=(0, 1.5), ylim=(0.3, 2.6), xlabel="Logarithmic imbalance t",
            ylabel="Mean of the two positive inputs", title="Inputs exp(−t), exp(t) have product 1")
axes[1].legend(loc="upper left", fontsize=10, framealpha=0.96)
fig.text(0.5, 0.025, "Original mathematical examples: multiplicative equivalence concerns the endpoint, not the intermediate values.",
         ha="center", fontsize=9.5)
fig.subplots_adjust(left=0.07, right=0.98, top=0.90, bottom=0.17, wspace=0.30)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
