"""Original cofactor/ATP recycling schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; writes glycolysis-nad-regeneration.png in the working directory.
Process boxes group transformations; arrows are not anatomical compartments.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(11, 7.3), dpi=100, facecolor="white")
    ax = fig.add_axes([0.025, 0.035, 0.95, 0.93])
    ax.set(xlim=(0, 11), ylim=(0, 7.3))
    ax.axis("off")
    blue, green, orange = "#256b93", "#23784f", "#a35713"

    def box(x, y, w, h, text, color, fill="white"):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                     edgecolor=color, linewidth=1.5, facecolor=fill))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center")

    def arrow(start, end, color=blue):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "lw": 1.8, "color": color})

    ax.text(5.5, 7.02, "Glycolysis can continue only if its carriers return",
            ha="center", fontsize=16, weight="bold")
    box(0.6, 5.30, 1.6, 1.0, "2 NAD⁺\noxidized", blue, "#edf5fa")
    box(8.8, 5.30, 1.6, 1.0, "2 NADH\nreduced", blue, "#edf5fa")
    arrow((2.35, 5.80), (8.65, 5.80))
    ax.text(5.5, 6.20, "Glycolysis: oxidation of carbon substrates", ha="center")
    ax.text(5.5, 5.94, "per glucose", ha="center", fontsize=10)
    ax.text(5.5, 5.44, "4 electrons transferred in total; no direct O₂ consumption",
            ha="center", fontsize=11)
    box(2.7, 3.84, 5.6, 0.80, "Fermentation\nExample: 2 pyruvate → 2 lactate", green)
    box(2.7, 2.60, 5.6, 0.88, "Respiratory oxidation via electron transport\nAerobic case: O₂ is the final acceptor", green)
    ax.plot([9.6, 9.6, 8.5], [5.18, 4.25, 4.25], color=green, lw=1.5)
    ax.plot([9.6, 9.6, 8.5], [4.25, 3.04, 3.04], color=green, lw=1.5)
    arrow((8.53, 4.25), (8.40, 4.25), green)
    arrow((8.53, 3.04), (8.40, 3.04), green)
    ax.plot([2.56, 1.4, 1.4], [4.25, 4.25, 5.02], color=green, lw=1.5)
    ax.plot([2.56, 1.4, 1.4], [3.04, 3.04, 4.25], color=green, lw=1.5)
    arrow((1.4, 5.02), (1.4, 5.18), green)
    ax.text(5.5, 3.60, "Alternative regeneration routes", ha="center", fontsize=10, color=green)
    ax.text(5.5, 2.18, "Finite NAD⁺ without regeneration → limited glucose conversion",
            ha="center", color=blue, fontsize=11)
    box(0.7, 0.48, 2.4, 0.84, "2 ADP + 2 Pᵢ", orange)
    box(7.9, 0.48, 2.4, 0.84, "2 ATP (net)", orange)
    arrow((3.25, 1.02), (7.74, 1.02), orange)
    ax.text(5.5, 1.48, "Glycolysis per glucose", ha="center", color=orange)
    arrow((7.74, 0.58), (3.25, 0.58), orange)
    ax.text(5.5, 0.18, "ATP use + water → ADP + Pᵢ", ha="center", color=orange, fontsize=11)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white",
                transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
