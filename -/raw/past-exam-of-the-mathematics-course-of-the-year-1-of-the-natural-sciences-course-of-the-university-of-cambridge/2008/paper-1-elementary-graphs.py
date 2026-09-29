"""Original sketches; write the PNG into the current working directory."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.8), layout="constrained")
ax = axes[0]
for lo, hi in [(-4, 0.95), (1.05, 6)]:
    x = np.linspace(lo, hi, 800)
    ax.plot(x, x / (x - 1), color="tab:blue", lw=2)
ax.axvline(1, color="tab:red", ls="--", label="asymptotes")
ax.axhline(1, color="tab:red", ls="--")
ax.scatter([0], [0], color="black", s=24, zorder=4)
ax.set(xlim=(-4, 6), ylim=(-4, 6), title=r"$y=x/(x-1)$")
ax.legend(fontsize=9)
ax = axes[1]
x = np.linspace(0.0001, 3, 1000)
ax.plot(x, x * np.log(x), color="tab:blue", lw=2)
ax.scatter([1 / np.e, 1], [-1 / np.e, 0], color="tab:red", s=30, zorder=4)
ax.scatter([0], [0], facecolor="white", edgecolor="tab:blue", s=35, zorder=5)
ax.annotate(r"$(e^{-1},-e^{-1})$", (1 / np.e, -1 / np.e), (0.75, -0.42),
            arrowprops={"arrowstyle": "-", "color": "0.4"}, fontsize=10)
ax.set(xlim=(-0.12, 3), ylim=(-0.65, 3.5), title=r"$y=x\log x$, $x>0$")
for ax in axes:
    ax.axhline(0, color="0.4", lw=0.7)
    ax.axvline(0, color="0.4", lw=0.7)
    ax.set(xlabel="$x$", ylabel="$y$")
    ax.grid(alpha=0.18)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
