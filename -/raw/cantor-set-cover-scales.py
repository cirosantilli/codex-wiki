"""Finite Cantor construction stages are interval covers, not finite samples."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def cantor_intervals(level):
    intervals = [(0., 1.)]
    for _ in range(level):
        intervals = [(a + offset * (b - a) / 3, a + (offset + 1) * (b - a) / 3)
                     for a, b in intervals for offset in (0, 2)]
    return intervals


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(11, 5.4), layout="constrained")
    for n in range(7):
        intervals = cantor_intervals(n)
        lengths = np.array([b - a for a, b in intervals])
        assert len(intervals) == 2 ** n
        assert np.allclose(lengths, 3. ** (-n))
        assert np.isclose(lengths.sum(), (2 / 3) ** n)
        y = 6 - n
        ax.hlines(np.full(2 ** n, y), [a for a, b in intervals], [b for a, b in intervals],
                  colors="#147d92", linewidth=6)
        noun = "interval" if n == 0 else "intervals"
        length_label = "1" if n == 0 else f"$3^{{-{n}}}$"
        ax.text(1.06, y, f"{2 ** n:2d} {noun}, length {length_label} each",
                va="center", fontsize=11)
    ax.set(yticks=np.arange(7), yticklabels=[f"n = {n}" for n in range(6, -1, -1)],
           xlim=(-.015, 1.78), ylim=(-.55, 6.65))
    ax.set_xticks([0, 1 / 3, 2 / 3, 1], ["0", "1/3", "2/3", "1"])
    ax.tick_params(axis="y", length=0, pad=12)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_bounds(0, 1)
    ax.set_title("Cantor set covers: twice as many intervals at one-third the scale",
                 fontsize=17, pad=18)
    fig.text(.5, .02, r"Each row is a finite-stage cover; the Cantor set is their infinite intersection.",
             ha="center", fontsize=11)
    # Reserve vertical space for the explanatory line without cropping the axes.
    fig.get_layout_engine().set(rect=(0, .06, 1, .94))
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
