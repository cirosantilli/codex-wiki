"""Synthetic sampling diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes only the matching PNG basename to the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.titlesize": 11})
    source = np.array([[0, 0, 1, 2, 3, 3], [0, 1, 1, 2, 3, 2],
                       [1, 1, 2, 3, 2, 1], [1, 2, 3, 2, 1, 0]]) / 3
    cx, cy = np.arange(6) + .5, np.arange(4) + .5
    ox, oy = (np.arange(24) + .5) / 4, (np.arange(16) + .5) / 4
    nearest = np.repeat(np.repeat(source, 4, axis=0), 4, axis=1)
    along_x = np.array([np.interp(ox, cx, row) for row in source])
    smooth = np.array([np.interp(oy, cy, col) for col in along_x.T]).T
    assert nearest.shape == smooth.shape == (16, 24)
    assert 0 <= smooth.min() <= smooth.max() <= 1
    fig = plt.figure(figsize=(10.5, 6.8), facecolor="white", layout="constrained")
    gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.05])
    titles = ["A. Recorded: 6 × 4 = 24 values", "B. Repeat: 24 × 16 output pixels",
              "C. Interpolate: 24 × 16 output pixels"]
    for i, data in enumerate([source, nearest, smooth]):
        ax = fig.add_subplot(gs[0, i])
        ax.imshow(data, cmap="gray", vmin=0, vmax=1, origin="lower",
                  extent=(0, 6, 0, 4), interpolation="nearest")
        ax.set_title(titles[i], pad=11)
        # Magenta rings locate the original sample positions in every view.
        xx, yy = np.meshgrid(cx, cy)
        ax.scatter(xx, yy, s=24, facecolors="none", edgecolors="#bd2876", linewidths=.8)
        if i == 0:
            for r in range(4):
                for c in range(6):
                    value = source[r, c]
                    ax.text(c + .5, r + .25, ["0", "⅓", "⅔", "1"][round(value * 3)],
                            color="white" if value < .5 else "black", ha="center", fontsize=9)
        pitch = 1 if i == 0 else .25
        ax.set_xticks(np.arange(0, 6.01, pitch), minor=True)
        ax.set_yticks(np.arange(0, 4.01, pitch), minor=True)
        ax.grid(which="minor", color="#678096", alpha=.5, linewidth=.35)
        ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
        ax.set_xlabel("Rings: original sample positions")
    ax = fig.add_subplot(gs[1, :])
    x = np.linspace(0, 2, 2001)
    samples_x = np.arange(9) / 4
    slow = .5 + .4 * np.sin(2 * np.pi * x)
    fast = .5 + .4 * np.sin(10 * np.pi * x)
    samples = .5 + .4 * np.sin(2 * np.pi * samples_x)
    assert np.allclose(samples, .5 + .4 * np.sin(10 * np.pi * samples_x), atol=1e-14)
    ax.plot(x, slow, color="#146caa", lw=2.4, label="f(x): 1 cycle per unit")
    ax.plot(x, fast, color="#bd2876", lw=1.5, label="g(x): 5 cycles per unit")
    ax.scatter(samples_x, samples, c="black", s=35, zorder=4, label="Common samples at x = j/4")
    ax.set(xlim=(0, 2), ylim=(0, 1), xlabel="Position x", ylabel="Synthetic shade value",
           title="D. Different originals, identical point samples (a separate toy example)")
    ax.set_xticks(samples_x)
    ax.grid(alpha=.2)
    ax.legend(loc="lower center", ncols=3, fontsize=9)
    fig.suptitle("A raster stores samples; a reconstruction chooses between them", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
