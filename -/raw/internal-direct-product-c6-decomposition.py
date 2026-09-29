"""Original internal-product addition table for C6; PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    h_values, k_values = [0, 3], [0, 2, 4]
    results = [[(h+k) % 6 for k in k_values] for h in h_values]
    assert sorted(v for row in results for v in row) == list(range(6))
    fig, ax = plt.subplots(figsize=(7.4, 4), dpi=120)
    fig.patch.set_facecolor("white")
    ax.axis("off")
    table = ax.table(
        cellText=[[str(v) for v in row] for row in results],
        rowLabels=[f"h = {h}" for h in h_values],
        colLabels=[f"k = {k}" for k in k_values],
        cellLoc="center", rowLoc="center", colLoc="center",
        bbox=[.17, .15, .78, .66])
    table.auto_set_font_size(False)
    table.set_fontsize(18)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#888888")
        cell.set_facecolor("#fff0df" if row == 0 else
                           "#e6f0f7" if col == -1 else "white")
    table[2, 2].set_facecolor("#ffe4bd")
    fig.suptitle("Internal direct product inside the additive group modulo six",
                 fontsize=14, y=.97)
    ax.set_title(r"$H=\{0,3\},\quad K=\{0,2,4\}$; entries are $h+k$ modulo 6",
                 fontsize=12, pad=12)
    fig.text(.5, .05,
             "Every result appears once. Highlighted: 1 = 3 + 4 modulo 6.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.02, right=.98, top=.76, bottom=.14)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
