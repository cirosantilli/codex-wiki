"""Original chemical-synapse schematic; writes basename.png in the CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Mechanisms and positions are illustrative, not measured or drawn to scale.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, Arc

INK = "#243446"
BLUE = "#23779a"
ORANGE = "#ba5418"
PURPLE = "#7950a1"


def arrow(ax, start, end, color=INK, curve=0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                               mutation_scale=14, lw=1.7, color=color,
                               connectionstyle=f"arc3,rad={curve}"))


def label(ax, text, target, position, ha="center"):
    ax.annotate(text, xy=target, xytext=position, ha=ha, va="center",
                color=INK, fontsize=10,
                arrowprops={"arrowstyle": "-", "lw": 1, "color": INK})


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, (ax, notes) = plt.subplots(1, 2, figsize=(10.8, 6.6),
                                   gridspec_kw={"width_ratios": [2.1, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Chemical synapse: release, recognition and current", fontsize=15, y=.965)
    ax.set(xlim=(0, 10), ylim=(0, 7))
    ax.set_facecolor("white")
    ax.axis("off")
    ax.add_patch(Rectangle((0, 4.45), 10, 2.55, fc="#edf5fa", ec="none"))
    ax.add_patch(Rectangle((0, 0), 10, 2.65, fc="#f2edf8", ec="none"))
    for y, color in [(4.45, BLUE), (2.65, PURPLE)]:
        ax.add_patch(Rectangle((0, y-.07), 10, .14, fc=color, ec=color))
    ax.text(.2, 6.93, "Presynaptic terminal", color=BLUE, weight="bold", va="top")
    ax.text(.2, .2, "Postsynaptic cell", color=PURPLE, weight="bold")
    ax.text(.2, 3.7, "Synaptic\ncleft", va="center", color=INK)

    ax.plot([.6, 1.1, 1.25, 1.4, 1.55, 1.8],
            [5.45, 5.45, 5.85, 5.2, 5.45, 5.45], color=ORANGE, lw=2)
    arrow(ax, (1.9, 5.45), (2.5, 5.45), ORANGE)
    ax.text(2.1, 6.12, "1  Action potential\nopens calcium channels", ha="center", color=ORANGE)
    # An open calcium channel through the sending membrane.
    ax.add_patch(Rectangle((2.25, 4.18), .5, .54, fc="white", ec=BLUE, lw=2))
    ax.plot([2.5, 2.5], [4.15, 4.75], color="white", lw=4)
    arrow(ax, (2.5, 3.6), (2.5, 5.05), BLUE)
    ax.text(1.75, 3.25, r"Ca$^{2+}$ enters", color=BLUE)
    for x, y in [(2.25, 3.7), (2.9, 3.85), (2.2, 4.95), (2.75, 5.12)]:
        ax.add_patch(Circle((x, y), .065, fc=BLUE, ec="none"))
    arrow(ax, (3, 5.05), (4.85, 4.94), BLUE)
    ax.text(4.2, 5.32, "Local calcium signal", ha="center", color=BLUE, fontsize=9)

    for x, y in [(5.3, 5.9), (6.55, 5.85)]:
        ax.add_patch(Circle((x, y), .38, fc="white", ec=BLUE, lw=1.8))
        for dx, dy in [(-.12, -.08), (.13, -.1), (0, .14)]:
            ax.add_patch(Circle((x+dx, y+dy), .055, fc=ORANGE, ec="none"))
    label(ax, "Filled synaptic vesicle", (6.6, 6.1), (7.65, 6.55))
    # Fusion pore joins vesicle and membrane; transmitter leaves through it.
    ax.plot([5.27, 5.73], [4.45, 4.45], color="white", lw=7)
    ax.add_patch(Arc((5.5, 4.72), .7, .6, theta1=-45, theta2=225, color=BLUE, lw=2))
    for dx, dy in [(-.12, 0), (.12, 0), (0, .16)]:
        ax.add_patch(Circle((5.5+dx, 4.72+dy), .055, fc=ORANGE, ec="none"))
    arrow(ax, (5.5, 4.65), (5.5, 3.65), ORANGE)
    label(ax, "2  Fusion / exocytosis", (5.85, 4.6), (7.45, 4.85))
    for x, y in [(5.22, 4), (5.7, 3.86), (5.05, 3.5), (5.5, 3.24), (5.9, 3.35)]:
        ax.add_patch(Circle((x, y), .065, fc=ORANGE, ec="none"))
    label(ax, "3  Transmitter diffuses\nand binds receptor", (5.7, 3.4), (7.75, 3.7))

    # Transmitter-gated channel in the receiving membrane, separate from Ca channel.
    for x in [5.1, 5.7]:
        ax.add_patch(Rectangle((x, 2.36), .3, .62, fc="#dac9eb", ec=PURPLE, lw=1.5))
    ax.plot([5.4, 5.7], [2.65, 2.65], color="white", lw=7)
    ax.add_patch(Circle((5.85, 3.02), .065, fc=ORANGE, ec="none"))
    arrow(ax, (5.55, 2.9), (5.55, 1.5), PURPLE)
    label(ax, "Ionotropic receptor\nwith its ion channel", (5.8, 2.6), (7.9, 1.9))
    ax.text(3.85, .8, "4  Conductance changes\nCurrent depends on E − V", color=PURPLE,
            ha="center", fontsize=10)
    ax.text(.25, 1.75, "Ion movement shown\nfor an inward-current\nexample only", fontsize=9, color=INK)

    notes.axis("off")
    notes.set(xlim=(0, 1), ylim=(0, 1))
    notes.text(0, .95, "Two receptor routes", color=INK, weight="bold", fontsize=12)
    notes.text(0, .875, "Ionotropic", color=PURPLE, weight="bold")
    notes.text(0, .83, "Transmitter → receptor/channel\n→ direct channel gating", va="top", linespacing=1.5)
    notes.text(0, .68, "Metabotropic", color=PURPLE, weight="bold")
    notes.text(0, .635, "Transmitter → receptor\n→ intracellular signaling\n→ indirect channel effects", va="top", linespacing=1.5)
    notes.text(0, .44, "Two recovery tasks", color=INK, weight="bold", fontsize=12)
    notes.text(0, .37, "Transmitter clearance", color=ORANGE, weight="bold")
    notes.text(0, .325, "Diffusion away, cellular uptake\nand/or enzymatic breakdown", va="top", linespacing=1.5)
    notes.text(0, .185, "Vesicle recycling", color=BLUE, weight="bold")
    notes.text(0, .14, "Membrane and proteins recovered\nby endocytosis for reuse", va="top", linespacing=1.5)
    fig.text(.5, .025, "Original schematic • typical fast pathway • not to scale • release is probabilistic",
             ha="center", fontsize=9, color=INK)
    fig.subplots_adjust(left=.025, right=.97, top=.88, bottom=.095, wspace=.16)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
