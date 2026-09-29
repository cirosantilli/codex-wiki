"""Draw the original five-vertex Kruskal trace; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


EDGES = [("A", "B", 1), ("B", "C", 2), ("A", "C", 3),
         ("C", "D", 4), ("D", "E", 5), ("C", "E", 6), ("B", "E", 7)]
POS = {"A": (0, 1.8), "B": (0, 0), "C": (1.7, 1.8),
       "D": (3.4, 1.8), "E": (3.4, 0)}
GREEN, RED, GREY = "#087e66", "#bf3346", "#bfc6ce"


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(2, 3, figsize=(12, 7.5), facecolor="white")
    fig.suptitle("Kruskal: buy a connection only when it joins different components",
                 fontsize=16, fontweight="bold", y=.98)
    stages = [(set(), "0  Start: five isolated vertices", "Accepted cost = 0"),
              ({1}, "1  Accept AB (weight 1)", "Accepted cost = 1"),
              ({1, 2}, "2  Accept BC (weight 2)", "Accepted cost = 3"),
              ({1, 2}, "3  Reject AC (weight 3)", "A–B–C already connects A to C"),
              ({1, 2, 4}, "4  Accept CD (weight 4)", "Accepted cost = 7"),
              ({1, 2, 4, 5}, "5  Accept DE (weight 5); stop", "4 edges; one tree; total cost = 12")]
    for step, (ax, (accepted, title, footer)) in enumerate(zip(axes.flat, stages)):
        for u, v, w in EDGES:
            x1, y1 = POS[u]
            x2, y2 = POS[v]
            rejected = w == 3 and step >= 3
            color = GREEN if w in accepted else RED if rejected else GREY
            ax.plot([x1, x2], [y1, y2], color=color,
                    lw=3.3 if w in accepted else 2.2 if rejected else 1.5,
                    ls="--" if rejected else "-", zorder=1)
            tx, ty = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(tx, ty, str(w), ha="center", va="center", color=color,
                    fontsize=12, fontweight="bold",
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1}, zorder=3)
        for label, (x, y) in POS.items():
            ax.add_patch(Circle((x, y), .19, fc="white", ec="#23374d", lw=1.7, zorder=4))
            ax.text(x, y, label, ha="center", va="center", zorder=5, fontweight="bold")
        ax.set_title(title, fontsize=12, fontweight="bold", pad=8)
        ax.text(1.7, -.62, footer, ha="center", fontsize=10, color="#23374d")
        ax.set(xlim=(-.4, 3.8), ylim=(-.85, 2.2), aspect="equal")
        ax.axis("off")
    fig.legend([Line2D([], [], color=GREEN, lw=3), Line2D([], [], color=RED, lw=2, ls="--"),
                Line2D([], [], color=GREY, lw=2)],
               ["Accepted", "Rejected: cycle", "Unexamined"],
               loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(.5, .025))
    fig.subplots_adjust(left=.035, right=.97, top=.87, bottom=.12, hspace=.45, wspace=.3)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
