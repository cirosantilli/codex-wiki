"""Draw an original sequence example under a simplified trypsin cleavage rule."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    sequence = "AGKARPKAGRAK"
    cuts = [i + 1 for i, aa in enumerate(sequence[:-1])
            if aa in "KR" and sequence[i + 1] != "P"]
    edges = [0, *cuts, len(sequence)]
    fragments = [sequence[a:b] for a, b in zip(edges, edges[1:])]
    assert cuts == [3, 7, 10]
    assert fragments == ["AGK", "ARPK", "AGR", "AK"]

    fig, ax = plt.subplots(figsize=(10, 5), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.98, bottom=0.06, top=0.90)
    ax.set(xlim=(-0.7, 11.9), ylim=(-2.6, 2.1))
    ax.axis("off")
    fig.suptitle("Trypsin: selected bonds, conserved residue order", fontsize=17)
    ax.text(-0.5, 1.65, "N → C direction  •  constructed sequence", fontsize=12)

    for i, aa in enumerate(sequence):
        basic = aa in "KR"
        color = "#e6f1fa" if basic else "#fff1dc" if aa == "P" else "#f0f2f4"
        ax.add_patch(FancyBboxPatch((i - 0.32, 0.62), 0.64, 0.64,
                                   boxstyle="round,pad=0.03", facecolor=color,
                                   edgecolor="#496173", linewidth=1.2))
        ax.text(i, 0.94, aa, fontsize=19, ha="center", va="center", weight="bold")
        ax.text(i, 0.40, str(i + 1), fontsize=10, ha="center", color="#495664")
        if basic:
            ax.text(i + 0.28, 1.29, "+", fontsize=16, color="#236c9a", weight="bold")
        if i < len(sequence) - 1:
            ax.plot([i + 0.35, i + 0.65], [0.94, 0.94], color="#66717b", lw=1.8)

    for cut in cuts:
        x = cut - 0.5
        ax.annotate("", xy=(x, 0.92), xytext=(x, 1.62),
                    arrowprops={"arrowstyle": "->", "color": "#b22936", "lw": 2})
    ax.annotate("R–P: retained\nin this rule", xy=(4.5, 0.85), xytext=(4.45, -0.10),
                ha="center", va="top", fontsize=11, color="#936011",
                arrowprops={"arrowstyle": "->", "color": "#936011"})
    ax.annotate("Terminal K:\nno following bond", xy=(11.25, 0.79), xytext=(10.6, -0.10),
                ha="center", va="top", fontsize=11, color="#495664",
                arrowprops={"arrowstyle": "->", "color": "#495664"})

    colors = ["#dcebf8", "#e2f0e3", "#fff0cf", "#eadff4"]
    for a, b, fragment, color in zip(edges, edges[1:], fragments, colors):
        ax.add_patch(FancyBboxPatch((a - 0.32, -1.46), b - a - 0.36, 0.50,
                                   boxstyle="round,pad=0.03", facecolor=color,
                                   edgecolor="#52626e"))
        ax.text((a + b - 1) / 2, -1.21, fragment, fontsize=17, ha="center", va="center")
        ax.text((a + b - 1) / 2, -1.78, f"{len(fragment)} residues", fontsize=11, ha="center")

    ax.text(-0.5, -2.15, "3 cuts → 4 fragments    •    3 + 4 + 3 + 2 = 12 residues", fontsize=13)
    ax.text(-0.5, -2.48, "+ marks a predominantly positive side chain near neutral pH, not total fragment charge.",
            fontsize=10, color="#495664")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
