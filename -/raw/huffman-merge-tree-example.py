"""Original Huffman tree; save its PNG basename to cwd.

Tested with Python 3.14.4 and Matplotlib 3.10.7 (repository dependencies).
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-mpl python3 ../huffman-merge-tree-example.py
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    probabilities = dict(zip("ABCD", map(Fraction, ("0.4", "0.3", "0.2", "0.1"))))
    codes = {"A": "0", "B": "10", "C": "110", "D": "111"}
    children = {"root": ("A", "BCD"), "BCD": ("B", "CD"), "CD": ("C", "D")}
    weights = probabilities | {"CD": probabilities["C"] + probabilities["D"]}
    weights["BCD"] = probabilities["B"] + weights["CD"]
    weights["root"] = probabilities["A"] + weights["BCD"]
    assert [weights[x] for x in ("CD", "BCD", "root")] == list(map(Fraction, ("0.3", "0.6", "1")))
    assert sum(probabilities[s] * len(codes[s]) for s in codes) == Fraction(19, 10)

    def walk(node, prefix=""):
        if node not in children:
            assert codes[node] == prefix
        else:
            for bit, child in enumerate(children[node]):
                walk(child, prefix + str(bit))

    walk("root")
    positions = {"root": (0.43, 0.91), "A": (0.15, 0.66), "BCD": (0.63, 0.66),
                 "B": (0.43, 0.40), "CD": (0.82, 0.40), "C": (0.71, 0.14), "D": (0.94, 0.14)}
    colors = {"A": "#2d6faa", "B": "#168475", "C": "#b16813", "D": "#9059a0"}
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(8.2, 5.5), layout="constrained", facecolor="white")
    ax.set(xlim=(0, 1.04), ylim=(-0.21, 1.04), facecolor="white")
    ax.axis("off")
    for parent, pair in children.items():
        x, y = positions[parent]
        for bit, child in enumerate(pair):
            xx, yy = positions[child]
            ax.plot([x, xx], [y, yy], color="#526173", linewidth=2, zorder=1)
            ax.text((x + xx) / 2, (y + yy) / 2, str(bit), ha="center", va="center",
                    fontsize=13, color="#182638", bbox={"facecolor": "white", "edgecolor": "none", "pad": 3}, zorder=3)
    for node, (x, y) in positions.items():
        label = f"{node}  {float(weights[node]):.1f}" if node in probabilities else f"{float(weights[node]):.1f}"
        ax.text(x, y, label, ha="center", va="center", fontsize=13,
                color="white" if node in colors else "#172638",
                bbox={"boxstyle": "round,pad=0.5", "facecolor": colors.get(node, "#e2eaf2"),
                      "edgecolor": "white", "linewidth": 1.5}, zorder=4)
    ax.text(0.02, 0.35, "Build upwards:\n1.  D + C = 0.3\n2.  B + CD = 0.6\n3.  A + BCD = 1.0",
            ha="left", va="center", fontsize=11, linespacing=1.65, color="#26384b")
    ax.text(0.52, -0.035, "Code legend:  A = 0     B = 10     C = 110     D = 111", ha="center", fontsize=12)
    ax.text(0.52, -0.145, "Read down from the root; each leaf ends one codeword.", ha="center", fontsize=11, color="#526173")
    ax.set_title("Huffman coding: merge the two smallest current weights", fontsize=14, pad=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
