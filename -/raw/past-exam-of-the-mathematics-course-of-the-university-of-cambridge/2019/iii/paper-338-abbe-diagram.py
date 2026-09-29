"""Original Abbe plot from selected catalogue facts; save PNG in cwd.

Numerical data: SCHOTT Optical Glass pocket catalogue, 2020, pp. 100,
102, 110, 122 (PDF pages 101, 103, 111, 123).
https://www.schott.com/en-au/products/optical-glass/-/media/project/onex/products/o/optical-glass/downloads/schott-optical-glass-pocket-catalog-2020_row.pdf
The polygons are schematic family ranges, not digitized catalogue boundaries.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


GLASSES = [
    ("N-FK58", 90.90, 1.45600, "crown"),
    ("N-FK51A", 84.47, 1.48656, "crown"),
    ("N-BK7", 64.17, 1.51680, "crown"),
    ("N-LAK10", 50.62, 1.72003, "crown"),
    ("N-SF1", 29.62, 1.71736, "flint"),
    ("N-SF10", 28.53, 1.72828, "flint"),
    ("N-SF11", 25.68, 1.78472, "flint"),
]


def main():
    fig, ax = plt.subplots(figsize=(8, 4.3), dpi=100, facecolor="white")
    ax.add_patch(Polygon([(95, 1.43), (78, 1.62), (55, 1.82), (48, 1.78),
                         (54, 1.50), (76, 1.43)], fc="#1766aa", alpha=.12, ec="none"))
    ax.add_patch(Polygon([(55, 1.52), (43, 1.75), (20, 2.06), (18, 1.90),
                         (28, 1.62), (45, 1.50)], fc="#c66b22", alpha=.13, ec="none"))
    offsets = {"N-FK58": (6, 10), "N-FK51A": (6, 10), "N-BK7": (6, -16),
               "N-LAK10": (-50, 10), "N-SF1": (-60, -17),
               "N-SF10": (-60, 9), "N-SF11": (-55, 11)}
    for label, V, n, family in GLASSES:
        color = "#1766aa" if family == "crown" else "#c66b22"
        ax.plot(V, n, "o", color=color, ms=5)
        ax.annotate(label, (V, n), xytext=offsets[label], textcoords="offset points",
                    fontsize=8.5, color=color)
    ax.text(74, 1.67, "Crown families", color="#1766aa", fontsize=11)
    ax.text(37, 1.94, "Flint families", color="#a35217", fontsize=11)
    ax.set(xlim=(100, 15), ylim=(1.4, 2.1), xlabel=r"Abbe number $V_d$ (decreasing to the right)",
           ylabel=r"Refractive index $n_d$", title="Representative optical glasses; schematic family ranges")
    ax.grid(alpha=.2)
    ax.text(.02, .97, "Markers: SCHOTT catalogue data", transform=ax.transAxes,
            fontsize=9, va="top", color="0.35")
    fig.tight_layout()
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
