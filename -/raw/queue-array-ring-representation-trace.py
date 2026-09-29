"""Draw two original queue representations; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


TRACE = [
    ("start", "—", (), (None, None, None), 0),
    ("enqueue(A)", "ok", ("A",), ("A", None, None), 0),
    ("enqueue(B)", "ok", ("A", "B"), ("A", "B", None), 0),
    ("enqueue(C)", "ok", ("A", "B", "C"), ("A", "B", "C"), 0),
    ("dequeue()", "A", ("B", "C"), (None, "B", "C"), 1),
    ("dequeue()", "B", ("C",), (None, None, "C"), 2),
    ("enqueue(D)", "ok", ("C", "D"), ("D", None, "C"), 2),
    ("enqueue(E)", "ok", ("C", "D", "E"), ("D", "E", "C"), 2),
    ("enqueue(F)", "full", ("C", "D", "E"), ("D", "E", "C"), 2),
    ("peek() / size()", "C / 3", ("C", "D", "E"), ("D", "E", "C"), 2),
]


def cells(ax, x, y, values, front=None):
    for i, value in enumerate(values):
        ax.add_patch(Rectangle((x + i * 0.62, y - 0.18), 0.56, 0.36,
                               facecolor="#edf3fa" if value else "#f8fafc",
                               edgecolor="#245b8c" if i == front else "#98a2b3",
                               linewidth=2.5 if i == front else 1))
        ax.text(x + i * 0.62 + 0.28, y, value or "·", ha="center", va="center", fontsize=12)


def main():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=110, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 8))
    ax.axis("off")
    ax.text(6, 7.65, "Same operations and results; different storage and work",
            ha="center", fontsize=18, weight="bold")
    ax.text(6, 7.15, "Capacity 3 • blue border marks the ring's front • dots mean ignored slots",
            ha="center", fontsize=12, color="#475467")
    for x, label in [(0.35, "Client call"), (2.6, "Result"), (4, "Abstract queue"),
                     (6.75, "Compact array"), (9.3, "Ring array")]:
        ax.text(x, 6.55, label, fontsize=12, weight="bold")
    for i in range(3):
        ax.text(6.75 + i * 0.62 + 0.28, 6.2, str(i), ha="center", fontsize=10, color="#667085")
        ax.text(9.3 + i * 0.62 + 0.28, 6.2, str(i), ha="center", fontsize=10, color="#667085")
    for index, (call, result, queue, ring, head) in enumerate(TRACE):
        y = 5.75 - index * 0.45
        if index == 8:
            ax.add_patch(Rectangle((0.2, y - 0.21), 11.6, 0.42, facecolor="#fff4e5", edgecolor="none"))
        ax.text(0.35, y, call, va="center", fontsize=11)
        ax.text(2.6, y, result, va="center", fontsize=11)
        ax.text(4, y, "(" + ", ".join(queue) + ")", va="center", fontsize=12)
        cells(ax, 6.75, y, list(queue) + [None] * (3 - len(queue)))
        cells(ax, 9.3, y, ring, front=head)
        ax.text(11.3, y, f"h={head}", va="center", fontsize=10)
    ax.text(6, 0.95, "dequeue: move n − 1 remaining labels                 dequeue: advance h modulo C",
            ha="center", fontsize=12)
    ax.text(6, 0.5, "Removal cost: O(n) vs O(1), assuming constant-cost slot access and index arithmetic.",
            ha="center", fontsize=12, color="#475467")
    ax.text(6, 0.15, "Inactive ring slots may retain old values; only the occupied n slots contribute to the abstract queue.",
            ha="center", fontsize=10, color="#475467")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
