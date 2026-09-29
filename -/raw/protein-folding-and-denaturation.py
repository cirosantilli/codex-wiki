"""Original fold/unfold/cleavage/aggregation schematic, not protein coordinates.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
The independent drawings deliberately preserve residue identity and connectivity.
Save the same-basename PNG in CWD for the repository's media rule.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch
import numpy as np


SEQUENCE = "AMAMAMAMAMAM"
COLORS = {"A": "#f3c66a", "M": "#75b5d4"}
INK = "#253745"
FOLD = np.array([
    [-2., .6], [-1.55, 1.3], [-.8, 1.5], [0., 1.05],
    [.75, 1.55], [1.6, 1.3], [1.7, .35], [1., -.2],
    [.15, .15], [-.6, -.3], [-1.35, -.9], [-2., -.5],
])


def chain(ax, points, edges, radius=.17, edgecolor=INK):
    for a, b in edges:
        ax.plot(*points[[a, b]].T, color=edgecolor, lw=2, zorder=2)
    for i, ((x, y), residue) in enumerate(zip(points, SEQUENCE, strict=True)):
        ax.add_patch(Circle((x, y), radius, facecolor=COLORS[residue],
                            edgecolor=edgecolor, lw=1, zorder=3))
        ax.text(x, y, str(i + 1), ha="center", va="center", fontsize=8,
                color=INK, zorder=4)


def components(n, edges):
    """Count connected chain fragments without an external graph dependency."""
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen, count = set(range(n)), 0
    while unseen:
        todo = [unseen.pop()]
        count += 1
        while todo:
            for vertex in adjacency[todo.pop()] & unseen:
                unseen.remove(vertex)
                todo.append(vertex)
    return count


def main():
    edges = [(i, i + 1) for i in range(11)]
    cleaved = [edge for edge in edges if edge != (5, 6)]
    unfolded = np.column_stack([np.linspace(-2.2, 2.2, 12),
                               .35 * np.sin(np.linspace(0, 3 * np.pi, 12))])
    fragments = unfolded.copy()
    fragments[:6, 0] -= .32
    fragments[6:, 0] += .32
    assert len(edges) == 11 and components(12, edges) == 1
    assert len(cleaved) == 10 and components(12, cleaved) == 2
    assert SEQUENCE.count("A") == SEQUENCE.count("M") == 6
    for points in (FOLD, unfolded, fragments):
        assert points.shape == (12, 2) and np.isfinite(points).all()
        distances = np.linalg.norm(points[:, None] - points[None, :], axis=-1)
        assert distances[np.triu_indices(12, 1)].min() > .34
    aggregate_edges = edges + [(a + 12, b + 12) for a, b in edges]
    assert len(aggregate_edges) == 22 and components(24, aggregate_edges) == 2

    fig = plt.figure(figsize=(10, 7), facecolor="white")
    plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK})
    fig.text(.5, .96, "Unfolding changes shape; cleavage changes connectivity", ha="center",
             fontsize=16, weight="bold")
    fig.text(.5, .916, "A = alanine      M = methionine      Numbers = sequence positions",
             ha="center", fontsize=11)

    def panel(rect, title):
        ax = fig.add_axes(rect)
        ax.set(xlim=(-3, 3), ylim=(-1.5, 2.0), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=12, weight="bold", pad=5)
        return ax

    folded = panel([.045, .535, .35, .325], "Folded")
    chain(folded, FOLD, edges)
    folded.text(0, -1.35, "12 residues · 11 peptide bonds", ha="center", fontsize=10)
    opened = panel([.605, .535, .35, .325], "Unfolded / denatured")
    chain(opened, unfolded + [0, .55], edges, radius=.16)
    opened.text(0, -.6, "Same order; backbone remains intact", ha="center", fontsize=10)
    opened.text(0, -1.05, "12 residues · 11 peptide bonds", ha="center", fontsize=10)

    for start, end, y in [(.40, .60, .75), (.60, .40, .63)]:
        fig.add_artist(FancyArrowPatch((start, y), (end, y), transform=fig.transFigure,
                                       arrowstyle="->", mutation_scale=16, lw=1.8, color=INK))
    fig.text(.5, .778, "Denaturing conditions", ha="center", fontsize=10)
    fig.text(.5, .592, "Refolding may occur", ha="center", fontsize=10, color="#39734c")
    fig.text(.5, .560, "in suitable conditions", ha="center", fontsize=10, color="#39734c")

    fig.text(.5, .465, "Different outcomes after unfolding — these are not the same event",
             ha="center", fontsize=12, weight="bold")
    cut = panel([.035, .145, .45, .255], "Chain cleavage: one peptide bond removed")
    chain(cut, fragments + [0, .55], cleaved, radius=.16)
    midpoint = (fragments[5] + fragments[6]) / 2 + [0, .55]
    cut.plot([midpoint[0] - .11, midpoint[0] + .11],
             [midpoint[1] - .16, midpoint[1] + .16], color="#b6423c", lw=2.5)
    cut.plot([midpoint[0] - .11, midpoint[0] + .11],
             [midpoint[1] + .16, midpoint[1] - .16], color="#b6423c", lw=2.5)
    cut.text(0, -.64, "Two fragments: positions 1–6 and 7–12", ha="center", fontsize=10)
    cut.text(0, -1.08, "12 residues · 10 remaining peptide bonds", ha="center", fontsize=10)

    aggregate = panel([.525, .145, .45, .255], "Aggregation: chains associate")
    aggregate.add_patch(Ellipse((0, .55), 4.8, 1.75, facecolor="#eef2f5",
                                edgecolor="#a1acb5", ls="--", zorder=1))
    for shift, edgecolor in [([0, .20], INK), ([0, 1.08], "#67558a")]:
        chain(aggregate, unfolded + shift, edges, radius=.16, edgecolor=edgecolor)
    aggregate.text(0, -.64, "Each backbone still has 11 peptide bonds", ha="center", fontsize=10)
    aggregate.text(0, -1.08, "Association can hinder recovery of function", ha="center", fontsize=10)
    fig.text(.5, .092, "Not all proteins refold. Cleavage and aggregation are distinct possible outcomes.",
             ha="center", fontsize=11)
    fig.text(.5, .042, "Original toy schematic: no actual protein coordinates, physical scale, or reaction rates.",
             ha="center", fontsize=10, color="#59636b")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1200 × 840 pixels")


if __name__ == "__main__":
    main()
