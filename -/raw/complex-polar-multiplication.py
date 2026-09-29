"""Illustrate fixed complex multiplication as a rotation and uniform scale.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write the matching opaque PNG to the current working directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, end, color, label, offset):
    ax.annotate("", (end.real, end.imag), (0, 0),
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2.4})
    ax.annotate(label, (end.real, end.imag), xytext=offset,
                textcoords="offset points", color=color, fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    blue, orange, purple = "#2468a0", "#b65718", "#81449b"
    z, multiplier = 3+4j, 1+1j
    product = multiplier*z
    assert product == -1+7j and 1j*z == -4+3j
    assert np.isclose(abs(product), 5*np.sqrt(2))
    assert np.isclose(np.angle(product)-np.angle(z), np.pi/4)
    matrix = np.array([[1., -1.], [1., 1.]])
    assert np.allclose(matrix.T @ matrix, 2*np.eye(2))
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 5.0), dpi=120,
                             constrained_layout=True)
    fig.patch.set_facecolor("white")
    left, right = axes
    arrow(left, z, blue, r"$z=3+4i$", (8, -6))
    arrow(left, 1j*z, purple, r"$iz=-4+3i$", (-22, 10))
    arrow(left, product, orange, r"$(1+i)z=-1+7i$", (-38, 9))
    arc = np.linspace(np.angle(z), np.angle(product), 150)
    left.plot(2*np.cos(arc), 2*np.sin(arc), color=orange, lw=1.8)
    left.annotate("", (2*np.cos(arc[-1]), 2*np.sin(arc[-1])),
                  (2*np.cos(arc[-8]), 2*np.sin(arc[-8])),
                  arrowprops={"arrowstyle": "->", "color": orange})
    left.text(.2, 2.4, r"$\pi/4$", color=orange)
    left.text(-5.5, -1.8, r"$|z|=|iz|=5$" + "\n" +
              r"$|(1+i)z|=5\sqrt{2}$", fontsize=11)
    left.set(title="One point: a quarter-turn or a scaled eighth-turn",
             xlim=(-6, 6), ylim=(-3.2, 8.8), xticks=[-4, -1, 0, 3],
             yticks=[0, 3, 4, 7])

    t = np.linspace(-2, 2, 100)
    for level in range(-2, 3):
        for curve in (level+1j*t, t+1j*level):
            right.plot(curve.real, curve.imag, color=blue, lw=1.0, alpha=.45)
            transformed = multiplier*curve
            right.plot(transformed.real, transformed.imag,
                       color=orange, lw=1.3, alpha=.7)
    theta = np.linspace(0, 2*np.pi, 400)
    right.plot(np.cos(theta), np.sin(theta), color=blue, lw=2)
    right.plot(np.sqrt(2)*np.cos(theta), np.sqrt(2)*np.sin(theta),
               color=orange, lw=2)
    arrow(right, 1+0j, blue, r"$1$", (0, -23))
    arrow(right, 1+1j, orange, r"$1+i$", (8, 0))
    right.plot([], [], color=blue, label="Input grid and unit circle")
    right.plot([], [], color=orange, label=r"Image under $z\mapsto(1+i)z$")
    right.legend(loc="lower center", fontsize=9, framealpha=1)
    right.set(title=r"Every point: rotation $\pi/4$, scale $\sqrt{2}$",
              xlim=(-4.8, 4.8), ylim=(-4.8, 4.8),
              xticks=[-4, -2, 0, 2, 4], yticks=[-4, -2, 0, 2, 4])
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.axhline(0, color="#555555", lw=.9)
        ax.axvline(0, color="#555555", lw=.9)
        ax.set(xlabel="Real part", ylabel="Imaginary part")
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
