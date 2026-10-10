"""Plot the kernel for two disconnected edges; write an opaque PNG in the CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    incidence = np.array([[1, -1, 0, 0], [0, 0, 1, -1]])
    laplacian = incidence.T @ incidence
    indicators = np.array([[1, 1, 0, 0], [0, 0, 1, 1]])
    assert np.array_equal(laplacian @ indicators.T, np.zeros((4, 2)))
    assert np.linalg.matrix_rank(indicators) == 2
    assert np.allclose(np.linalg.eigvalsh(laplacian), [0, 0, 2, 2])

    colors = ["#2868a6", "#d07826"]
    fig = plt.figure(figsize=(9.6, 4.8), dpi=110, facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[0.85, 1], hspace=0.4,
                           left=0.075, right=0.97, bottom=0.18, top=0.86,
                           wspace=0.3)
    graph = fig.add_subplot(grid[0, :])
    positions = [0, 0.8, 2, 2.8]
    for component, (i, j) in enumerate([(0, 1), (2, 3)]):
        color = colors[component]
        graph.plot([positions[i], positions[j]], [0, 0], color=color,
                   lw=4, zorder=1)
        graph.scatter([positions[i], positions[j]], [0, 0], s=850,
                      facecolor="white", edgecolor=color, linewidth=2,
                      zorder=3)
        graph.text((positions[i] + positions[j]) / 2, 0.4,
                   f"Component {component + 1}: independent constant level",
                   ha="center", fontsize=12, color=color)
    for x, label in zip(positions, "ABCD"):
        graph.text(x, 0, label, ha="center", va="center", fontsize=15,
                   zorder=4)
    graph.set_xlim(-0.4, 3.2)
    graph.set_ylim(-0.3, 0.75)
    graph.axis("off")

    for k, vector in enumerate(indicators):
        ax = fig.add_subplot(grid[1, k])
        ax.bar(range(4), vector, color=colors[k], width=0.55)
        ax.axhline(0, color="#777777", lw=0.8)
        for i, value in enumerate(vector):
            ax.text(i, value + 0.055, str(value), ha="center", fontsize=12)
        ax.set_xticks(range(4), list("ABCD"))
        ax.set_yticks([0, 1])
        ax.set_ylim(-0.06, 1.35)
        ax.set_title(rf"Zero eigenvector $u_{k+1}$: $Lu_{k+1}=0$",
                     fontsize=13)
        ax.set_ylabel("Entry at vertex", fontsize=11)
        ax.grid(axis="y", alpha=0.15)
    fig.suptitle("Two components give a two-dimensional Laplacian kernel",
                 fontsize=15, y=0.965)
    fig.text(0.5, 0.065,
             r"Every kernel vector is $a u_1 + b u_2$: "
             r"values $(a,a,b,b)$. Eigenvalues: $0,0,2,2$.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "graph-laplacian-connected-components.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
