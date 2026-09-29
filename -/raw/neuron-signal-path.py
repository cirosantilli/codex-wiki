"""Original neuron and chemical-synapse schematic; output basename.png in cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Illustrative anatomy and mechanism, not microscopy or a scale drawing.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle


BLUE = "#256f95"
ORANGE = "#ba5418"
INK = "#243446"


def arrow(ax, start, end, color=ORANGE, width=1.8):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=13, color=color, lw=width))


def label(ax, text, target, position, align="center"):
    ax.annotate(text, xy=target, xytext=position, ha=align, va="center",
                fontsize=10, color=INK,
                arrowprops={"arrowstyle": "-", "color": INK, "lw": 1})


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, (neuron, synapse) = plt.subplots(2, 1, figsize=(9.2, 6.3))
    fig.set_facecolor("white")
    for ax in (neuron, synapse):
        ax.set(xlim=(0, 12), ylim=(0, 4.5))
        ax.set_facecolor("white")
        ax.axis("off")

    neuron.set_title("A. A common neuronal plan", loc="left", fontsize=12)
    branches = [
        [(2.95, 2.65), (2.0, 3.3), (1.25, 3.6), (0.7, 4.0)],
        [(2.0, 3.3), (1.9, 3.95), (2.3, 4.2)],
        [(2.9, 2.25), (1.85, 2.15), (1.0, 2.5), (0.5, 2.35)],
        [(1.85, 2.15), (1.1, 1.85), (0.45, 1.75)],
        [(3.0, 1.75), (2.0, 1.2), (1.45, 0.65), (0.65, 0.75)],
        [(2.0, 1.2), (1.45, 1.2), (0.9, 1.3)],
    ]
    for points in branches:
        x, y = zip(*points)
        neuron.plot(x, y, color=BLUE, lw=3, solid_capstyle="round")
    neuron.add_patch(Ellipse((3.5, 2.2), 1.65, 1.9,
                            facecolor="#e7f2f8", edgecolor=BLUE, lw=2.5))
    neuron.add_patch(Circle((3.42, 2.25), 0.32, facecolor="#dccce8",
                           edgecolor="#75628c", lw=1.5))
    neuron.plot([4.22, 5.1, 9.3], [2.2, 2.2, 2.2], color=BLUE, lw=5,
                solid_capstyle="round")
    neuron.plot([4.25, 4.95], [2.2, 2.2], color=ORANGE, lw=6,
                solid_capstyle="round")
    for y in (1.15, 2.2, 3.25):
        neuron.plot([9.3, 10.1, 10.8], [2.2, y, y], color=BLUE, lw=3)
        neuron.add_patch(Ellipse((10.95, y), 0.4, 0.28,
                                facecolor="#e7f2f8", edgecolor=BLUE, lw=2))
    label(neuron, "Dendrites\nreceive inputs", (1.5, 3.5), (0.9, 4.35))
    label(neuron, "Soma\n(cell body)", (3.5, 2.95), (3.65, 4.0))
    label(neuron, "Cell nucleus", (3.42, 2.25), (3.55, 0.45))
    label(neuron, "Axon initial segment\ncommon initiation site", (4.7, 2.2), (5.8, 0.65))
    label(neuron, "Axon\npropagation", (8.3, 2.2), (8.3, 0.65))
    label(neuron, "Axon terminals\noutput at synapses", (10.95, 3.25), (10.4, 4.0))
    arrow(neuron, (5.6, 2.65), (8.8, 2.65))
    neuron.text(7.2, 2.95, "Action potential travels", ha="center", color=ORANGE)
    label(neuron, "Cell membrane", (4.05, 2.85), (5.25, 3.75))

    synapse.set_title("B. Chemical synapse: electrical → chemical → electrical", loc="left", fontsize=12)
    synapse.add_patch(Ellipse((5.5, 3.05), 3.35, 2.5,
                             facecolor="#e7f2f8", edgecolor=BLUE, lw=2.5))
    synapse.add_patch(Rectangle((3.65, 0.05), 3.75, 1.0,
                               facecolor="#f3f0fa", edgecolor="#75628c", lw=2.5))
    for x, y in ((4.8, 3.1), (5.55, 3.5), (6.2, 2.9), (5.5, 2.25)):
        synapse.add_patch(Circle((x, y), 0.22, facecolor="white",
                                edgecolor=BLUE, lw=1.5))
        for dx, dy in ((-0.08, -0.06), (0.07, -0.04), (0, 0.09)):
            synapse.add_patch(Circle((x + dx, y + dy), 0.035, color=ORANGE))
    synapse.add_patch(Rectangle((3.83, 2.72), 0.17, 0.45,
                               facecolor="#71a5bb", edgecolor=BLUE))
    arrow(synapse, (2.95, 2.95), (4.45, 2.95), color=BLUE)
    synapse.text(3.0, 3.23, "Ca²⁺ entry", color=BLUE, ha="center")
    synapse.add_patch(Rectangle((5.32, 0.84), 0.36, 0.4,
                               facecolor="#ddb8a0", edgecolor=ORANGE, lw=1.5))
    for x, y in ((5.4, 1.65), (5.68, 1.52), (5.48, 1.36)):
        synapse.add_patch(Circle((x, y), 0.055, color=ORANGE))
    arrow(synapse, (5.52, 2.04), (5.52, 1.78))
    arrow(synapse, (5.5, 0.85), (5.5, 0.28))
    label(synapse, "1. Arriving action potential\nopens calcium channels", (4.5, 3.75), (1.65, 4.0))
    label(synapse, "Presynaptic terminal", (6.25, 3.95), (9.55, 4.0))
    label(synapse, "2. Vesicles release\nneurotransmitter", (5.5, 2.25), (9.55, 2.75))
    label(synapse, "Synaptic cleft", (5.85, 1.47), (9.55, 1.65))
    label(synapse, "3. Receptor changes\npostsynaptic current", (5.5, 1.06), (1.6, 1.15))
    label(synapse, "Postsynaptic membrane", (7.35, 1.04), (9.55, 0.45))

    fig.suptitle("How a neuron passes a signal", fontsize=15)
    fig.text(0.5, 0.025, "Original schematic • not to scale • signaling routes vary between neurons",
             ha="center", color=INK, fontsize=9)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.90, bottom=0.08, hspace=0.35)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
