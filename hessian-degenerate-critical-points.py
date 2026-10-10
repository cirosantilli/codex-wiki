"""Identical zero Hessians can conceal different quartic behavior; output to CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.linspace(-1.2, 1.2, 301)
    x, y = np.meshgrid(values, values)
    examples = [
        (x**4+y**4, r"$f_+=x^4+y^4$", "Strict minimum", "Blues"),
        (x**4-y**4, r"$f_-=x^4-y^4$", "Saddle", "RdBu_r"),
    ]
    assert np.all(x**4+y**4 >= 0)
    probe = np.array([.01, .1, .5, 1.])
    assert np.all(probe**4 > 0) and np.all(-probe**4 < 0)
    for sign in [1, -1]:
        hessian_at_origin = np.diag([12*0.**2, sign*12*0.**2])
        assert np.all(hessian_at_origin == 0)
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 5.6), dpi=110)
    fig.patch.set_facecolor("white")
    for i, (ax, (z, formula, label, cmap)) in enumerate(zip(axes, examples)):
        levels = [.02, .08, .25, .6, 1.2, 2.4] if i == 0 else [
            -1.5, -.6, -.15, 0, .15, .6, 1.5]
        fill = np.linspace(0, 4.2, 25) if i == 0 else np.linspace(-2.1, 2.1, 25)
        ax.contourf(x, y, z, levels=fill, cmap=cmap, alpha=.65, extend="both")
        contour = ax.contour(x, y, z, levels=levels, colors="#343434",
                             linewidths=.8)
        ax.clabel(contour, inline=True, fontsize=9, fmt="%g")
        ax.axhline(0, color="#777777", lw=.7, ls="--")
        ax.axvline(0, color="#777777", lw=.7, ls="--")
        ax.plot(0, 0, "ko", ms=5)
        ax.set_aspect("equal")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(formula + "\n" + label, fontsize=13, pad=10)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
    fig.suptitle("Both Hessians at the origin are the zero matrix", fontsize=16)
    fig.text(.5, .06,
             "Second derivatives vanish at the origin; fourth-order terms determine "
             "the different local geometry.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.065, right=.98, bottom=.16, top=.78, wspace=.22)
    fig.savefig(Path.cwd() / "hessian-degenerate-critical-points.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
