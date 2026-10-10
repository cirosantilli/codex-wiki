"""Generate matroid-triangle-and-hereditary-greedy-obstruction.png in CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (graph, family) = plt.subplots(1, 2, figsize=(9.6, 4.4))
    green, red, gray = "#13734b", "#b3443c", "#a2a2a2"
    pos = {"P": (0.08, 0.14), "Q": (0.90, 0.14), "R": (0.49, 0.86)}
    for start, end, accepted in [("P", "Q", True), ("P", "R", True), ("Q", "R", False)]:
        p, q = pos[start], pos[end]
        graph.plot([p[0], q[0]], [p[1], q[1]], color=green if accepted else red,
                   linewidth=3, linestyle="-" if accepted else "--", zorder=1)
    for name, (x, y) in pos.items():
        graph.scatter([x], [y], s=240, color="white", edgecolor="#333333", zorder=3)
        graph.text(x, y, name, ha="center", va="center", zorder=4)
    graph.text(0.49, 0.04, "a: 8 (first)", ha="center", color=green)
    graph.text(0.12, 0.55, "c: 6\n(second)", ha="center", color=green)
    graph.text(0.90, 0.55, "b: 5\n(reject)", ha="center", color=red)
    graph.text(0.49, -0.14, "Every pair is a forest.\nThe triple has a cycle.", ha="center")
    graph.text(0.49, -0.36, "Greedy basis {a,c}: 14\nOther bases: {a,b}: 13; {b,c}: 11",
               ha="center", color=green)
    graph.set_title("Graphic matroid: triangle", pad=12)
    graph.set(xlim=(-0.14, 1.13), ylim=(-0.50, 1.02), aspect="equal")
    graph.axis("off")
    nodes = {"empty": (0.5, 0.22), "x": (0.13, 0.48),
             "y": (0.50, 0.48), "z": (0.88, 0.48), "yz": (0.69, 0.90)}
    for start, end in [("empty", "x"), ("empty", "y"), ("empty", "z"),
                       ("y", "yz"), ("z", "yz")]:
        p, q = nodes[start], nodes[end]
        family.plot([p[0], q[0]], [p[1], q[1]], color=gray, lw=1.6, zorder=1)
    labels = {"empty": r"$\varnothing$" + "\n0", "x": "{x}\n10",
              "y": "{y}\n6", "z": "{z}\n6", "yz": "{y,z}\n12"}
    for name, (x, y) in nodes.items():
        color = red if name == "x" else green if name == "yz" else "#555555"
        family.text(x, y, labels[name], ha="center", va="center", color=color,
                    bbox={"boxstyle": "round,pad=0.28", "facecolor": "white",
                          "edgecolor": color}, zorder=3)
    family.text(0.13, 0.78, "Greedy stuck", ha="center", color=red)
    family.text(0.69, 1.12, "Better selection", ha="center", color=green)
    family.text(0.50, -0.10, "All admissible subsets shown;\nlines indicate one-element additions.",
                ha="center")
    family.text(0.50, -0.36, "Cannot add y or z to {x}.\nMaximal sizes differ: 1 and 2.",
                ha="center", color=red)
    family.set_title("Hereditary family: exchange fails", pad=12)
    family.set(xlim=(-0.10, 1.10), ylim=(-0.50, 1.26))
    family.axis("off")
    fig.subplots_adjust(left=0.02, right=0.97, top=0.87, bottom=0.08, wspace=0.19)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
