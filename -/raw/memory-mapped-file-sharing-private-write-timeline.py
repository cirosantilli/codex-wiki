"""Draw shared visibility, private copying and a separate persistence boundary.

Original state model: ordered actions, no background writeback in this interval,
successful synchronous completion and honored storage contracts. No benchmark.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def model_states():
    """Pairs are x,y on relative page 1; untouched page 0 remains file-backed."""
    shared = [7, 8]
    durable = tuple(shared)
    private = None
    rows = []

    def record(event):
        rows.append((event, tuple(shared), tuple(shared),
                     tuple(shared) if private is None else tuple(private), durable))

    record("1  All mappings read both pages")
    private = shared.copy()
    private[0] = 99
    record("2  B privately stores x = 99")
    shared[:] = [11, 12]
    record("3  A shares x = 11, y = 12")
    record("4  B reads after coordination")
    durable = tuple(shared)
    record("5  Shared MS_SYNC succeeds")
    return rows


def main():
    fig, ax = plt.subplots(figsize=(10, 6.1), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.1))
    ax.axis("off")
    ink, blue, purple, green = "#203448", "#2166ac", "#7952a3", "#337144"
    ax.text(5, 5.8, "Shared visibility and persistence are separate events",
            ha="center", fontsize=16, weight="bold", color=ink)
    ax.text(5, 5.44, "Toy timeline • pairs show (x, y) at file offsets (8229, 8230) • actions ordered externally",
            ha="center", fontsize=10.3, color=ink)
    centers = [4.5, 5.9, 7.3, 8.9]
    colors = [blue, blue, purple, green]
    headings = ["A shared", "B shared", "B private", "Durable file"]
    for x, title, color in zip(centers, headings, colors):
        ax.text(x, 4.98, title, ha="center", fontsize=11.5,
                weight="bold", color=color)
    for index, row in enumerate(model_states()):
        y = 4.2 - .65 * index
        ax.text(.2, y + .23, row[0], va="center", fontsize=10.8, color=ink)
        for col, (x, pair, edge) in enumerate(zip(centers, row[1:], colors)):
            fill = "#eff4fa" if col < 2 else "#f4eef9" if col == 2 else "#edf5ef"
            ax.add_patch(FancyBboxPatch(
                (x - .6, y), 1.2, .46, boxstyle="round,pad=0.025",
                facecolor=fill, edgecolor=edge, linewidth=1.2,
            ))
            ax.text(x, y + .23, f"{pair[0]}, {pair[1]}", ha="center",
                    va="center", fontsize=12, color=edge, weight="bold")
    ax.plot([.2, 9.7], [1.42, 1.42], color="#c5cdd3", linewidth=1)
    ax.text(5, 1.15, "Row 2: private copy of page 1 preserves y = 8 as well as B's new x = 99.",
            ha="center", fontsize=10.7, color=purple)
    ax.text(5, .83, "Rows 3–4: shared cache is dirty and visible; the durable copy stays old by model choice.",
            ha="center", fontsize=10.3, color=blue)
    ax.text(5, .51, "Row 5: successful synchronous writeback under honored storage contracts; private 99 is not saved.",
            ha="center", fontsize=10.1, color=green)
    ax.text(5, .18, "No background writeback here; real writes may persist earlier. MS_SYNC is not a reader/writer lock.",
            ha="center", fontsize=9.9, color=ink)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
