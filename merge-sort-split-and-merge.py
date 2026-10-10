"""Draw a computed stable merge-sort tree; save an opaque PNG to cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


VALUES = (7, 2, 5, 2, 9, 1, 4, 3)


def merge(left, right):
    """Compare numeric keys only, retaining original indices as identities."""
    result, trace = [], []
    i = j = 0
    while i < len(left) and j < len(right):
        trace.append((left[i], right[j]))
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:], trace


def sort_tree(items, start=0, depth=0):
    """Return the sorted items and every node of a floor-midpoint recursion."""
    node = {"start": start, "size": len(items), "depth": depth,
            "input": items, "comparisons": 0}
    if len(items) < 2:
        node["output"] = items
        return items, [node]
    mid = len(items) // 2
    left, left_nodes = sort_tree(items[:mid], start, depth + 1)
    right, right_nodes = sort_tree(items[mid:], start + mid, depth + 1)
    output, trace = merge(left, right)
    node.update(output=output, comparisons=len(trace), trace=trace)
    return output, [node] + left_nodes + right_nodes


def label(items):
    tags = {1: "2a", 3: "2b"}
    return "  ".join(tags[index] if value == 2 else str(value)
                     for value, index in items)


def center(node):
    return 2.65 + 1.05 * (node["start"] + (node["size"] - 1) / 2)


def box(ax, node, y, output=False):
    width = 0.47 * node["size"] + 0.23
    x = center(node)
    color = "#e3eef8" if not output else "#e0f1e5"
    ax.add_patch(FancyBboxPatch((x - width / 2, y - 0.23), width, 0.46,
                              boxstyle="round,pad=0.04", facecolor=color,
                              edgecolor="#577187", linewidth=1.0, zorder=3))
    ax.text(x, y, label(node["output"] if output else node["input"]),
            ha="center", va="center", fontsize=13, color="#172c3c", zorder=4)


def main():
    items = [(value, index) for index, value in enumerate(VALUES)]
    output, nodes = sort_tree(items)
    counts = [sum(n["comparisons"] for n in nodes if n["depth"] == depth)
              for depth in (2, 1, 0)]
    assert [v for v, _ in output] == [1, 2, 2, 3, 4, 5, 7, 9]
    assert [i for v, i in output if v == 2] == [1, 3]
    assert counts == [4, 6, 7]
    assert sum(counts) == 17
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(12, 8.2), facecolor="white")
    labels = ("Input", "Split halves", "Split pairs", "Base cases",
              "Merge pairs", "Merge halves", "Merge all")
    ys = [7.5 - 1.05 * i for i in range(7)]
    for y, text in zip(ys, labels):
        ax.text(0.05, y, text, va="center", fontsize=12, color="#172c3c")
    for node in nodes:
        depth = node["depth"]
        box(ax, node, ys[depth])
        if depth < 3:
            box(ax, node, ys[6 - depth], output=True)
        if node["size"] > 1:
            children = [child for child in nodes
                        if child["depth"] == depth + 1
                        and node["start"] <= child["start"]
                        < node["start"] + node["size"]]
            for child in children:
                ax.annotate("", xy=(center(child), ys[depth + 1] + 0.28),
                            xytext=(center(node), ys[depth] - 0.28),
                            arrowprops={"arrowstyle": "->", "color": "#7291ab"})
                ax.annotate("", xy=(center(node), ys[6 - depth] + 0.28),
                            xytext=(center(child), ys[5 - depth] - 0.28),
                            arrowprops={"arrowstyle": "->", "color": "#5a9270"})
    ax.text(10.35, ys[3] + 0.45, "Head comparisons", fontsize=11)
    for y, count in zip(ys[4:], counts):
        ax.text(10.65, y, str(count), fontsize=15, va="center")
    ax.text(10.35, 0.43, "Total: 17", weight="bold", fontsize=12)
    ax.text(0.05, 0.43, "2a: original index 1     2b: original index 3     Equal keys: take left first",
            fontsize=11, color="#172c3c")
    ax.set(xlim=(-0.05, 12.15), ylim=(0.05, 8.05))
    ax.axis("off")
    fig.suptitle("Merge sort: split down, merge back in order", fontsize=18, y=0.98)
    fig.subplots_adjust(left=0.025, right=0.99, top=0.93, bottom=0.025)
    fig.savefig(Path.cwd() / "merge-sort-split-and-merge.png", dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Output: {label(output)}; comparisons by merge level: {counts}; total: 17")


if __name__ == "__main__":
    main()
