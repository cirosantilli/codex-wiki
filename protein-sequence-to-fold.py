"""Original sequence/fold/binding schematic; no protein coordinates or predictor.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Save the same-basename PNG in CWD for the repository's media rule.
"""

from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch
import numpy as np


SEQUENCE = "AMAMAMAMAMAM"
REORDERED = "AAAAAAMMMMMM"
COLORS = {"A": "#f3c66a", "M": "#75b5d4"}
INK = "#253745"
FOLD = np.array([
    [-2.0, .6], [-1.55, 1.3], [-.8, 1.5], [0., 1.05],
    [.75, 1.55], [1.6, 1.3], [1.7, .35], [1., -.2],
    [.15, .15], [-.6, -.3], [-1.35, -.9], [-2., -.5],
])


def chain(ax, points, sequence, radius=.17, labels="letters"):
    """Connect consecutive residues only; color always follows sequence order."""
    ax.plot(*points.T, color=INK, lw=2, zorder=1)
    for i, ((x, y), residue) in enumerate(zip(points, sequence, strict=True)):
        ax.add_patch(Circle((x, y), radius, facecolor=COLORS[residue],
                            edgecolor=INK, lw=1.1, zorder=3))
        ax.text(x, y, residue if labels == "letters" else str(i + 1),
                ha="center", va="center", fontsize=10, color=INK, zorder=4)


def main():
    assert Counter(SEQUENCE) == Counter(REORDERED) == {"A": 6, "M": 6}
    assert sum(a != b for a, b in zip(SEQUENCE, SEQUENCE[1:])) == 11
    assert sum(a != b for a, b in zip(REORDERED, REORDERED[1:])) == 1
    assert FOLD.shape == (12, 2) and np.isfinite(FOLD).all()
    assert len(np.unique(FOLD, axis=0)) == len(SEQUENCE)
    # Every circle is separate, and sequence positions 4 and 9 are non-neighbours.
    distances = np.linalg.norm(FOLD[:, None] - FOLD[None, :], axis=-1)
    assert distances[np.triu_indices(12, 1)].min() > 2 * .17
    assert np.linalg.norm(FOLD[3] - FOLD[8]) < .95

    fig = plt.figure(figsize=(10.0, 6.7), facecolor="white")
    plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK})
    fig.text(.5, .96, "Sequence → abstract fold → binding site", ha="center",
             fontsize=17, weight="bold")
    fig.text(.5, .915, "A = alanine      M = methionine      Lines = peptide connectivity",
             ha="center", fontsize=11)

    ax = fig.add_axes([.08, .62, .84, .25])
    ax.set(xlim=(-1.3, 12.5), ylim=(-1.0, 2.0), aspect="equal")
    ax.axis("off")
    for y, sequence, label in [(1.35, SEQUENCE, "11 unlike neighbours"),
                                (.05, REORDERED, "1 unlike neighbour")]:
        points = np.column_stack([np.arange(12), np.full(12, y)])
        chain(ax, points, sequence, radius=.28)
        ax.text(-.7, y, "N", ha="center", va="center", fontsize=11)
        ax.text(11.7, y, "C", ha="center", va="center", fontsize=11)
        ax.text(5.5, y - .56, label, ha="center", fontsize=10)
    fig.text(.5, .60, "Same counts: 6 A + 6 M. Different order changes the neighbours.",
             ha="center", fontsize=12)

    folded = fig.add_axes([.06, .16, .40, .39])
    folded.set(xlim=(-2.6, 2.1), ylim=(-1.5, 2.25), aspect="equal")
    folded.axis("off")
    chain(folded, FOLD, SEQUENCE, labels="numbers")
    folded.text(-2.35, .65, "N", fontsize=11, ha="center")
    folded.text(-2.35, -.5, "C", fontsize=11, ha="center")
    for point in FOLD[[3, 8]]:
        folded.add_patch(Circle(point, .24, fill=False, edgecolor="#b96724", lw=2))
    folded.plot(*FOLD[[3, 8]].T, ls=":", color="#b96724", lw=2, zorder=2)
    folded.text(-.25, 2.04, "One imagined arrangement", ha="center", fontsize=12,
                weight="bold")
    folded.text(-.25, -1.35, "Numbers keep the sequence order", ha="center", fontsize=11)

    binding = fig.add_axes([.59, .16, .35, .39])
    binding.set(xlim=(-1.8, 1.8), ylim=(-1.5, 2.25), aspect="equal")
    binding.axis("off")
    binding.add_patch(Ellipse((0, .65), 2.3, 1.3, facecolor="#faf2dc",
                              edgecolor="#b96724", ls="--", lw=1.5))
    # A conceptual magnification of residues 4 and 9, not an atomic surface.
    chain(binding, np.array([[-.9, .65]]), "M", radius=.34)
    chain(binding, np.array([[.9, .65]]), "A", radius=.34)
    binding.text(-.9, .02, "position 4", ha="center", fontsize=10)
    binding.text(.9, .02, "position 9", ha="center", fontsize=10)
    binding.add_patch(Ellipse((0, .65), .7, .46, facecolor="#a9d3af",
                              edgecolor="#39734c", lw=1.5, zorder=4))
    binding.annotate("Bound molecule", xy=(0, .65), xytext=(0, 1.65),
                     ha="center", fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": INK})
    binding.text(0, 2.04, "Binding-site idea", ha="center", fontsize=12, weight="bold")
    binding.text(0, -.70, "Distant positions can cooperate", ha="center", fontsize=11)
    binding.text(0, -1.05, "Shape AND chemistry affect binding", ha="center", fontsize=11)

    fig.add_artist(FancyArrowPatch((.48, .36), (.58, .36), transform=fig.transFigure,
                                   arrowstyle="->", mutation_scale=18, lw=1.8, color=INK))
    fig.text(.5, .085, "The 12-residue strings are bookkeeping toys, not known functional proteins.",
             ha="center", fontsize=10)
    fig.text(.5, .045, "Original schematic: no measured coordinates, physical scale, or fold prediction.",
             ha="center", fontsize=10, color="#59636b")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1200 × 804 pixels")


if __name__ == "__main__":
    main()
