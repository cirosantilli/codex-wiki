"""Compare integer radicals and the two prime-factor counts.

Run from _media: python3 ../prime-factor-multiplicity-comparison.py
The PNG basename is written to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository's pyproject.toml.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    primes = np.array([2, 3, 5])
    exponents = np.array([[3, 2, 0], [1, 1, 1], [5, 0, 0], [2, 2, 0]])
    numbers = np.prod(primes ** exponents, axis=1)
    radicals = np.prod(np.where(exponents > 0, primes, 1), axis=1)
    distinct = np.count_nonzero(exponents, axis=1)
    total = exponents.sum(axis=1)
    labels = [r"$72=2^3\cdot3^2$", r"$30=2\cdot3\cdot5$",
              r"$32=2^5$", r"$36=2^2\cdot3^2$"]
    colors = ["#256796", "#aa551b", "#27804c"]
    plt.rcParams.update({"font.size": 12})
    fig, (blocks, table_ax) = plt.subplots(
        1, 2, figsize=(9.0, 5.6), dpi=120,
        gridspec_kw={"width_ratios": [1.65, 1]}, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.25, top=0.80, wspace=0.10)
    blocks.set(xlim=(-2.8, 6.7), ylim=(-0.7, 3.7))
    blocks.axis("off")
    blocks.set_title("Prime occurrences, grouped by prime", fontsize=12, pad=12)
    for row, (powers, label) in enumerate(zip(exponents, labels)):
        y = 3 - row
        blocks.text(-2.65, y, label, va="center", fontsize=13)
        x = 0.0
        for prime, exponent, color in zip(primes, powers, colors):
            if exponent == 0:
                continue
            for _ in range(int(exponent)):
                blocks.add_patch(Rectangle((x, y - 0.29), 0.73, 0.58,
                                           facecolor=color, edgecolor="white", linewidth=1.5))
                blocks.text(x + 0.365, y, str(prime), color="white",
                            ha="center", va="center", weight="bold", fontsize=13)
                x += 0.80
            x += 0.28
    table_ax.axis("off")
    table_ax.set_title("Three summaries", fontsize=12, pad=12)
    cells = np.column_stack([numbers, radicals, distinct, total]).astype(str)
    table = table_ax.table(
        cellText=cells, colLabels=[r"$n$", r"$\mathrm{rad}(n)$", r"$\omega(n)$", r"$\Omega(n)$"],
        colWidths=[0.18, 0.33, 0.245, 0.245], cellLoc="center", bbox=[0.0, 0.055, 1.0, 0.89])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, _), cell in table.get_celld().items():
        cell.set_edgecolor("#d4d4d4")
        cell.set_facecolor("#eef2f5" if row == 0 else "white")
        if row == 0:
            cell.get_text().set_weight("bold")
    fig.suptitle("Keep the primes, count the groups, or count every copy", fontsize=16, y=0.96)
    fig.text(0.5, 0.18, r"$\mathrm{rad}$: multiply one prime per group     "
             r"$\omega$: count groups     $\Omega$: count boxes", ha="center", fontsize=12)
    fig.text(0.5, 0.105, "72 and 36 share their primes; 72 and 32 share their total count.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, r"No prime boxes for 1: $\mathrm{rad}(1)=1$, $\omega(1)=\Omega(1)=0$.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "prime-factor-multiplicity-comparison.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
