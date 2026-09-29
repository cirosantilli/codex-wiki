"""Draw the five-state chain; run from _media to write the matching PNG.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.path import Path as MplPath


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9.6, 4.4), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    blue, orange, ink = "#1769aa", "#b54b14", "#172b3a"
    radius = 0.21
    for i in range(1, 4):
        for direction, color, y in ((1, blue, 0.12), (-1, orange, -0.12)):
            j = i + direction
            start = (i + direction * radius, y)
            end = (j - direction * radius, y)
            ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                        mutation_scale=15, linewidth=2, color=color))
            ax.text((i + j) / 2, 0.39 if direction == 1 else -0.39,
                    r"$p=\frac{1}{2}$" if direction == 1 else r"$q=\frac{1}{2}$",
                    ha="center", va="center", color=color, fontsize=14)
    for i in range(5):
        absorbing = i in (0, 4)
        ax.add_patch(Circle((i, 0), radius, facecolor="#edf4fa" if absorbing else "white",
                            edgecolor=ink, linewidth=2, zorder=3))
        if absorbing:
            ax.add_patch(Circle((i, 0), radius - 0.045, fill=False, edgecolor=ink,
                                linewidth=1, zorder=4))
            loop = MplPath([(i - 0.15, 0.17), (i - 0.75, 0.98),
                            (i + 0.75, 0.98), (i + 0.15, 0.17)],
                           [MplPath.MOVETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4])
            ax.add_patch(FancyArrowPatch(path=loop, arrowstyle="-|>", mutation_scale=15,
                                        linewidth=1.8, color=ink))
            ax.text(i, 0.82, "stay: 1", ha="center", color=ink)
            ax.text(i, -0.66, "absorbing", ha="center", color=ink)
        else:
            ax.text(i, -0.66, "interior", ha="center", color=ink)
        ax.text(i, 0, str(i), ha="center", va="center", color=ink, fontsize=16, zorder=5)
        value = ("0", r"\frac{1}{4}", r"\frac{1}{2}", r"\frac{3}{4}", "1")[i]
        ax.text(i, -1.07, rf"$h_{i}={value}$", ha="center", va="center", color=blue, fontsize=16)
    ax.set(xlim=(-0.65, 4.65), ylim=(-1.35, 1.10), aspect="equal")
    ax.axis("off")
    fig.suptitle("A five-state absorbing Markov chain", fontsize=17, y=0.96, color=ink)
    fig.text(0.5, 0.86, "Up and down refer to the state number; only interior states move.",
             ha="center", fontsize=11, color=ink)
    fig.text(0.5, 0.05, r"$h_i = \Pr_i(\mathrm{hit}\ 4\ \mathrm{before}\ 0)$: success probability",
             ha="center", fontsize=12, color=ink)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.80, bottom=0.13)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
