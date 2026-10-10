"""Generate image-preimage-intersection-asymmetry.png in the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def node(ax, xy, label, color):
    ax.add_patch(Circle(xy, 0.22, facecolor=color, edgecolor="white",
                        linewidth=1.0, zorder=3))
    ax.text(*xy, label, ha="center", va="center", color="white",
            fontsize=14, zorder=4)


def arrow(ax, start, end, color):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16,
                                linewidth=2, color=color, shrinkA=15, shrinkB=15))


def main():
    blue, orange, green = "#2875ad", "#d4652b", "#23815b"
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.6), dpi=120,
                             facecolor="white")
    left, right = axes
    node(left, (0, 2), "a", blue)
    node(left, (0, 0.8), "b", orange)
    node(left, (2.5, 1.4), "0", green)
    arrow(left, (0, 2), (2.5, 1.4), blue)
    arrow(left, (0, 0.8), (2.5, 1.4), orange)
    left.text(-0.1, 2.55, "E = {a}", color=blue, ha="center", fontsize=12)
    left.text(-0.1, 0.20, "F = {b}", color=orange, ha="center", fontsize=12)
    left.text(1.15, -0.55, "E ∩ F = ∅\nf(E ∩ F) = ∅\nf(E) ∩ f(F) = {0}",
              ha="center", fontsize=13, linespacing=1.7)
    left.set_title("Images can merge disjoint inputs", fontsize=14, pad=16)
    node(right, (0, 2), "a", blue)
    node(right, (0, 0.8), "b", blue)
    node(right, (2.5, 1.4), "0", green)
    arrow(right, (0, 2), (2.5, 1.4), blue)
    arrow(right, (0, 0.8), (2.5, 1.4), blue)
    right.text(2.5, 2.20, "U ∩ V = {0}", ha="center", fontsize=12, color=green)
    right.text(1.2, -0.45, "U = {0, 1},   V = {0, 2}\nf⁻¹(U ∩ V) = {a, b}\nf⁻¹(U) ∩ f⁻¹(V) = {a, b}",
               ha="center", fontsize=13, linespacing=1.7)
    right.set_title("Preimages test both conditions on one input", fontsize=14, pad=16)
    for ax in axes:
        ax.set(xlim=(-0.65, 3.25), ylim=(-1.35, 3.05))
        ax.axis("off")
    fig.suptitle("One collision explains the intersection asymmetry",
                 fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.83, bottom=0.13, wspace=0.24)
    fig.text(0.5, 0.04,
             "Same function: f(a) = f(b) = 0, f(c) = 1, f(d) = 2.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "image-preimage-intersection-asymmetry.png",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
