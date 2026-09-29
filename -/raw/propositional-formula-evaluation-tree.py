"""Draw syntax and values for (p implies q) and p at p true, q false.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write an opaque white-background PNG to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    p, q = True, False
    conditional = (not p) or q
    result = conditional and p
    fig, ax = plt.subplots(figsize=(7.8, 4.9), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    positions = {"root": (0.55, 0.82), "imp": (0.28, 0.49),
                 "right-p": (0.80, 0.49), "left-p": (0.12, 0.17),
                 "q": (0.43, 0.17)}
    nodes = {"root": (r"$\wedge$", result), "imp": (r"$\to$", conditional),
             "right-p": (r"$p$", p), "left-p": (r"$p$", p), "q": (r"$q$", q)}
    for child, parent in [("imp", "root"), ("right-p", "root"),
                          ("left-p", "imp"), ("q", "imp")]:
        start, end = positions[child], positions[parent]
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "-|>", "lw": 1.8,
                                "color": "#707b8a", "shrinkA": 29, "shrinkB": 30})
    for name, (label, value) in nodes.items():
        x, y = positions[name]
        ax.text(x, y, label + "\n" + ("True" if value else "False"),
                ha="center", va="center", fontsize=16,
                color="#14624b" if value else "#933a25",
                bbox={"boxstyle": "round,pad=0.45",
                      "facecolor": "#d8eee5" if value else "#f9e1d8",
                      "edgecolor": "#14624b" if value else "#933a25", "linewidth": 1.5})
    ax.text(0.08, 0.86, "3. Combine\nFalse and True", fontsize=11, color="#444444")
    ax.text(0.02, 0.52, "2. Evaluate\nconditional", fontsize=11, color="#444444",
            ha="right")
    ax.text(0.71, 0.17, "1. Assign atoms\nBoth p leaves are True", fontsize=11,
            color="#444444", ha="center")
    ax.set(xlim=(-0.20, 1.02), ylim=(-0.03, 1.02))
    ax.axis("off")
    fig.suptitle(r"$(p\to q)\wedge p$: syntax with values flowing upward",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.035, "Assignment: p = True, q = False     Result: False",
             ha="center", fontsize=12)
    fig.tight_layout(rect=(0.01, 0.07, 0.99, 0.93))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
