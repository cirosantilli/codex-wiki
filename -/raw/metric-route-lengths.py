"""Draw metric-route-lengths.png in the current directory.

Uses the repository's NumPy/Matplotlib environment; tested with Python 3.14.4.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    origin, corner, endpoint = np.array([(0, 0), (3, 0), (3, 4)], dtype=float)
    norms = [1, 2, np.inf]
    direct = [np.linalg.norm(endpoint - origin, p) for p in norms]
    via = [np.linalg.norm(corner - origin, p) + np.linalg.norm(endpoint - corner, p) for p in norms]
    assert np.allclose(direct, [7, 5, 4])
    assert np.allclose(via, [7, 7, 7])
    # A straight segment's length is the same sum at every subdivision.
    sampled_segment = np.linspace(origin, endpoint, 101)
    for p, length in zip(norms, direct):
        assert np.isclose(np.linalg.norm(np.diff(sampled_segment, axis=0), ord=p, axis=1).sum(), length)
    blue, orange = "#17678b", "#b3571b"
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.3), facecolor="white")
    titles = ["Manhattan / L1", "Euclidean / L2", "Chebyshev / L∞"]
    for ax, title, length, detour in zip(axes, titles, direct, via):
        ax.set_facecolor("white")
        ax.plot([0, 3, 3], [0, 0, 4], color=orange, lw=3.5, zorder=3)
        ax.plot([0, 3], [0, 4], color=blue, lw=3, linestyle="--", zorder=4)
        ax.scatter([0, 3, 3], [0, 0, 4], s=35, color="#20272d", zorder=5)
        ax.annotate("O = (0, 0)", origin, xytext=(-8, -15), textcoords="offset points", ha="left", fontsize=11)
        ax.annotate("Q = (3, 0)", corner, xytext=(8, -15), textcoords="offset points", ha="right", fontsize=11)
        ax.annotate("P = (3, 4)", endpoint, xytext=(-8, 12), textcoords="offset points", ha="right", fontsize=11)
        ax.text(1.5, 0.15, "3", color=orange, ha="center", fontsize=14, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
        ax.text(3.2, 2, "4", color=orange, va="center", fontsize=14)
        ax.text(1.15, 2.0, f"length {length:g}", color=blue, rotation=np.degrees(np.arctan2(4, 3)), ha="center", va="bottom", fontsize=12)
        ax.set(xlim=(-0.55, 3.65), ylim=(-0.7, 4.65), xticks=[0, 1, 2, 3], yticks=[0, 1, 2, 3, 4])
        ax.set_aspect("equal")
        ax.grid(color="#dce1e5", lw=0.6, zorder=0)
        ax.set_xlabel("x", labelpad=0)
        ax.set_ylabel("y", rotation=0, labelpad=8)
        ax.set_title(title, pad=12)
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#b7bec3")
        ax.text(0.5, -0.25, f"Direct: {length:g}    Via Q: {detour:g}", transform=ax.transAxes, ha="center", fontsize=13)
        comparison = "=" if length == detour else r"\leq"
        ax.text(0.5, -0.35, rf"${length:g} {comparison} 3+4=7$", transform=ax.transAxes, ha="center", fontsize=14)
    fig.suptitle("Same endpoints, same routes, different lengths", fontsize=18, y=0.98)
    fig.legend(
        handles=[Line2D([0], [0], color=blue, lw=3, linestyle="--", label="Direct segment"), Line2D([0], [0], color=orange, lw=3.5, label="Route through Q")],
        loc="upper center", bbox_to_anchor=(0.5, 0.92), ncol=2, frameon=False,
    )
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.29, top=0.78, wspace=0.35)
    fig.savefig("metric-route-lengths.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
