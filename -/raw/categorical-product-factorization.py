"""Explicit pairing map and projection equations; write the PNG to cwd."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    source = ["u", "v", "w"]
    first = {"u": 0, "v": 1, "w": 1}
    second = {"u": "a", "v": "b", "w": "a"}
    pairs = [(a, b) for a in [0, 1] for b in ["a", "b", "c"]]
    pairing = {x: (first[x], second[x]) for x in source}
    assert all(pairing[x][0] == first[x] and pairing[x][1] == second[x]
               for x in source)
    colors = ["#176997", "#b95f22", "#43804d"]
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2), dpi=120,
                             gridspec_kw={"width_ratios": [1.1, 1]})
    ax = axes[0]
    pair_positions = {pair: 5 - i for i, pair in enumerate(pairs)}
    for i, x in enumerate(source):
        y = 4 - 1.5 * i
        ax.text(0, y, x, ha="center", va="center", fontsize=15,
                bbox={"boxstyle": "circle", "fc": "white", "ec": colors[i]})
        ax.annotate("", xy=(1.9, pair_positions[pairing[x]]), xytext=(0.13, y),
                    arrowprops={"arrowstyle": "-|>", "color": colors[i],
                                "lw": 2, "mutation_scale": 16})
    for pair, y in pair_positions.items():
        used = pair in pairing.values()
        ax.text(2.15, y, f"({pair[0]}, {pair[1]})", ha="center", va="center",
                fontsize=13, color="#222222" if used else "#879099",
                bbox={"boxstyle": "round,pad=0.3", "fc": "#f1f5f8",
                      "ec": "#b6c1cc"})
    ax.text(0, 5.75, "X", ha="center", fontsize=14)
    ax.text(2.15, 5.75, r"$A\times B$", ha="center", fontsize=14)
    ax.text(1.05, 5.05, "unique h", ha="center", fontsize=12)
    ax.set_xlim(-0.4, 2.7)
    ax.set_ylim(-0.65, 6.2)
    ax.axis("off")
    ax.set_title("Pair the two specified outputs", fontsize=13, pad=14)
    ax = axes[1]
    positions = {"X": (0.5, 1), "P": (0.5, 0.45),
                 "A": (0.06, 0.05), "B": (0.94, 0.05)}
    for name, position in positions.items():
        label = r"$P=A\times B$" if name == "P" else name
        ax.text(*position, label, ha="center", va="center", fontsize=14,
                bbox={"boxstyle": "round,pad=0.3", "fc": "#f1f5f8",
                      "ec": "#b6c1cc"}, zorder=5)
    for start, end, label, point, color in [
        ("X", "P", "h", (0.59, 0.72), "#43804d"),
        ("X", "A", "f", (0.17, 0.62), "#176997"),
        ("X", "B", "g", (0.83, 0.62), "#b95f22"),
        ("P", "A", r"$p_A$", (0.23, 0.22), "#176997"),
        ("P", "B", r"$p_B$", (0.77, 0.22), "#b95f22"),
    ]:
        ax.annotate("", xy=positions[end], xytext=positions[start],
                    arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2,
                                "shrinkA": 22, "shrinkB": 22,
                                "mutation_scale": 18})
        ax.text(*point, label, fontsize=13, ha="center", color=color,
                bbox={"fc": "white", "ec": "none", "pad": 1})
    ax.text(0.5, -0.21, r"$p_A\circ h=f$     $p_B\circ h=g$",
            fontsize=14, ha="center")
    ax.set_xlim(-0.15, 1.15)
    ax.set_ylim(-0.32, 1.22)
    ax.axis("off")
    ax.set_title("Both projection equations must hold", fontsize=13, pad=14)
    fig.suptitle("A product combines maps without extra choices", fontsize=16)
    fig.subplots_adjust(top=0.8, bottom=0.08, left=0.025, right=0.975, wspace=0.15)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
