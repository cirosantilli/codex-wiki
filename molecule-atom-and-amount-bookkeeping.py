"""Original particle bookkeeping; run from _media, Python 3.14 / matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(9, 5), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 5.5))
    ax.axis("off")
    ax.text(5, 5.15, "One sample, three different counts", ha="center", fontsize=18)
    for x, y in [(0.95, 3.45), (2.8, 3.45), (0.95, 1.9), (2.8, 1.9)]:
        ax.add_patch(FancyBboxPatch((x - 0.7, y - 0.7), 1.4, 1.35, boxstyle="round,pad=0.05", fill=False, edgecolor="#9bb3cc", ls="--"))
        pts = [(x - 0.43, y - 0.2, "H", "#e8edf3"), (x, y + 0.2, "O", "#f3ada9"), (x + 0.43, y - 0.2, "H", "#e8edf3")]
        ax.plot([pts[0][0], pts[1][0], pts[2][0]], [pts[0][1], pts[1][1], pts[2][1]], color="#465166", lw=3)
        for xx, yy, text, color in pts:
            ax.add_patch(Circle((xx, yy), 0.2, facecolor=color, edgecolor="#253348", zorder=3))
            ax.text(xx, yy, text, ha="center", va="center", fontsize=12, zorder=4)
    ax.text(1.85, 0.85, r"4 H$_2$O molecules", ha="center", fontsize=14)
    labels = [(4.05, r"Molecules: $N=4$", "Count each dashed group once"),
              (2.65, r"Constituent atoms: $2N+N=12$", "8 hydrogen + 4 oxygen; still bound in water"),
              (1.25, r"Amount of water: $n=4/N_{\mathrm{A}}$", r"$\approx 6.6422\times10^{-24}$ mol of H$_2$O")]
    for y, heading, note in labels:
        ax.annotate("", xy=(4.65, y), xytext=(3.65, 2.8), arrowprops={"arrowstyle": "->", "color": "#557a9e", "lw": 1.8})
        ax.text(4.9, y + 0.16, heading, fontsize=14, va="center")
        ax.text(4.9, y - 0.26, note, fontsize=11, va="center", color="#465166")
    ax.text(5, 0.22, r"Specify the entity: amount of H atoms = $2n$; amount of O atoms = $n$", ha="center", fontsize=12)
    fig.text(0.5, 0.025, "Original inventory cartoon • not a photograph, measured structure, or dissociation process", ha="center", fontsize=10, color="#465166")
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.09, top=0.97)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
