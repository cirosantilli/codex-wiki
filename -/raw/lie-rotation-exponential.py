"""Generate lie-rotation-exponential.png in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media to place the figure beside the other wiki images.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def rotation(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])


def exponential_series(matrix, terms=48):
    result = np.eye(matrix.shape[0])
    term = result.copy()
    for n in range(1, terms):
        term = term @ matrix / n
        result += term
    return result


def main():
    generator = np.array([[0., -1.], [1., 0.]])
    identity = np.eye(2)
    e1 = np.array([1., 0.])
    assert np.allclose(generator @ generator, -identity)
    error = np.max(np.abs(exponential_series(np.pi / 2 * generator)
                          - rotation(np.pi / 2)))
    assert error < 1e-14
    assert np.allclose(rotation(np.pi / 2) @ e1, [0, 1])
    assert np.allclose(rotation(np.pi), -identity)
    assert np.allclose(rotation(2 * np.pi), identity)
    assert np.allclose(rotation(.7) @ rotation(-.2), rotation(.5))
    assert np.allclose(rotation(np.pi / 2).T @ rotation(np.pi / 2), identity)
    assert np.isclose(np.linalg.det(rotation(.7)), 1)
    h = 1e-5
    tangent_error = np.max(np.abs((rotation(h) - rotation(-h)) / (2 * h)
                                  - generator))
    assert tangent_error < 2e-11

    blue, green, orange, gray = "#276ba3", "#218366", "#bf6224", "#667887"
    angles = np.linspace(0, 2 * np.pi, 500)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), dpi=120,
                             facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.plot(np.cos(angles), np.sin(angles), color=gray, lw=1.3)
        ax.axhline(0, color="#d4dce1", lw=.8)
        ax.axvline(0, color="#d4dce1", lw=.8)
        ax.set(xlim=(-1.4, 1.65), ylim=(-1.35, 1.4), aspect="equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xlabel("x")
        ax.set_ylabel("y", rotation=0)

    ax = axes[0]
    ax.set_title(r"Initial velocity: $J(1,0)^T=(0,1)^T$", fontsize=12, pad=14)
    ax.annotate("", xy=(1, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=blue, lw=2))
    ax.scatter([1], [0], color=blue, s=42, zorder=5)
    ax.text(.47, -.19, r"$v(0)$", color=blue, fontsize=12)
    ax.annotate("", xy=(1, 1), xytext=(1, 0),
                arrowprops=dict(arrowstyle="->", color=green, lw=2.5))
    ax.text(1.08, .76, r"$Jv(0)$", color=green, fontsize=12)
    theta = .35
    point = rotation(theta) @ e1
    ax.plot([1, point[0]], [0, point[1]], "--", color=orange, lw=2)
    ax.scatter(*point, color=orange, s=42, zorder=5)
    ax.annotate(r"$R_hv(0)$", xy=point, xytext=(.05, .58),
                color=orange, fontsize=12,
                arrowprops=dict(arrowstyle="-", color=orange))
    ax.text(0, -1.22, "The tangent gives direction and speed", ha="center",
            fontsize=10, color=gray)

    ax = axes[1]
    ax.set_title(r"Finite motion: $v(t)=\exp(tJ)v(0)$", fontsize=12, pad=14)
    labels = [(0, r"$t=0, 2\pi$", (1.05, -.2)),
              (np.pi / 2, r"$t=\pi/2$", (.12, 1.1)),
              (np.pi, r"$t=\pi$", (-1.31, .15)),
              (3 * np.pi / 2, r"$t=3\pi/2$", (.12, -1.14))]
    for theta, label, position in labels:
        point = rotation(theta) @ e1
        color = green if theta == np.pi / 2 else blue
        ax.annotate("", xy=point, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color=color, lw=2))
        ax.scatter(*point, color=color, s=42, zorder=5)
        ax.text(*position, label, fontsize=11, color=color)
    arc = np.linspace(.08, np.pi / 2 - .08, 100)
    ax.plot(.7 * np.cos(arc), .7 * np.sin(arc), color=orange, lw=2)
    ax.annotate("", xy=(.7 * np.cos(arc[-1]), .7 * np.sin(arc[-1])),
                xytext=(.7 * np.cos(arc[-8]), .7 * np.sin(arc[-8])),
                arrowprops=dict(arrowstyle="->", color=orange, lw=2))
    ax.text(.31, .27, "quarter-turn", color=orange, fontsize=10, ha="center")
    fig.tight_layout(pad=1.5, w_pad=2)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"quarter-turn series error = {error:.3g}")
    print(f"central-difference generator error = {tangent_error:.3g}")
    print(output.name)


if __name__ == "__main__":
    main()
