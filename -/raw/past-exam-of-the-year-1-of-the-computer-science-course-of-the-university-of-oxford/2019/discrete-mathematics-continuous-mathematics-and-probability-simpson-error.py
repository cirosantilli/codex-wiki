"""Compute original Simpson-error evidence; write the opaque PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (+dfsg1 build).
Dependencies are the existing root pyproject dependencies; no SciPy is used.
The integral and every quadrature value are computed with Decimal precision 80.
"""

from decimal import Decimal, localcontext
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def computed_errors(strip_counts):
    """Return the exact-integral comparison and the two proved upper bounds."""
    with localcontext() as context:
        context.prec = 80
        one = Decimal(1)
        e = one.exp()
        integral = e - one - e / Decimal(720)
        rows = []
        for count in strip_counts:
            n = int(count)
            if n < 2 or n % 2:
                raise ValueError("Simpson strip counts must be positive and even")
            dn = Decimal(n)
            spacing = one / dn

            def integrand(x):
                return x.exp() - e * x**5 / Decimal(120)

            weighted_sum = integrand(Decimal(0)) + integrand(one)
            weighted_sum += sum(
                (4 if j % 2 else 2) * integrand(Decimal(j) * spacing)
                for j in range(1, n)
            )
            actual = spacing * weighted_sum / 3 - integral
            global_bound = one / (180 * dn**4)
            panel_bound = (
                (e - one) / ((2 / dn).exp() - one) - e * dn / 4 + e / 2
            ) / (90 * dn**5)
            if not (0 < actual <= panel_bound <= global_bound):
                raise ArithmeticError("Computed error violates a proved bound")
            rows.append((n, actual, global_bound, panel_bound))
        return rows


def main():
    counts = np.arange(8, 130, 2, dtype=int)
    rows = computed_errors(counts)
    actual = np.array([float(row[1]) for row in rows])
    global_bound = np.array([float(row[2]) for row in rows])
    panel_bound = np.array([float(row[3]) for row in rows])
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 11,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
        }
    )
    fig, ax = plt.subplots(figsize=(8.4, 5.2), layout="constrained")
    ax.loglog(counts, global_bound, "--", color="#b45f06", lw=2,
              label="Global derivative bound")
    ax.loglog(counts, panel_bound, "-.", color="#215a9c", lw=2,
              label="Panelwise derivative bound")
    ax.loglog(counts, actual, "-", color="#247047", lw=2,
              label="Computed Simpson error (80-digit arithmetic)")
    ax.axhline(1e-10, color="#555555", lw=1)
    ax.text(8.4, 1.18e-10, "Required error: less than 10⁻¹⁰",
            color="#333333", fontsize=10)
    for n, colour, label, height in [
        (68, "#215a9c", "68 strips\npanelwise guarantee", 1.9e-8),
        (88, "#b45f06", "88 strips\nglobal guarantee", 2.0e-9),
    ]:
        ax.axvline(n, color=colour, lw=1, alpha=0.65)
        ax.annotate(label, xy=(n, 1e-10), xytext=(n, height),
                    ha="center", va="bottom", fontsize=9, color=colour,
                    arrowprops={"arrowstyle": "-", "color": colour, "lw": 0.8})
    ax.set(
        xlabel="Number of strips n (even)",
        ylabel="Absolute error or certified upper bound",
        title="Simpson quadrature: uniform and panelwise guarantees",
        xlim=(8, 130),
        ylim=(5e-12, 2e-6),
    )
    ax.set_xticks([8, 16, 32, 64, 128], labels=["8", "16", "32", "64", "128"])
    ax.grid(which="major", color="#dedede", linewidth=0.6)
    ax.legend(loc="lower left", fontsize=9, framealpha=1, facecolor="white")
    output = Path(Path(__file__).stem + ".png")
    temporary = output.with_suffix(".png.tmp")
    fig.savefig(temporary, format="png", dpi=150, transparent=False,
                metadata={"Software": "Original Decimal/Matplotlib quadrature calculation"})
    temporary.replace(output)
    plt.close(fig)
    print(output.name)


if __name__ == "__main__":
    main()
