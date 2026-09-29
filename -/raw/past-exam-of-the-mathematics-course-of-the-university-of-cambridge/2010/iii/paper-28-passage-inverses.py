"""Original schematic of the two inverses at a running-maximum plateau.

Tested with Python 3.14.4 and the root numpy/matplotlib dependencies.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "paper28-matplotlib"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(8.5, 3.6), dpi=130)
    fig.patch.set_facecolor("white")
    times = np.array([0, .35, .7, 1.2, 1.8, 2.5, 3.2, 3.8, 4.2])
    heights = np.array([0, .3, 1, .45, .65, -.1, .5, 1, 1.5])
    mesh = np.unique(np.r_[np.linspace(0, 4.2, 1600), times])
    path = np.interp(mesh, times, heights)
    ax.plot(mesh, path, color="#365e87", lw=1.7, label="schematic path")
    ax.plot(mesh, np.maximum.accumulate(path), color="#ca7c2b", lw=2,
            label="running maximum")
    ax.axhline(1, color="#888888", ls=":", lw=1)
    for time, color, label in [(.7, "#277a56", "$H_a$"), (3.8, "#b94b43", "$S_a$")]:
        ax.axvline(time, color=color, ls="--", lw=1.1)
        ax.text(time, -.33, label, color=color, ha="center", fontsize=12)
    ax.text(.07, 1.05, "$a$", fontsize=12)
    ax.set(xlim=(0, 4.3), ylim=(-.38, 1.7), xlabel="time", ylabel="height",
           title="An excursion below the record level")
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    bx.plot([0, .3, 1], [0, .35, .7], color="#365e87", lw=2)
    bx.plot([1, 1.4], [3.8, 4.12], color="#365e87", lw=2,
            label="$H_b=S_b$ away from the jump")
    bx.plot([1, 1], [.7, 3.8], color="#aaaaaa", ls=":", lw=1.3)
    bx.scatter([1], [.7], color="#277a56", s=48, zorder=4)
    bx.scatter([1], [3.8], color="#b94b43", s=48, zorder=4)
    bx.annotate("$H_a=S_{a-}$", (1, .7), xytext=(.45, 1.5),
                arrowprops=dict(arrowstyle="->", color="#277a56"),
                color="#277a56", fontsize=11)
    bx.annotate("$S_a=H_{a+}$", (1, 3.8), xytext=(.2, 3.25),
                arrowprops=dict(arrowstyle="->", color="#b94b43"),
                color="#b94b43", fontsize=11)
    bx.set(xlim=(0, 1.45), ylim=(-.1, 4.4), xlabel="level $b$", ylabel="passage time",
           title="The inverse selects a plateau endpoint")
    bx.set_xticks([0, .5, 1, 1.4], ["0", "0.5", "$a$", "1.4"])
    bx.legend(loc="upper left", fontsize=8, frameon=False)
    for axes in (ax, bx):
        axes.set_facecolor("white")
        axes.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
