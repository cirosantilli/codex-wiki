"""Illustrate an original linear-program primal/dual certificate; output to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 13, "axes.titlesize": 15})
    fig, (ax, table_ax) = plt.subplots(1, 2, figsize=(12, 6), dpi=100)
    fig.patch.set_facecolor("white")
    u = np.linspace(0, 4.4, 500)
    boundary = np.maximum(0, 3 - u)
    ax.fill_between(u, boundary, 4.1, color="#e3f1eb", label="Feasible region (shown portion)")
    ax.plot(u, boundary, color="#287557", linewidth=2.5, label=r"$u+v\geq3$ and $v\geq0$")
    for cost in (3, 4, 5, 6):
        v = (cost - u) / 2
        ax.plot(u[v >= 0], v[v >= 0], "--", color="#4f78a0", alpha=0.8, linewidth=1.5)
        ax.text(0.12, cost / 2 + 0.06, f"cost {cost}", color="#315c85", fontsize=11)
    ax.scatter([3], [0], s=95, color="#a43a25", zorder=5)
    ax.annotate("Optimal decision (3, 0)\nCost = lower bound = 3", (3, 0),
                xytext=(2.0, 0.85), fontsize=12, color="#8f301f",
                arrowprops={"arrowstyle": "->", "color": "#8f301f"})
    ax.set(xlim=(-0.15, 4.4), ylim=(-0.15, 4.1), xlabel=r"$u$", ylabel=r"$v$",
           title="Primal: minimize u + 2v")
    ax.legend(loc="upper right", fontsize=10, framealpha=0.96)
    ax.grid(alpha=0.15)
    table_ax.axis("off")
    table_ax.set_title("Dual: combine valid inequalities", pad=15)
    rows = [[r"$u\geq0$", "0", "0", "0"],
            [r"$v\geq0$", "1", r"$v$", "0"],
            [r"$u+v\geq3$", "1", r"$u+v$", "3"],
            ["Sum", "", r"$u+2v$", "3"]]
    table = table_ax.table(cellText=rows,
                          colLabels=["Constraint", "Weight", "Weighted\nleft side", "Weighted\nright side"],
                          cellLoc="center", colWidths=[0.30, 0.14, 0.28, 0.28],
                          bbox=[0.0, 0.33, 1.0, 0.55])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d0d6d9")
        if row == 0:
            cell.set_facecolor("#e9eff5")
        if row == 4:
            cell.set_facecolor("#e3f1eb")
    table_ax.text(0.5, 0.23, r"$y=(0,1,1)^T\geq0,\quad A^Ty=(1,2)^T$", ha="center", fontsize=14)
    table_ax.text(0.5, 0.12, r"$u+2v\geq b^Ty=3$ for every feasible decision", ha="center", fontsize=13)
    fig.suptitle("One decision plus one certificate proves optimality", fontsize=18)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.11, top=0.85, wspace=0.23)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
