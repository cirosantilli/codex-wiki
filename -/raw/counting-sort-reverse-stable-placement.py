"""Draw every placement of an original labelled-record counting-sort example.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes counting-sort-reverse-stable-placement.png to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    records = [(2, "A"), (0, "B"), (2, "C"), (1, "D"),
               (0, "E"), (3, "F"), (2, "G")]
    counts = [sum(key == k for key, _ in records) for k in range(4)]
    endpoints = []
    total = 0
    for count in counts:
        total += count
        endpoints.append(total)
    output = [None] * len(records)
    colors = ["#2475ad", "#c67c15", "#23855b", "#8259aa"]
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 7.9), dpi=100, facecolor="white")
    fig.suptitle("Stable placement: scan right to left, fill each range right to left", fontsize=17, y=.97)
    fig.text(.5, .917, "Endpoint update first: E[k] ← E[k] − 1; then write the complete record at output[E[k]].",
             ha="center", fontsize=12)
    ax = fig.add_axes((.025, .025, .95, .855))
    ax.set(xlim=(0, 13.4), ylim=(-.3, 10.8))
    ax.axis("off")

    def box(x, y, record, newest=False):
        face = "white" if record is None else colors[record[0]]
        ax.add_patch(Rectangle((x, y), .86, .52, facecolor=face,
                               alpha=1 if newest or record is None else .27,
                               edgecolor="#c3c9cf", linewidth=1))
        if record is not None:
            ax.text(x + .43, y + .26, f"({record[0]},{record[1]})", ha="center", va="center",
                    fontsize=12, color="white" if newest else "#20313d",
                    fontweight="bold" if newest else "normal")

    ax.text(.15, 10.3, "Input index i", fontsize=11)
    ax.text(.15, 9.7, "Input record", fontsize=11)
    for i, record in enumerate(records):
        x = 5.8 + i
        ax.text(x + .43, 10.35, str(i), ha="center", fontsize=11)
        box(x, 9.45, record, newest=True)
    ax.annotate("", xy=(5.8, 9.1), xytext=(12.6, 9.1), arrowprops={"arrowstyle": "->", "lw": 2})
    ax.text(9.2, 8.77, "Scan order: G, F, E, D, C, B, A", ha="center", fontsize=11)

    headers = [(.15, "Step"), (1.0, "Read i"), (2.1, "Record"),
               (3.8, "E[k]: before → after"), (9.2, "Output slots j = 0, 1, 2, 3, 4, 5, 6")]
    for x, title in headers:
        ax.text(x, 8.12, title, ha="center" if x == 9.2 else "left", fontsize=11, fontweight="bold")
    ax.plot([.15, 12.65], [7.9, 7.9], color="#bcc4cb", lw=1)
    for step, i in enumerate(range(len(records) - 1, -1, -1), start=1):
        record = records[i]
        key = record[0]
        old = endpoints[key]
        endpoints[key] -= 1
        j = endpoints[key]
        output[j] = record
        y = 7.1 - (step - 1) * .83
        for x, label in [(.32, str(step)), (1.2, str(i)), (2.15, f"({key},{record[1]})"),
                         (3.8, f"E[{key}]: {old} → {j}")]:
            ax.text(x, y + .26, label, va="center", fontsize=12)
        for slot, item in enumerate(output):
            box(5.8 + slot, y, item, newest=(slot == j))
    ax.text(.15, .97, "Stable output", fontweight="bold")
    for j, record in enumerate(output):
        box(5.8 + j, .69, record, newest=True)
        ax.text(6.23 + j, .42, str(j), ha="center", fontsize=10)
    ax.text(.15, -.05, "Equal-key arrival order survives:  B before E;  A before C before G.  Letters travel with their keys.",
            fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
