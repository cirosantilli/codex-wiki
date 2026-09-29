"""Show projection subtraction and unit directions; write a PNG to CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media to create gram-schmidt-vector-steps.png there.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


BLUE, RED, ORANGE, TEAL = "#2465a0", "#9c3042", "#c05a10", "#13796d"


def arrow(ax, end, color, start=(0, 0), dashed=False):
    ax.annotate("", xy=end, xytext=start, arrowprops={
        "arrowstyle": "->", "color": color, "lw": 2.6,
        "linestyle": "--" if dashed else "-", "shrinkA": 0,
        "shrinkB": 0, "mutation_scale": 16}, zorder=5)


def corner(ax, origin, direction_a, direction_b):
    scale = 0.11
    a, b = scale * direction_a, scale * direction_b
    points = np.array([origin + a, origin + a + b, origin + b])
    ax.plot(*points.T, color="#59636c", lw=1.2, zorder=6)


def main():
    v1, v2 = np.array([1., 1.]), np.array([1., 0.])
    q1 = v1 / np.linalg.norm(v1)
    projection = np.dot(v2, q1) * q1
    u2 = v2 - projection
    q2 = u2 / np.linalg.norm(u2)
    assert np.allclose(projection, [0.5, 0.5], atol=1e-14)
    assert np.allclose(u2, [0.5, -0.5], atol=1e-14)
    assert np.isclose(np.linalg.norm(u2), 1 / np.sqrt(2), atol=1e-14)
    assert np.allclose(np.column_stack([q1, q2]).T @
                       np.column_stack([q1, q2]), np.eye(2), atol=1e-14)
    dependent = np.array([2., 2.])
    assert np.allclose(dependent - np.dot(dependent, q1) * q1, 0, atol=1e-14)

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.7))
    fig.subplots_adjust(left=0.055, right=0.98, top=0.77, bottom=0.20, wspace=0.35)
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.set_xlim(-0.25, 1.55)
        ax.set_ylim(-1.0, 1.5)
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([-0.5, 0, 0.5, 1])
        ax.axhline(0, color="#b8c0c6", lw=0.8)
        ax.axvline(0, color="#b8c0c6", lw=0.8)
        ax.grid(alpha=0.12)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=10)
        ax.plot(0, 0, "o", color="#253b46", ms=4, zorder=7)

    first, second, third = axes
    first.set_title("1. Original vectors", fontsize=13, pad=12)
    arrow(first, v1, BLUE)
    arrow(first, v2, RED)
    first.text(0.73, 1.15, r"$v_1=(1,1)$", color=BLUE, fontsize=11)
    first.text(0.72, -0.23, r"$v_2=(1,0)$", color=RED, fontsize=11)

    second.set_title("2. Subtract the projection", fontsize=13, pad=12)
    second.plot([0, 1.22], [0, 1.22], color=BLUE, lw=1, alpha=0.3)
    arrow(second, v2, RED)
    arrow(second, projection, TEAL)
    arrow(second, u2, ORANGE)
    arrow(second, v2, ORANGE, start=projection, dashed=True)
    corner(second, projection, -q1, q2)
    second.text(0.03, 0.67, r"$p=(1/2,1/2)$", color=TEAL, fontsize=11)
    second.text(0.54, -0.63, r"$u_2=(1/2,-1/2)$", color=ORANGE, fontsize=11)
    second.text(1.06, 0.08, r"$v_2$", color=RED)
    second.text(0.57, 1.19, r"$v_2=p+u_2$", fontsize=12)

    third.set_title("3. Divide by each length", fontsize=13, pad=12)
    angle = np.linspace(0, 2 * np.pi, 300)
    third.plot(np.cos(angle), np.sin(angle), color="#7e8993", alpha=0.5, lw=1)
    arrow(third, q1, BLUE)
    arrow(third, q2, ORANGE)
    corner(third, np.zeros(2), q1, q2)
    third.text(0.67, 0.83, r"$q_1$", color=BLUE)
    third.text(0.80, -0.73, r"$q_2$", color=ORANGE)
    third.text(0.00, 1.19, r"$\|q_1\|=\|q_2\|=1$", fontsize=12)
    fig.suptitle("Gram–Schmidt: remove overlap, then set length to one", fontsize=17, y=0.96)
    fig.text(0.5, 0.08, "All panels use equal horizontal and vertical units. "
             "The dashed arrow is the residual translated to the projection tip.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Checked: p=(1/2,1/2); u2=(1/2,-1/2); Q.T Q=I; dependent input has zero remainder.")


if __name__ == "__main__":
    main()
