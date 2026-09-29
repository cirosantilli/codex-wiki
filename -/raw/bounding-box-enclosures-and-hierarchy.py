"""Exact planar enclosures and their binary hierarchy.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5:
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3.14 ../bounding-box-enclosures-and-hierarchy.py
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle


TRIANGLES = {
    "A": np.array([(0, 0), (2, 0), (0, 2)], dtype=float),
    "B": np.array([(1.5, 1.5), (3.5, 1.5), (3.5, 3.5)]),
    "C": np.array([(6, 0), (8, 0), (6, 2)], dtype=float),
    "D": np.array([(6, 3), (8, 3), (8, 5)], dtype=float),
}
CHILDREN = {"root": ("L", "R"), "L": ("A", "B"), "R": ("C", "D")}
COLORS = {"A": "#2467a4", "B": "#147d69", "C": "#b45f28", "D": "#85509a"}


def boxes():
    result = {name: (p.min(axis=0), p.max(axis=0)) for name, p in TRIANGLES.items()}
    for name in ("L", "R", "root"):
        left, right = (result[c] for c in CHILDREN[name])
        result[name] = (np.minimum(left[0], right[0]), np.maximum(left[1], right[1]))
    return result


def verify(bounds):
    for name, p in TRIANGLES.items():
        lo, hi = bounds[name]
        assert np.all(lo <= p) and np.all(p <= hi)
    for parent, children in CHILDREN.items():
        lo, hi = bounds[parent]
        for child in children:
            clo, chi = bounds[child]
            assert np.all(lo <= clo) and np.all(chi <= hi)
    lo = np.maximum(bounds["A"][0], bounds["B"][0])
    hi = np.minimum(bounds["A"][1], bounds["B"][1])
    assert np.array_equal(lo, (1.5, 1.5)) and np.array_equal(hi, (2, 2))
    assert max(TRIANGLES["A"].sum(axis=1)) == 2
    assert min(TRIANGLES["B"].sum(axis=1)) == 3
    assert len(bounds) == 7 and len(TRIANGLES) == 4


def draw_scene(ax, bounds):
    for name in ("root", "L", "R"):
        lo, hi = bounds[name]
        ax.add_patch(Rectangle(lo, *(hi - lo), fill=False,
                               ec="#232c35" if name == "root" else "#737b83",
                               lw=2 if name == "root" else 1.7))
    ax.add_patch(Rectangle((1.5, 1.5), .5, .5, fc="#ffcf66", ec="none", zorder=2))
    for name, p in TRIANGLES.items():
        lo, hi = bounds[name]
        ax.add_patch(Rectangle(lo, *(hi - lo), fill=False, ec=COLORS[name],
                               lw=1.8, linestyle="--", zorder=3))
        ax.add_patch(Polygon(p, fc=COLORS[name], alpha=.18, ec=COLORS[name], lw=2))
        center = p.mean(axis=0)
        ax.text(*center, name, color=COLORS[name], ha="center", va="center",
                weight="bold", fontsize=14)
    ax.annotate("Boxes overlap;\ntriangles do not", xy=(1.75, 1.75),
                xytext=(4.3, 4.4), ha="center", fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#6d551f"})
    ax.text(3.75, 5.12, "root", weight="bold", ha="center")
    ax.text(.1, 3.6, "L", weight="bold")
    ax.text(6.1, 5.12, "R", weight="bold")
    ax.set(xlim=(-.4, 8.4), ylim=(-.4, 5.7), xlabel="x", ylabel="y")
    ax.set_aspect("equal")
    ax.set_xticks(range(9))
    ax.set_yticks(range(6))
    ax.grid(alpha=.18)
    ax.set_title("Exact enclosures in the plane", pad=12)


def draw_tree(ax):
    locations = {"root": (.5, .84), "L": (.25, .51), "R": (.75, .51),
                 "A": (.1, .16), "B": (.4, .16), "C": (.6, .16), "D": (.9, .16)}
    labels = {"root": "root\n[0, 8] × [0, 5]", "L": "L\n[0, 3.5] × [0, 3.5]",
              "R": "R\n[6, 8] × [0, 5]", "A": "A\n[0, 2] × [0, 2]",
              "B": "B\n[1.5, 3.5] × [1.5, 3.5]", "C": "C\n[6, 8] × [0, 2]",
              "D": "D\n[6, 8] × [3, 5]"}
    for parent, children in CHILDREN.items():
        x, y = locations[parent]
        for child in children:
            cx, cy = locations[child]
            ax.annotate("", xy=(cx, cy + .09), xytext=(x, y - .09),
                        arrowprops={"arrowstyle": "->", "color": "#6b737b"})
    for name, (x, y) in locations.items():
        # Leaf endpoint labels on separate lines fit without overlap.
        label = labels[name]
        if name in TRIANGLES:
            label = label.replace(" × ", " ×\n")
        ax.text(x, y, label, ha="center", va="center", fontsize=9.5,
                bbox={"boxstyle": "round,pad=.45", "facecolor": "white",
                      "edgecolor": COLORS.get(name, "#4c555d"), "linewidth": 1.7})
    ax.set(xlim=(-.07, 1.07), ylim=(-.06, 1))
    ax.axis("off")
    ax.set_title("Each parent contains both child boxes", pad=12)
    ax.text(.5, -.04, "4 leaf objects + 3 internal nodes = 7 nodes",
            ha="center", fontsize=10.5)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    bounds = boxes()
    verify(bounds)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.7), gridspec_kw={"width_ratios": [1.05, 1]})
    draw_scene(axes[0], bounds)
    draw_tree(axes[1])
    fig.suptitle("Bounding boxes enclose objects; hierarchy boxes enclose descendants", fontsize=14)
    fig.tight_layout(rect=(0, .03, 1, .94))
    output = Path(Path(__file__).stem + ".png")
    fig.savefig(output, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": str(output), "nodes": 7, "leaves": 4,
                      "boxes": {n: [lo.tolist(), hi.tolist()] for n, (lo, hi) in bounds.items()},
                      "A_B_box_overlap": [[1.5, 1.5], [2, 2]], "A_B_shapes_disjoint": True}))


if __name__ == "__main__":
    main()
