"""Draw the original six-activity DAG; write the matching PNG basename to cwd.

Run from _media. Tested with Python 3.14.4 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    durations = {"Start": 0, "A": 3, "B": 2, "C": 4,
                 "D": 2, "E": 3, "F": 1, "Finish": 0}
    predecessors = {"Start": [], "A": ["Start"], "B": ["A"],
                    "C": ["A"], "D": ["B", "C"], "E": ["Start"],
                    "F": ["D", "E"], "Finish": ["F"]}
    order = ["Start", "A", "B", "C", "D", "E", "F", "Finish"]
    early = {}
    for task in order:
        early[task] = max((early[p] + durations[p]
                           for p in predecessors[task]), default=0)
    successors = {task: [] for task in order}
    for task, parents in predecessors.items():
        for parent in parents:
            successors[parent].append(task)
    late = {"Finish": early["Finish"]}
    for task in reversed(order[:-1]):
        late[task] = min(late[s] - durations[task] for s in successors[task])
    assert early["Finish"] == 10
    assert [late[t] - early[t] for t in "ABCDEF"] == [0, 2, 0, 0, 6, 0]

    positions = {"Start": (0, 1.7), "A": (1.85, 2.55),
                 "B": (3.8, 3.55), "C": (3.8, 1.55),
                 "D": (5.8, 2.55), "E": (3.8, -0.35),
                 "F": (7.75, 1.7), "Finish": (9.65, 1.7)}
    critical_edges = {("Start", "A"), ("A", "C"), ("C", "D"),
                      ("D", "F"), ("F", "Finish")}
    teal, gray, ink = "#007b78", "#697a8c", "#203548"
    fig, ax = plt.subplots(figsize=(9.4, 5.1), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    boxes = {}
    for task in order:
        x, y = positions[task]
        critical = early[task] == late[task]
        boxes[task] = FancyBboxPatch(
            (x - 0.67, y - 0.49), 1.34, 0.98,
            boxstyle="round,pad=0.04,rounding_size=0.1",
            facecolor="#eaf7f4" if critical else "white",
            edgecolor=teal if critical else gray,
            linewidth=2 if critical else 1.6, zorder=3)
        ax.add_patch(boxes[task])
        ax.text(x, y + 0.22, task, ha="center", va="center",
                fontsize=12, fontweight="bold", color=ink, zorder=4)
        ax.text(x, y - 0.05, f"duration {durations[task]}",
                ha="center", va="center", fontsize=10, color=ink, zorder=4)
        ax.text(x, y - 0.30, f"ES {early[task]}   LS {late[task]}",
                ha="center", va="center", fontsize=9.5, color=ink, zorder=4)
    for child, parents in predecessors.items():
        for parent in parents:
            critical = (parent, child) in critical_edges
            ax.add_patch(FancyArrowPatch(
                positions[parent], positions[child],
                patchA=boxes[parent], patchB=boxes[child],
                arrowstyle="-|>", mutation_scale=16,
                shrinkA=4, shrinkB=4,
                linewidth=2.7 if critical else 1.7,
                color=teal if critical else gray, zorder=2))
    ax.set_title("Critical path A → C → D → F: 3 + 4 + 2 + 1 = 10",
                 fontsize=15, pad=16, color=ink)
    ax.legend(handles=[Line2D([0], [0], color=teal, lw=2.7,
                             label="Critical path"),
                       Line2D([0], [0], color=gray, lw=1.7,
                             label="Other precedence")],
              loc="lower center", bbox_to_anchor=(0.5, -0.04),
              ncol=2, frameon=False, fontsize=10)
    fig.text(0.5, 0.04,
             "ES / LS = earliest / latest start. Every incoming requirement must hold.",
             ha="center", fontsize=10, color=ink)
    ax.set(xlim=(-0.95, 10.6), ylim=(-1.2, 4.3), aspect="equal")
    ax.axis("off")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.87, bottom=0.13)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output.name}: finish 10, critical path A-C-D-F")


if __name__ == "__main__":
    main()
