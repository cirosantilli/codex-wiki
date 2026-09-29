"""Original logarithmic rulers; write matching opaque PNG to the working directory."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter, NullFormatter

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig = plt.figure(figsize=(10, 5.2), layout="constrained")
grid = fig.add_gridspec(2, 2, height_ratios=[1.05, 1])
top = fig.add_subplot(grid[0, :])
top.set_xscale("log")
top.set_xlim(0.85, 1180)
top.set_ylim(-0.35, 1.35)
top.plot([1, 1000], [0, 0], color="#334155", lw=2)
for a, b in [(1, 10), (10, 100), (100, 1000)]:
    top.annotate("", xy=(b, 0.5), xytext=(a, 0.5), arrowprops={"arrowstyle": "<->", "color": "#2563eb", "lw": 1.8})
    top.text(np.sqrt(a*b), 0.7, r"$\times 10$: one equal gap", ha="center", color="#2563eb")
for x in [1, 10, 100, 1000]:
    top.plot([x, x], [-0.08, 0.08], color="#334155", lw=2)
    top.text(x, -0.23, str(x), ha="center")
top.set_title("Equal ratios have equal distances on a logarithmic ruler", pad=12)
top.axis("off")

geometric = np.sqrt(10*100)
arithmetic = (10+100)/2
for index, scale in enumerate(["linear", "log"]):
    ax = fig.add_subplot(grid[1, index])
    ax.set_xscale(scale)
    ax.set_xlim(8 if scale == "log" else 4, 112 if scale == "log" else 106)
    ax.set_ylim(-0.8, 1.1)
    ax.plot([10, 100], [0, 0], color="#334155", lw=2)
    for x, label, color, level in [(10, "10", "#334155", -0.26), (100, "100", "#334155", -0.26),
                                  (geometric, "Geometric mean\n31.62", "#2563eb", 0.65),
                                  (arithmetic, "Arithmetic mean\n55", "#c2410c", -0.56)]:
        ax.scatter([x], [0], color=color, s=40, zorder=4)
        ax.annotate(label, (x, 0), xytext=(x, level), ha="center", va="center", color=color,
                    arrowprops={"arrowstyle": "-", "color": color, "lw": 0.9})
    ax.text(0.5, 0.97, "Equal differences" if scale == "linear" else "Equal ratios", transform=ax.transAxes, ha="center")
    ax.set_title("Linear ruler" if scale == "linear" else "Logarithmic ruler")
    ax.axis("off")
fig.suptitle("A halfway position depends on the scale", fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
