"""Two stipulated journeys using speeds of 30 and 60 kilometres per hour.

White PNG output uses this script's basename in the current directory.
No experimental measurements are represented. See pyproject.toml for versions.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=120, facecolor="white")
for ax in axes:
    ax.set_facecolor("white")
    ax.grid(alpha=0.17)
    ax.set(xlim=(0, 3.15), ylim=(0, 137), xlabel="Elapsed time (hours)",
           ylabel="Cumulative distance traveled (km)", xticks=[0, 1, 2, 3])
axes[0].plot([0, 3], [0, 120], "--", color="#35916d", linewidth=1.8, label="Average speed: H = 40 km/h")
axes[0].plot([0, 2], [0, 60], color="#bb644a", linewidth=3, label="First leg: 30 km/h")
axes[0].plot([2, 3], [60, 120], color="#286f99", linewidth=3, label="Second leg: 60 km/h")
axes[0].scatter([0, 2, 3], [0, 60, 120], color="#2e3c44", zorder=4, s=24)
axes[0].annotate("60 km in 2 h", (1.35, 40.5), xytext=(0.20, 64),
                 arrowprops={"arrowstyle": "->", "color": "#bb644a"}, fontsize=10)
axes[0].annotate("60 km in 1 h", (2.60, 96), xytext=(1.35, 113),
                 arrowprops={"arrowstyle": "->", "color": "#286f99"}, fontsize=10)
axes[0].set_title("Equal distances: 120 km in 3 hours")
axes[1].plot([0, 2], [0, 90], "--", color="#35916d", linewidth=1.8, label="Average speed: A = 45 km/h")
axes[1].plot([0, 1], [0, 30], color="#bb644a", linewidth=3, label="First hour: 30 km/h")
axes[1].plot([1, 2], [30, 90], color="#286f99", linewidth=3, label="Second hour: 60 km/h")
axes[1].scatter([0, 1, 2], [0, 30, 90], color="#2e3c44", zorder=4, s=24)
axes[1].annotate("30 km in 1 h", (0.65, 19.5), xytext=(0.15, 57),
                 arrowprops={"arrowstyle": "->", "color": "#bb644a"}, fontsize=10)
axes[1].annotate("60 km in 1 h", (1.60, 66), xytext=(1.65, 111),
                 arrowprops={"arrowstyle": "->", "color": "#286f99"}, fontsize=10)
axes[1].set_title("Equal times: 90 km in 2 hours")
for ax in axes:
    ax.legend(loc="lower right", fontsize=8.9, framealpha=0.96)
fig.text(0.5, 0.025, "Idealized constant-speed legs, with no stops or transition time; cumulative distance need not equal displacement.",
         ha="center", fontsize=9.5)
fig.subplots_adjust(left=0.065, right=0.98, top=0.90, bottom=0.17, wspace=0.27)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
