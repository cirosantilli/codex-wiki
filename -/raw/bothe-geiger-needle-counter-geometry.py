"""Functional reading of Bothe's Nobel lecture, pp. 272–273; not to scale.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media; write an opaque PNG to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def arrow(ax, start, end, color, lw=2):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color=color, lw=lw))


def main():
    fig, (ax, rec) = plt.subplots(1, 2, figsize=(11, 5.6),
                                  gridspec_kw={"width_ratios": [1.6, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Bothe–Geiger: one scattering, two different detection channels", fontsize=15)
    ax.set(xlim=(0, 10), ylim=(0, 7.5))
    ax.axis("off")
    for y, col in [(3.1, "#eef5fa"), (0.8, "#fcf1e4")]:
        ax.add_patch(Rectangle((1.8, y), 6.7, 2.3, facecolor=col,
                               edgecolor="#555555", lw=1.5))
    ax.plot([1.8, 8.5], [3.1, 3.1], color="#444444", lw=4)
    ax.text(2, 5.65, "Hydrogen atmosphere", fontsize=12)
    ax.text(8.25, 5.13, "Counter 1\nrecoil electron", ha="right", va="top", fontsize=11)
    ax.text(8.25, 1.0, "Counter 2\nscattered photon", ha="right", va="bottom", fontsize=11)
    arrow(ax, (0.1, 3.6), (8.9, 3.6), "#2574a9")
    ax.text(0.1, 3.95, "Incident X-rays", color="#2574a9", fontsize=11)
    ax.plot(4.2, 3.6, "o", color="#222222", ms=6)
    arrow(ax, (4.2, 3.6), (5.5, 4.6), "#b55220")
    ax.text(4.45, 4.82, "Local electron recoil", color="#b55220", fontsize=10)
    arrow(ax, (4.2, 3.6), (5.2, 2.2), "#2574a9")
    ax.text(5.5, 2.8, "Photon crosses wall", color="#2574a9", fontsize=10)
    arrow(ax, (5.2, 2.2), (5.7, 1.8), "#b55220")
    ax.text(2.1, 0.35, "Photon detection requires electron release", fontsize=10)
    for y in [4.4, 1.6]:
        ax.plot([1.8, 2.5], [y, y], color="#555555", lw=2)
        ax.plot([2.5, 2.85, 2.5], [y+0.12, y, y-0.12], color="#555555")
    ax.text(1.9, 6.5, "Needle counters share a wall; beam passes beside it", fontsize=10)
    ax.text(2.0, 5.98, "Functional layout; dimensions and angles schematic", fontsize=10, color="#555555")
    rec.set(xlim=(0, 10), ylim=(0, 7.5))
    rec.axis("off")
    rec.text(5, 6.45, "Paired photographic records", ha="center", fontsize=12)
    rec.add_patch(Rectangle((0.5, 1.8), 9, 3.7, facecolor="#f7f7f7", edgecolor="#555555"))
    t = np.linspace(1, 9, 1400)
    for base, shift, label in [(4.4, 0, "1"), (2.9, 0.06, "2")]:
        trace = sum(0.5 * np.exp(-((t - center - shift)/0.08)**2)
                    for center in [2.4, 5.2, 7.7])
        rec.plot(t, base+trace, color="#333333", lw=1.5)
        rec.text(0.65, base, label, va="center", fontsize=11)
    for center in [2.4, 5.2, 7.7]:
        rec.plot([center, center], [2.3, 5.2], color="#a6a6a6", ls="--", lw=1)
    arrow(rec, (1, 1.2), (8.8, 1.2), "#333333", 1.5)
    rec.text(5, 0.75, "Common time coordinate", ha="center", fontsize=11)
    rec.text(5, 0.15, "Illustrative marks, not a historical trace", ha="center", fontsize=10)
    fig.subplots_adjust(left=.025, right=.98, bottom=.075, top=.9, wspace=.1)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
