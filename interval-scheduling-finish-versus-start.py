"""Compare two selection rules on an original seven-job instance.

Tested with Python 3.14, matplotlib 3.10.7; run from the output directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch


JOBS = [("A", 0, 6), ("B", 1, 2), ("C", 2, 4), ("D", 4, 6),
        ("E", 5, 8), ("F", 6, 7), ("G", 7, 9)]


def select(key):
    chosen = []
    finish = None
    for name, start, end in sorted(JOBS, key=key):
        if finish is None or start >= finish:
            chosen.append(name)
            finish = end
    return chosen


def main():
    finish_choice = select(lambda job: (job[2], job[0]))
    start_choice = select(lambda job: (job[1], job[0]))
    assert finish_choice == ["B", "C", "D", "F", "G"]
    assert start_choice == ["A", "F", "G"]
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.8), dpi=100,
                             sharex=True, sharey=True, facecolor="white")
    for ax, chosen, color, title in zip(
        axes, [finish_choice, start_choice], ["#167c99", "#c56a24"],
        ["Earliest finish: 5 jobs", "Earliest start: 3 jobs"]
    ):
        for row, (name, start, end) in enumerate(JOBS):
            y = 6 - row
            accepted = name in chosen
            shade = color if accepted else "#d5dbe0"
            ax.plot([start, end], [y, y], color=shade, lw=15,
                    solid_capstyle="butt", zorder=2)
            ax.plot(start, y, "o", ms=7, color=shade, mec="#374151", zorder=3)
            ax.plot(end, y, "o", ms=7, mfc="white", mec="#374151", zorder=3)
            ax.text((start + end) / 2, y + .26, f"{name} [{start}, {end})",
                    ha="center", fontsize=11, color="#172b3a")
        ax.set_title(title, pad=20, color=color, fontweight="bold")
        ax.set_xlim(-.35, 9.35)
        ax.set_ylim(-.6, 6.8)
        ax.set_xticks(range(10))
        ax.set_yticks([])
        ax.set_xlabel("Time")
        ax.grid(axis="x", color="#e9edf0", zorder=0)
        for spine in ["left", "right", "top"]:
            ax.spines[spine].set_visible(False)
        ax.text(.5, -.2, "Chosen: " + ", ".join(chosen), transform=ax.transAxes,
                ha="center", fontsize=12, color=color, fontweight="bold")
        ax.legend(handles=[Patch(facecolor=color, label="Accepted"),
                           Patch(facecolor="#d5dbe0", label="Rejected")],
                  loc="upper center", bbox_to_anchor=(.5, 1.04), ncol=2,
                  frameon=False, fontsize=10)
    fig.suptitle("Which local choice leaves room for more jobs?", fontsize=17,
                 y=.98, color="#172b3a")
    fig.text(.5, .02, "Constructed instance • filled start, hollow finish • adjacent endpoints allowed",
             ha="center", fontsize=11, color="#374151")
    fig.subplots_adjust(left=.045, right=.975, top=.80, bottom=.22, wspace=.12)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
