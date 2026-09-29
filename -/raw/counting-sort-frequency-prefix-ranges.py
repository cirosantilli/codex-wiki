"""Draw original counting-sort frequencies and exclusive output ranges.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes counting-sort-frequency-prefix-ranges.png to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    records = [(2, "A"), (0, "B"), (2, "C"), (1, "D"),
               (0, "E"), (3, "F"), (2, "G")]
    counts = [sum(key == k for key, _ in records) for k in range(4)]
    boundaries = [0]
    for count in counts:
        boundaries.append(boundaries[-1] + count)
    colors = ["#2475ad", "#c67c15", "#23855b", "#8259aa"]
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.5, 6.2), dpi=100, facecolor="white")
    fig.suptitle("Counting sort: frequencies become output ranges", fontsize=18, y=.97)
    fig.text(.5, .895, "Original input: (2,A), (0,B), (2,C), (1,D), (0,E), (3,F), (2,G)",
             ha="center", fontsize=12)

    ax = fig.add_axes((.085, .48, .34, .32))
    ax.bar(range(4), counts, color=colors, width=.62)
    for k, count in enumerate(counts):
        ax.text(k, count + .12, str(count), ha="center", fontsize=14)
    ax.set(xlabel="Integer key k", ylabel="Count c[k] (records)",
           xticks=range(4), yticks=range(4), ylim=(0, 3.7))
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("n = 7 records; K = 4 possible keys", fontsize=12, pad=14)

    table_ax = fig.add_axes((.48, .45, .48, .35))
    table_ax.axis("off")
    table = table_ax.table(
        cellText=[[k, counts[k], boundaries[k], boundaries[k + 1],
                   f"[{boundaries[k]}, {boundaries[k + 1]})"] for k in range(4)],
        colLabels=["Key k", "c[k]", "S[k]", "P[k]", "Output range"],
        colWidths=[.14, .14, .14, .14, .30], cellLoc="center", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.1, 1.9)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d7dce1")
        if row == 0:
            cell.set_facecolor("#eef1f4")
        elif col == 0:
            cell.set_facecolor(colors[row - 1])
            cell.get_text().set_color("white")

    slots = fig.add_axes((.085, .105, .86, .255))
    slots.set(xlim=(-.25, 7.25), ylim=(-.5, 1.55))
    slots.axis("off")
    for k in range(4):
        left, right = boundaries[k:k + 2]
        for j in range(left, right):
            slots.add_patch(Rectangle((j, .2), 1, .52, facecolor=colors[k],
                                      edgecolor="white", linewidth=2))
            slots.text(j + .5, .46, f"key {k}", ha="center", va="center", color="white")
            slots.text(j + .5, -.02, str(j), ha="center", va="center")
        slots.plot([left, right], [1.02, 1.02], color=colors[k], linewidth=3)
        slots.plot([left, left], [.9, 1.12], color=colors[k], linewidth=2)
        slots.plot([right, right], [.9, 1.12], color=colors[k], linewidth=2)
        slots.text((left + right) / 2, 1.32, f"[{left}, {right})", ha="center", color=colors[k])
    for boundary in boundaries:
        slots.text(boundary, .83, str(boundary), ha="center", fontsize=10)
    slots.text(3.5, -.4, "Output slot j (zero-based): 0 through 6", ha="center")
    fig.text(.5, .025, "S[k] counts keys < k; P[k] counts keys ≤ k.  P[k] is an endpoint, not an occupied slot.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
