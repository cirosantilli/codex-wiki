"""Ordered factor pairs and their convolution weights; write basename PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Reproduce: make _media/dirichlet-convolution-factor-pairs.png
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 12
    divisors = np.array([d for d in range(1, n + 1) if n % d == 0])
    complements = n // divisors
    tau_weights = np.ones_like(divisors)
    sigma_weights = divisors.copy()
    assert np.all(divisors * complements == n)
    assert tau_weights.sum() == 6 and sigma_weights.sum() == 28
    assert sum(1 for a in range(1, 13) for b in range(1, 13)
               for c in range(1, 13) if a * b * c == n) == 18

    fig, (ax, tab_ax) = plt.subplots(1, 2, figsize=(11, 5), dpi=120,
                                   gridspec_kw={"width_ratios": [1, 1.24]},
                                   facecolor="white")
    blue, orange, ink = "#176997", "#b55d20", "#243746"
    x = np.linspace(1, n, 300)
    ax.plot(x, n / x, color="#a8bdcb", lw=1.4, zorder=1)
    ax.scatter(divisors, complements, s=65, color=blue, zorder=3)
    offsets = [(7, 0), (8, 8), (-16, 14), (8, 8), (8, 4), (-58, 10)]
    for d, e, offset in zip(divisors, complements, offsets):
        ax.annotate(f"({d}, {e})", (d, e), xytext=offset,
                    textcoords="offset points", fontsize=11, color=ink)
    ax.set(xlim=(0, 14), ylim=(0, 14), xlabel=r"First factor $d$",
           ylabel=r"Second factor $12/d$")
    ax.set_xticks([1, 2, 3, 4, 6, 12])
    ax.set_yticks([1, 2, 3, 4, 6, 12])
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.14)
    ax.set_title("Six ordered positive pairs", fontsize=14, pad=13)
    ax.text(0.5, -0.22, "(3, 4) and (4, 3) are separate pairs.",
            transform=ax.transAxes, ha="center", fontsize=11, color=ink)

    rows = [[str(d), str(e), str(t), str(s)]
            for d, e, t, s in zip(divisors, complements, tau_weights, sigma_weights)]
    rows.append(["Sum", "", str(tau_weights.sum()), str(sigma_weights.sum())])
    table = tab_ax.table(cellText=rows,
                         colLabels=[r"$d$", r"$12/d$", r"$\mathbf{1}(d)\mathbf{1}(12/d)$",
                                    r"$\mathrm{id}(d)\mathbf{1}(12/d)$"],
                         colWidths=[0.13, 0.17, 0.34, 0.36],
                         cellLoc="center", bbox=[0, 0.08, 1, 0.86])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d9e2e8")
        cell.set_linewidth(0.7)
        cell.set_text_props(color=ink)
        if row == 0:
            cell.set_facecolor("#edf2f6")
        elif col == 2:
            cell.set_facecolor("#edf5fa")
            cell.set_text_props(color=blue)
        elif col == 3:
            cell.set_facecolor("#fff1e4")
            cell.set_text_props(color=orange)
        if row == len(rows):
            cell.set_text_props(weight="bold", fontsize=14)
    tab_ax.axis("off")
    tab_ax.set_title("Add one contribution from each pair", fontsize=14, pad=13)
    tab_ax.text(0.5, -0.05, r"$(\mathbf{1}*\mathbf{1})(12)=6\qquad(\mathrm{id}*\mathbf{1})(12)=28$",
                transform=tab_ax.transAxes, ha="center", fontsize=14)
    fig.suptitle("Dirichlet convolution sums over factor pairs of 12", fontsize=17, y=0.97)
    fig.text(0.52, 0.035,
             r"Pointwise products use only the input 12: $(\mathbf{1}\cdot\mathbf{1})(12)=1$, $(\mathrm{id}\cdot\mathbf{1})(12)=12$.",
             ha="center", fontsize=12, color=ink)
    fig.subplots_adjust(left=0.065, right=0.98, bottom=0.24, top=0.82, wspace=0.26)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
