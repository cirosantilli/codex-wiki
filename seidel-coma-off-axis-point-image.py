"""Uniform-area pupil samples mapped into geometrical coma spot diagrams.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; writes an opaque white PNG to the working directory.
Each point has equal pupil-area weight. No smoothing or diffraction PSF.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def ray_map(u, v, h):
    return h * (3 * u * u + v * v), 2 * h * u * v


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    count = 7000
    index = np.arange(count // 4)
    rho = np.sqrt((index + .5) / len(index))
    theta = np.random.default_rng(831).uniform(0, 2*np.pi, len(index))
    u0, v0 = rho * np.cos(theta), rho * np.sin(theta)
    # Four symmetric azimuths per equal-area radial sample preserve the
    # exact centroid while avoiding a visible spiral sampling pattern.
    u = np.concatenate([u0, -u0, v0, -v0])
    v = np.concatenate([v0, -v0, -u0, u0])
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.8), sharex=True, sharey=True)
    fig.subplots_adjust(left=.09, right=.98, bottom=.14, top=.84, hspace=.5, wspace=.3)
    fig.suptitle("Comet-like geometrical point images as field angle changes", y=.98)
    fig.text(.5, .91, r"$w=h\,u(u^2+v^2)$;  same pupil samples and image scale in every panel",
             ha="center")
    for ax, h in zip(axes.flat, [0, .5, 1, -1]):
        x, y = ray_map(u, v, h)
        if h == 0:
            ax.plot(0, 0, "o", color="#2458a4", ms=5)
            ax.text(.2, .7, "All rays coincide.\nDiffraction is omitted.", fontsize=10)
        else:
            ax.scatter(x, y, s=.6, alpha=.32, color="#2458a4", linewidths=0)
            t = np.linspace(0, 2*np.pi, 500)
            ax.plot(h*(2+np.cos(t)), h*np.sin(t), color="#b1b1b1", lw=.8)
        ax.plot(h, 0, "+", color="#c85518", ms=10, mew=1.7,
                label=r"area-weighted centroid $(h,0)$")
        ax.set(xlim=(-3.3, 3.3), ylim=(-1.25, 1.25), title=fr"Normalized signed field $h={h:g}$")
        ax.set_aspect("equal")
        ax.axhline(0, color="#dddddd", lw=.8, zorder=0)
        ax.axvline(0, color="#dddddd", lw=.8, zorder=0)
    for ax in axes[:, 0]:
        ax.set_ylabel("Y: normalized error")
    for ax in axes[1]:
        ax.set_xlabel("X: normalized image error")
    fig.text(.5, .045, "Blue: equal-weight rays from a uniform circular pupil; orange +: centroid.\n"
             "An illustrative geometrical spot diagram, not a measured or diffraction PSF.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
