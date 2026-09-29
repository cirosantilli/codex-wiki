"""Illustrate addition and conjugation at z = 3 + 4i.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write the matching opaque PNG to the current working directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, label, offset):
    ax.annotate("", (end.real, end.imag), (start.real, start.imag),
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2.4})
    ax.annotate(label, (end.real, end.imag), xytext=offset,
                textcoords="offset points", color=color, fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    blue, orange, purple = "#2468a0", "#b65718", "#81449b"
    z, w = 3 + 4j, 1 + 1j
    assert z + w == 4 + 5j
    assert z.conjugate() == 3 - 4j
    assert abs(z) == abs(z.conjugate()) == 5
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.8), dpi=120,
                             constrained_layout=True)
    fig.patch.set_facecolor("white")
    left, right = axes
    arrow(left, 0j, z, blue, r"$z=3+4i$", (-83, 2))
    arrow(left, z, z + w, orange, r"$z+w=4+5i$", (-68, 9))
    arrow(left, 0j, w, orange, r"$w=1+i$", (9, -5))
    left.plot([w.real, (z+w).real], [w.imag, (z+w).imag],
              color=blue, ls="--", lw=1.4)
    left.plot([z.real, z.real, 0], [0, z.imag, z.imag],
              color=blue, ls=":", lw=1.1)
    left.set(title="Addition: follow one arrow, then the other",
             xlim=(-.7, 5.8), ylim=(-.7, 5.8),
             xticks=range(6), yticks=range(6))
    theta = np.linspace(0, 2*np.pi, 400)
    right.plot(5*np.cos(theta), 5*np.sin(theta), color="#888888",
               lw=1.2, ls="--")
    right.plot([3, 3], [-4, 4], color="#999999", lw=1.2, ls=":")
    arrow(right, 0j, z, blue, r"$z=3+4i$", (-40, 13))
    arrow(right, 0j, z.conjugate(), purple, r"$\overline{z}=3-4i$", (-58, -24))
    right.text(1.2, 1.2, r"$|z|=5$", color=blue, rotation=53)
    right.text(1.2, -1.7, r"$|\overline{z}|=5$", color=purple, rotation=-53)
    right.set(title="Conjugation: reflect across the real axis",
              xlim=(-5.8, 5.8), ylim=(-5.8, 5.8),
              xticks=[-5, 0, 3, 5], yticks=[-5, -4, 0, 4, 5])
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.axhline(0, color="#555555", lw=.9)
        ax.axvline(0, color="#555555", lw=.9)
        ax.grid(alpha=.17)
        ax.set(xlabel="Real part", ylabel="Imaginary part")
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
