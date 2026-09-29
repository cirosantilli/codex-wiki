"""Original receptor mechanism cartoons; run from _media to write the PNG.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Shapes are conceptual, not molecular structures; arrows carry no timing data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle


BLUE = "#176b9b"
ORANGE = "#ba5a19"
INK = "#213547"
GREEN = "#267659"


def signal(ax, start, end, rad=0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13,
                               lw=1.7, color=ORANGE, linestyle="--",
                               connectionstyle=f"arc3,rad={rad}"))


def label_box(ax, x, y, label, color=GREEN, width=2.15):
    ax.add_patch(FancyBboxPatch((x-width/2, y-0.32), width, 0.64,
                               boxstyle="round,pad=0.06", facecolor="white",
                               edgecolor=color, linewidth=1.6))
    ax.text(x, y, label, ha="center", va="center", fontsize=10.5, color=INK)


def pore(ax, x, ion_y=4.93):
    for dx in (-0.38, 0.16):
        ax.add_patch(FancyBboxPatch((x+dx, 3.58), 0.22, 1.13,
                                   boxstyle="round,pad=0.025", facecolor="#d8eaf5",
                                   edgecolor=BLUE, linewidth=1.6))
    ax.add_patch(Circle((x, ion_y), 0.10, facecolor=BLUE))
    ax.text(x, ion_y+0.24, "+", ha="center", va="center", color=BLUE, fontsize=15)
    ax.add_patch(FancyArrowPatch((x, ion_y-0.15), (x, 3.42),
                               arrowstyle="-|>", mutation_scale=13, lw=2, color=BLUE))


def receptor(ax, x):
    ax.add_patch(FancyBboxPatch((x-0.24, 3.62), 0.48, 1.03,
                               boxstyle="round,pad=0.04", facecolor="#fff1e4",
                               edgecolor=ORANGE, linewidth=1.6))
    ax.add_patch(Circle((x, 5.22), 0.13, facecolor=ORANGE))
    signal(ax, (x, 5.02), (x, 4.72))


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 7.0))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.03, right=0.98, top=0.82, bottom=0.14, wspace=0.12)
    fig.suptitle("Recognition can reach a pore through different routes", fontsize=17,
                 color=INK, y=0.97)
    fig.text(0.5, 0.91, "MECHANISM MODELS • conceptual geometry • no measured timing",
             ha="center", fontsize=11, color=INK)
    for ax in axes:
        ax.set(xlim=(0, 4), ylim=(0, 6))
        ax.axis("off")
        ax.add_patch(Rectangle((0.1, 3.88), 3.8, 0.45, facecolor="#eef0f2",
                               edgecolor="#afb7c0", lw=0.9))
        ax.text(0.14, 4.40, "outside", fontsize=9, color="#52606d")
        ax.text(0.14, 3.68, "inside", fontsize=9, color="#52606d")

    ax = axes[0]
    ax.set_title("Ionotropic\nreceptor and pore in one complex", fontsize=12, color=INK, pad=10)
    pore(ax, 2.58)
    ax.add_patch(Circle((1.16, 5.22), 0.13, facecolor=ORANGE))
    ax.text(1.16, 5.63, "ligand", ha="center", fontsize=10, color=ORANGE)
    signal(ax, (1.28, 5.08), (2.16, 4.48))
    # Bracket unites the binding function and pore; it is not a second relay.
    ax.plot([1.74, 1.74, 3.15, 3.15], [4.73, 3.35, 3.35, 4.73], color=BLUE, lw=1.2)
    ax.text(2.48, 3.02, "binding changes pore gating", ha="center", fontsize=10, color=INK)
    label_box(ax, 2.00, 1.94, "ionic current", color=BLUE, width=2.4)
    ax.text(2.0, 0.62, "No obligatory intracellular relay\nbetween binding and this pore", ha="center",
            fontsize=10.5, linespacing=1.5, color=INK)

    ax = axes[1]
    ax.set_title("Metabotropic: local route\nreceptor and pore are separate", fontsize=12, color=INK, pad=10)
    receptor(ax, 1.16)
    ax.text(1.16, 5.63, "ligand", ha="center", fontsize=10, color=ORANGE)
    pore(ax, 2.95)
    signal(ax, (1.16, 3.51), (1.16, 3.02))
    label_box(ax, 1.16, 2.65, "G protein", width=1.64)
    signal(ax, (2.01, 2.65), (2.73, 3.66), rad=0.18)
    ax.text(3.02, 2.33, "channel", ha="center", fontsize=10, color=BLUE)
    ax.text(2.0, 1.36, "A G-protein component\nregulates the separate pore", ha="center",
            fontsize=10.5, linespacing=1.5, color=INK)
    ax.text(2.0, 0.40, "No obligatory diffusible\nsecond messenger", ha="center",
            fontsize=10.5, linespacing=1.5, color=INK)

    ax = axes[2]
    ax.set_title("Metabotropic: messenger route\nexample using stored calcium", fontsize=12, color=INK, pad=10)
    receptor(ax, 1.04)
    ax.text(1.04, 5.63, "ligand", ha="center", fontsize=10, color=ORANGE)
    pore(ax, 3.10)
    signal(ax, (1.04, 3.51), (1.04, 3.18))
    label_box(ax, 1.04, 2.83, "G protein", width=1.6)
    signal(ax, (1.04, 2.45), (1.04, 2.22))
    label_box(ax, 1.04, 1.85, "enzyme", width=1.6)
    signal(ax, (1.04, 1.46), (1.04, 1.23))
    label_box(ax, 1.04, 0.86, r"$\mathrm{IP}_3$", width=1.6)
    signal(ax, (1.91, 0.86), (2.32, 0.86))
    label_box(ax, 3.04, 0.86, "stored Ca²⁺\nreleased", width=1.28)
    signal(ax, (3.04, 1.23), (3.04, 3.46))
    ax.text(3.63, 2.36, "regulates\nchannel", ha="center", fontsize=9, color=ORANGE)

    fig.text(0.5, 0.070, "Blue solid arrows: possible net positive-ion entry. Orange dashed arrows: signal relay.",
             ha="center", fontsize=10.5, color=INK)
    fig.text(0.5, 0.027, "Ion flow still needs an electrochemical drive; arrows do not imply universal excitation.",
             ha="center", fontsize=10.5, color=INK)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
