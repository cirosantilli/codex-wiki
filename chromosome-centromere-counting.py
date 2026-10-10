"""Draw an original illustrative 2n=6 chromosome ledger; save in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def chromosome(ax, x, y, length, color, replicated):
    """A paired sister unit has two centromere dots but one chromosome count."""
    offsets = (-0.07, 0.07) if replicated else (0,)
    for offset in offsets:
        ax.plot([x + offset] * 2, [y - length / 2, y + length / 2],
                lw=6, color=color, solid_capstyle="round", zorder=2)
        ax.add_patch(Circle((x + offset, y), 0.035, facecolor="white",
                            edgecolor="#233248", lw=1.4, zorder=3))
    if replicated:
        ax.plot([x - 0.07, x + 0.07], [y, y], color="#233248", lw=2, zorder=4)


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 4, figsize=(13.5, 5.7), dpi=100)
    fig.patch.set_facecolor("white")
    titles = ["G1: before copying", "G2: after S phase",
              "After meiosis I", "After meiosis II"]
    counts = [(6, 6, "2n", "2C"), (6, 12, "2n", "4C"),
              (3, 6, "n", "2C"), (3, 3, "n", "1C")]
    blue, orange = "#167c91", "#bd4b36"
    for stage, (ax, title, (nchr, copies, ploidy, amount)) in enumerate(zip(axes, titles, counts)):
        ax.set(xlim=(0, 2.4), ylim=(-1.35, 3.15))
        ax.set_facecolor("white")
        ax.axis("off")
        ax.set_title(title, fontsize=14, weight="bold", pad=14)
        ax.add_patch(FancyBboxPatch((0.12, 0.12), 2.16, 2.83,
                                   boxstyle="round,pad=0.03", facecolor="#f6f8fa",
                                   edgecolor="#b7c4cf", lw=1.2))
        for row, (label, length) in enumerate(zip("ABD", (0.72, 0.54, 0.36))):
            y = 2.45 - row * 0.84
            ax.text(0.27, y, label, va="center", weight="bold", color="#233248")
            replicated = stage in (1, 2)
            if stage < 2:
                chromosome(ax, 0.95, y, length, blue, replicated)
                chromosome(ax, 1.65, y, length, orange, replicated)
            else:
                chromosome(ax, 1.25, y, length, blue if row != 1 else orange, replicated)
        ax.text(1.2, -0.11, f"{nchr} chromosomes\n{copies} chromatid copies",
                ha="center", va="top", linespacing=1.5, fontsize=13)
        ax.text(1.2, -0.85, f"{ploidy}  |  {amount}", ha="center", fontsize=17,
                color="#233248", weight="bold")
        if stage >= 2:
            ax.text(1.2, -1.17, "One representative product", ha="center", fontsize=10)
    fig.suptitle("Illustrative chromosome bookkeeping: stipulated 2n = 6 (n = 3)",
                 fontsize=18, weight="bold", y=0.97)
    fig.text(0.5, 0.075, "Colors: parental homologs   •   Paired rods: sister chromatids   •   White dots: centromere regions",
             ha="center", fontsize=11)
    fig.text(0.5, 0.032, "Attached sister centromeres count as one chromosome unit. No crossover shown; not measurements.",
             ha="center", fontsize=11, color="#435267")
    fig.subplots_adjust(left=0.035, right=0.985, top=0.85, bottom=0.14, wspace=0.13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
