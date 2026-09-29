"""Generate logical-implication-truth-table.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    numbers = [4, 2, 3, 1]
    rows = []
    implications = []
    converses = []
    for n in numbers:
        a, b = n % 2 == 0, n > 2
        implication = not a or b
        contrapositive = b or not a
        converse = not b or a
        assert implication == contrapositive
        implications.append(implication)
        converses.append(converse)
        rows.append([str(n)] + ["T" if x else "F" for x in
                                (a, b, implication, contrapositive, converse)])
    assert implications == [True, False, True, True]
    assert converses == [True, True, False, True]
    fig, ax = plt.subplots(figsize=(9.3, 4.0), dpi=120, facecolor="white")
    ax.axis("off")
    fig.suptitle("Classical implication: one forbidden case", fontsize=17, y=.96)
    ax.set_title(r"$A$: $n$ is even       $B$: $n>2$       T = true, F = false",
                 fontsize=12, pad=15)
    table = ax.table(cellText=rows,
                     colLabels=[r"$n$", r"$A$", r"$B$", r"$A\to B$",
                                r"$\neg B\to\neg A$", r"$B\to A$"],
                     colWidths=[.09, .11, .11, .21, .25, .23],
                     cellLoc="center", bbox=[0, .16, 1, .76])
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#9fa9b2")
        if row == 0:
            cell.set_facecolor("#edf1f4")
        elif col >= 3:
            true = rows[row - 1][col] == "T"
            cell.set_facecolor("#e2f0e9" if true else "#f9dedb")
            cell.set_text_props(color="#166044" if true else "#a12f28")
    fig.text(.5, .10, "Implication and contrapositive agree in every row.",
             ha="center", fontsize=12)
    fig.text(.5, .045, "The converse differs at n = 2 and n = 3.",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=.04, right=.96, top=.75, bottom=.15)
    fig.savefig(Path.cwd() / "logical-implication-truth-table.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
