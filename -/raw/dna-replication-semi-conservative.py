"""Original DNA ancestry diagram; Python 3.14, repository Matplotlib.

Build: make _media/dna-replication-semi-conservative.png
Writes an opaque white, same-basename PNG in the current directory.
"""

from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


@dataclass(frozen=True)
class Strand:
    label: str
    sequence: str
    born: int


def daughters(duplex, generation, first_label):
    top, bottom = duplex
    complement = str.maketrans("ATGC", "TACG")
    return [(top, Strand(f"N{first_label}", top.sequence.translate(complement), generation)),
            (Strand(f"N{first_label + 1}", bottom.sequence.translate(complement), generation), bottom)]


def lineage():
    original = (Strand("O1", "ATGCC", 0), Strand("O2", "TACGG", 0))
    first = daughters(original, 1, 1)
    second = daughters(first[0], 2, 3) + daughters(first[1], 2, 5)
    stages = [[original], first, second]
    for generation, stage in enumerate(stages):
        assert len(stage) == 2 ** generation
        assert sum(s.born == 0 for d in stage for s in d) == 2
        assert len({s.label for d in stage for s in d}) == 2 ** (generation + 1)
        for top, bottom in stage:
            assert top.sequence == "ATGCC" and bottom.sequence == "TACGG"
        if generation:
            assert all(sum(s.born < generation for s in d) == 1 for d in stage)
    assert sum(any(s.born == 0 for s in d) for d in second) == 2
    return stages


def main():
    stages = lineage()
    colors = {"O1": "#1766ac", "O2": "#7a429a", 1: "#16805d", 2: "#c46a18"}
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(10.2, 6.6))
    fig.subplots_adjust(left=0.035, right=0.985, bottom=0.035, top=0.91)
    ax.set(xlim=(-0.5, 10.25), ylim=(-0.8, 7.8))
    ax.axis("off")
    fig.suptitle("DNA replication: each daughter keeps one parental strand", fontsize=15)
    xs = [0.0, 3.7, 7.4]
    ys = [[4.0], [5.45, 2.65], [6.15, 4.75, 3.35, 1.95]]
    width = 2.0
    for generation in range(2):
        for i, y in enumerate(ys[generation]):
            for target in ys[generation + 1][2 * i:2 * i + 2]:
                ax.annotate("", (xs[generation + 1] - 0.35, target),
                            (xs[generation] + width + 0.35, y),
                            arrowprops={"arrowstyle": "->", "lw": 1.2, "color": "#a2adb5"})
    for generation, stage in enumerate(stages):
        x = xs[generation]
        ax.text(x + width / 2, 7.4, ["Before copying", "After round 1", "After round 2"][generation],
                ha="center", fontsize=13, weight="bold")
        ax.text(x + width / 2, 7.03, f"{len(stage)} duplex{'es' if len(stage) != 1 else ''}", ha="center")
        for i, (top, bottom) in enumerate(stage):
            y = ys[generation][i]
            for j in range(5):
                ax.plot([x + 0.25 + j * 0.375] * 2, [y - 0.25, y + 0.25],
                        color="#d3d9dc", lw=1, zorder=1)
            for offset, strand, left, right in [(0.25, top, "5′", "3′"),
                                                 (-0.25, bottom, "3′", "5′")]:
                color = colors.get(strand.label, colors.get(strand.born))
                ax.plot([x, x + width], [y + offset] * 2, color=color, lw=4, zorder=2)
                ax.text(x + width / 2, y + offset, "  ".join(strand.sequence),
                        ha="center", va="center", family="monospace", fontsize=12,
                        bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.0}, zorder=3)
                ax.text(x - 0.12, y + offset, left, ha="right", va="center", fontsize=10)
                ax.text(x + width + 0.12, y + offset, right, ha="left", va="center", fontsize=10)
                ax.text(x + width / 2, y + offset + (0.30 if offset > 0 else -0.30),
                        strand.label, ha="center", va="center", color=color, fontsize=10)
        original_duplexes = sum(any(s.born == 0 for s in d) for d in stage)
        ax.text(x + width / 2, 0.66, f"{original_duplexes}/{len(stage)} duplexes\ncontain an original strand",
                ha="center", fontsize=10, linespacing=1.4)
    legend = [("#1766ac", "O1: original"), ("#7a429a", "O2: original"),
              ("#16805d", "N1–N2: made in round 1"), ("#c46a18", "N3–N6: made in round 2")]
    for x, (color, label) in zip([-0.1, 2.3, 4.65, 7.7], legend):
        ax.plot([x, x + 0.22], [0.22, 0.22], color=color, lw=4)
        ax.text(x + 0.32, 0.22, label, va="center", fontsize=9)
    ax.text(4.8, -0.56, "After two rounds: 8 strands = 2 original + 2 from round 1 + 4 from round 2.\n"
            "Complete, error-free copying; flattened ancestry schematic, not a replication fork.",
            ha="center", fontsize=10, color="#475569", linespacing=1.5)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)
    print("Duplexes: 1, 2, 4; original strands: 2, 2, 2; round-2 strand ages: 2/2/4.")


if __name__ == "__main__":
    main()
