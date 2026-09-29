"""Same constructed exponential function on linear and logarithmic vertical axes."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter, NullFormatter

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
t = np.linspace(0, 8, 401)
y = 3*np.exp(0.4*t)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
for ax in axes:
    ax.plot(t, y, color="#2563eb", lw=2.4)
    tx = np.array([0, 2, 4, 6, 8])
    ax.scatter(tx, 3*np.exp(0.4*tx), color="#2563eb", s=32, zorder=3)
    ax.set_xlim(-0.2, 8.2)
    ax.set_xticks([0, 2, 4, 6, 8])
    ax.set_xlabel("Dimensionless t")
    ax.set_ylabel("Dimensionless y (original values)")
    ax.grid(alpha=0.25)
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylim(0, 82)
axes[0].set_title("Linear vertical axis: increasing absolute gain")
axes[0].text(0.04, 0.93, r"$y(0)=3,\quad y(8)\approx 73.60$", transform=axes[0].transAxes, va="top")
axes[1].set_yscale("log")
axes[1].set_ylim(2.5, 85)
axes[1].yaxis.set_major_locator(FixedLocator([3, 6, 12, 24, 48]))
axes[1].yaxis.set_major_formatter(FixedFormatter(["3", "6", "12", "24", "48"]))
axes[1].yaxis.set_minor_formatter(NullFormatter())
axes[1].set_title("Logarithmic vertical axis: equal ratios")
axes[1].text(0.04, 0.93, r"$\log_{10} y=\log_{10}3+\frac{0.4}{\ln 10}t$", transform=axes[1].transAxes, va="top")
axes[1].text(0.04, 0.83, "Slope in transformed coordinates: 0.17372", transform=axes[1].transAxes, va="top", fontsize=10)
fig.suptitle(r"One exact model: $y(t)=3e^{0.4t}$", fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
