"""Original shear/translation illustration; write the PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media to create the repository's image asset.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def cut_closed(points):
    following = np.roll(points, -1, axis=0)
    result = np.empty((2 * len(points), points.shape[1]))
    result[0::2] = 0.75 * points + 0.25 * following
    result[1::2] = 0.25 * points + 0.75 * following
    return result


def transform(points):
    shear = np.array([[1., 0.5], [0., 1.]])
    translation = np.array([1., -1.])
    return points @ shear.T + translation


def close(points):
    return np.vstack((points, points[0]))


def main():
    points = np.array([[0., 0.], [4., 0.], [4., 2.], [0., 2.]])
    cut = cut_closed(points)
    mapped = transform(points)
    cut_after_map = cut_closed(mapped)
    map_after_cut = transform(cut)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=120)
    fig.patch.set_facecolor("white")
    for ax, polygon, refined in zip(axes, (points, mapped), (cut, cut_after_map)):
        ax.set_facecolor("white")
        old = close(polygon)
        new = close(refined)
        ax.plot(old[:, 0], old[:, 1], "--s", color="#777777",
                lw=1.5, markersize=5, label="Control polygon")
        ax.plot(new[:, 0], new[:, 1], color="#17679b", lw=1.8)
        ax.scatter(refined[:, 0], refined[:, 1], color="#17679b", s=28,
                   zorder=4, label="Cut after transforming" if ax is axes[1]
                   else "One Chaikin refinement")
        ax.set_aspect("equal")
        ax.set_xlabel("x")
        ax.set_ylabel("y", labelpad=1)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(color="#eeeeee", lw=0.6)
        ax.set_axisbelow(True)
    axes[0].set(xlim=(-0.5, 4.5), ylim=(-0.6, 2.6),
                xticks=range(5), yticks=[0, 1, 2])
    axes[1].set(xlim=(0.5, 6.5), ylim=(-1.6, 1.6),
                xticks=range(1, 7), yticks=[-1, 0, 1])
    axes[0].set_title("Original rectangle and its cut", fontsize=12)
    axes[1].set_title("Sheared, translated polygon: both routes agree", fontsize=12)
    axes[1].scatter(map_after_cut[:, 0], map_after_cut[:, 1], s=115,
                    facecolors="none", edgecolors="#c76a16", lw=1.8,
                    zorder=3, label="Transform after cutting")
    axes[0].annotate(r"$Q_1=(4,\,1/2)$", xy=cut[2], xytext=(2.0, 0.7),
                     fontsize=10, arrowprops=dict(arrowstyle="->", color="#444444"))
    axes[1].annotate(r"$T(Q_1)=(21/4,\,-1/2)$", xy=map_after_cut[2],
                     xytext=(2.0, -0.3), fontsize=10,
                     arrowprops=dict(arrowstyle="->", color="#444444"))
    axes[0].legend(loc="lower center", bbox_to_anchor=(0.5, -0.56),
                   frameon=False, fontsize=10)
    axes[1].legend(loc="lower center", bbox_to_anchor=(0.5, -0.56),
                   frameon=False, fontsize=10)
    fig.suptitle(r"$T(x,y)=(x+y/2+1,\ y-1)$: $T(S(P))=S(T(P))$",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.035, "The orange rings coincide with all eight blue dots.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.065, right=0.985, top=0.79, bottom=0.32, wspace=0.22)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
