"""A reflection about 2*x1+x2=0, with vector decomposition; output to CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    normal = np.array([2., 1.]) / np.sqrt(5)
    reflection = np.eye(2) - 2 * np.outer(normal, normal)
    source = np.array([3., 4.])
    image = reflection @ source
    foot = source - normal * (normal @ source)
    assert np.allclose(image, [-5, 0])
    assert np.allclose(foot, [-1, 2])
    assert np.allclose(reflection @ reflection, np.eye(2))
    assert np.isclose(np.linalg.norm(image), 5)
    assert np.isclose(normal @ foot, 0)
    fig, ax = plt.subplots(figsize=(8.2, 7.0), dpi=110)
    fig.patch.set_facecolor("white")
    theta = np.linspace(0, 2*np.pi, 401)
    ax.plot(5*np.cos(theta), 5*np.sin(theta), color="#b0b0b0",
            ls=":", lw=1.4, label="Equal-norm circle")
    t = np.linspace(-4, 4, 101)
    ax.plot(t, -2*t, color="#777777", lw=2, label=r"Mirror: $2x_1+x_2=0$")
    for end, color in [(source, "#245f9b"), (image, "#c56521")]:
        ax.annotate("", end, (0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=color,
                                    lw=2.5, mutation_scale=18))
    ax.plot([source[0], image[0]], [source[1], image[1]],
            color="#8b529f", ls="--", lw=1.7)
    ax.scatter([source[0], image[0], foot[0]], [source[1], image[1], foot[1]],
               c=["#245f9b", "#c56521", "#8b529f"], s=60, zorder=5)
    ax.text(source[0]+.2, source[1]+.15, "x = (3, 4)", color="#245f9b",
            fontsize=12)
    ax.text(image[0]-.6, image[1]-.7, "Hx = (−5, 0)", color="#c56521",
            fontsize=12)
    ax.annotate("Mirror component\n(−1, 2)", foot, (-3.8, 3.6),
                color="#8b529f", fontsize=11,
                arrowprops=dict(arrowstyle="->", color="#8b529f", lw=1))
    ax.annotate("", (2, 1), (0, 0),
                arrowprops=dict(arrowstyle="->", color="#8b529f", lw=1.5))
    ax.text(2.15, .8, "Normal direction", color="#8b529f", fontsize=10)
    ax.axhline(0, color="#777777", lw=.6)
    ax.axvline(0, color="#777777", lw=.6)
    ax.set_aspect("equal")
    ax.set_xlim(-6.4, 6.1)
    ax.set_ylim(-5.6, 5.6)
    ax.set_xlabel(r"$x_1$", fontsize=13)
    ax.set_ylabel(r"$x_2$", fontsize=13)
    ax.set_title("Householder reflection: one component changes sign", fontsize=14)
    ax.grid(alpha=.15)
    ax.legend(loc="lower right", fontsize=10)
    fig.text(.5, .035,
             "The two tips are equally far from the mirror; both vectors have norm 5.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.08, right=.98, bottom=.12, top=.9)
    fig.savefig(Path.cwd() / "householder-reflection-geometry.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
