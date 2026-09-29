"""Plot path edge energy and eigenvectors; write an opaque PNG in the CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    incidence = np.array([[1, -1, 0], [0, 1, -1]])
    laplacian = incidence.T @ incidence
    values = np.array([2, 0, -1])
    energies = (incidence @ values) ** 2
    modes = np.array([[1, 1, 1], [1, 0, -1], [1, -2, 1]])
    eigenvalues = np.array([0, 1, 3])
    assert np.array_equal(energies, [4, 1])
    assert values @ laplacian @ values == energies.sum() == 5
    assert np.array_equal(laplacian @ modes.T, modes.T * eigenvalues)

    colors = ["#2868a6", "#d07826", "#4b8651"]
    fig = plt.figure(figsize=(9.6, 5.6), dpi=110, facecolor="white")
    grid = fig.add_gridspec(2, 3, height_ratios=[1.1, 1], hspace=0.55,
                           left=0.075, right=0.97, bottom=0.12, top=0.88,
                           wspace=0.37)
    graph = fig.add_subplot(grid[0, :])
    for i, energy in enumerate(energies):
        graph.plot([i, i + 1], [0, 0], color=colors[i], lw=4, zorder=1)
        graph.text(i + 0.5, -0.35,
                   rf"$({values[i]} - ({values[i+1]}))^2 = {energy}$",
                   ha="center", fontsize=13, color=colors[i])
    graph.scatter(range(3), [0] * 3, s=900, facecolor="white",
                  edgecolor="#34495e", linewidth=2, zorder=3)
    for i, label in enumerate("ABC"):
        graph.text(i, 0, label, ha="center", va="center", fontsize=15,
                   zorder=4)
        graph.text(i, 0.36, f"Value {values[i]}", ha="center", fontsize=13)
    graph.text(1, -0.67, r"Total edge energy: $x^T L x = 4 + 1 = 5$",
               ha="center", fontsize=14)
    graph.set_xlim(-0.35, 2.35)
    graph.set_ylim(-0.85, 0.65)
    graph.axis("off")

    for k in range(3):
        ax = fig.add_subplot(grid[1, k])
        ax.axhline(0, color="#888888", lw=0.8)
        ax.plot(range(3), modes[k], "o-", lw=2.2, markersize=7,
                color=colors[k])
        ax.set_title(rf"Eigenvalue $\lambda={eigenvalues[k]}$", fontsize=13)
        ax.set_xticks(range(3), list("ABC"))
        ax.set_yticks([-2, -1, 0, 1])
        ax.set_ylim(-2.4, 1.65)
        ax.set_xlim(-0.15, 2.15)
        ax.grid(axis="y", alpha=0.2)
        if k == 0:
            ax.set_ylabel("Eigenvector entry", fontsize=11)
        for i, value in enumerate(modes[k]):
            ax.annotate(str(value), (i, value), xytext=(0, 8),
                        textcoords="offset points", ha="center", fontsize=11)
    fig.suptitle("Three-vertex path: edge disagreement and Laplacian modes",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.035, "Each edge is counted once. The eigenvectors below are not normalized.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "graph-laplacian-edge-energy.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
