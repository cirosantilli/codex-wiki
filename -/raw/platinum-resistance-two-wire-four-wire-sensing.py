"""Original two-wire versus four-wire platinum sensing circuit.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Ideal sensing inputs draw no current; numerical examples are stipulated.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


FORCE = "#b74337"
SENSE = "#246f9d"


def wire(ax, points, color):
    ax.plot(*zip(*points), color=color, lw=2.3, solid_capstyle="round")


def resistor(ax, x0, x1, y, label):
    ax.add_patch(Rectangle((x0, y - 0.14), x1 - x0, 0.28,
                           facecolor="white", edgecolor=FORCE, lw=2))
    ax.text((x0 + x1) / 2, y + 0.23, label, ha="center", fontsize=10)


def voltmeter(ax, x, y):
    ax.add_patch(Circle((x, y), 0.22, facecolor="white", edgecolor=SENSE, lw=2))
    ax.text(x, y, "V", ha="center", va="center", color=SENSE, fontsize=13)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), layout="constrained")
    for ax, four in zip(axes, (False, True)):
        ax.set(xlim=(0, 6), ylim=(0, 5.25))
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title("Four wires: sense at element" if four else "Two wires: sense at readout",
                     fontsize=12, pad=12)
        # Closed force loop: source -> upper lead -> platinum -> lower lead -> source.
        wire(ax, [(0.7, 2.82), (0.7, 4), (1.3, 4)], FORCE)
        resistor(ax, 1.3, 2.3, 4, "r₁ = 0.50 Ω")
        wire(ax, [(2.3, 4), (4.8, 4), (4.8, 3.15)], FORCE)
        ax.add_patch(Rectangle((4.58, 1.85), 0.44, 1.3,
                               facecolor="#f5f1df", edgecolor=FORCE, lw=2))
        ax.text(4.8, 2.5, "Pt", ha="center", va="center", fontsize=11)
        ax.text(5.12, 2.5, "R(t)", va="center", fontsize=11)
        wire(ax, [(4.8, 1.85), (4.8, 1), (2.3, 1)], FORCE)
        resistor(ax, 1.3, 2.3, 1, "r₂ = 0.50 Ω")
        wire(ax, [(1.3, 1), (0.7, 1), (0.7, 2.18)], FORCE)
        ax.add_patch(Circle((0.7, 2.5), 0.32, facecolor="white", edgecolor=FORCE, lw=2))
        ax.annotate("", (0.7, 2.72), (0.7, 2.28),
                    arrowprops={"arrowstyle": "->", "color": FORCE, "lw": 1.5})
        ax.text(0.7, 3.18, "I", color=FORCE, ha="center")
        ax.annotate("", (3.45, 4), (2.65, 4),
                    arrowprops={"arrowstyle": "->", "color": FORCE, "lw": 2})
        voltmeter(ax, 2.9, 2.5)
        if four:
            wire(ax, [(4.8, 3.15), (2.9, 3.15), (2.9, 2.72)], SENSE)
            wire(ax, [(4.8, 1.85), (2.9, 1.85), (2.9, 2.28)], SENSE)
            nodes = [(4.8, 3.15), (4.8, 1.85)]
            formula = "V / I = R(t)"
            result = "109.625 Ω → 25 °C"
        else:
            wire(ax, [(0.7, 4), (0.7, 4.68), (2.9, 4.68), (2.9, 2.72)], SENSE)
            wire(ax, [(0.7, 1), (0.7, 0.45), (2.9, 0.45), (2.9, 2.28)], SENSE)
            nodes = [(0.7, 4), (0.7, 1)]
            formula = "V / I = R(t) + r₁ + r₂"
            result = "110.625 Ω → 27.597… °C"
        for x, y in nodes:
            ax.plot(x, y, "o", color=SENSE, ms=5)
        ax.text(3, -0.07, formula, ha="center", fontsize=12)
        ax.text(3, -0.48, result, ha="center", fontsize=11)
    fig.suptitle("Illustrative Pt100 at true 25 °C: lead drops belong outside the sensing interval",
                 fontsize=13)
    fig.supxlabel("Red: force current    Blue: negligible sensing current\n"
                  "Four wires do not remove self-heating or heat conduction along the probe.",
                  fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
