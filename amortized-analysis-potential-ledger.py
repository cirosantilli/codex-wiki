"""Draw a nonnegative potential ledger; Python 3.14 and matplotlib 3.10."""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    capacity = 1
    potential = 0
    rows = [["0 (empty)", "1", "—", "—", "—", "0"]]
    resize_rows = []
    for i in range(1, 11):
        copied = 0
        if i - 1 == capacity:
            copied = capacity
            capacity *= 2
            resize_rows.append(i + 1)
        actual = 1 + copied
        new_potential = max(0, 2 * i - capacity)
        change = new_potential - potential
        rows.append([str(i), str(capacity), str(actual), f"{change:+d}",
                     str(actual + change), str(new_potential)])
        potential = new_potential

    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(10.6, 6.1), dpi=110)
    fig.set_facecolor("white")
    ax.set_axis_off()
    labels = ["Append i", "Capacity Cᵢ", "Actual cᵢ", "Change ΔΦᵢ",
              "Charge ĉᵢ", "Credit Φᵢ"]
    table = ax.table(cellText=rows, colLabels=labels, cellLoc="center",
                     colLoc="center", bbox=[0.02, 0.24, 0.96, 0.65])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#d1d8dc")
        cell.set_linewidth(0.65)
        if r == 0:
            cell.set_facecolor("#236b8e")
            cell.set_text_props(color="white", weight="bold")
        elif r in resize_rows:
            cell.set_facecolor("#fff1df")
        else:
            cell.set_facecolor("white")
        if r == 10:
            cell.set_text_props(weight="bold", color="#934214")
    ax.text(0.5, 0.97, "Potential is saved work: Φ(n, C) = max(0, 2n − C)",
            ha="center", va="center", fontsize=17, transform=ax.transAxes)
    ax.text(0.5, 0.17, "Append 9: 8 old credits + 3 charged − 9 actual cost = 2 credits left",
            ha="center", fontsize=12, color="#934214", transform=ax.transAxes)
    ax.text(0.5, 0.10, "Every row: charge = actual cost + change in credit.  Shaded rows resize.",
            ha="center", fontsize=11, transform=ax.transAxes)
    ax.text(0.5, 0.035, "Initially: size 0, capacity 1, credit 0.  First charge 2; every later charge 3.",
            ha="center", fontsize=11, transform=ax.transAxes)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
