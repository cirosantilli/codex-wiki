"""Draw independent-mark thinning and exact model expectations.

The points and uniform marks are hand-chosen illustrations, not observations.
Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    arrivals = np.array([0.35, 0.70, 1.25, 1.80, 2.15, 2.55, 2.85, 3.05, 3.70])
    marks = np.array([0.12, 0.60, 0.80, 0.40, 0.20, 0.55, 0.40, 0.90, 0.65])
    probabilities = np.where(arrivals <= 2, 0.25, 0.75)
    keep = marks <= probabilities
    green, orange, blue = "#087e70", "#bd5c22", "#245a91"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig = plt.figure(figsize=(10, 6.0), layout="constrained")
    grid = fig.add_gridspec(2, 1, height_ratios=[2.7, 1.4])
    ax, table = fig.add_subplot(grid[0]), fig.add_subplot(grid[1])
    fig.suptitle("Independent thinning with a changing retention probability", fontsize=17)
    ax.set_title("Synthetic times and marks — not measured data", fontsize=12, pad=34)
    for a, b, text in [(0, 2, "$p(s)=1/4$"), (2, 4, "$p(s)=3/4$")]:
        ax.text((a+b)/2, 3.70, text, ha="center", fontsize=13)
    ax.axvspan(0, 2, color="#f1f5f8", zorder=0)
    ax.axvline(2, color="#999999", linestyle=":", linewidth=1)
    rows = [(3, "Original: 9", arrivals, blue),
            (1.8, "Retained: 5", arrivals[keep], green),
            (0.6, "Rejected: 4", arrivals[~keep], orange)]
    for y, label, times, color in rows:
        ax.hlines(y, 0, 4, color="#bbbbbb", linewidth=1)
        ax.scatter(times, np.full(len(times), y), color=color, s=52, zorder=4)
    for t, u, retained in zip(arrivals, marks, keep):
        y = 1.8 if retained else 0.6
        color = green if retained else orange
        ax.annotate("", (t, y+0.08), (t, 2.90),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.3})
        ax.text(t, 3.18, f"{u:.2f}", ha="center", fontsize=10)
    ax.text(0.02, 3.48, r"Uniform marks $U_i$ (retain if $U_i\leq p(T_i)$)", fontsize=10)
    ax.set(xlim=(0, 4), ylim=(0.25, 3.96), xticks=np.arange(5), xlabel="Time (minutes)",
           yticks=[r[0] for r in rows], yticklabels=[r[1] for r in rows])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="y", length=0, pad=10)
    table.axis("off")
    table.set_title("Exact expected counts: rate 2 per minute", fontsize=13, pad=9)
    cells = [["Original", "4", "4", "8"],
             ["Retained", r"$2\cdot2\cdot\frac{1}{4}=1$", r"$2\cdot2\cdot\frac{3}{4}=3$", "4"],
             ["Rejected", r"$2\cdot2\cdot\frac{3}{4}=3$", r"$2\cdot2\cdot\frac{1}{4}=1$", "4"]]
    tab = table.table(cellText=cells,
                      colLabels=["Stream", "0–2 minutes", "2–4 minutes", "0–4 minutes"],
                      cellLoc="center", colWidths=[0.19, 0.29, 0.29, 0.23], bbox=[0, 0, 1, 0.92])
    tab.auto_set_font_size(False)
    tab.set_fontsize(12)
    for (row, col), cell in tab.get_celld().items():
        cell.set_edgecolor("#d0d0d0")
        if row == 0:
            cell.set_facecolor("#f1f5f8")
        if col == 0 and row > 0:
            cell.get_text().set_color([blue, green, orange][row-1])
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
