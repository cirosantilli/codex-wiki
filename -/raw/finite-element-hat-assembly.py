"""Illustrate Poisson hat functions and local assembly; opaque PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def assemble(nodes):
    matrix = np.zeros((len(nodes), len(nodes)))
    load = np.zeros(len(nodes))
    for j, length in enumerate(np.diff(nodes)):
        matrix[j:j + 2, j:j + 2] += np.array([[1., -1.], [-1., 1.]]) / length
        load[j:j + 2] += length / 2
    return matrix[1:-1, 1:-1], load[1:-1]


def main():
    nodes = np.linspace(0, 1, 5)
    matrix, load = assemble(nodes)
    expected = np.array([[8., -4., 0.], [-4., 8., -4.], [0., -4., 8.]])
    np.testing.assert_array_equal(matrix, expected)
    np.testing.assert_array_equal(load, np.full(3, 0.25))
    coefficients = np.linalg.solve(matrix, load)
    np.testing.assert_allclose(coefficients, [3 / 32, 1 / 8, 3 / 32], atol=1e-16)
    # Check local assembly also on a nonuniform partition.
    other_nodes = np.array([0., 0.125, 0.25, 0.5, 1.])
    other_matrix, other_load = assemble(other_nodes)
    np.testing.assert_allclose(other_matrix @ (other_nodes[1:-1] *
                               (1 - other_nodes[1:-1]) / 2), other_load, atol=1e-15)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig = plt.figure(figsize=(9.6, 6.4), layout="constrained", facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.2, 1])
    ax = fig.add_subplot(grid[0, :])
    x = np.linspace(0, 1, 801)
    colors = ["#2166ac", "#25834a", "#b43b35"]
    for i, color in zip(range(1, 4), colors):
        values = np.maximum(1 - np.abs(x - nodes[i]) / 0.25, 0)
        ax.plot(x, values, color=color, lw=2.5, label=rf"$\phi_{i}$")
        ax.scatter(nodes, (np.arange(5) == i).astype(float), color=color,
                   s=35, zorder=4)
    ax.axhline(-0.13, color="0.35", lw=2)
    ax.scatter(nodes, np.full(5, -0.13), color="0.25", s=40)
    for j in range(4):
        ax.text((nodes[j] + nodes[j + 1]) / 2, -0.23, f"element {j + 1}",
                ha="center", va="center", fontsize=10)
    ax.set(xlim=(-0.035, 1.035), ylim=(-0.31, 1.43), xlabel="$x$",
           ylabel="Basis value", xticks=nodes,
           xticklabels=["0", "1/4", "1/2", "3/4", "1"], yticks=[0, 0.5, 1],
           title="Four mesh intervals, three interior hat functions")
    ax.legend(loc="upper right", ncols=3, framealpha=1)
    ax.grid(alpha=0.16)
    ax.spines[["top", "right"]].set_visible(False)

    ax = fig.add_subplot(grid[1, 0])
    ax.axis("off")
    ax.set_title("One interval contributes to two nodes", pad=10)
    ax.text(0.5, 0.87, r"$d=1/4$, unit forcing", ha="center")
    table = ax.table(cellText=[["4", "−4", "1/8"], ["−4", "4", "1/8"]],
                     rowLabels=["left", "right"], colLabels=["left", "right", "load"],
                     cellLoc="center", bbox=[0.15, 0.33, 0.78, 0.4])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    ax.text(0.5, 0.13, "Add contributions at shared nodes.\nFix endpoint values to zero.",
            ha="center", va="center", linespacing=1.6)

    ax = fig.add_subplot(grid[1, 1])
    ax.axis("off")
    ax.set_title("Assembled interior system: Kc = F", pad=10)
    table = ax.table(cellText=[["8", "−4", "0", "1/4"],
                              ["−4", "8", "−4", "1/4"],
                              ["0", "−4", "8", "1/4"]],
                     rowLabels=["node 1", "node 2", "node 3"],
                     colLabels=["$c_1$", "$c_2$", "$c_3$", "$F$"],
                     cellLoc="center", bbox=[0.17, 0.28, 0.8, 0.52])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("0.72")
        if col == 3:
            cell.set_facecolor("#eaf2fa")
        elif row > 0 and col >= 0 and abs(row - 1 - col) > 1:
            cell.set_facecolor("#f0f0f0")
    ax.text(0.5, 0.10, r"$c=(3/32,\ 1/8,\ 3/32)$", ha="center", fontsize=13)
    for ax in fig.axes:
        ax.set_facecolor("white")
    fig.savefig(Path.cwd() / "finite-element-hat-assembly.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Uniform K, F and coefficients, plus nonuniform nodal exactness verified.")


if __name__ == "__main__":
    main()
