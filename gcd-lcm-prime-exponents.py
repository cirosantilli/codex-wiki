"""Show the minimum and maximum prime exponents for 12 and 18.

Run from _media to save the PNG there. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7; dependencies are in pyproject.toml.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    exponents = np.array([[2, 1], [1, 2], [1, 1], [2, 2]])
    colors = ["#245a81", "#b45c24", "#27764d", "#80539c"]
    labels = [r"$12=2^2\cdot3$", r"$18=2\cdot3^2$",
              r"$\gcd=6=2\cdot3$", r"$\mathrm{lcm}=36=2^2\cdot3^2$"]
    fig, (ax, table_ax) = plt.subplots(1, 2, figsize=(8.4, 4.6), dpi=120,
                                      gridspec_kw={"width_ratios": [1.15, 1]})
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.32, top=0.78, wspace=0.22)
    x = np.arange(2)
    width = 0.18
    for i, (values, color, label) in enumerate(zip(exponents, colors, labels)):
        bars = ax.bar(x + (i - 1.5) * width, values, width=width,
                      color=color, label=label, zorder=3)
        ax.bar_label(bars, padding=3)
    ax.set_xticks(x, ["Prime 2", "Prime 3"])
    ax.set(ylim=(0, 2.55), ylabel="Exponent in prime factorization")
    ax.set_yticks([0, 1, 2])
    ax.grid(axis="y", alpha=0.18, zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    table_ax.axis("off")
    rows = [["12", "2", "1"], ["18", "1", "2"],
            ["gcd: minimum", "1", "1"], ["lcm: maximum", "2", "2"]]
    table = table_ax.table(cellText=rows,
                           colLabels=["Number / rule", r"$v_2$", r"$v_3$"],
                           colWidths=[0.62, 0.19, 0.19], cellLoc="center",
                           bbox=[0, 0.08, 1, 0.80])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#cccccc")
        if row == 0:
            cell.set_facecolor("#f1f1f1")
            cell.get_text().set_weight("bold")
        elif row == 3:
            cell.set_facecolor("#e5f2e9")
        elif row == 4:
            cell.set_facecolor("#eee5f4")
    fig.legend(loc="lower center", bbox_to_anchor=(0.52, 0.09), ncol=2,
               frameon=False, fontsize=11)
    fig.text(0.5, 0.045, r"$6\times36=12\times18=216$", ha="center", fontsize=14)
    fig.suptitle("Shared factors: take the smaller or larger exponent", fontsize=15, y=0.95)
    ax.set_facecolor("white")
    fig.savefig(Path.cwd() / "gcd-lcm-prime-exponents.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
