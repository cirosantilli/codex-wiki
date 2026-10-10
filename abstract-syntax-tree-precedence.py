"""Draw two assignment trees parsed by Python's standard-library ast module.

Run from _media; tested with Python 3.14.4 and matplotlib 3.10.7.
Operator and context marker nodes are displayed inside their owning node.
"""

import ast
from pathlib import Path

import matplotlib.pyplot as plt


def children(node):
    if isinstance(node, ast.Assign):
        return [("target", node.targets[0]), ("value", node.value)]
    if isinstance(node, ast.BinOp):
        return [("left", node.left), ("right", node.right)]
    return []


def label(node):
    if isinstance(node, ast.Assign):
        return "Assign"
    if isinstance(node, ast.BinOp):
        return f"BinOp\n{type(node.op).__name__}"
    if isinstance(node, ast.Name):
        return f"Name: {node.id}\n{type(node.ctx).__name__}"
    if isinstance(node, ast.Constant):
        return f"Constant\n{node.value}"
    raise TypeError(node)


def draw_tree(ax, node):
    positions = {}
    edges = []
    cursor = 0

    def place(item, depth):
        nonlocal cursor
        branches = children(item)
        if not branches:
            x = cursor
            cursor += 1
        else:
            xs = [place(child, depth + 1) for _, child in branches]
            x = sum(xs) / len(xs)
            edges.extend((item, child, field) for field, child in branches)
        positions[item] = (x, -depth)
        return x

    place(node, 0)
    for parent, child, field in edges:
        x, y = positions[parent]
        u, v = positions[child]
        ax.plot([x, u], [y, v], color="#566779", linewidth=1.7, zorder=1)
        ax.text((x + u) / 2, (y + v) / 2, field, fontsize=9,
                ha="center", va="center", color="#34465a", backgroundcolor="white")
    for item, (x, y) in positions.items():
        color = "#e6f1fb" if children(item) else "#fff1d7"
        ax.text(x, y, label(item), ha="center", va="center", fontsize=11,
                bbox={"boxstyle": "round,pad=0.45", "fc": color,
                      "ec": "#48627b", "lw": 1.2}, zorder=2)
    ax.set_xlim(-0.75, cursor - 0.25)
    ax.set_ylim(-3.7, 0.8)
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.0), facecolor="white")
    for ax, source, expected in zip(axes, ("x=2+3*4", "x=(2+3)*4"), (14, 20)):
        tree = ast.parse(source, optimize=0)
        scope = {}
        exec(compile(tree, "<precedence example>", "exec"), scope)
        assert scope["x"] == expected
        draw_tree(ax, tree.body[0])
        ax.set_title(source, fontsize=15, fontfamily="monospace", pad=12)
        ax.text(0.5, -0.04, f"After execution: x = {expected}",
                transform=ax.transAxes, ha="center", fontsize=13)
    fig.suptitle("Parentheses change the operator nesting", fontsize=17)
    fig.text(0.5, 0.035,
             "Module wrapper omitted; operator and context markers shown inside nodes.",
             ha="center", fontsize=10, color="#34465a")
    fig.subplots_adjust(top=0.82, bottom=0.16, left=0.035, right=0.965, wspace=0.15)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
