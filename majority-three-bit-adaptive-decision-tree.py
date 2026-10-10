"""Draw an exact Boolean query tree. Python 3.14, matplotlib 3.10.7.

Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9, 5.9), facecolor="white")
    ax.set(xlim=(-0.3, 8.3), ylim=(-0.62, 3.6))
    ax.axis("off")
    fig.suptitle("Three-bit majority: read only what is needed", fontsize=17, y=0.97)
    ax.text(4, 3.48, "Internal nodes query one bit; edges carry its observed value.",
            ha="center", fontsize=12, color="#334155")

    nodes = {
        "root": (4, 3.05, r"Query $x_1$", False),
        "left": (1.9, 2.05, r"Query $x_2$", False),
        "right": (6.1, 2.05, r"Query $x_2$", False),
        "00": (0.65, 1.05, "Output 0\nq = 2\n000, 001", True),
        "01": (3.1, 1.05, r"Query $x_3$", False),
        "10": (4.9, 1.05, r"Query $x_3$", False),
        "11": (7.35, 1.05, "Output 1\nq = 2\n110, 111", True),
        "010": (2.25, -0.05, "Output 0\nq = 3\n010", True),
        "011": (3.65, -0.05, "Output 1\nq = 3\n011", True),
        "100": (4.95, -0.05, "Output 0\nq = 3\n100", True),
        "101": (6.35, -0.05, "Output 1\nq = 3\n101", True),
    }
    edges = [
        ("root", "left", 0), ("root", "right", 1),
        ("left", "00", 0), ("left", "01", 1),
        ("right", "10", 0), ("right", "11", 1),
        ("01", "010", 0), ("01", "011", 1),
        ("10", "100", 0), ("10", "101", 1),
    ]
    for parent, child, bit in edges:
        x0, y0, *_ = nodes[parent]
        x1, y1, *_ = nodes[child]
        ax.plot([x0, x1], [y0, y1], color="#64748b", lw=1.7, zorder=1)
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, str(bit), ha="center", va="center",
                fontsize=12, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2},
                zorder=2)
    for x, y, label, leaf in nodes.values():
        ax.text(x, y, label, ha="center", va="center", fontsize=11.5,
                bbox={"boxstyle": "round,pad=0.4", "facecolor": "#dcfce7" if leaf else "#dbeafe",
                      "edgecolor": "#15803d" if leaf else "#1d4ed8", "linewidth": 1.3},
                zorder=3)
    fig.text(0.5, 0.035, "00* and 11*: the third bit cannot change the answer.   * = unread bit",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.09, top=0.90)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
