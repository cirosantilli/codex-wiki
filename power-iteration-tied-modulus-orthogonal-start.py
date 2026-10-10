"""Exact power-iteration obstructions and sign alternation.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def axes_frame(ax):
    theta = np.linspace(0, 2 * np.pi, 250)
    ax.plot(np.cos(theta), np.sin(theta), color="0.82", lw=1)
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8)
    ax.set(xlim=(-1.18, 1.18), ylim=(-1.15, 1.15), xticks=[-1, 0, 1], yticks=[-1, 0, 1])
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)


def arrow(ax, q, color, style="-"):
    ax.annotate("", xy=q, xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": color, "linestyle": style})


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
    fig, panels = plt.subplots(1, 3, figsize=(10.8, 4.8))
    fig.subplots_adjust(left=0.055, right=0.985, top=0.79, bottom=0.27, wspace=0.16)
    fig.suptitle("Power iteration: two failures and one successful direction limit", fontsize=14)
    for ax in panels:
        axes_frame(ax)
        ax.set_xlabel("first coordinate")
    panels[0].set_ylabel("second coordinate")
    blue, orange, green = "#285a9b", "#c66a18", "#23804c"
    tied, absent, alternating = panels
    z = np.array([1, 1]) / np.sqrt(2)
    arrow(tied, z, blue)
    arrow(tied, z * [1, -1], orange)
    tied.text(-1.08, 0.87, "even k", color=blue)
    tied.text(-1.08, -0.9, "odd k", color=orange)
    tied.set_title("Tied moduli: λ = 2, −2\nD = diag(2, −2)", fontsize=11)
    tied.text(0.5, -0.29, "Two distinct lines keep cycling\nρₖ = 0;  ‖rₖ‖₂ = 2", ha="center",
              va="top", transform=tied.transAxes, fontsize=10)
    absent.plot([-1, 1], [-1, 1], "--", color=green)
    arrow(absent, np.array([1, -1]) / np.sqrt(2), blue)
    absent.text(-1.07, 0.82, "target λ = 3", color=green)
    absent.text(-1.07, -0.88, "all k: λ = 1", color=blue)
    absent.set_title("Missing dominant component\nA = [[2, 1], [1, 2]]", fontsize=11)
    absent.text(0.5, -0.29, "Orthogonal start stays fixed\nρₖ = 1;  ‖rₖ‖₂ = 0", ha="center",
                va="top", transform=absent.transAxes, fontsize=10)
    alternating.axhline(0, color=green, linestyle="--", lw=1.7)
    for k in range(4):
        q = np.array([(-1.0) ** k, 3.0 ** (-k)]) / np.sqrt(1 + 3.0 ** (-2 * k))
        color = blue if k % 2 == 0 else orange
        arrow(alternating, q, color)
        offsets = [(1, 8), (-20, 8), (-20, 9), (0, -18)]
        alternating.annotate(f"k = {k}", xy=q, xytext=offsets[k],
                             textcoords="offset points", fontsize=9, color=color)
    alternating.set_title("Negative dominant λ = −3\nN = diag(−3, 1)", fontsize=11)
    alternating.text(0.5, -0.29, "Signs alternate; direction converges\nUnwanted component ratio = 3⁻ᵏ", ha="center",
                     va="top", transform=alternating.transAxes, fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
