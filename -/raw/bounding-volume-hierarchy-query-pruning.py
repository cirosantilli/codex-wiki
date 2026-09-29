"""Exact box query, hierarchy pruning and a false broad-phase candidate.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5:
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3.14 ../bounding-volume-hierarchy-query-pruning.py
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
QUERY = (np.array([1.6, 1.6]), np.array([1.8, 1.8]))
BLUE, GREEN, GRAY = "#2467a4", "#147d69", "#7c848b"


def bounds_and_traversal():
    bounds = {n: (p.min(axis=0), p.max(axis=0)) for n, p in TRIANGLES.items()}
    for n in ("L", "R", "root"):
        children = [bounds[c] for c in CHILDREN[n]]
        bounds[n] = (np.min([b[0] for b in children], axis=0),
                     np.max([b[1] for b in children], axis=0))
    visited, accepted, candidates = [], [], []

    def visit(n):
        visited.append(n)
        lo, hi = bounds[n]
        if not np.all(np.maximum(lo, QUERY[0]) <= np.minimum(hi, QUERY[1])):
            return
        accepted.append(n)
        if n in CHILDREN:
            for c in CHILDREN[n]:
                visit(c)
        else:
            candidates.append(n)

    visit("root")
    assert visited == ["root", "L", "A", "B", "R"]
    assert accepted == ["root", "L", "A", "B"]
    assert candidates == ["A", "B"]
    assert QUERY[0].sum() > TRIANGLES["A"].sum(axis=1).max()
    hit_point = np.array([7 / 4, 13 / 8])
    assert np.all(QUERY[0] <= hit_point) and np.all(hit_point <= QUERY[1])
    assert hit_point[1] <= hit_point[0] and hit_point[1] >= 1.5 and hit_point[0] <= 3.5
    return bounds, visited, candidates


def rectangle(ax, box, **kwargs):
    lo, hi = box
    ax.add_patch(Rectangle(lo, *(hi - lo), **kwargs))


def draw_scene(ax, bounds):
    for name in ("root", "L", "R"):
        rectangle(ax, bounds[name], fill=False, ec=GRAY, lw=1.5)
    for name, p in TRIANGLES.items():
        color = BLUE if name == "A" else GREEN if name == "B" else GRAY
        rectangle(ax, bounds[name], fill=False, ec=color, lw=1.2, linestyle="--")
        ax.add_patch(Polygon(p, fc=color, ec=color, alpha=.22, lw=1.5))
        ax.text(*p.mean(axis=0), name, ha="center", va="center", weight="bold", color=color)
    rectangle(ax, QUERY, fc="#ffcf66", ec="#995c00", lw=2, zorder=6)
    ax.annotate("Q", xy=(1.7, 1.7), xytext=(4.4, 2.5), weight="bold",
                arrowprops={"arrowstyle": "->", "color": "#995c00"})
    ax.text(7, 5.18, "R: reject", ha="center", color=GRAY)
    ax.set(xlim=(-.4, 8.4), ylim=(-.4, 5.6), xlabel="x", ylabel="y")
    ax.set_aspect("equal")
    ax.set_xticks([0, 2, 4, 6, 8])
    ax.grid(alpha=.15)
    ax.set_title("Query misses all of R", fontsize=12)


def draw_zoom(ax):
    p = TRIANGLES["B"]
    ax.add_patch(Polygon(p, fc=GREEN, ec=GREEN, alpha=.23, lw=2))
    ax.axvline(2, color=BLUE, linestyle="--", lw=1.7)
    ax.axhline(2, color=BLUE, linestyle="--", lw=1.7)
    rectangle(ax, QUERY, fill=False, ec="#995c00", lw=2.5, zorder=5)
    ax.text(1.7, 1.71, "Q", ha="center", va="center", color="#995c00", weight="bold")
    ax.scatter([7 / 4], [13 / 8], color=GREEN, s=35, zorder=7)
    ax.annotate("Point in Q and B", xy=(7 / 4, 13 / 8), xytext=(1.91, 1.46),
                ha="center", fontsize=9, color=GREEN,
                arrowprops={"arrowstyle": "->", "color": GREEN})
    ax.text(1.91, 1.91, "A's box", fontsize=9, color=BLUE, ha="center")
    ax.text(1.7, 2.16, "A lies in x + y ≤ 2\n(all outside this close-up)",
            fontsize=9, ha="center", color=BLUE)
    ax.set(xlim=(1.38, 2.1), ylim=(1.38, 2.3), xlabel="x", ylabel="y")
    ax.set_aspect("equal")
    ax.set_xticks([1.5, 1.6, 1.8, 2])
    ax.set_yticks([1.5, 1.6, 1.8, 2])
    ax.grid(alpha=.15)
    ax.set_title("Close-up: only B is a true hit", fontsize=12)


def draw_tree(ax):
    locations = {"root": (.5, .86), "L": (.25, .53), "R": (.75, .53),
                 "A": (.1, .19), "B": (.4, .19), "C": (.65, .19), "D": (.9, .19)}
    labels = {"root": "1  root\npass", "L": "2  L\npass", "R": "5  R\nreject",
              "A": "3  A\ncandidate\nshape misses", "B": "4  B\ncandidate\nshape hits",
              "C": "C\nskipped", "D": "D\nskipped"}
    for parent, children in CHILDREN.items():
        x, y = locations[parent]
        for child in children:
            cx, cy = locations[child]
            ax.annotate("", xy=(cx, cy + .1), xytext=(x, y - .09),
                        arrowprops={"arrowstyle": "->", "color": GRAY,
                                    "linestyle": "--" if parent == "R" else "-"})
    for name, (x, y) in locations.items():
        color = BLUE if name == "A" else GREEN if name == "B" else GRAY
        bg = "#f0f1f2" if name in ("R", "C", "D") else "white"
        ax.text(x, y, labels[name], ha="center", va="center", fontsize=9.5,
                bbox={"boxstyle": "round,pad=.4", "facecolor": bg,
                      "edgecolor": color, "linewidth": 1.5})
    ax.set(xlim=(-.03, 1.04), ylim=(-.06, 1.06))
    ax.axis("off")
    ax.set_title("Left-first traversal; numbers give test order", fontsize=12)
    ax.text(.5, -.04, "5 box tests → 2 shape tests → 1 hit", ha="center", fontsize=10.5)


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})
    bounds, visited, candidates = bounds_and_traversal()
    fig, axes = plt.subplots(1, 3, figsize=(13, 5.5),
                             gridspec_kw={"width_ratios": [1.05, .75, 1.2]})
    draw_scene(axes[0], bounds)
    draw_zoom(axes[1])
    draw_tree(axes[2])
    fig.suptitle("Closed query Q = [1.6, 1.8] × [1.6, 1.8]: box overlap leaves candidates", fontsize=14)
    fig.tight_layout(rect=(0, .03, 1, .94), w_pad=2)
    output = Path(Path(__file__).stem + ".png")
    fig.savefig(output, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": str(output), "visited": visited, "candidates": candidates,
                      "skipped": ["C", "D"], "box_tests": 5, "shape_tests": 2,
                      "hits": ["B"], "hit_point": [7 / 4, 13 / 8]}))


if __name__ == "__main__":
    main()
