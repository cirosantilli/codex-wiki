"""Map a unit circle to an ellipse; write an opaque PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, end, color):
    ax.annotate("", end, (0, 0), arrowprops={
        "arrowstyle": "->", "color": color, "lw": 2.6,
        "shrinkA": 0, "shrinkB": 0, "mutation_scale": 16}, zorder=5)


def main():
    matrix = np.array([[3., 4.], [-4 / 5, 3 / 5]])
    right = np.array([[3., -4.], [4., 3.]]) / 5
    sigma = np.diag([5., 1.])
    assert np.allclose(right.T @ right, np.eye(2))
    assert np.allclose(sigma @ right.T, matrix)
    assert np.allclose(matrix @ right, sigma)
    assert np.allclose(matrix.T @ matrix, np.array([[241, 288], [288, 409]]) / 25)
    assert np.allclose(np.linalg.eigvalsh(matrix.T @ matrix), [1, 25])
    assert np.allclose(np.linalg.eigvals(matrix), (9 + np.array([1j, -1j]) * np.sqrt(44)) / 5)
    mixed = right @ np.array([1., 1.]) / np.sqrt(2)
    assert np.isclose(np.linalg.norm(mixed), 1)
    assert np.isclose(np.linalg.norm(matrix @ mixed), np.sqrt(13))
    epsilon = 0.01
    weak_matrix = np.diag([5., epsilon]) @ right.T
    assert np.allclose(weak_matrix, [[3, 4], [-0.008, 0.006]])
    assert np.isclose(np.linalg.cond(weak_matrix), 500)
    assert np.allclose(np.linalg.solve(weak_matrix, [0, 0.001]), [-0.08, 0.06])
    angle = np.linspace(0, 2 * np.pi, 600)
    circle = right @ np.array([np.cos(angle), np.sin(angle)])
    ellipse = matrix @ circle
    assert np.allclose(ellipse[0] ** 2 / 25 + ellipse[1] ** 2, 1)

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4),
                             gridspec_kw={"width_ratios": [1, 3.7]})
    fig.subplots_adjust(left=0.055, right=0.98, bottom=0.22, top=0.73, wspace=0.22)
    blue, orange, ink = "#2365a0", "#c05621", "#253b46"
    for ax, limit in zip(axes, [1.55, 5.75]):
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-1.65, 1.65)
        ax.axhline(0, color="#bbbbbb", lw=0.8)
        ax.axvline(0, color="#bbbbbb", lw=0.8)
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_yticks([-1, 0, 1])
        ax.plot(0, 0, "o", color=ink, ms=4, zorder=6)
    source, target = axes
    source.set_title("Input: unit circle", fontsize=13, pad=10)
    target.set_title("Output: ellipse with semiaxes 5 and 1", fontsize=13, pad=10)
    source.set_xticks([-1, 0, 1])
    target.set_xticks([-5, -3, -1, 0, 1, 3, 5])
    source.plot(*circle, color=ink, lw=2)
    target.plot(*ellipse, color=ink, lw=2)
    for j, color in enumerate([blue, orange]):
        arrow(source, right[:, j], color)
        arrow(target, sigma[:, j], color)
        source.plot(*(-right[:, j]), "o", color=color, ms=5)
        target.plot(*(-sigma[:, j]), "o", color=color, ms=5)
    source.text(0.7, 1.03, r"$v_1$", color=blue)
    source.text(-1.22, 0.75, r"$v_2$", color=orange)
    target.text(2.5, 0.15, r"$Av_1=5u_1$", color=blue, ha="center")
    target.text(0.25, 1.12, r"$Av_2=u_2$", color=orange)
    target.text(-3.8, -1.30, r"$y_1^2/25+y_2^2=1$", color=ink)
    fig.suptitle("Singular directions: perpendicular in, perpendicular out", fontsize=17, y=0.97)
    fig.text(0.5, 0.84, "A = [[3, 4], [−4/5, 3/5]]     " + r"$\sigma_1=5,\ \sigma_2=1$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.09, "Each panel has equal horizontal and vertical units. Colored endpoints correspond.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Checked: A=UΣVᵀ; Av₁=5u₁; Av₂=u₂; eigenvalues of AᵀA = 25,1; ellipse equation; A has no real eigenvalues.")


if __name__ == "__main__":
    main()
