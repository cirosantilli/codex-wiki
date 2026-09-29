"""Original tree sketch; tested on Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write the basename PNG to the caller's current directory. Honor MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib.pyplot as plt

CHILDREN = {1: (2, 3), 3: (6, 7), 6: (12, 13), 12: (24, 25), 7: (14, 15)}
SPLITS = {1: "Petal length < 2.45?", 3: "Petal width < 1.75?", 6: "Petal length < 4.95?", 12: "Sepal length < 5.15?", 7: "Petal length < 4.95?"}
COUNTS = {2: (50, 0, 0), 24: (0, 4, 1), 25: (0, 43, 0), 13: (0, 2, 4), 14: (0, 1, 5), 15: (0, 0, 40)}
CLASS_NAMES = ("setosa", "versicolor", "virginica")
COLORS = ("#cde6f7", "#d5efcf", "#ffe0bb")

def main():
    positions = {}
    cursor = 0
    def place(node, depth):
        nonlocal cursor
        if node not in CHILDREN:
            x = cursor
            cursor += 1
        else:
            left, right = CHILDREN[node]
            x = (place(left, depth + 1) + place(right, depth + 1)) / 2
        positions[node] = (x, 4 - depth)
        return x
    place(1, 0)
    def count(node):
        return sum(COUNTS[node]) if node in COUNTS else sum(count(child) for child in CHILDREN[node])
    fig, ax = plt.subplots(figsize=(14.8, 7.8), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.09, top=0.88)
    for node, kids in CHILDREN.items():
        for side, child in enumerate(kids):
            x, y = positions[node]
            u, v = positions[child]
            ax.annotate("", xy=(u, v + 0.23), xytext=(x, y - 0.23), arrowprops={"arrowstyle": "->", "color": "#666666", "lw": 1.5})
            ax.text(0.6*x + 0.4*u, 0.6*y + 0.4*v, "yes (<)" if side == 0 else "no (≥)", fontsize=10, ha="center", backgroundcolor="white")
    for node, (x, y) in positions.items():
        if node in COUNTS:
            counts = COUNTS[node]
            idx = max(range(3), key=lambda i: counts[i])
            errors = sum(counts) - max(counts)
            text = f"node {node}: {CLASS_NAMES[idx]}\nn = {sum(counts)}, errors = {errors}"
            color = COLORS[idx]
        else:
            text = f"node {node}, n = {count(node)}\n{SPLITS[node]}"
            color = "#f3f3f3"
        ax.text(x, y, text, ha="center", va="center", fontsize=11, bbox={"boxstyle": "round,pad=0.55", "fc": color, "ec": "#555555"})
    ax.set(xlim=(-0.55, 5.65), ylim=(-0.5, 4.5))
    ax.axis("off")
    fig.suptitle("The fitted six-leaf classification rule", fontsize=18, y=0.96)
    fig.text(0.5, 0.025, "Left branches use <; right branches include equality. Training errors: 1 + 2 + 1 = 4 out of 150.", ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "paper-46-classification-tree.png", facecolor="white", transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
