"""Draw symbolic phosphate transfer and its separate free-energy accounting.

Python 3.14.4; Matplotlib 3.10.7 as in pyproject.toml.
This is an illustrative grouped catalytic cycle, not a molecular structure.
All energy changes are chosen, consistently defined reference values.
Run in _media; the opaque white PNG is written to cwd with this basename.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    ink, blue, orange = "#253947", "#167294", "#b35e22"
    fig = plt.figure(figsize=(9.0, 6.1), facecolor="white")
    fig.text(0.5, 0.945, "ATP couples phosphate transfer to sugar", ha="center",
             fontsize=17, color=ink, weight="bold")
    fig.text(0.5, 0.895, "S and S–P label hypothetical sugar states; no molecular structure drawn",
             ha="center", fontsize=10.5, color=ink)
    ax = fig.add_axes((0.045, 0.48, 0.91, 0.35))
    ax.set(xlim=(0, 10), ylim=(0, 4))
    ax.axis("off")
    for x, label in [(1.6, "Free enzyme E"),
                     (5, "Bound reactants\nE · S · ATP"),
                     (8.4, "Bound products\nE · S–P · ADP")]:
        ax.add_patch(FancyBboxPatch((x - 1.3, 1.5), 2.6, 1.05,
                     boxstyle="round,pad=0.12", facecolor="#edf6f8",
                     edgecolor=blue, linewidth=1.5))
        ax.text(x, 2.04, label, ha="center", va="center", fontsize=11,
                color=ink)
    for start, end in [((3, 2), (3.6, 2)), ((6.4, 2), (7, 2))]:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                     mutation_scale=16, linewidth=2, color=blue))
    ax.text(3.3, 2.96, "S + ATP\nbind", ha="center", fontsize=10, color=ink)
    ax.text(6.7, 2.96, "Group\ntransfer", ha="center", fontsize=10, color=ink)
    ax.add_patch(FancyArrowPatch((8.4, 1.36), (1.6, 1.36),
                 connectionstyle="arc3,rad=-0.17", arrowstyle="-|>",
                 mutation_scale=16, linewidth=2, color=blue))
    ax.text(5, 0.16, "Release S–P + ADP; regenerate E", ha="center",
            fontsize=11, color=ink)
    fig.text(0.5, 0.445, "Net: S + ATP → S–P + ADP", ha="center",
             fontsize=13, color=blue, weight="bold")
    fig.text(0.5, 0.37, "Separate thermodynamic accounting (chosen ΔG°′ in kJ/mol)",
             ha="center", fontsize=11.5, color=ink, weight="bold")
    for y, equation, value, color in [
        (0.30, "S + Pi → S–P + H₂O", "+12", orange),
        (0.235, "ATP + H₂O → ADP + Pi", "−32", blue),
        (0.15, "S + ATP → S–P + ADP", "−20", blue),
    ]:
        fig.text(0.23, y, equation, fontsize=12, color=ink)
        fig.text(0.78, y, value, ha="right", fontsize=13, color=color,
                 weight="bold")
    fig.add_artist(plt.Line2D([0.22, 0.79], [0.206, 0.206],
                   transform=fig.transFigure, color="#8ca1ad", linewidth=1))
    fig.text(0.5, 0.052, "Water and Pi cancel in the sum; the sum does not specify microscopic steps.",
             ha="center", fontsize=10, color=ink)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Chosen reference changes: +12 − 32 = −20 kJ/mol")


if __name__ == "__main__":
    main()
