"""Contrast totient aggregation and Möbius inversion; write basename PNG to cwd.

Tested with Python 3.14.4 and Matplotlib 3.10.7.
Reproduce: make _media/mobius-inversion-totient.png
"""

from math import gcd
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def mobius(n):
    """Compute mu by trial division, detecting any repeated prime factor."""
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def main():
    n = 12
    divisors = [d for d in range(1, n + 1) if n % d == 0]
    phi = [sum(gcd(a, d) == 1 for a in range(1, d + 1)) for d in divisors]
    groups = [[j for j in range(1, n + 1) if gcd(j, n) == n // d]
              for d in divisors]
    weights = [mobius(d) for d in divisors]
    contributions = [mu * (n // d) for d, mu in zip(divisors, weights)]
    assert divisors == [1, 2, 3, 4, 6, 12]
    assert phi == [1, 1, 2, 2, 2, 4] and sum(phi) == n
    assert list(map(len, groups)) == phi
    assert sorted(j for group in groups for j in group) == list(range(1, 13))
    assert weights == [1, -1, -1, 0, 1, 0]
    assert contributions == [12, -6, -4, 0, 2, 0]
    assert sum(contributions) == phi[-1] == 4
    assert groups[-1] == [1, 5, 7, 11]
    assert mobius(30) == -1 and mobius(60) == 0

    ink, blue, orange = "#243746", "#176997", "#b45325"
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.6), dpi=100,
                             facecolor="white")
    left_rows = [[str(d), str(value), ", ".join(map(str, group))]
                 for d, value, group in zip(divisors, phi, groups)]
    left_rows.append(["Sum", "12", "All 12 integers"])
    right_rows = [[str(d), f"{mu:+d}" if mu else "0", str(n // d),
                   f"{term:+d}" if term else "0"]
                  for d, mu, term in zip(divisors, weights, contributions)]
    right_rows.append(["Sum", "", "", "4"])
    tables = [
        axes[0].table(cellText=left_rows,
                      colLabels=[r"$d$", r"$\varphi(d)$", r"$j$ with $\gcd(j,12)=12/d$"],
                      colWidths=[0.15, 0.2, 0.65],
                      cellLoc="center", bbox=[0, 0.1, 1, 0.82]),
        axes[1].table(cellText=right_rows,
                      colLabels=[r"$d$", r"$\mu(d)$", r"$g(12/d)$", "Contribution"],
                      colWidths=[0.14, 0.2, 0.28, 0.38],
                      cellLoc="center", bbox=[0, 0.1, 1, 0.82]),
    ]
    for panel, table in enumerate(tables):
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        for (row, col), cell in table.get_celld().items():
            cell.set_edgecolor("#d9e2e8")
            cell.set_linewidth(0.8)
            cell.set_text_props(color=ink)
            if row == 0:
                cell.set_facecolor("#edf2f6")
                cell.set_text_props(fontsize=11)
            elif panel == 0 and col == 1:
                cell.set_facecolor("#edf5fa")
                cell.set_text_props(color=blue)
            elif panel == 1 and row <= len(divisors):
                mu = weights[row - 1]
                cell.set_facecolor("#edf5fa" if mu > 0 else
                                   "#fff2e9" if mu < 0 else "#f3f3f3")
                if col == 3:
                    cell.set_text_props(color=blue if mu > 0 else
                                        orange if mu < 0 else "#6c7780")
            if row == 7:
                cell.set_facecolor("#e6eef5")
                cell.set_text_props(weight="bold", fontsize=13)
        axes[panel].axis("off")
    axes[0].set_title("Aggregate: classify all 12 integers by gcd", fontsize=14,
                      color=ink, pad=13)
    axes[1].set_title("Invert: weight the aggregates by μ", fontsize=14,
                      color=ink, pad=13)
    axes[0].text(0.5, -0.04, r"$g(12)=1+1+2+2+2+4=12$", ha="center",
                 transform=axes[0].transAxes, fontsize=15, color=blue)
    axes[1].text(0.5, -0.04, r"$\varphi(12)=12-6-4+0+2+0=4$", ha="center",
                 transform=axes[1].transAxes, fontsize=15, color=blue)
    fig.suptitle("Möbius inversion recovers the totient from g(n) = n",
                 fontsize=17, color=ink, y=0.975)
    fig.text(0.5, 0.045, "The four integers coprime to 12 are 1, 5, 7, 11.",
             ha="center", fontsize=13, color=ink)
    fig.subplots_adjust(left=0.035, right=0.975, bottom=0.2,
                        top=0.81, wspace=0.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
