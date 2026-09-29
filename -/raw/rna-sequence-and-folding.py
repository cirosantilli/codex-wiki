"""Draw an original numbered RNA hairpin; write basename.png in cwd.

Build: make _media/rna-sequence-and-folding.png
Uses the repository's Python 3.14, NumPy and Matplotlib dependencies.
The chosen pairing is illustrative, not an equilibrium-folding prediction.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


COLORS = {"A": "#f3c86a", "U": "#9dd9e8", "G": "#bdb0e2", "C": "#a7d2a2"}


def base(ax, x, y, letter, number, dx=0, dy=-0.45):
    ax.text(x, y, letter, ha="center", va="center", fontsize=15,
            bbox={"boxstyle": "circle,pad=0.3", "fc": COLORS[letter], "ec": "#526779"},
            zorder=3)
    ax.text(x + dx, y + dy, str(number), ha="center", va="center", fontsize=9,
            color="#526779", zorder=4)


def main():
    sequence = "GCAUUUUUAUGC"
    pairs = [(1, 12), (2, 11), (3, 10), (4, 9)]
    partners = {"A": "U", "U": "A", "G": "C", "C": "G"}
    assert len(sequence) == 12
    assert all(partners[sequence[i - 1]] == sequence[j - 1] for i, j in pairs)
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (linear, folded) = plt.subplots(1, 2, figsize=(9.2, 5.5),
                                       gridspec_kw={"width_ratios": [1.45, 1]})
    fig.subplots_adjust(left=0.025, right=0.98, top=0.82, bottom=0.2, wspace=0.09)
    fig.suptitle("RNA: one continuous strand can pair with itself", fontsize=16, y=0.97)
    linear.set(xlim=(-1.0, 12.1), ylim=(-1.9, 2.0))
    folded.set(xlim=(-1.15, 3.25), ylim=(-0.75, 5.0), aspect="equal")
    for ax in (linear, folded):
        ax.axis("off")
    linear.set_title("Numbered sequence, read 5′ → 3′", fontsize=12, pad=20)
    linear.plot(range(12), [0] * 12, color="#526779", lw=2, zorder=1)
    for i, letter in enumerate(sequence):
        base(linear, i, 0, letter, i + 1)
    linear.text(-0.8, 0, "5′", ha="center", va="center", fontsize=13)
    linear.text(11.8, 0, "3′", ha="center", va="center", fontsize=13)
    linear.annotate("", (11, -0.9), (0, -0.9),
                    arrowprops={"arrowstyle": "->", "color": "#176b92", "lw": 1.8})
    linear.text(5.5, 1.25, "GCAU  +  UUUU  +  AUGC", ha="center", fontsize=15)
    linear.text(5.5, -1.5, "4 paired bases  +  4 loop bases  +  4 paired bases",
                ha="center", fontsize=10)
    folded.set_title("Illustrative hairpin (stem-loop)", fontsize=12, pad=20)
    left = np.column_stack((np.zeros(4), np.arange(4)))
    angles = np.linspace(np.pi, 0, 6)[1:-1]
    loop = np.column_stack((1 + np.cos(angles), 3 + 1.35 * np.sin(angles)))
    right = np.column_stack((np.full(4, 2), np.arange(3, -1, -1)))
    coords = np.vstack((left, loop, right))
    folded.plot(coords[:, 0], coords[:, 1], color="#526779", lw=2, zorder=1)
    for i, j in pairs:
        folded.plot([0.32, 1.68], [coords[i - 1, 1]] * 2,
                    color="#526779", lw=1.8, ls=":", zorder=2)
    for i, (letter, (x, y)) in enumerate(zip(sequence, coords), start=1):
        if i <= 4:
            dx, dy = -0.48, 0
        elif i >= 9:
            dx, dy = 0.48, 0
        else:
            dx, dy = 0, 0.42
        base(folded, x, y, letter, i, dx, dy)
    folded.text(0, -0.5, "5′", ha="center", fontsize=13)
    folded.text(2, -0.5, "3′", ha="center", fontsize=13)
    for x, start, end in [(-0.84, 0.3, 2.5), (2.85, 2.5, 0.3)]:
        folded.annotate("", (x, end), (x, start),
                        arrowprops={"arrowstyle": "->", "color": "#176b92", "lw": 1.8})
    fig.text(0.5, 0.12, "Pairs: 1–12 (G–C), 2–11 (C–G), 3–10 (A–U), 4–9 (U–A)",
             ha="center", fontsize=11)
    fig.text(0.5, 0.065, "Solid line: backbone     Dotted lines: base pairs     Numbers: sequence positions",
             ha="center", fontsize=10, color="#526779")
    fig.text(0.5, 0.025, "Schematic pairing pattern; not a measured shape or a folding prediction",
             ha="center", fontsize=10, color="#526779")
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{sequence}: {len(sequence)} nucleotides, {len(pairs)} pairs, loop positions 5–8")


if __name__ == "__main__":
    main()
