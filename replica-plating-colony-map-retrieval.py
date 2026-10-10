"""Original colony-map logic. Run from _media; Python 3.14, matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle


BLUE = "#236c91"
ORANGE = "#bb6615"
RED = "#b44b52"
GRAY = "#66727a"
ALL_SITES = {f"{r}{c}" for r in "ABCD" for c in range(1, 5)}
ABSENT = {"A4", "D1", "D4"}
MASTER = ALL_SITES - ABSENT
UNRESOLVED = {"B2", "C3"}
CONTROL = MASTER - UNRESOLVED
CANDIDATES = {"A2", "C1"}
OMISSION = CONTROL - CANDIDATES


def panel(ax, x, title, growing, index):
    ax.text(x + 1.5, 5.60, title, ha="center", fontsize=13, weight="bold")
    ax.text(x + 1.5, 5.27, f"{len(growing)} growing sites", ha="center", fontsize=11)
    ax.add_patch(Rectangle((x - .45, .97), 3.9, 3.95, fc="#fafcfd", ec=GRAY, lw=1.3))
    ax.add_patch(Polygon([(x - .3, 5.05), (x -.1, 5.05), (x -.2, 4.84)], color=GRAY))
    for c in range(1, 5):
        ax.text(x + c - 1, 4.57, str(c), ha="center", color=GRAY)
    for row, r in enumerate("ABCD"):
        y = 4.12 - .85 * row
        ax.text(x - .70, y, r, ha="center", va="center", color=GRAY)
        for c in range(1, 5):
            site, cx = f"{r}{c}", x + c - 1
            ax.add_patch(Circle((cx, y), .21, fc="white", ec="#dce2e6", lw=1))
            if site in growing:
                ax.add_patch(Circle((cx, y), .17, fc=BLUE, ec="white", lw=.5))
            elif site in ABSENT:
                ax.plot([cx -.11, cx +.11], [y, y], color=GRAY, lw=2)
            elif site in UNRESOLVED and index > 0:
                ax.plot([cx -.11, cx +.11], [y -.11, y +.11], color=RED, lw=2)
                ax.plot([cx -.11, cx +.11], [y +.11, y -.11], color=RED, lw=2)
            if site in CANDIDATES:
                ax.add_patch(Circle((cx, y), .27, fc="none", ec=ORANGE, lw=2))


def main():
    assert len(MASTER) == 13 and len(CONTROL) == 11 and len(OMISSION) == 9
    assert CONTROL - OMISSION == CANDIDATES
    assert MASTER - CONTROL == UNRESOLVED
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(11, 7.1), dpi=110, facecolor="white")
    ax = fig.add_axes([.04, .04, .93, .84])
    ax.set(xlim=(-.9, 12.5), ylim=(-2.05, 5.95), aspect="equal")
    ax.axis("off")
    fig.suptitle("An empty replica site has more than one explanation", y=.97, fontsize=18)
    fig.text(.5, .92, "Constructed 4 × 4 example • matching orientation • X is an assumed nutrient",
             ha="center", fontsize=11, color=GRAY)
    panel(ax, 0, "Master M", MASTER, 0)
    panel(ax, 4.45, "Control C", CONTROL, 1)
    panel(ax, 8.90, "Without X: S", OMISSION, 2)
    ax.text(5.9, .57, "Blue disc = growth    Orange ring = retrieval candidate    ▲ = orientation mark",
            ha="center", fontsize=10)
    rows = [
        (ORANGE, "A2, C1", "Present on master; grows on control; fails without X",
         "Recover MASTER source; retest with and without X"),
        (RED, "B2, C3", "Present on master; no growth even on control",
         "Unresolved transfer or viability; not an X-requirement call"),
        (GRAY, "A4, D1, D4", "Empty on master and both replicas",
         "No source colony to recover at that location"),
    ]
    for i, (color, sites, evidence, action) in enumerate(rows):
        y = -.10 - .63 * i
        ax.plot([-.6, 12.35], [y +.29, y +.29], color="#e0e5e8", lw=1)
        ax.text(-.5, y, sites, color=color, weight="bold", va="center", fontsize=11)
        ax.text(2.05, y +.06, evidence, va="center", fontsize=10)
        ax.text(2.05, y -.19, action, va="center", fontsize=10, color=color)
    ax.text(5.9, -1.94, "7 empty omission sites = 2 candidates + 2 unresolved + 3 absent sources",
            ha="center", fontsize=11)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
