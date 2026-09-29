"""Plot real embeddings of powers of 1+sqrt(2), with exact coefficients.

PNG output goes to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    exponents = np.arange(-4, 5)
    epsilon = 1 + np.sqrt(2)
    plus = epsilon**exponents
    minus_absolute = epsilon**(-exponents)
    rows = []
    a, b = 1, 0
    for n in range(5):
        norm = a*a - 2*b*b
        assert norm == (-1)**n
        rows.append([str(n), str(a), str(b), f"{norm:+d}"])
        a, b = a + 2*b, a + b
    assert np.allclose(plus * minus_absolute, 1)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, table_ax) = plt.subplots(1, 2, figsize=(9.6, 4.8), dpi=120,
                                     gridspec_kw={"width_ratios": [1.4, 1]})
    ax.semilogy(exponents, plus, "o-", color="#186b9c", linewidth=2,
                label=r"$|\sigma_+(\varepsilon^n)|=(1+\sqrt{2})^n$")
    ax.semilogy(exponents, minus_absolute, "s-", color="#a65419", linewidth=2,
                label=r"$|\sigma_-(\varepsilon^n)|=(1+\sqrt{2})^{-n}$")
    ax.axhline(1, color="#757575", linewidth=0.8, linestyle="--")
    ax.set(xlabel=r"integer exponent $n$", ylabel="absolute value (logarithmic scale)",
           xlim=(-4.35, 4.35), ylim=(0.02, 50))
    ax.set_xticks(exponents)
    ax.grid(alpha=0.22)
    ax.legend(loc="upper center", fontsize=10, framealpha=1)
    table_ax.axis("off")
    table_ax.set_title(r"$\varepsilon^n=a_n+b_n\sqrt{2}$", pad=18)
    table = table_ax.table(cellText=rows,
                           colLabels=[r"$n$", r"$a_n$", r"$b_n$", r"$N(\varepsilon^n)$"],
                           cellLoc="center", colWidths=[0.17, 0.22, 0.22, 0.39],
                           bbox=[0, 0.28, 1, 0.63])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#cbd4dd")
        if row == 0:
            cell.set_facecolor("#dbeaf7")
        elif row % 2 == 0:
            cell.set_facecolor("#f5edf7")
        else:
            cell.set_facecolor("#eff7f2")
    table_ax.text(0.5, 0.12, "Even powers: norm +1\nOdd powers: norm −1",
                   ha="center", va="center", fontsize=12, transform=table_ax.transAxes)
    fig.suptitle(r"Powers of the unit $\varepsilon=1+\sqrt{2}$", fontsize=16, y=0.97)
    fig.text(0.5, 0.035, r"One embedding grows as the other shrinks:"
             r" $\sigma_+(\varepsilon^n)\,\sigma_-(\varepsilon^n)=(-1)^n$.",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.085, right=0.97, bottom=0.17, top=0.81, wspace=0.27)
    fig.savefig(Path.cwd() / "quadratic-field-unit-powers.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
