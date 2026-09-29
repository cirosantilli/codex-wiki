"""Generate matroid-three-vector-independence.png in the working directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, table) = plt.subplots(1, 2, figsize=(9.2, 4.2),
                                  gridspec_kw={"width_ratios": [1, 1.3]})
    vectors = {"a": (1, 0), "b": (0, 1), "c": (1, 1)}
    weights = {"a": 8, "b": 5, "c": 6}
    colors = {"a": "#13734b", "b": "#366ba5", "c": "#9c6a13"}
    for label, vector in vectors.items():
        ax.annotate("", vector, (0, 0),
                    arrowprops={"arrowstyle": "->", "lw": 2.8,
                                "color": colors[label]})
        offset = {"a": (0.03, -0.14), "b": (-0.18, 0.04),
                  "c": (0.02, 0.05)}[label]
        ax.text(vector[0] + offset[0], vector[1] + offset[1],
                f"{label}, w={weights[label]}", color=colors[label])
    ax.set(xlim=(-0.28, 1.45), ylim=(-0.28, 1.45), aspect="equal",
           xticks=[0, 1], yticks=[0, 1], xlabel="First coordinate",
           ylabel="Second coordinate", title="Three labelled vectors")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.2)
    fig.text(0.25, 0.035, r"$v_c=v_a+v_b$: the triple is dependent",
             ha="center", fontsize=11)
    table.set(xlim=(0, 2), ylim=(0, 4.8))
    table.axis("off")
    table.set_title("All eight subsets", pad=12)
    subsets = [(), ("a",), ("b",), ("c",), ("a", "b"),
               ("a", "c"), ("b", "c"), ("a", "b", "c")]
    for index, subset in enumerate(subsets):
        col, row = index % 2, index // 2
        x, y = col + 0.03, 3.78 - row
        independent = len(subset) <= 2
        optimal = subset == ("a", "c")
        box = FancyBboxPatch((x, y), 0.91, 0.82,
                             boxstyle="round,pad=0.015",
                             facecolor="#e9f5ee" if independent else "#fbeceb",
                             edgecolor="#13734b" if optimal else "#b5b5b5",
                             linewidth=2.4 if optimal else 0.8)
        table.add_patch(box)
        label = r"$\varnothing$" if not subset else "{" + ",".join(subset) + "}"
        state = "independent" if independent else "dependent"
        weight = sum(weights[e] for e in subset)
        table.text(x + 0.455, y + 0.58, label, ha="center", fontsize=13)
        table.text(x + 0.455, y + 0.31, state, ha="center", fontsize=10)
        table.text(x + 0.455, y + 0.09, f"weight {weight}", ha="center", fontsize=10)
    table.text(1, -0.28, "Greedy: a (8), c (6), reject b (5)\nBest basis: {a,c}, weight 14",
               ha="center", va="top", color="#13734b", fontsize=11)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.87, bottom=0.18, wspace=0.28)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
