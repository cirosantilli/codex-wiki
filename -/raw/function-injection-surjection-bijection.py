"""Render finite functions that separate injectivity and surjectivity to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def properties(mapping, source_count, target_count):
    assert len(mapping) == source_count
    assert all(0 <= target < target_count for target in mapping)
    return len(set(mapping)) == source_count, len(set(mapping)) == target_count


def main():
    cases = [
        (3, 4, [0, 1, 2], "Injective, not surjective", "Distinct inputs stay distinct;\ntarget 4 is unused."),
        (4, 3, [0, 1, 1, 2], "Surjective, not injective", "Every target is reached;\nB and C share target 2."),
        (3, 3, [0, 1, 2], "Bijective", "Each target has one predecessor;\nall arrows reverse uniquely."),
    ]
    assert [properties(m, n, k) for n, k, m, _, _ in cases] == [(True, False), (False, True), (True, True)]
    inverse = {target: source for source, target in enumerate(cases[-1][2])}
    assert all(inverse[target] == source for source, target in enumerate(cases[-1][2]))
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.6), dpi=120, facecolor="white")
    colors = ["#236c9f", "#bc7624", "#2c8467"]
    for ax, (source_count, target_count, mapping, title, explanation), color in zip(axes, cases, colors):
        ax.add_patch(Ellipse((.21, .5), .33, .87, facecolor="#edf3f7", edgecolor="#9eb2c1", lw=1.2))
        ax.add_patch(Ellipse((.79, .5), .33, .87, facecolor="#f3f5f1", edgecolor="#adb8a7", lw=1.2))
        source_y = np.linspace(.79, .21, source_count)
        target_y = np.linspace(.79, .21, target_count)
        for i, ordinate in enumerate(source_y):
            ax.scatter([.21], [ordinate], s=70, color=color, zorder=4)
            ax.text(.12, ordinate, chr(ord("A")+i), ha="center", va="center", fontsize=13)
        for i, ordinate in enumerate(target_y):
            used = i in mapping
            ax.scatter([.79], [ordinate], s=75, facecolors=color if used else "white",
                       edgecolors=color if used else "#b43a47", linewidths=1.5, zorder=4)
            ax.text(.89, ordinate, str(i+1), ha="center", va="center", fontsize=13)
        for source, target in enumerate(mapping):
            offset = .015 if source == 1 and source_count == 4 else (-.015 if source == 2 and source_count == 4 else 0)
            ax.annotate("", xy=(.755, target_y[target]+offset), xytext=(.25, source_y[source]),
                        arrowprops={"arrowstyle": "->", "color": color, "lw": 1.9})
        ax.text(.21, 1.005, "Domain X", ha="center", fontsize=12)
        ax.text(.79, 1.005, "Codomain Y", ha="center", fontsize=12)
        ax.set(xlim=(0, 1), ylim=(-.11, 1.14), title=title)
        ax.text(.5, -.08, explanation, ha="center", va="center", fontsize=11, color="#334550")
        ax.set_axis_off()
    fig.suptitle("A function assigns exactly one output to every input", fontsize=16, y=.985)
    fig.text(.5, .027, "The output pattern determines injectivity, surjectivity and invertibility",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=.025, right=.98, top=.85, bottom=.105, wspace=.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
