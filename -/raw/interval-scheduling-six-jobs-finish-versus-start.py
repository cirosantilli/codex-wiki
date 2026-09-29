"""Original six-job comparison; Python 3.14, matplotlib 3.10.7.

Run from _media; writes this script's basename with a .png extension.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch


JOBS = [("A", 0, 6), ("B", 1, 3), ("C", 3, 5),
        ("D", 5, 7), ("E", 6, 9), ("F", 8, 10)]


def scan(key):
    chosen = []
    finish = None
    for name, start, end in sorted(JOBS, key=key):
        if finish is None or start >= finish:
            chosen.append(name)
            finish = end
    return chosen


def main():
    finish = scan(lambda job: job[2])
    start = scan(lambda job: job[1])
    assert finish == ["B", "C", "D", "F"]
    assert start == ["A", "E"]
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(11, 6.1), dpi=110,
                             sharex=True, sharey=True, facecolor="white")
    for ax, accepted, color, title in zip(
        axes, [finish, start], ["#087e8b", "#b86118"],
        ["Earliest finish: 4 jobs", "Earliest start: 2 jobs"]
    ):
        ax.set_facecolor("white")
        for row, (name, left, right) in enumerate(JOBS):
            y = 5 - row
            shade = color if name in accepted else "#d4dbe1"
            ax.plot([left, right], [y, y], color=shade, lw=15,
                    solid_capstyle="butt", zorder=2)
            ax.plot(left, y, "o", ms=7, color=shade, mec="#334155", zorder=3)
            ax.plot(right, y, "o", ms=7, mfc="white", mec="#334155", zorder=3)
            ax.text((left + right) / 2, y + .25,
                    f"{name} [{left}, {right})", ha="center", fontsize=11)
        ax.set_title(title, color=color, fontweight="bold", pad=37)
        ax.set_xlim(-.4, 10.4)
        ax.set_ylim(-.55, 5.7)
        ax.set_xticks(range(11))
        ax.set_yticks([])
        ax.set_xlabel("Time (arbitrary units)")
        ax.grid(axis="x", color="#edf0f3", zorder=0)
        ax.spines[["left", "right", "top"]].set_visible(False)
        ax.legend(handles=[Patch(facecolor=color, label="Accepted"),
                           Patch(facecolor="#d4dbe1", label="Rejected")],
                  ncol=2, frameon=False, loc="lower center",
                  bbox_to_anchor=(.5, 1.005), fontsize=11)
        ax.text(.5, -.22, "Chosen: " + ", ".join(accepted),
                transform=ax.transAxes, ha="center", fontweight="bold",
                color=color)
    fig.suptitle("Finishing sooner can leave room for more jobs", y=.97,
                 fontsize=18, color="#172b3a")
    fig.text(.5, .035, "Filled start, hollow finish: [start, finish)  •  Meeting endpoints are compatible",
             ha="center", fontsize=11, color="#334155")
    fig.subplots_adjust(left=.045, right=.98, top=.77, bottom=.25, wspace=.14)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
