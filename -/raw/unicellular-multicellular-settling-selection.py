"""Original settling workflow and toy conditional-frequency comparison.

Python 3.14 / matplotlib 3.10 / numpy 2.3; run from _media.
Output basename is written to CWD. Toy weights are not experimental data.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np

INK = "#243746"
C_COLOR = "#247ba0"
U_COLOR = "#d28a38"


def tube(ax, x, y):
    ax.add_patch(Rectangle((x, y), 0.14, 0.25, facecolor="#f3f8fa",
                           edgecolor=INK, linewidth=1.5))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans",
                         "text.color": INK, "axes.labelcolor": INK})
    fig = plt.figure(figsize=(10.4, 6.6), dpi=100, facecolor="white")
    fig.suptitle("Transfer favors material that reaches the bottom",
                 fontsize=16, fontweight="bold", y=0.965)
    flow = fig.add_axes([0.03, 0.56, 0.94, 0.32])
    flow.set(xlim=(0, 1), ylim=(0, 1))
    flow.axis("off")
    centers = [0.15, 0.5, 0.85]
    titles = ["1  Grow", "2  Let settle", "3  Transfer bottom fraction"]
    for x, title in zip(centers, titles):
        flow.text(x, 0.99, title, ha="center", va="top", fontsize=12, fontweight="bold")
        tube(flow, x - 0.07, 0.44)
    for x in [0.30, 0.65]:
        flow.add_patch(FancyArrowPatch((x - 0.04, 0.59), (x + 0.06, 0.59),
                                       arrowstyle="->", mutation_scale=18, color=INK))
    # Counts and coordinates illustrate the workflow; none are sampled data.
    for x, y in [(0.11, 0.48), (0.17, 0.54), (0.12, 0.61), (0.18, 0.65), (0.16, 0.47)]:
        flow.add_patch(Circle((x, y), 0.008, facecolor=C_COLOR))
    for x, y in [(0.45, 0.45), (0.48, 0.46), (0.52, 0.45), (0.54, 0.47)]:
        flow.add_patch(Circle((x, y), 0.008, facecolor=C_COLOR))
    flow.add_patch(Rectangle((0.43, 0.44), 0.14, 0.05, facecolor=C_COLOR, alpha=0.16))
    flow.annotate("discard upper liquid", xy=(0.56, 0.64), xytext=(0.62, 0.83),
                  ha="center", fontsize=10, arrowprops={"arrowstyle": "->", "color": INK})
    flow.add_patch(Circle((0.85, 0.46), 0.01, facecolor=C_COLOR))
    labels = ["Culture between daily transfers",
              "Initial protocol: 45 min at 1 g",
              "Bottom 100 µL → fresh medium"]
    for x, label in zip(centers, labels):
        flow.text(x, 0.27, label, ha="center", fontsize=11)
    flow.text(0.5, 0.05, "Qualitative protocol schematic; drawn particle counts are arbitrary",
              ha="center", fontsize=10)

    ax = fig.add_axes([0.27, 0.16, 0.68, 0.27])
    p, s_c, s_u = 0.2, 0.8, 0.1
    after = p * s_c / (p * s_c + (1 - p) * s_u)
    fractions = np.array([p, after, p])
    y = np.array([2, 1, 0])
    ax.barh(y, fractions, height=0.58, color=C_COLOR, label="type C")
    ax.barh(y, 1 - fractions, left=fractions, height=0.58, color=U_COLOR, label="type U")
    for row, frac in zip(y, fractions):
        ax.text(frac / 2, row, f"{100 * frac:.1f}% C", color="white",
                ha="center", va="center", fontweight="bold", fontsize=11)
    ax.set_yticks(y, ["Before transfer", "Unequal transfer", "Equal transfer"])
    ax.set(xlim=(0, 1), xticks=[0, 0.2, 0.4, 0.6, 0.8, 1],
           xlabel="Fraction of equally weighted tracked units")
    ax.set_xticklabels(["0%", "20%", "40%", "60%", "80%", "100%"])
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_title("TOY NUMBERS — not measured yeast frequencies", loc="left",
                 fontsize=12, fontweight="bold", pad=12)
    fig.text(0.5, 0.065, "Unequal: sC = 0.8, sU = 0.1     Equal comparison: sC = sU = 0.1",
             ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Equal unit weights and equal multiplication assumed; cluster and cell frequencies can differ",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
