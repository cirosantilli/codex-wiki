"""Smallest-leaf Prüfer encoding and its inverse; tested with Python 3.14.

Write the matching opaque PNG into the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def encoding_steps(edges, labels):
    adjacency = {v: set() for v in labels}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    steps, code = [], []
    while len(adjacency) > 2:
        leaf = min(v for v, neighbours in adjacency.items() if len(neighbours) == 1)
        neighbour = next(iter(adjacency[leaf]))
        current = [(a, b) for a in adjacency for b in adjacency[a] if a < b]
        steps.append((set(adjacency), current, leaf, neighbour))
        code.append(neighbour)
        adjacency[neighbour].remove(leaf)
        del adjacency[leaf]
    steps.append((set(adjacency), [tuple(sorted(adjacency))], None, None))
    return steps, tuple(code)


def main():
    edges = [(1, 2), (1, 3), (3, 4), (3, 5), (5, 6)]
    steps, code = encoding_steps(edges, range(1, 7))
    assert code == (1, 3, 3, 5)
    positions = {1: (-0.7, 0.4), 2: (-1.2, 1.35), 3: (0, -0.1),
                 4: (-0.65, -1.05), 5: (0.9, 0.4), 6: (1.4, 1.35)}
    blue, orange, dark = "#226b96", "#b55c1c", "#243746"
    fig = plt.figure(figsize=(12, 6.2), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 5, height_ratios=(1.1, 1.15))
    for i, (remaining, current, leaf, neighbour) in enumerate(steps):
        ax = fig.add_subplot(grid[0, i])
        for a, b in current:
            active = leaf in (a, b)
            ax.plot([positions[a][0], positions[b][0]],
                    [positions[a][1], positions[b][1]],
                    color=orange if active else blue, lw=2.5, zorder=1)
        for v in sorted(remaining):
            active = v == leaf
            ax.scatter(*positions[v], s=460, facecolor="#fff0e3" if active else "white",
                       edgecolor=orange if active else blue, lw=1.8, zorder=2)
            ax.text(*positions[v], str(v), ha="center", va="center", fontsize=12,
                    color=dark, zorder=3)
        ax.set_xlim(-1.7, 1.9)
        ax.set_ylim(-1.65, 1.9)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(f"Step {i + 1}" if leaf is not None else "Final pair", fontsize=12)
        caption = f"Remove {leaf}; record {neighbour}" if leaf is not None else "Stop; keep edge {5, 6}"
        ax.text(0.5, -0.08, caption, transform=ax.transAxes, ha="center", fontsize=11,
                color=orange if leaf is not None else blue)
    ax = fig.add_subplot(grid[1, :])
    ax.axis("off")
    ax.text(0.5, 1.04, "Decode (1, 3, 3, 5): choose the smallest remaining label absent from the code",
            ha="center", transform=ax.transAxes, fontsize=12, color=dark)
    remaining, pending, recovered, rows = set(range(1, 7)), list(code), [], []
    while pending:
        leaf = min(remaining - set(pending))
        neighbour = pending[0]
        rows.append([str(tuple(pending)), str(leaf), f"{{{leaf}, {neighbour}}}"])
        recovered.append(tuple(sorted((leaf, neighbour))))
        remaining.remove(leaf)
        pending.pop(0)
    a, b = sorted(remaining)
    recovered.append((a, b))
    rows.append(["Empty; remaining labels {5, 6}", "Final pair", "{5, 6}"])
    assert set(recovered) == set(edges)
    table = ax.table(cellText=rows,
                     colLabels=["Remaining code", "Smallest absent label", "Edge added"],
                     colWidths=[0.48, 0.28, 0.24], cellLoc="center", bbox=[0.08, 0.05, 0.84, 0.87])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, _), cell in table.get_celld().items():
        cell.set_edgecolor("#d2dce3")
        cell.set_facecolor("#eaf3f8" if row == 0 else "white")
        cell.set_text_props(color=dark, weight="bold" if row == 0 else "normal")
    fig.suptitle("A tree becomes four freely chosen labels", fontsize=17, y=0.97, color=dark)
    fig.text(0.5, 0.915, "Orange marks the smallest leaf and the edge removed; node positions stay fixed.",
             ha="center", fontsize=11, color=dark)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.85, bottom=0.055, wspace=0.16, hspace=0.37)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
