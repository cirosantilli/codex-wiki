"""Original rectangle proof of logarithmic factorial bounds; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

N = 6
fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.8), layout="constrained")
for ax, upper in zip(axes, [False, True]):
    start, stop = (2, N + 1) if upper else (1, N)
    x = np.linspace(start, stop, 500)
    for k in range(2, N + 1):
        left = k if upper else k - 1
        ax.add_patch(Rectangle((left, 0), 1, np.log(k), edgecolor="#316e9f", facecolor="#a7c7df", alpha=0.6))
    ax.plot(x, np.log(x), color="#aa431f", lw=2, label=r"$\ln x$")
    ax.set_xlim(start - 0.1, stop + 0.1)
    ax.set_ylim(0, 2.15)
    ax.set_xticks(np.arange(start, stop + 1))
    ax.set_xlabel("x")
    ax.set_ylabel("Height")
    ax.grid(alpha=0.15)
    ax.set_title("Rectangles above the curve" if not upper else "Rectangles below the curve")
    ax.text(0.04, 0.94, r"$\int_1^N\ln x\,dx\leq\ln(N!)$" if not upper else r"$\ln(N!)\leq\int_2^{N+1}\ln x\,dx$", transform=ax.transAxes, va="top", fontsize=11)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
