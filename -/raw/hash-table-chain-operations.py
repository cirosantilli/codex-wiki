"""Draw a deterministic separate-chaining example; write the PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, x, y, width, text, color="#eef4fa"):
    ax.add_patch(FancyBboxPatch((x, y), width, 0.48,
                              boxstyle="round,pad=0.025", facecolor=color,
                              edgecolor="#35516b", linewidth=1.2))
    ax.text(x + width / 2, y + 0.24, text, ha="center", va="center", fontsize=13)


def main():
    records = [(1, "A"), (5, "B"), (9, "C"), (2, "D")]
    buckets = [[] for _ in range(4)]
    for key, value in records:
        buckets[key % 4].insert(0, (key, value))
    assert buckets == [[], [(9, "C"), (5, "B"), (1, "A")], [(2, "D")], []]

    fig, ax = plt.subplots(figsize=(10.8, 7), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 10.8), ylim=(0, 7))
    ax.axis("off")
    ax.text(5.4, 6.72, "Separate chaining: compare keys inside the selected bucket",
            ha="center", fontsize=16, weight="bold")
    ax.text(5.4, 6.3, "Constructed example • h₄(k) = k mod 4 • insert new keys at the head",
            ha="center", fontsize=12)
    for i, chain in enumerate(buckets):
        y = 5.54 - i * 0.62
        box(ax, 0.4, y, 1.2, f"bucket {i}")
        if not chain:
            ax.text(2.2, y + 0.24, "empty", va="center", fontsize=13, color="#687787")
        for j, (key, value) in enumerate(chain):
            x = 2.1 + j * 2
            ax.annotate("", xy=(x - 0.05, y + 0.24),
                        xytext=(1.65 if j == 0 else x - 0.52, y + 0.24),
                        arrowprops=dict(arrowstyle="->", color="#35516b", lw=1.5))
            box(ax, x, y, 1.45, f"{key} : {value}", "#fff0ce" if i == 1 else "#eef4fa")
    ax.text(9.0, 5.16, "4 records\n4 buckets\nα = 1", ha="center", va="center",
            fontsize=14, linespacing=1.6)

    rows = [
        ["get(5)", "9, 5", "B", "9:C → 5:B → 1:A", "4"],
        ["get(13)", "9, 5, 1", "absent", "9:C → 5:B → 1:A", "4"],
        ["put(5, B*)", "9, 5", "replace", "9:C → 5:B* → 1:A", "4"],
        ["delete(9)", "9", "unlink", "5:B* → 1:A", "3"],
        ["put(13, E)", "5, 1", "insert", "13:E → 5:B* → 1:A", "4"],
    ]
    table = ax.table(cellText=rows,
                     colLabels=["Operation", "Keys checked", "Result", "Bucket 1 after operation", "n"],
                     colWidths=[0.18, 0.16, 0.12, 0.46, 0.08],
                     bbox=[0.025, 0.07, 0.95, 0.37], cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#c1cdd7")
        cell.set_facecolor("#e5edf5" if row == 0 else ("white" if row % 2 else "#f6f8fa"))
        if row == 0:
            cell.set_text_props(weight="bold")
    ax.text(5.4, 0.12, "All five operations select bucket 1. Equal bucket indices do not establish equal keys.",
            ha="center", fontsize=11)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
