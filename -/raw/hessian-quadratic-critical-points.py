"""Quadratic critical-point geometry; write PNG in the current directory."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.linspace(-1.5, 1.5, 301)
    x, y = np.meshgrid(values, values)
    q = x*x + 2*x*y + 3*y*y
    hessian = np.array([[2., 2.], [2., 6.]])
    eigenvalues, eigenvectors = np.linalg.eigh(hessian)
    assert np.allclose(eigenvalues, [4-2*np.sqrt(2), 4+2*np.sqrt(2)])
    assert np.allclose(q, (x+y)**2 + 2*y*y)
    assert np.allclose(hessian @ eigenvectors, eigenvectors * eigenvalues)
    samples = [
        (q, r"$q=x^2+2xy+3y^2$", "Strict minimum", "Blues"),
        (-q, r"$-q=-x^2-2xy-3y^2$", "Strict maximum", "Oranges_r"),
        (x*x-y*y, r"$s=x^2-y^2$", "Saddle", "RdBu_r"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(12.7, 4.8), dpi=110)
    fig.patch.set_facecolor("white")
    for i, (ax, (z, formula, label, cmap)) in enumerate(zip(axes, samples)):
        if i < 2:
            positive = np.array([.15, .35, .7, 1.4, 2.8, 5.6, 11.2])
            levels = positive if i == 0 else -positive[::-1]
            filled = np.linspace(0, 18, 25) if i == 0 else np.linspace(-18, 0, 25)
        else:
            levels = [-2, -1, -.5, 0, .5, 1, 2]
            filled = np.linspace(-2.3, 2.3, 25)
        ax.contourf(x, y, z, levels=filled, cmap=cmap, alpha=.6, extend="both")
        contour = ax.contour(x, y, z, levels=levels, colors="#343434",
                             linewidths=.75)
        ax.clabel(contour, inline=True, fontsize=8, fmt="%g")
        ax.plot(0, 0, "ko", ms=5)
        directions = eigenvectors.T if i < 2 else np.eye(2)
        for direction in directions:
            ax.plot([-1.3*direction[0], 1.3*direction[0]],
                    [-1.3*direction[1], 1.3*direction[1]],
                    color="#6b447d", ls="--", lw=1.2)
        ax.set_aspect("equal")
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(formula + "\n" + label, fontsize=12, pad=10)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
    fig.suptitle("Hessian eigenvalue signs classify these quadratic critical points",
                 fontsize=15)
    fig.text(.5, .035,
             "All three have value 0 at the origin. "
             "Dashed lines show eigenvector directions; contour labels give function values.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.055, right=.98, bottom=.20, top=.78, wspace=.25)
    fig.savefig(Path.cwd() / "hessian-quadratic-critical-points.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
