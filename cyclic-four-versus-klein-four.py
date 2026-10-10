"""Compare the addition tables of C4 and C2 x C2; write PNG to CWD."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
import numpy as np


def operation_tables():
    elements = np.arange(4)
    c4 = (elements[:, None] + elements[None, :]) % 4
    # Binary labels 00, 01, 10, 11: XOR is componentwise addition modulo two.
    v4 = np.bitwise_xor(elements[:, None], elements[None, :])
    assert np.array_equal(c4, c4.T)
    assert np.array_equal(v4, v4.T)
    assert np.array_equal(np.diag(c4), [0, 2, 0, 2])
    assert np.all(np.diag(v4) == 0)
    return c4, v4


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.5), dpi=100)
    cmap = ListedColormap(["#e6eef7", "#f7d9bb", "#d7eedf", "#eddcf4"])
    c4, v4 = operation_tables()
    panels = [
        (c4, ["0", "1", "2", "3"], r"$C_4$: addition modulo four",
         "1 and 3 have order 4\nA single step can visit all four states"),
        (v4, ["00", "01", "10", "11"], r"$C_2 \times C_2$: add each bit modulo two",
         "01, 10 and 11 each have order 2\nEvery state added to itself gives 00"),
    ]
    for ax, (table, labels, title, note) in zip(axes, panels, strict=True):
        ax.imshow(table, cmap=cmap, vmin=-0.5, vmax=3.5)
        for row in range(4):
            for column in range(4):
                ax.text(column, row, labels[table[row, column]],
                        ha="center", va="center", fontsize=17, color="#172434")
            ax.add_patch(Rectangle((row - 0.48, row - 0.48), 0.96, 0.96,
                                   fill=False, linewidth=2, edgecolor="#45566b"))
        ax.set_xticks(range(4), labels=labels)
        ax.set_yticks(range(4), labels=labels)
        ax.xaxis.tick_top()
        ax.tick_params(axis="both", length=0, pad=9)
        ax.set_xticks(np.arange(-0.5, 4, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 4, 1), minor=True)
        ax.grid(which="minor", color="white", linewidth=3)
        ax.tick_params(which="minor", bottom=False, left=False, top=False)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_title(title, fontsize=13, weight="bold", pad=24)
        ax.text(1.5, 4.15, note, ha="center", va="top",
                fontsize=12, linespacing=1.5)
        ax.set_ylim(3.5, -0.5)
    fig.suptitle("Same size and commutativity; different repetition periods",
                 fontsize=16, weight="bold", y=0.965)
    fig.subplots_adjust(left=0.07, right=0.95, top=0.78, bottom=0.22, wspace=0.32)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
