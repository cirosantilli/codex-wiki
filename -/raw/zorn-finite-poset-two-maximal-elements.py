"""Draw an original finite inclusion poset; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    positions = {"empty": (0, 0), "a": (-1.7, 1.2), "b": (0, 1.2),
                 "c": (1.7, 1.2), "ab": (-1.05, 2.6), "bc": (1.05, 2.6)}
    labels = {"empty": r"$\varnothing$", "a": r"$\{a\}$", "b": r"$\{b\}$",
              "c": r"$\{c\}$", "ab": r"$\{a,b\}$", "bc": r"$\{b,c\}$"}
    edges = [("empty", "a"), ("empty", "b"), ("empty", "c"),
             ("a", "ab"), ("b", "ab"), ("b", "bc"), ("c", "bc")]
    chain_edges = {("empty", "b"), ("b", "ab")}
    for lower, upper in edges:
        x0, y0 = positions[lower]
        x1, y1 = positions[upper]
        ax.plot([x0, x1], [y0, y1], color="#2465aa" if (lower, upper) in chain_edges else "#aeb8c4",
                linewidth=3 if (lower, upper) in chain_edges else 1.8, zorder=1)
    for name, (x, y) in positions.items():
        maximal = name in {"ab", "bc"}
        ax.text(x, y, labels[name], ha="center", va="center", fontsize=17,
                bbox={"boxstyle": "round,pad=0.3", "facecolor": "#fff0d8" if maximal else "white",
                      "edgecolor": "#bd6519" if maximal else "#2465aa" if name in {"empty", "b"} else "#758291",
                      "linewidth": 2}, zorder=3)
    ax.text(0, 3.17, "Two maximal elements; no greatest element", ha="center", fontsize=17, weight="bold")
    ax.text(0, 2.99, "Higher along a path means larger by inclusion", ha="center", fontsize=11, color="#52606e")
    ax.text(2.65, 2.5, "Orange: maximal\nNo larger member in P", va="center", color="#9a4c0e")
    ax.text(2.65, 1.4, "Blue path: a chain\nEvery pair is comparable", va="center", color="#2465aa")
    ax.text(2.65, 0.3, "No member contains\nboth {a} and {c}", va="center", color="#52606e")
    ax.text(0.9, -0.62, r"For $C=\{\varnothing,\{b\}\}$, upper bounds are $\{b\}$, $\{a,b\}$ and $\{b,c\}$.",
            ha="center", fontsize=12)
    ax.set(xlim=(-2.6, 5.2), ylim=(-0.9, 3.5))
    ax.axis("off")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.06, top=0.96)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
