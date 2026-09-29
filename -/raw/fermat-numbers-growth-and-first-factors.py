"""Original exact-arithmetic illustration of Fermat numbers.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes its matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    numbers = [2 ** (2**n) + 1 for n in range(9)]
    assert numbers[5] == 641 * 6700417
    digits = [len(str(number)) for number in numbers]
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.6), gridspec_kw={"width_ratios": [1.6, 1]})
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.17, top=0.79, wspace=0.14)
    fig.suptitle("Fermat numbers: a striking start is not a universal pattern", fontsize=18, y=0.97)
    fig.text(0.5, 0.885, r"Exact integers: $F_n=2^{2^n}+1$; each step doubles the exponent", ha="center")
    axes[0].axis("off")
    rows = [[str(n), str(2**n), f"{numbers[n]:,}", "prime" if n < 5 else "641 × 6,700,417"] for n in range(6)]
    table = axes[0].table(cellText=rows, colLabels=["n", "Exponent", "Fₙ", "Arithmetic verdict"], cellLoc="center", colWidths=[0.08, 0.17, 0.30, 0.45], bbox=[0, 0.10, 1, 0.84])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, column), cell in table.get_celld().items():
        cell.set_edgecolor("#d2d9e0")
        if row == 0:
            cell.set_facecolor("#e9eff5")
            cell.set_text_props(weight="bold")
        else:
            cell.set_facecolor("#fff0e5" if row == 6 else "white")
    axes[0].text(0.5, 0, "One proper factor is enough to refute ‘all are prime’.", transform=axes[0].transAxes, ha="center", va="center", fontsize=11)
    ax = axes[1]
    ax.bar(range(9), digits, color="#235d9f", width=0.65)
    for n, value in enumerate(digits):
        ax.text(n, value + 1.2, str(value), ha="center", fontsize=11)
    ax.set(xlabel="Index n", ylabel="Number of decimal digits", ylim=(0, 87), xticks=range(9))
    ax.set_title("Size grows very quickly", fontsize=14)
    ax.grid(axis="y", color="#e2e6ea")
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    fig.text(0.5, 0.055, "Bars show digit counts, not primality. All entries are calculated exactly, not measured data.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
