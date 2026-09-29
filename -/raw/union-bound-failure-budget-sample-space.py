"""Draw finite failure-event budgets and their exact complements.

Run from _media. Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Every outcome has probability 1/20 in each of the two illustrative models.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    omega = set(range(1, 21))
    cases = [
        ("Separate failure outcomes", [{1}, {2}, {3}], Fraction(3, 20)),
        ("One shared failure outcome", [{1}, {1}, {1}], Fraction(1, 20)),
    ]
    colors = ["#276888", "#ba6421", "#8150a5"]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 6.8), facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.97, bottom=0.10, top=0.80, wspace=0.18)
    fig.suptitle("Three failure allowances, one simultaneous-success guarantee", fontsize=15, y=0.97)
    fig.text(0.5, 0.915, "20 equally likely outcomes; each P(Fᵢ) = 1/20; total budget = 3/20", ha="center")
    fig.legend(handles=[Patch(facecolor=c, label=f"Failure F{i + 1}") for i, c in enumerate(colors)],
               loc="upper center", bbox_to_anchor=(0.5, 0.887), ncol=3, frameon=False)
    for ax, (title, events, expected) in zip(axes, cases, strict=True):
        union = set().union(*events)
        exact = Fraction(len(union), len(omega))
        budget = sum((Fraction(len(event), len(omega)) for event in events), Fraction())
        success = Fraction(len(omega - union), len(omega))
        assert exact == expected and budget == Fraction(3, 20)
        assert success == 1 - exact and success >= 1 - budget
        ax.set(xlim=(-0.65, 4.70), ylim=(-3.5, 4.2), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=13, pad=6)
        ax.add_patch(Rectangle((-0.54, 0.12), 5.08, 3.98, facecolor="white", edgecolor="#8a919c", lw=1))
        for index, outcome in enumerate(sorted(omega)):
            x, y = index % 5, 3.55 - index // 5
            ax.add_patch(Rectangle((x - 0.39, y - 0.34), 0.78, 0.76,
                                   facecolor="#fff3e7" if outcome in union else "white",
                                   edgecolor="#586273", lw=0.9))
            ax.text(x, y + 0.14, str(outcome), ha="center", va="center", fontsize=11)
            for i, event in enumerate(events):
                ax.add_patch(Rectangle((x - 0.30 + 0.21 * i, y - 0.21), 0.17, 0.12,
                                       facecolor=colors[i] if outcome in event else "white",
                                       edgecolor=colors[i], lw=0.7))
        ax.text(2, -0.13, f"{len(union)} failure outcomes; {len(omega - union)} success outcomes", ha="center", fontsize=11)
        for y, value, label, color in [
            (-0.65, exact, "Exact any-failure probability", "#1b627f"),
            (-1.50, budget, "Union bound / total budget", "#a65b20"),
        ]:
            ax.text(-0.48, y + 0.28, f"{label}: {value}", fontsize=11)
            ax.add_patch(Rectangle((-0.48, y - 0.10), 4.94, 0.20, facecolor="#f0f1f3", edgecolor="none"))
            ax.add_patch(Rectangle((-0.48, y - 0.10), 4.94 * float(value), 0.20, facecolor=color, edgecolor="none"))
        for tick in np.array([0, 0.5, 1.0]):
            ax.plot([-0.48 + 4.94 * tick] * 2, [-1.70, -1.61], color="#586273", lw=0.8)
            ax.text(-0.48 + 4.94 * tick, -1.93, f"{tick:g}", ha="center", fontsize=9)
        ax.text(2, -2.55, f"Exact all-success probability: {success}", ha="center", fontsize=12)
        ax.text(2, -3.0, "Guaranteed all-success probability: at least 17/20", ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Colored marks show event membership. The budget is valid under either pattern of dependence.",
             ha="center", fontsize=11)
    destination = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(destination, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(destination)


if __name__ == "__main__":
    main()
