"""Three events under an exact beta=4/5 Lorentz boost.

The same event labels are used in minkowski-light-cone-events.py.
Outputs an opaque matching PNG to CWD; Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    beta, gamma = 4/5, 5/3
    # Columns are x and ct, in light-seconds.
    original = np.array([[3, 4], [3, 3], [3, 2]], dtype=float)
    transformed = np.column_stack([
        gamma*(original[:, 0]-beta*original[:, 1]),
        gamma*(original[:, 1]-beta*original[:, 0]),
    ])
    colors = ["#275aa0", "#29795c", "#bb6430"]
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 6.8), dpi=100,
                             facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.19, top=0.81, wspace=0.24)
    labels = [
        ["A: (3, 4)", "N: (3, 3)", "B: (3, 2)"],
        ["A: (−1/3, 8/3)", "N: (1, 1)", "B: (7/3, −2/3)"],
    ]
    label_positions = [
        [(0.7, 4.45), (3.22, 3.0), (3.22, 1.62)],
        [(-3.85, 3.38), (1.45, 1.04), (0.75, -1.6)],
    ]
    for panel, (ax, data) in enumerate(zip(axes, [original, transformed])):
        x = np.linspace(-4.2, 4.7, 401)
        ax.fill_between(x, np.abs(x), 5.0, color="#eef4fc", zorder=0)
        ax.fill_between(x, -np.abs(x), -2.1,
                        where=np.abs(x)<2.1, color="#f1f4f8", zorder=0)
        ax.plot(x, x, color="#85ae98", linewidth=1.4)
        ax.plot(x, -x, color="#85ae98", linewidth=1.4)
        ax.axhline(0, color="#727d89", linewidth=0.8)
        ax.axvline(0, color="#727d89", linewidth=0.8)
        for index, ((ex, et), color) in enumerate(zip(data, colors)):
            ax.scatter([ex], [et], color=color, s=65, edgecolor="white", zorder=5)
            ax.annotate(labels[panel][index], xy=(ex, et),
                        xytext=label_positions[panel][index], color=color,
                        fontsize=11, arrowprops={"arrowstyle": "-", "color": color})
        ax.scatter([0], [0], color="#273643", s=40, zorder=5)
        ax.text(-0.4, -0.5, "O")
        ax.set(xlim=(-4.2, 4.7), ylim=(-2.1, 5.0), aspect="equal",
               xlabel=("x" if panel == 0 else "x′") + "  [light-seconds]",
               ylabel=("ct" if panel == 0 else "ct′") + "  [light-seconds]")
        ax.grid(alpha=0.15)
        ax.set_title("Frame S" if panel == 0 else "Frame S′, moving at +0.8c",
                     fontsize=13, pad=12)
    fig.suptitle("Coordinates change; the Minkowski intervals stay fixed",
                 fontsize=16, y=0.965)
    fig.text(0.5, 0.885, "ct′ = (5/3)(ct − 0.8x)     x′ = (5/3)(x − 0.8ct)",
             ha="center", fontsize=12)
    fig.text(0.5, 0.06,
             "A: s² = −7     N: s² = 0     B: s² = 5   [light-seconds squared]\n"
             "B is later than O in S and earlier in S′.  It remains spacelike in both.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.savefig(Path.cwd() / "lorentz-boost-preserves-intervals.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
