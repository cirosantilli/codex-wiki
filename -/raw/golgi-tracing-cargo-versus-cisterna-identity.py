"""Draw tracer interpretation and two observationally ambiguous histories.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media; the opaque
PNG is written to the current directory. No experimental counts are plotted.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


EARLY = "#267ca7"
LATE = "#be6627"
CARGO = "#78449a"
INK = "#243744"


def text(ax, x, y, content, size=12, **kwargs):
    ax.text(x, y, content, color=INK, fontsize=size, va="center", **kwargs)


def arrow(ax, start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                               mutation_scale=15, color=INK, lw=1.7))


def sac(ax, x, y, name, identity, cargo=True):
    ax.add_patch(FancyBboxPatch((x, y), 2.2, 0.70,
                              boxstyle="round,pad=0.04,rounding_size=0.2",
                              fc="white", ec=identity, lw=3))
    text(ax, x + 1.10, y + 0.98, name, 11, ha="center")
    if cargo:
        ax.add_patch(Circle((x + 1.10, y + 0.35), 0.12, fc=CARGO, ec="none"))


def main():
    fig, ax = plt.subplots(figsize=(14, 8.6), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 14), ylim=(0, 8.6), aspect="equal")
    ax.axis("off")
    text(ax, 7, 8.20, "What does a Golgi tracer experiment identify?", 21,
         ha="center", fontweight="bold")
    text(ax, 0.45, 7.52, "Experimental comparison: a fraction name is not a structure label", 15,
         fontweight="bold")
    ax.add_patch(FancyBboxPatch((0.55, 5.65), 4.0, 1.4,
                              boxstyle="round,pad=0.10", fc="#f2f5f7", ec="#d4dde2"))
    text(ax, 2.55, 6.7, "Isolated “granule” fraction", 14, ha="center")
    text(ax, 2.55, 6.14, "mixture of structures\n+ an early radioactive signal", 12, ha="center")
    arrow(ax, (4.75, 6.32), (6.0, 6.32))
    text(ax, 5.35, 7.0, "EM +\nautoradiography", 10, ha="center")
    ax.add_patch(FancyBboxPatch((6.20, 5.65), 7.0, 1.4,
                              boxstyle="round,pad=0.10", fc="#fff9ed", ec="#e3d3ae"))
    text(ax, 9.7, 6.72, "Where were the early labeled structures?", 14, ha="center")
    text(ax, 9.7, 6.14, "Substantial labeling in condensing vacuoles\ncontaminating the mature-granule fraction", 12, ha="center")
    ax.plot([0.45, 13.55], [5.18, 5.18], color="#d7dee1", lw=1)
    text(ax, 0.45, 4.82, "Constructed histories: both record cargo in early identity, then late identity", 14,
         fontweight="bold")
    text(ax, 0.45, 4.05, "V: cargo changes\ncontainers", 13, fontweight="bold")
    sac(ax, 3.2, 3.15, "C₁ · early", EARLY, True)
    sac(ax, 7.0, 3.15, "C₂ · late", LATE, True)
    arrow(ax, (5.62, 3.5), (6.75, 3.5))
    text(ax, 6.15, 2.92, "transfer", 11, ha="center")
    text(ax, 10.3, 3.6, "persistent compartments\nwith different identities", 12)
    text(ax, 0.45, 1.92, "M: container\nchanges identity", 13, fontweight="bold")
    sac(ax, 3.2, 1.05, "C₁ · early", EARLY, True)
    sac(ax, 7.0, 1.05, "C₁ · late", LATE, True)
    arrow(ax, (5.62, 1.4), (6.75, 1.4))
    text(ax, 6.15, 0.82, "maturation", 11, ha="center")
    text(ax, 10.3, 1.55, "resident proteins change;\ncargo stays enclosed", 12)
    text(ax, 7, 0.28, "Purple dot = cargo • outline color = compartment identity • no measured times, counts or fluorescence", 11,
         ha="center")
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
