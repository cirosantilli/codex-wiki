"""Draw paired original schedule bars; write the matching PNG basename to cwd.

Run from _media. Tested with Python 3.14.4 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def main():
    tasks = list("ABCDEF")
    durations = dict(zip(tasks, [3, 2, 4, 2, 3, 1]))
    predecessors = {"A": [], "B": ["A"], "C": ["A"],
                    "D": ["B", "C"], "E": [], "F": ["D", "E"]}
    early = {}
    for task in tasks:
        early[task] = max((early[p] + durations[p]
                           for p in predecessors[task]), default=0)
    finish = max(early[t] + durations[t] for t in tasks)
    successors = {t: [] for t in tasks}
    for task, parents in predecessors.items():
        for parent in parents:
            successors[parent].append(task)
    late = {}
    for task in reversed(tasks):
        late[task] = min((late[s] for s in successors[task]),
                         default=finish) - durations[task]
    floats = [late[t] - early[t] for t in tasks]
    assert finish == 10 and floats == [0, 2, 0, 0, 6, 0]

    teal, blue, ink = "#007b78", "#476c9c", "#203548"
    fig, ax = plt.subplots(figsize=(9.0, 6.0), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    centers = list(range(5, -1, -1))
    for task, y, slack in zip(tasks, centers, floats):
        color = teal if slack == 0 else blue
        # Two separate tracks make coincident critical bars visible too.
        early_y, late_y, height = y + 0.20, y - 0.20, 0.25
        ax.barh(early_y, durations[task], left=early[task], height=height,
                color=color, edgecolor=color, linewidth=1.5, zorder=3)
        ax.barh(late_y, durations[task], left=late[task], height=height,
                facecolor="white", edgecolor=color, linewidth=1.8, zorder=3)
        ax.text(early[task] + durations[task] / 2, early_y,
                f"{early[task]}–{early[task] + durations[task]}",
                ha="center", va="center", fontsize=9, color="white", zorder=4)
        ax.text(late[task] + durations[task] / 2, late_y,
                f"{late[task]}–{late[task] + durations[task]}",
                ha="center", va="center", fontsize=9, color=color, zorder=4)
        if slack:
            bracket_y = y - 0.42
            ax.plot([early[task], late[task]], [bracket_y, bracket_y],
                    color=color, linewidth=1.3, zorder=4)
            ax.vlines([early[task], late[task]], bracket_y - 0.05,
                      bracket_y + 0.05, color=color, linewidth=1.3, zorder=4)
        ax.text(10.32, y, str(slack), ha="center", va="center",
                fontsize=12, color=color, fontweight="bold")
        ax.axhline(y - 0.50, color="#e6eaef", lw=0.8, zorder=0)
    ax.axvline(finish, color=ink, linestyle="--", lw=1.5, zorder=2)
    ax.text(10.32, 5.60, "Float", ha="center", va="center",
            fontsize=10, color=ink)
    ax.set(yticks=centers, yticklabels=tasks, xticks=range(11),
           xlim=(-0.15, 10.65), ylim=(-0.65, 5.7), xlabel="Time units")
    ax.tick_params(axis="both", labelsize=11, length=0, pad=7)
    ax.grid(axis="x", color="#e2e8ee", linewidth=0.8, zorder=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("Same project finish: earliest and latest schedules",
                 fontsize=15, color=ink, pad=40)
    ax.legend(handles=[Patch(facecolor=blue, edgecolor=blue,
                             label="Earliest (solid)"),
                       Patch(facecolor="white", edgecolor=blue,
                             label="Latest (hollow)"),
                       Patch(facecolor=teal, edgecolor=teal,
                             label="Critical activity (float 0)")],
              loc="lower center", bbox_to_anchor=(0.5, 1.01),
              ncol=3, frameon=False, fontsize=9.5)
    fig.text(0.5, 0.035,
             "Paired tracks show separate schedules. Brackets mark start-time shifts; finish = 10.",
             ha="center", fontsize=10, color=ink)
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.15, top=0.81)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output.name}: starts {list(early.values())}, "
          f"latest {list(late[t] for t in tasks)}, floats {floats}")


if __name__ == "__main__":
    main()
