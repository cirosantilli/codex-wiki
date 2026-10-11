"""Original second-law energy-flow schematics; output PNG basename in cwd.

Python 3.14 and matplotlib 3.10.7, from the top-level pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, centre, label, color):
    x, y = centre
    ax.add_patch(FancyBboxPatch((x - .29, y - .075), .58, .15,
                               boxstyle="round,pad=0.015", facecolor=color, edgecolor="#555555"))
    ax.text(x, y, label, ha="center", va="center", fontsize=11)


def arrow(ax, start, end, label, offset=(.05, 0)):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "-|>", "lw": 1.8, "color": "#333333"})
    ax.text((start[0] + end[0]) / 2 + offset[0], (start[1] + end[1]) / 2 + offset[1],
            label, va="center", fontsize=10)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.7), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
    left, right = axes
    box(left, (.45, .82), r"Hot reservoir $T_h$", "#ffe1d4")
    box(left, (.45, .48), "Cyclic device", "#eeeeee")
    box(left, (.45, .14), r"Cold reservoir $T_c$", "#dbeaf8")
    arrow(left, (.45, .23), (.45, .39), r"$Q$")
    arrow(left, (.45, .57), (.45, .73), r"$Q$")
    left.text(.87, .48, r"$W=0$", ha="center", fontsize=11)
    left.set_title("Clausius: forbidden sole effect", fontsize=12)
    box(right, (.45, .82), "Single heat reservoir", "#ffe1d4")
    box(right, (.45, .48), "Cyclic engine", "#eeeeee")
    arrow(right, (.45, .73), (.45, .57), r"$Q$")
    arrow(right, (.76, .48), (.97, .48), "", offset=(0, 0))
    right.text(.85, .56, r"$W=Q$", ha="center", fontsize=11)
    right.text(.45, .19, "No heat rejected\nNo other net change", ha="center", fontsize=11)
    right.set_title("Kelvin–Planck: forbidden sole effect", fontsize=12)
    fig.suptitle("Energy-flow diagrams of the two excluded cyclic processes", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
