"""Compare two-input Boolean operations; emit the matching PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.965, bottom=0.20, top=0.78)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5)
    ax.axis("off")
    headers = ["P", "Q", "AND\n" + r"$P\wedge Q$", "OR\n" + r"$P\vee Q$",
               "XOR\n" + r"$P\oplus Q$", "NOT P\n" + r"$\neg P$", "NOT Q\n" + r"$\neg Q$"]
    for j, label in enumerate(headers):
        ax.add_patch(Rectangle((j, 4), 1, 1, facecolor="#25374a", edgecolor="white"))
        ax.text(j + 0.5, 4.5, label, ha="center", va="center", color="white", fontsize=15)
    for i, (p, q) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
        values = [p, q, p & q, p | q, p ^ q, 1 - p, 1 - q]
        for j, v in enumerate(values):
            y = 3 - i
            color = "#eef1f5" if j < 2 else ("#cee9e6" if v else "#ffffff")
            ax.add_patch(Rectangle((j, y), 1, 1, facecolor=color, edgecolor="#bdc7d2"))
            ax.text(j + 0.5, y + 0.5, str(v), ha="center", va="center", fontsize=23,
                    color="#123e42" if v else "#536071", weight="bold" if j >= 2 else "normal")
    ax.add_patch(Rectangle((3.02, 0.03), 1.96, 0.94, fill=False, linewidth=3,
                           edgecolor="#be5918"))
    fig.text(0.5, 0.94, "Two input bits, four possible cases", ha="center", fontsize=22, weight="bold")
    fig.text(0.5, 0.865, "1 = true     0 = false     shaded cells = true outputs", ha="center", fontsize=14)
    fig.text(0.5, 0.115, "Both true: inclusive OR accepts; XOR excludes.", ha="center",
             fontsize=17, color="#914414", weight="bold")
    fig.text(0.5, 0.045, "NOT has one input; its value repeats when only the other input changes.",
             ha="center", fontsize=13, color="#425165")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
