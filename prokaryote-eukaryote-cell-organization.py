"""Original cell cross-sections; writes basename.png in the working directory.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Schematics, not micrographs: positions, counts and relative sizes are illustrative.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch
import numpy as np


BLUE = "#216b91"
ORANGE = "#b45b12"
PURPLE = "#684593"
GREEN = "#367759"


def label(ax, text, position, target, color="#29313b"):
    ax.annotate(text, xy=target, xytext=position, ha="center", va="center",
                fontsize=10.5, color=color,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 1.2,
                            "shrinkA": 5, "shrinkB": 3})


def mitochondrion(ax, x, y):
    ax.add_patch(Ellipse((x, y), 1.35, 0.62, facecolor="#ecf5ee",
                         edgecolor=GREEN, lw=2))
    # A folded inner membrane is shown schematically, not as structural data.
    ax.plot(x + np.array([-.48, -.3, -.12, .04, .2, .37, .48]),
            y + np.array([0, .16, -.16, .16, -.16, .14, 0]), color=GREEN, lw=1.4)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 6.6))
    fig.subplots_adjust(left=.025, right=.975, top=.80, bottom=.15, wspace=.10)
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set(xlim=(0, 10), ylim=(0, 8), aspect="equal")
        ax.set_facecolor("white")
        ax.axis("off")

    ax = axes[0]
    ax.set_title("Prokaryotic: Escherichia coli", fontsize=13, pad=13)
    ax.add_patch(FancyBboxPatch((1.65, 2.6), 6.7, 3.6,
                               boxstyle="round,pad=0,rounding_size=1.75",
                               facecolor="#f5eee1", edgecolor="#958363", lw=3))
    ax.add_patch(FancyBboxPatch((1.85, 2.8), 6.3, 3.2,
                               boxstyle="round,pad=0,rounding_size=1.55",
                               facecolor="#edf5fa", edgecolor=BLUE, lw=2))
    ax.add_patch(Ellipse((5, 4.4), 3.0, 1.7, fill=False, edgecolor=ORANGE,
                         lw=1, linestyle=(0, (3, 3))))
    t = np.linspace(0, 2 * np.pi, 361)
    x = 5 + 1.18 * np.cos(t) + .12 * np.sin(7 * t)
    y = 4.4 + .55 * np.sin(t) + .09 * np.cos(6 * t)
    assert np.allclose([x[0], y[0]], [x[-1], y[-1]])
    ax.plot(x, y, color=ORANGE, lw=2)
    points = np.array([(2.8, 4.9), (3.0, 3.8), (4.0, 5.6),
                       (6.5, 5.5), (7.1, 4.9), (6.7, 3.4), (4.2, 3.2)])
    ax.scatter(points[:, 0], points[:, 1], s=19, color=PURPLE, zorder=3)
    label(ax, "Cytoplasm", (1.6, 7.25), (3.15, 5.45), BLUE)
    label(ax, "Nucleoid region\n(no surrounding membrane)", (5.2, 7.25), (5, 5.25), ORANGE)
    label(ax, "Ribosomes", (8.4, 6.8), (7.1, 4.9), PURPLE)
    label(ax, "Cell membrane", (2.0, 1.45), (2.75, 3.0), BLUE)
    label(ax, "Circular chromosome\nDNA in this example", (5.3, .65), (5.1, 3.92), ORANGE)
    label(ax, "Cell wall", (8.5, 1.6), (7.6, 2.85), "#796b52")

    ax = axes[1]
    ax.set_title("Eukaryotic: nucleated animal cell", fontsize=13, pad=13)
    ax.add_patch(Ellipse((5, 4.4), 6.6, 4.2, facecolor="#edf5fa",
                         edgecolor=BLUE, lw=2))
    for radius in (.94, .84):
        ax.add_patch(Circle((5, 5.0), radius, facecolor="#fff0df",
                            edgecolor=ORANGE, lw=1.5))
    for offset in (-.32, 0, .32):
        x = np.linspace(4.50, 5.5, 80)
        y = 5 + offset + .10 * np.sin(13 * (x - 4.5))
        ax.plot(x, y, color=ORANGE, lw=1.7)
    mitochondrion(ax, 3.5, 3.4)
    mitochondrion(ax, 6.55, 3.35)
    points = np.array([(2.7, 4.7), (3.3, 5.4), (6.7, 5.3),
                       (7.1, 4.6), (6.3, 4.1), (4.7, 2.8)])
    assert np.all(np.linalg.norm(points - [5, 5], axis=1) > .94)
    ax.scatter(points[:, 0], points[:, 1], s=19, color=PURPLE, zorder=3)
    label(ax, "Cytoplasm", (1.5, 7.2), (3, 4.2), BLUE)
    label(ax, "Nuclear envelope\n(two membranes)", (5.0, 7.35), (5.0, 5.94), ORANGE)
    label(ax, "Ribosomes\noutside nucleus", (8.4, 6.85), (7.1, 4.6), PURPLE)
    label(ax, "Cell membrane", (1.9, 1.35), (2.7, 2.9), BLUE)
    label(ax, "Nucleus:\nlinear chromosome DNA", (5, .55), (5.0, 4.8), ORANGE)
    label(ax, "Mitochondrion", (8.2, 1.6), (6.55, 3.35), GREEN)

    fig.suptitle("Same cellular essentials, different compartmentalization", fontsize=15, y=.97)
    fig.text(.5, .91, "Illustrative cross-sections • not micrographs • not at exact relative scale",
             ha="center", fontsize=11, color="#4d5661")
    fig.text(.5, .08, "Simplified E. coli envelope: outer membrane omitted. Many other cell structures are omitted.",
             ha="center", fontsize=9.5, color="#4d5661")
    fig.text(.5, .04, "Colors identify components; positions, shapes and counts are illustrative.",
             ha="center", fontsize=9.5, color="#4d5661")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1200 × 792 pixels")


if __name__ == "__main__":
    main()
