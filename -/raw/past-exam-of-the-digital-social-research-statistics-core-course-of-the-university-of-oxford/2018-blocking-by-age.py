"""Original count-derived plot; write 2018-blocking-by-age.png to the cwd.

Use the Python, NumPy and Matplotlib versions in the root pyproject.toml.
All proportions include the recorded Not know responses in their denominators.
"""
from pathlib import Path

import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.ticker import PercentFormatter


COUNTS = np.array([
    [[9, 70, 19], [13, 132, 55]],
    [[11, 56, 7], [15, 139, 63]],
    [[16, 85, 10], [9, 174, 45]],
    [[12, 53, 9], [20, 174, 28]],
    [[6, 79, 5], [16, 272, 27]],
])


def main():
    totals = COUNTS.sum(axis=2)
    rates = COUNTS[:, :, 2] / totals
    weights = totals.sum(axis=1) / totals.sum()
    displayed = np.vstack((rates, weights @ rates))
    differences = displayed[:, 1] - displayed[:, 0]
    labels = ["18–24", "25–34", "35–44", "45–54", "55+", "Common age mix"]
    y = np.arange(len(labels))
    figure = Figure(figsize=(9.4, 5.5), dpi=110, facecolor="white")
    FigureCanvasAgg(figure)
    left, right = figure.subplots(1, 2, gridspec_kw={"width_ratios": [1.5, 1]})
    figure.subplots_adjust(left=0.15, right=0.97, top=0.79,
                           bottom=0.24, wspace=0.25)
    colors = ("#436b9a", "#bd573c")
    for j, (name, color) in enumerate(zip(("Not populist", "Populist"), colors)):
        left.barh(y + (j - 0.5) * 0.29, displayed[:, j], height=0.26,
                  label=name, color=color)
    left.set(yticks=y, yticklabels=labels, xlim=(0, 0.34),
             xlabel="Reported Yes / all valid responses in group")
    left.xaxis.set_major_formatter(PercentFormatter(1, decimals=0))
    left.set_title("Reported blocking", fontsize=12, pad=12)
    left.legend(loc="upper left", bbox_to_anchor=(0, 1.25),
                ncol=2, frameon=False, fontsize=9)
    right.barh(y, differences * 100, height=0.42,
               color=["#657d98"] * 5 + ["#333f4b"])
    for k, value in enumerate(differences * 100):
        right.text(value + 0.4, k, f"{value:.2f}", va="center", fontsize=10)
    right.set(yticks=y, yticklabels=[], xlim=(0, 23.5),
              xlabel="Populist − Not populist\n(percentage points)")
    right.set_title("Difference in reported Yes", fontsize=12, pad=12)
    for ax in (left, right):
        ax.set_ylim(-0.6, 5.6)
        ax.invert_yaxis()
        ax.axhline(4.5, color="#969696", lw=0.8, linestyle="--")
        ax.set_axisbelow(True)
        ax.grid(axis="x", color="#e0e0e0", lw=0.7)
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.tick_params(axis="y", length=0)
    figure.text(0.5, 0.96, "Reported blocking by age and populism classification",
                ha="center", va="top", fontsize=15, color="#202832")
    figure.text(0.5, 0.055,
                "Common age mix uses the 1,629 complete cases as weights.\n"
                "Not know remains a valid response. These are descriptive comparisons.",
                ha="center", va="center", fontsize=10, color="#414141")
    figure.savefig(Path.cwd() / "2018-blocking-by-age.png", dpi=110,
                   facecolor="white", transparent=False)


if __name__ == "__main__":
    main()
