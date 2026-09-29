"""Draw the sharp weighted-greedy matching example.

Tested with Python 3.14.4 and Matplotlib 3.10.7; dependencies are in the
repository's pyproject.toml. Write the opaque PNG into the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 3.2), dpi=100, facecolor="white")
    specs = [({1}, "#8051a6", r"Greedy: $1+\varepsilon$"),
             ({0, 2}, "#197356", r"Optimal: $2$")]
    for ax, (chosen, color, heading) in zip(axes, specs):
        ax.set_xlim(-0.9, 4.5)
        ax.set_ylim(-0.5, 0.85)
        ax.axis("off")
        ax.text(-0.8, 0.60, heading, color=color, fontsize=13, weight="bold")
        for edge in range(3):
            selected = edge in chosen
            ax.plot((edge, edge + 1), (0, 0),
                    color=color if selected else "#999999",
                    linewidth=5 if selected else 1.5,
                    linestyle="-" if selected else "--", zorder=1)
            ax.text(edge + 0.5, 0.19,
                    r"$1+\varepsilon$" if edge == 1 else "$1$",
                    ha="center", fontsize=13)
        for node in range(4):
            ax.scatter(node, 0, s=270, facecolors="white", edgecolors="#333333", zorder=2)
            ax.text(node, 0, str(node + 1), ha="center", va="center", fontsize=10, zorder=3)
    fig.suptitle(r"One edge can block two: $0<\varepsilon<1$", fontsize=15, y=0.97)
    fig.text(0.52, 0.025, r"Ratio $2/(1+\varepsilon)\;\longrightarrow\;2$", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.03, right=0.99, bottom=0.12, top=0.84, hspace=0.25)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
