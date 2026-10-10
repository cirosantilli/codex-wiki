"""Draw exact unions of finite events. Run from _media with Python 3.14.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
All twelve outcomes have probability 1/12; no independence is assumed.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    omega = set(range(1, 13))
    event_a = {1, 2, 3, 4}
    cases = [
        ("Disjoint events", {5, 6, 7, 8}, Fraction(2, 3)),
        ("Two shared outcomes", {3, 4, 5, 6}, Fraction(1, 2)),
        ("Identical events", {1, 2, 3, 4}, Fraction(1, 3)),
    ]
    colors = {"A": "#c3e2f2", "B": "#f8d6ad", "AB": "#ddc8ef", "": "white"}
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 6.4), facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.10, top=0.79, wspace=0.13)
    fig.suptitle("Union bound: overlap changes the union, not the sum", fontsize=16, y=0.97)
    fig.text(0.5, 0.915, "12 equally likely outcomes; P(A) = P(B) = 4/12 in every panel", ha="center")
    fig.legend(
        handles=[Patch(facecolor=colors[k], edgecolor="#586273", label=label)
                 for k, label in [("A", "A only"), ("B", "B only"), ("AB", "A and B"), ("", "neither")]],
        loc="upper center", bbox_to_anchor=(0.5, 0.885), ncol=4, frameon=False,
    )
    for ax, (title, event_b, expected) in zip(axes, cases, strict=True):
        union = event_a | event_b
        exact = Fraction(len(union), len(omega))
        bound = Fraction(len(event_a) + len(event_b), len(omega))
        assert exact == expected and bound == Fraction(2, 3)
        assert bound - exact == Fraction(len(event_a & event_b), len(omega))
        ax.set(xlim=(-0.6, 3.6), ylim=(-3.0, 3.5), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=13, pad=8)
        ax.add_patch(Rectangle((-0.48, 0.40), 3.96, 2.90, facecolor="white", edgecolor="#8a919c", lw=1))
        for index, outcome in enumerate(sorted(omega)):
            x, y = index % 4, 2.8 - index // 4
            membership = ("A" if outcome in event_a else "") + ("B" if outcome in event_b else "")
            ax.add_patch(Circle((x, y), 0.35, facecolor=colors[membership], edgecolor="#586273", lw=1.1))
            ax.text(x, y + 0.08, str(outcome), ha="center", va="center", fontsize=11)
            ax.text(x, y - 0.16, membership or "–", ha="center", va="center", fontsize=8)
        ax.text(1.5, 0.13, f"Union: {len(union)} distinct outcomes", ha="center", fontsize=11)
        for y, value, label, color in [
            (-0.62, exact, "Exact union", "#1b627f"),
            (-1.42, bound, "Union bound", "#a65b20"),
        ]:
            ax.text(-0.4, y + 0.29, f"{label}: {value}", fontsize=11)
            ax.add_patch(Rectangle((-0.4, y - 0.10), 3.8, 0.20, facecolor="#f0f1f3", edgecolor="none"))
            ax.add_patch(Rectangle((-0.4, y - 0.10), 3.8 * float(value), 0.20, facecolor=color, edgecolor="none"))
        ticks = np.array([0, 0.5, 1.0])
        for tick in ticks:
            ax.plot([-0.4 + 3.8 * tick] * 2, [-1.63, -1.53], color="#586273", lw=0.8)
            ax.text(-0.4 + 3.8 * tick, -1.80, f"{tick:g}", ha="center", fontsize=9)
        ax.text(1.5, -2.35, f"Extra counts: {bound - exact}", ha="center", fontsize=11)
    fig.text(0.5, 0.035, "The sum counts a shared outcome twice; the union counts it once.", ha="center", fontsize=12)
    destination = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(destination, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(destination)


if __name__ == "__main__":
    main()
