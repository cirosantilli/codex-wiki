"""Draw the Q2(d) channel schematic into the current working directory.

Tested with Python 3.14.4 and matplotlib 3.10.7 (repository pyproject.toml).
Uses only matplotlib plus the standard library. Bodies are omitted; tie PMOS
bodies to VDD and NMOS bodies to ground. Four input inverters are not drawn.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(8, 10), dpi=140, facecolor="white")
    ax.set_facecolor("white")

    def wire(xs, ys):
        ax.plot(xs, ys, color="#263238", linewidth=1.5, solid_capstyle="round")

    def device(x, y, gate, kind):
        # Vertical channel, source/drain contacts and insulated gate.
        wire([x, x], [y - 0.5, y - 0.18])
        wire([x, x], [y - 0.18, y + 0.18])
        wire([x, x], [y + 0.18, y + 0.5])
        wire([x - 0.16, x - 0.16], [y - 0.16, y + 0.16])
        end = x - (0.29 if kind == "p" else 0.16)
        wire([x - 0.48, end], [y, y])
        if kind == "p":
            ax.add_patch(Circle((x - 0.225, y), 0.065, facecolor="white",
                                edgecolor="#263238", linewidth=1.3, zorder=3))
        ax.text(x - 0.56, y, gate, ha="right", va="center", fontsize=13)

    # Each PMOS branch consists of two parallel pairs in series.
    for center, labels in [(3.0, ("$a$", "$\\overline{c}$", "$\\overline{a}$", "$c$")),
                           (7.0, ("$b$", "$\\overline{d}$", "$\\overline{b}$", "$d$"))]:
        left, right = center - 0.65, center + 0.65
        for y, pair in [(8.0, labels[:2]), (6.5, labels[2:])]:
            for x, label in zip((left, right), pair):
                device(x, y, label, "p")
            wire([left, right], [y + 0.5, y + 0.5])
            wire([left, right], [y - 0.5, y - 0.5])
        wire([center, center], [8.5, 9.0])
        wire([center, center], [7.5, 7.0])
        wire([center, center], [6.0, 5.5])
    wire([3, 7], [9, 9])
    wire([5, 5], [9, 9.35])
    ax.text(5, 9.43, "$V_{DD}$", ha="center", va="bottom", fontsize=15)
    wire([3, 7], [5.5, 5.5])
    wire([5, 5], [5.5, 5.0])
    wire([5, 8.3], [5.0, 5.0])
    ax.add_patch(Circle((5, 5), 0.045, color="#263238"))
    ax.text(8.45, 5, "$z$", va="center", fontsize=17)

    # Each NMOS module has two parallel branches, each with two series devices.
    for top, gates in [(4.7, ("$a$", "$\\overline{c}$", "$\\overline{a}$", "$c$")),
                       (2.3, ("$b$", "$\\overline{d}$", "$\\overline{b}$", "$d$"))]:
        bottom = top - 2.0
        wire([3.5, 6.5], [top, top])
        wire([3.5, 6.5], [bottom, bottom])
        for x, pair in [(3.5, gates[:2]), (6.5, gates[2:])]:
            device(x, top - 0.5, pair[0], "n")
            device(x, top - 1.5, pair[1], "n")
    wire([5, 5], [5, 4.7])
    wire([5, 5], [2.7, 2.3])
    wire([5, 5], [0.3, -0.05])
    for y, half in [(-0.05, 0.35), (-0.17, 0.23), (-0.29, 0.10)]:
        wire([5 - half, 5 + half], [y, y])

    ax.text(0.1, 7.5, "Pull-up\n8 PMOS", ha="left", va="center", color="#235789")
    ax.text(0.1, 2.8, "Pull-down\n8 NMOS", ha="left", va="center", color="#235789")
    ax.set_title("Static CMOS: output high when either input pair agrees", fontsize=15, pad=20)
    ax.text(5, -0.8, "Gate bubble: PMOS conducts at 0.  NMOS conducts at 1.\n"
            "Add four input inverters: 16 network devices + 8 = 24 transistors.",
            ha="center", va="center", fontsize=11)
    ax.set_xlim(-0.2, 9.5)
    ax.set_ylim(-1.2, 10)
    ax.axis("off")
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.03, top=0.94)
    fig.savefig(Path.cwd() / "digital-resit-2015-cmos-network.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
