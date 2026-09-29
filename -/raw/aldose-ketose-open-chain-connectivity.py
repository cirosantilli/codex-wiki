"""Original Fischer comparison; Python 3.14, matplotlib 3.10.7.

Run in the intended output directory. No source artwork is used.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


CARBONYL = "#aa3b20"
REFERENCE = "#166280"
INK = "#223344"


def text(ax, x, y, s, size=13, color=INK, **kwargs):
    return ax.text(x, y, s, ha="center", va="center", fontsize=size,
                   color=color, **kwargs)


def bond(ax, a, b, color=INK, lw=1.7):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw,
            solid_capstyle="round", zorder=1)


def fischer(ax, x, ketose=False):
    ys = [6.9 - i * .87 for i in range(6)]
    for a, b in zip(ys, ys[1:]):
        bond(ax, (x, a - .13), (x, b + .13))
    for i, y in enumerate(ys, start=1):
        col = CARBONYL if i == (2 if ketose else 1) else REFERENCE if i == 5 else INK
        text(ax, x - 1.60, y, f"C{i}", 11, col)
        if i == 6 or (ketose and i == 1):
            text(ax, x, y, r"CH$_2$OH", 14)
        elif (ketose and i == 2) or (not ketose and i == 1):
            text(ax, x, y, "C", 14, CARBONYL)
            for dy in [-.045, .045]:
                bond(ax, (x + .16, y + dy), (x + .77, y + dy), CARBONYL)
            text(ax, x + 1, y, "O", 15, CARBONYL)
            if not ketose:
                bond(ax, (x - .77, y), (x - .16, y), CARBONYL)
                text(ax, x - 1, y, "H", 14)
        else:
            # D-glucose C2..C5: R,L,R,R; D-fructose C3..C5: L,R,R.
            oh_right = i != 3
            text(ax, x, y, "C", 14, col)
            for sign, label in [(-1, "H" if oh_right else "HO"),
                                (1, "OH" if oh_right else "H")]:
                bond(ax, (x + sign * .16, y), (x + sign * .77, y))
                text(ax, x + sign * 1.04, y, label, 14, col if i == 5 else INK)
    text(ax, x, 7.68, "D-fructose" if ketose else "D-glucose", 19, weight="bold")
    text(ax, x, 7.25, "ketose • six carbons" if ketose else "aldose • six carbons", 12)
    text(ax, x, 1.89, "C2 carbonyl between C1 and C3" if ketose else "C1 carbonyl at a chain end", 12, CARBONYL)
    text(ax, x, 1.47, "3 open-chain stereocenters" if ketose else "4 open-chain stereocenters", 12)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 7.3), dpi=140, facecolor="white")
    fig.subplots_adjust(left=.025, right=.975, bottom=.035, top=.96)
    ax.set(xlim=(0, 12), ylim=(0, 9))
    ax.axis("off")
    text(ax, 6, 8.65, "One formula, different carbonyl connectivity", 20, weight="bold")
    for x, ketose in [(3, False), (9, True)]:
        fischer(ax, x, ketose)
    ax.axvline(6, ymin=.18, ymax=.85, color="#d3dde2", lw=1)
    ax.add_patch(FancyBboxPatch((.5, .12), 11, .86, boxstyle="round,pad=.12",
                               facecolor="#edf4f6", edgecolor="none"))
    text(ax, 6, .71, r"Both: C$_6$H$_{12}$O$_6$    •    C5 OH on the right specifies D here", 12, REFERENCE)
    text(ax, 6, .33, "Fischer stereocenters: horizontal bonds toward you; vertical bonds away.", 11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
