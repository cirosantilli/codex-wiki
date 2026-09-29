"""Original signed cancellation ledger for a nonmonotone finite sequence."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
a = [4, 9, 2, 7, 5]
fig, ax = plt.subplots(figsize=(9, 5.2), layout="constrained")
ax.set(xlim=(0, 9), ylim=(-0.8, 5.3))
ax.axis("off")
fig.suptitle(r"A nonmonotone sequence: $(a_0,a_1,a_2,a_3,a_4)=(4,9,2,7,5)$", fontsize=14)
ax.text(0.35, 4.9, "k", weight="bold")
ax.text(2.55, 4.9, r"$+a_k$", ha="center", weight="bold")
ax.text(5.05, 4.9, r"$-a_{k-1}$", ha="center", weight="bold")
ax.text(7.5, 4.9, "Actual increment", ha="center", weight="bold")
for k in range(1, 5):
    y = 4.5-k
    ax.text(0.35, y, str(k), va="center")
    plus_color = "#2563eb" if k == 4 else "#15803d"
    minus_color = "#c2410c" if k == 1 else "#15803d"
    for x, value, color in [(2.55, f"+{a[k]}", plus_color), (5.05, f"−{a[k-1]}", minus_color)]:
        ax.add_patch(FancyBboxPatch((x-0.55, y-0.3), 1.1, 0.6, boxstyle="round,pad=0.05", edgecolor=color, facecolor="white", lw=1.5, zorder=3))
        ax.text(x, y, value, ha="center", va="center", color=color, fontsize=14, zorder=4)
    difference = a[k]-a[k-1]
    ax.text(7.5, y, f"{a[k]} − {a[k-1]} = {difference}", va="center", ha="center")
    if k < 4:
        ax.annotate("", (4.45, y-1), (3.15, y), arrowprops={"arrowstyle": "<->", "color": "#64748b", "connectionstyle": "arc3,rad=0.08", "lw": 1.5}, zorder=1)
ax.text(4.5, -0.1, "Linked green entries cancel with opposite signs", ha="center", color="#15803d")
ax.text(4.5, -0.55, r"$5-7+5-2=a_4-a_0=5-4=1$", ha="center", fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
