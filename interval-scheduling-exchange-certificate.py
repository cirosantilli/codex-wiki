"""Show a safe first-job exchange and a combinatorial upper bound.

Original examples. Tested with Python 3.14 and matplotlib 3.10.7.
Run from the output directory; the PNG basename matches this script.
"""
from pathlib import Path

import matplotlib.pyplot as plt


BLUE = "#167c99"
ORANGE = "#c56a24"
DARK = "#172b3a"


def interval(ax, start, finish, y, label, color, width=15):
    ax.plot([start, finish], [y, y], color=color, lw=width,
            solid_capstyle="butt", zorder=2)
    ax.plot(start, y, "o", ms=7, color=color, mec=DARK, zorder=3)
    ax.plot(finish, y, "o", ms=7, mfc="white", mec=DARK, zorder=3)
    ax.text((start + finish) / 2, y + .23, label, ha="center", fontsize=12, color=DARK)


def clean(ax, ticks):
    ax.set_xticks(ticks)
    ax.set_yticks([])
    ax.grid(axis="x", color="#e9edf0", zorder=0)
    for spine in ["left", "right", "top"]:
        ax.spines[spine].set_visible(False)
    ax.set_xlabel("Time", fontsize=12)


def main():
    plt.rcParams.update({"font.size": 12})
    fig = plt.figure(figsize=(10.6, 8.1), dpi=100, facecolor="white")
    top = fig.add_axes([.19, .64, .73, .22])
    for y, first, color in [(1.1, (0, 4, "q [0, 4)"), ORANGE),
                            (0, (1, 2, "g [1, 2)"), BLUE)]:
        interval(top, first[0], first[1], y, first[2], color)
        interval(top, 4, 6, y, "u [4, 6)", BLUE)
        interval(top, 6, 7, y, "v [6, 7)", BLUE)
    top.text(-.35, 1.1, "Before\n3 jobs", ha="right", va="center", color=ORANGE)
    top.text(-.35, 0, "After\n3 jobs", ha="right", va="center", color=BLUE)
    top.axvspan(2, 4, ymin=.0, ymax=.32, color="#ebf5f7", zorder=0)
    top.text(3, -.36, "Extra room", ha="center", fontsize=11, color=BLUE)
    top.set_xlim(-.15, 7.3)
    top.set_ylim(-.55, 1.75)
    clean(top, range(8))
    fig.text(.08, .95, "1. Replace the first job without disturbing later jobs", fontsize=17,
             fontweight="bold", color=DARK)
    fig.text(.55, .895, r"$f_g = 2\ \leq\ f_q = 4\ \leq\ s_u = 4$",
             ha="center", fontsize=15, color=DARK)
    fig.text(.55, .565, "Both schedules are optimal for this separate four-job instance.",
             ha="center", fontsize=11, color="#374151")

    bottom = fig.add_axes([.19, .13, .73, .32])
    groups = [[("A", 0, 6), ("B", 1, 2)], [("C", 2, 4)],
              [("D", 4, 6), ("E", 5, 8)], [("F", 6, 7)], [("G", 7, 9)]]
    selected = {"B", "C", "D", "F", "G"}
    for row, group in enumerate(groups):
        y = (4 - row) * 1.35
        for i, (name, start, finish) in enumerate(group):
            yy = y + (.35 if len(group) == 2 and i == 0 else -.2 if len(group) == 2 else 0)
            interval(bottom, start, finish, yy, name,
                     BLUE if name in selected else "#bbc4cd", width=11)
        bottom.text(-.45, y, "{" + ", ".join(job[0] for job in group) + "}",
                    ha="right", va="center", color=DARK)
        bottom.text(9.5, y, "≤ 1 job", va="center", fontsize=12, color=DARK)
    bottom.set_xlim(-.15, 10.4)
    bottom.set_ylim(-.7, 6.1)
    clean(bottom, range(10))
    fig.text(.08, .505, "2. Five conflict groups certify the seven-job optimum", fontsize=17,
             fontweight="bold", color=DARK)
    fig.text(.5, .055, "At most 1 per group ⇒ at most 5 jobs.  B, C, D, F, G attain 5.",
             ha="center", fontsize=13, fontweight="bold", color=BLUE)
    fig.text(.5, .018, "Constructed examples • filled start, hollow finish • adjacent endpoints allowed",
             ha="center", fontsize=10, color="#374151")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
