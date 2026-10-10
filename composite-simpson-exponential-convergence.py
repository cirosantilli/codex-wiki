"""Compute and plot original composite Simpson convergence data.

Run from _media; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Decimal arithmetic prevents floating-point cancellation in the plotted errors.
"""

from decimal import Decimal, localcontext
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def convergence_data():
    with localcontext() as context:
        context.prec = 80
        counts = [2, 4, 8, 16, 32, 64, 128]
        exact = Decimal(1).exp() - 1
        errors = []
        for n in counts:
            h = Decimal(1) / n
            samples = [(Decimal(j)*h).exp() for j in range(n+1)]
            weights = [1 if j in (0, n) else 4 if j % 2 else 2 for j in range(n+1)]
            estimate = h * sum(w*y for w, y in zip(weights, samples)) / 3
            errors.append(estimate - exact)
        ratios = [None] + [errors[j-1]/errors[j] for j in range(1, len(errors))]
        return counts, errors, ratios


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    counts, errors, ratios = convergence_data()
    n = np.array(counts, dtype=float)
    fig, (ax, tab) = plt.subplots(1, 2, figsize=(9, 4.5), dpi=120,
                                gridspec_kw={"width_ratios": [1.25, 1]},
                                layout="constrained")
    fig.suptitle(r"Composite Simpson: $f(x)=e^x$ on $[0,1]$", fontsize=16)
    ax.loglog(n, np.e/(180*n**4), "--", color="#777777", lw=1.8,
              label=r"Bound $e/(180n^4)$")
    ax.loglog(n, [float(e) for e in errors], "o-", color="#176b9b", lw=2,
              label=r"Computed $S_n-(e-1)$")
    ax.set_xlabel(r"Even subinterval count $n$")
    ax.set_ylabel("Absolute error")
    ax.set_xticks(n, labels=[str(k) for k in counts])
    ax.minorticks_off()
    ax.grid(alpha=0.2)
    ax.legend(loc="upper right", fontsize=10, framealpha=1)
    ax.text(0.08, 0.09, "Doubling n divides error\nby nearly 16 (slope −4)",
            transform=ax.transAxes, fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    tab.axis("off")
    cells = [[str(k), f"{float(e):.4e}", "—" if r is None else f"{float(r):.5f}"]
             for k, e, r in zip(counts, errors, ratios)]
    table = tab.table(cellText=cells,
                      colLabels=["n", "Absolute error", "Previous / current"],
                      colWidths=[0.13, 0.39, 0.48], cellLoc="center",
                      bbox=[0.01, 0.20, 0.98, 0.72])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for (row, column), cell in table.get_celld().items():
        cell.set_edgecolor("#cccccc")
        if row == 0:
            cell.set_facecolor("#e7eff4")
            cell.set_text_props(weight="bold")
    tab.text(0.5, 0.08, r"Exact integral: $e-1$" + "\nAll errors are positive: Simpson overestimates.",
             ha="center", va="center", transform=tab.transAxes, fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
