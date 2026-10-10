"""Original shortest-duration counterexample; Python 3.14, matplotlib 3.10.7.

Run from _media; writes this script's basename with a .png extension.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch


JOBS = [("A", 0, 5), ("B", 5, 10), ("C", 4, 6)]


def main():
    plt.rcParams.update({"font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.2), dpi=110,
                             sharex=True, sharey=True, facecolor="white")
    for ax, chosen, color, title in zip(
        axes, [{"C"}, {"A", "B"}], ["#b86118", "#087e8b"],
        ["Shortest duration: 1 job", "Optimum: 2 jobs"]
    ):
        ax.set_facecolor("white")
        for left, right in [(4, 5), (5, 6)]:
            ax.axvspan(left, right, facecolor="#fce2d6", zorder=0)
        ax.axvline(5, color="#a85d36", ls="--", lw=1, zorder=1)
        for row, (name, left, right) in enumerate(JOBS):
            y = 2 - row
            shade = color if name in chosen else "#cbd3db"
            ax.plot([left, right], [y, y], color=shade, lw=16,
                    solid_capstyle="butt", zorder=2)
            ax.plot(left, y, "o", ms=7, color=shade, mec="#334155", zorder=3)
            ax.plot(right, y, "o", ms=7, mfc="white", mec="#334155", zorder=3)
            ax.text((left + right) / 2, y + .24,
                    f"{name} [{left}, {right})", ha="center", fontsize=12)
        ax.set_title(title, fontsize=16, color=color, fontweight="bold", pad=19)
        ax.set_xlim(-.4, 10.4)
        ax.set_ylim(-.5, 2.65)
        ax.set_xticks(range(11))
        ax.set_yticks([])
        ax.set_xlabel("Time (arbitrary units)")
        ax.spines[["left", "right", "top"]].set_visible(False)
        ax.text(.5, -.34, "Chosen: " + ", ".join(sorted(chosen)),
                transform=ax.transAxes, ha="center", fontweight="bold",
                color=color)
    fig.suptitle("Separate example: the shortest job straddles the handover", y=.96,
                 fontsize=17, color="#172b3a")
    fig.legend(handles=[Patch(facecolor="#fce2d6", label="Overlap with C: [4, 5) and [5, 6)")],
               loc="lower center", bbox_to_anchor=(.5, .07), frameon=False,
               fontsize=11)
    fig.text(.5, .025, "A and B meet at time 5 and are compatible; C overlaps both.",
             ha="center", fontsize=11, color="#334155")
    fig.subplots_adjust(left=.045, right=.98, top=.77, bottom=.35, wspace=.14)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
