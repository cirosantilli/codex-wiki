"""Draw bottom-up integer constant folding and the corresponding traversal.

Run from _media; tested with Python 3.14.4 and matplotlib 3.10.7.
Only literal integer Add/Sub/Mult nodes are folded; names and calls survive.
"""

import ast
from pathlib import Path

import matplotlib.pyplot as plt


class FoldIntegers(ast.NodeTransformer):
    def __init__(self):
        self.steps = []

    def visit_BinOp(self, node):
        self.generic_visit(node)
        if not (isinstance(node.left, ast.Constant)
                and isinstance(node.right, ast.Constant)
                and type(node.left.value) is int
                and type(node.right.value) is int):
            return node
        a, b = node.left.value, node.right.value
        if isinstance(node.op, ast.Add):
            value = a + b
        elif isinstance(node.op, ast.Sub):
            value = a - b
        elif isinstance(node.op, ast.Mult):
            value = a * b
        else:
            return node
        self.steps.append((type(node.op).__name__, a, b, value))
        return ast.copy_location(ast.Constant(value=value), node)


def expression_tree(ax, node, x, y, gap):
    if isinstance(node, ast.BinOp):
        for child, dx in ((node.left, -gap), (node.right, gap)):
            ax.plot([x, x + dx], [y, y - 1.1], color="#526b82", lw=1.7, zorder=1)
            expression_tree(ax, child, x + dx, y - 1.1, gap * 0.48)
        text, color = type(node.op).__name__, "#e6f1fb"
    else:
        assert isinstance(node, ast.Constant)
        text, color = str(node.value), "#fff1d7"
    ax.text(x, y, text, ha="center", va="center", fontsize=13,
            bbox={"boxstyle": "round,pad=0.5", "fc": color, "ec": "#48627b"}, zorder=2)


def main():
    original = ast.parse("2+3*4", mode="eval", optimize=0)
    folder = FoldIntegers()
    folded = ast.fix_missing_locations(folder.visit(ast.parse("2+3*4", mode="eval", optimize=0)))
    assert folder.steps == [("Mult", 3, 4, 12), ("Add", 2, 12, 14)]
    assert eval(compile(original, "<before>", "eval")) == eval(compile(folded, "<after>", "eval")) == 14
    fig, ax = plt.subplots(figsize=(10.5, 4.7), facecolor="white")
    expression_tree(ax, original.body, 1.7, 3.8, 0.7)
    expression_tree(ax, ast.parse("2+12", mode="eval").body, 5.1, 3.8, 0.7)
    expression_tree(ax, folded.body, 8.6, 3.8, 0.7)
    for start, end, text in ((2.85, 3.95, "3 × 4 → 12"), (6.25, 7.75, "2 + 12 → 14")):
        ax.annotate("", xy=(end, 3.1), xytext=(start, 3.1),
                    arrowprops={"arrowstyle": "->", "color": "#326e52", "lw": 2})
        ax.text((start + end) / 2, 2.65, text, ha="center", fontsize=11, color="#23583f")
    for x, title in ((1.7, "Original expression"), (5.1, "After first replacement"), (8.6, "After second replacement")):
        ax.text(x, 4.65, title, ha="center", fontsize=12)
    ax.text(5.0, 0.65, "Postorder of the original expression:  2 → 3 → 4 → Mult → Add",
            ha="center", fontsize=13)
    ax.text(5.0, 0.05, "Visit children first. Replace only constant subtrees; keep Assign and Name(x, Store).",
            ha="center", fontsize=11, color="#34465a")
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.35, 5.0)
    ax.axis("off")
    fig.suptitle("Constant folding follows the tree from leaves to root", fontsize=17)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.04, top=0.87)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
