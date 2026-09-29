"""Draw receptor activation cartoons; write the matching PNG to the CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Positions are explanatory, not atomic coordinates or measured distances.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle


BLUE = "#216a94"
GREEN = "#287c61"
ORANGE = "#b34f18"


def box(ax, x, y, text, color=BLUE, width=1.35, height=0.9):
    ax.add_patch(FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                               boxstyle="round,pad=0.05", linewidth=1.7,
                               edgecolor=color, facecolor="white", zorder=4))
    ax.text(x, y, text, ha="center", va="center", fontsize=10, color=color, zorder=5)


def arrow(ax, start, end, color=ORANGE, curved=False):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "color": color,
                "lw": 1.8, "connectionstyle": "arc3,rad=0.3" if curved else "arc3"})


def base(ax, title):
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.axis("off")
    ax.set_title(title, loc="left", fontsize=12, pad=8, weight="bold")
    ax.add_patch(Rectangle((0.2, 4.8), 9.6, 0.55, color="#e6e9ec", zorder=0))
    ax.text(0.3, 5.7, "outside", fontsize=9, color="#666666")
    ax.text(0.3, 4.1, "cytosol", fontsize=9, color="#666666")


def ligand(ax, x, y, text):
    ax.add_patch(Ellipse((x, y), 1.25, 0.65, facecolor="#fce7d8", edgecolor=ORANGE, zorder=5))
    ax.text(x, y, text, ha="center", va="center", fontsize=9, color=ORANGE, zorder=6)


def egfr(ax, active):
    xs = (4.0, 5.5) if active else (3.0, 7.0)
    for i, x in enumerate(xs):
        color = (BLUE, GREEN)[i]
        ax.plot([x, x], [2.1, 7.2], color=color, lw=3, zorder=2)
        ax.add_patch(Ellipse((x, 7.2), 1.6, 2.1, facecolor="white", edgecolor=color, lw=2, zorder=3))
        ky = (3.5, 2.9)[i] if active else 3.3
        box(ax, x, ky, "kinase", color)
        ax.plot([x, x + 0.55, x + 0.25], [ky - 0.5, 1.8, 1.0 if active else 1.65], color=color, lw=2)
        if active:
            ligand(ax, x + (-1 if i == 0 else 1), 7.7, "EGF")
            ax.add_patch(Circle((x + 0.4, 1.6), 0.21, facecolor=ORANGE, edgecolor="white", zorder=5))
    if active:
        arrow(ax, (4.7, 3.5), (5.1, 3.1), BLUE)
        ax.text(7.1, 3.9, "asymmetric\nkinase contact", ha="center", fontsize=10)
        arrow(ax, (6.5, 3.5), (5.1, 3.3), BLUE)
        box(ax, 8.1, 1.6, "SH2", ORANGE, 1.2, 0.8)
        ax.plot([5.9, 7.45], [1.6, 1.6], color=ORANGE, ls="--", lw=1.5)
        ax.text(7.8, 0.55, "recruitment to pY", ha="center", fontsize=10)
        arrow(ax, (5.0, 2.5), (4.4, 1.8), curved=True)
        ax.text(3.0, 0.15, "partner-tail phosphorylation", fontsize=9, ha="center", color=ORANGE)
    else:
        ax.text(5, 0.45, "Illustrative separated chains; inactive\npreassociated receptors can also occur.", ha="center", fontsize=10)
    ax.text(5, 9.15, "one membrane-spanning chain per receptor", ha="center", fontsize=10)


def insulin_receptor(ax, active):
    xs = (4.1, 5.9) if active else (3.1, 6.9)
    for i, x in enumerate(xs):
        color = (BLUE, GREEN)[i]
        ax.plot([x, x], [2.1, 7.0], color=color, lw=3, zorder=2)
        box(ax, x, 7.25, r"$\alpha$", color, 1.6, 1.2)
        box(ax, x, 3.3, "kinase", color)
        ax.text(x + (-0.95 if i == 0 else 0.95), 4.55, r"$\beta$", ha="center", fontsize=12, color=color)
        ax.text(x, 6.2, "S–S", fontsize=9, ha="center", bbox={"facecolor": "white", "edgecolor": "none", "pad": 1}, zorder=6)
        if active:
            ax.add_patch(Circle((x + 0.6, 3.1), 0.21, facecolor=ORANGE, edgecolor="white", zorder=5))
    ax.plot(xs, [8.0, 8.0], color="#666666", lw=1.7)
    ax.text(5, 8.45, "S–S: covalent links already present", ha="center", fontsize=10)
    if active:
        ligand(ax, 5, 9.25, "insulin")
        arrow(ax, (4.5, 2.65), (5.5, 2.65), curved=True)
        arrow(ax, (5.5, 3.9), (4.5, 3.9), curved=True)
        ax.text(5, 1.1, "rearrangement permits partner\nactivation-loop phosphorylation", ha="center", fontsize=10)
    else:
        ax.text(5, 1.1, "preassembled receptor;\ndimer formation alone is insufficient", ha="center", fontsize=10)


def main():
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 8.1))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.03, right=0.98, top=0.87, bottom=0.07, hspace=0.36, wspace=0.10)
    for ax, title in zip(axes.flat, ["EGFR: before EGF", "EGFR: EGF stabilizes an active dimer",
                                    "Insulin receptor: before insulin", "Insulin receptor: after insulin"]):
        base(ax, title)
    egfr(axes[0, 0], False)
    egfr(axes[0, 1], True)
    insulin_receptor(axes[1, 0], False)
    insulin_receptor(axes[1, 1], True)
    fig.suptitle("Ligand recognition outside, kinase activity inside", y=0.98, fontsize=16)
    fig.text(0.5, 0.925, "Different activation mechanisms; orange dots denote phosphorylated tyrosine sites (pY)", ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Original topology cartoons: shapes, ligand counts and spacings do not specify atomic structures or stoichiometry.", ha="center", fontsize=10)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(output.name)


if __name__ == "__main__":
    main()
