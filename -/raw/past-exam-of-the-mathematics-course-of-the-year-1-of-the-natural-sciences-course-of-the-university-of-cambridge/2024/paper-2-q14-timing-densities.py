"""Generate this exam figure in cwd; run from its _media source directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository pyproject.toml.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), layout="constrained")
axes[0].plot([-0.3, 0, 0, 1, 1, 1.3], [0, 0, 1, 1, 0, 0], color="#176b9c", linewidth=2.2)
axes[0].fill_between([0, 1], [1, 1], color="#176b9c", alpha=0.12)
axes[0].set(xlabel=r"Endpoint offset $s$ (minutes)", ylabel=r"$p(s)$", xlim=(-0.3, 1.3), title="One truncated reading")
t = np.linspace(-1.3, 1.3, 600)
q = np.maximum(1 - np.abs(t), 0)
axes[1].plot(t, q, color="#176b9c", linewidth=2.2)
tail = np.linspace(0.5, 1, 100)
axes[1].fill_between(tail, 1-tail, color="#b33b35", alpha=0.4, label=r"$P(T>1/2)=1/8$")
axes[1].set(xlabel=r"Elapsed-time error $t$ (minutes)", ylabel=r"$q(t)$", xlim=(-1.3, 1.3), title="Difference of independent offsets")
axes[1].legend(loc="upper left", fontsize=9)
for ax in axes:
    ax.axhline(0, color="0.6", linewidth=0.7)
    ax.set_ylim(-0.05, 1.2)
    ax.grid(alpha=0.15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
