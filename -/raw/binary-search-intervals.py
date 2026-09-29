"""Compute two binary-search traces and save a white PNG in the working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Invoke from _media to put binary-search-intervals.png there.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle


VALUES = (2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 104, 130, 160, 205, 260)


def search_trace(values, target):
    """Return (matching index or -1, trace, final inclusive endpoints)."""
    left, right = 0, len(values) - 1
    rows = []
    while left <= right:
        middle = left + (right - left) // 2
        value = values[middle]
        rows.append((left, right, middle, value))
        if value == target:
            return middle, rows, (left, right)
        if value < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, rows, (left, right)


def draw_trace(ax, target):
    result, rows, endpoints = search_trace(VALUES, target)
    for index in range(len(VALUES)):
        ax.text(index, 4.62, str(index), ha="center", color="#52606d", fontsize=9)
    ax.text(-1.1, 4.62, "Index", ha="right", fontsize=10)
    for step, (left, right, middle, value) in enumerate(rows, 1):
        y = 4.15 - (step - 1) * 0.9
        ax.text(-1.1, y, f"Step {step}", ha="right", va="center", fontsize=11)
        for index, entry in enumerate(VALUES):
            color = "#e8edf1"
            if left <= index <= right:
                color = "#c9dff4"
            if index == middle:
                color = "#f6bf75" if result != middle or step != len(rows) else "#8ed1a5"
            ax.add_patch(Rectangle((index - 0.45, y - 0.29), 0.9, 0.58,
                                   facecolor=color, edgecolor="white"))
            ax.text(index, y, str(entry), ha="center", va="center", fontsize=10,
                    color="#152b3c" if left <= index <= right else "#737e88")
        if value == target:
            decision = f"{target} = {value}: return index {middle}"
        elif value > target:
            decision = f"{target} < {value}: R = {middle - 1}"
        else:
            decision = f"{target} > {value}: L = {middle + 1}"
        ax.text(15.25, y, decision, va="center", fontsize=11)
    if result == -1:
        left, right = endpoints
        outcome = f"Empty range: L = {left} > R = {right}. Target absent."
    else:
        outcome = f"Found after {len(rows)} comparisons; candidate sizes: " + " → ".join(
            str(right - left + 1) for left, right, _, _ in rows)
    ax.text(-2.5, 0.35, outcome, fontsize=11, color="#152b3c")
    ax.set(xlim=(-2.6, 22.5), ylim=(0.05, 5.35))
    ax.set_title(f"Target {target}", loc="left", fontsize=13, weight="bold")
    ax.axis("off")


def main():
    found, successful, _ = search_trace(VALUES, 23)
    absent, failed, endpoints = search_trace(VALUES, 24)
    assert found == 5 and [row[2] for row in successful] == [7, 3, 5]
    assert absent == -1 and [row[2] for row in failed] == [7, 3, 5, 6]
    assert endpoints == (6, 5)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(2, 1, figsize=(11.5, 6.6), facecolor="white")
    for ax, target in zip(axes, (23, 24)):
        draw_trace(ax, target)
    fig.suptitle("Binary search: ordered data makes each exclusion safe", fontsize=16)
    fig.legend(handles=[Patch(facecolor="#c9dff4", label="Candidate"),
                        Patch(facecolor="#f6bf75", label="Middle entry"),
                        Patch(facecolor="#8ed1a5", label="Match"),
                        Patch(facecolor="#e8edf1", label="Already excluded")],
               loc="lower center", ncol=4, frameon=False)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.89, bottom=0.085, hspace=0.26)
    fig.savefig(Path.cwd() / "binary-search-intervals.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
