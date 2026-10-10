"""Draw ordered pair sums and their counts; tested with Python 3.14.

Write sumset-pair-sums.png to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def main():
    examples = [np.array([0, 1, 2, 3]), np.array([0, 1, 4, 10])]
    expected_sums = [np.arange(7), np.array([0, 1, 2, 4, 5, 8, 10, 11, 14, 20])]
    expected_counts = [[1, 2, 3, 4, 3, 2, 1], [1, 2, 1, 2, 2, 1, 2, 2, 2, 1]]
    all_sums = np.unique(np.concatenate(expected_sums))
    palette = plt.colormaps["tab20"](np.arange(len(all_sums)))
    palette[:, :3] = 0.65 * palette[:, :3] + 0.35
    colors = dict(zip(all_sums, palette))
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.6), dpi=120, facecolor="white")
    fig.suptitle("Sixteen ordered pairs, different numbers of sums", fontsize=16, y=0.975)
    fig.text(0.5, 0.915, "Each cell shows row + column. The same sum has the same color.",
             ha="center", fontsize=11)
    for col, (values, name) in enumerate(zip(examples, ["A", "B"])):
        pair_sums = values[:, None] + values[None, :]
        sums, counts = np.unique(pair_sums, return_counts=True)
        assert np.array_equal(sums, expected_sums[col])
        assert counts.tolist() == expected_counts[col]
        assert int(counts.sum()) == len(values) ** 2 == 16
        ax = axes[0, col]
        indices = np.searchsorted(all_sums, pair_sums)
        ax.imshow(indices, cmap=ListedColormap(palette), vmin=-0.5,
                  vmax=len(palette) - 0.5, interpolation="nearest")
        for row in range(4):
            for column in range(4):
                ax.text(column, row, str(pair_sums[row, column]), ha="center",
                        va="center", fontsize=15, fontweight="bold")
        ax.set_xticks(range(4), labels=values)
        ax.set_yticks(range(4), labels=values)
        ax.set_xticks(np.arange(-0.5, 4, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 4, 1), minor=True)
        ax.grid(which="minor", color="white", linewidth=2)
        ax.tick_params(which="both", length=0)
        ax.set_xlabel("Second member")
        ax.set_ylabel("First member")
        ax.set_title(f"{name} = {{{', '.join(map(str, values))}}}", pad=10)
        ax.spines[:].set_visible(False)

        ax = axes[1, col]
        ax.bar(sums, counts, color=[colors[s] for s in sums], width=0.72,
               edgecolor="#344454", linewidth=0.5)
        for total, count in zip(sums, counts):
            ax.text(total, count + 0.1, str(count), ha="center", fontsize=11)
        ax.set_title(f"{len(sums)} distinct sums; counts total 16", pad=10)
        ax.set_xlabel("Sum s (ordinary integer addition)")
        ax.set_ylabel(r"Ordered-pair count $r_{" + name + "+" + name + r"}(s)$")
        ax.set_xticks(sums)
        if col == 1:
            plt.setp(ax.get_xticklabels(), rotation=40, ha="right", fontsize=10)
        ax.set_yticks(range(5))
        ax.set_ylim(0, 4.7)
        ax.set_xlim(-0.85, sums[-1] + 0.85)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_axisbelow(True)
        ax.grid(axis="y", color="#e3e8eb")
    fig.subplots_adjust(left=0.09, right=0.98, top=0.83, bottom=0.105,
                        wspace=0.34, hspace=0.65)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
