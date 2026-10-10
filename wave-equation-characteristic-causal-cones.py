"""Synthetic causal geometry; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG basename in the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (back, forward) = plt.subplots(1, 2, figsize=(11.6, 5.7))
    x_star, t_star, c = 0.5, 1.5, 1.0
    t = np.linspace(0, t_star, 201)
    lo = x_star - c * (t_star - t)
    hi = x_star + c * (t_star - t)
    back.fill_betweenx(t, lo, hi, color="#dbeaf3")
    back.plot(lo, t, color="#1976a3", lw=2)
    back.plot(hi, t, color="#1976a3", lw=2)
    back.plot([-1, 2], [0, 0], color="#c77719", lw=5, solid_capstyle="round", zorder=4)
    back.scatter([-1, 2, x_star], [0, 0, t_star], color="#242424", zorder=5)
    back.annotate("Observation (0.5, 1.5)", (x_star, t_star), (-1.6, 1.83),
                  arrowprops={"arrowstyle": "->", "color": "#333333"})
    back.text(0.5, 0.46, "Backward cone", ha="center", color="#235f82")
    back.text(0.5, -0.31, "Initial-data interval [−1, 2]", ha="center", color="#995810")
    back.annotate("x − t = −1", (-0.65, 0.35), (-2.55, 0.8),
                  arrowprops={"arrowstyle": "->", "color": "#1976a3"}, color="#1976a3", fontsize=10)
    back.annotate("x + t = 2", (1.65, 0.35), (1.6, 1.05),
                  arrowprops={"arrowstyle": "->", "color": "#1976a3"}, color="#1976a3", fontsize=10)
    back.set_title("Which initial data can affect an observation?", fontsize=12, pad=12)
    back.set_xlim(-2.8, 3.3)
    back.set_ylim(-0.43, 2.15)
    back.set_xticks((-2, -1, 0, 0.5, 1, 2, 3))
    back.set_yticks((0, 0.5, 1, 1.5, 2))
    back.set_xlabel("Position x")
    back.set_ylabel("Time t")

    t = np.linspace(0, 2, 301)
    forward.fill_betweenx(t, -1 - t, 1 + t, color="#edf3e6", label="Possible influence")
    forward.fill_betweenx(t, -1 - t, 1 - t, color="#f1b6a8", alpha=0.9, label="Left-pulse support")
    forward.fill_betweenx(t, -1 + t, 1 + t, color="#a9cee3", alpha=0.8, label="Right-pulse support")
    forward.plot(-1 - t, t, color="#63834c", lw=2, linestyle="--")
    forward.plot(1 + t, t, color="#63834c", lw=2, linestyle="--")
    forward.plot([-1, 1], [0, 0], color="#c77719", lw=5, zorder=4)
    forward.axhline(1.5, color="#777777", lw=1, linestyle=":")
    forward.text(0, 1.82, "g = 0:\ncentral gap", ha="center", fontsize=10)
    forward.text(-2.7, 0.75, "u = 0", ha="center", color="#555555")
    forward.text(2.7, 0.75, "u = 0", ha="center", color="#555555")
    forward.annotate("−1 − t", (-2.65, 1.65), (-3.45, 2.09), color="#4f6a3c",
                     arrowprops={"arrowstyle": "->", "color": "#63834c"}, fontsize=10)
    forward.annotate("1 + t", (2.65, 1.65), (2.4, 2.09), color="#4f6a3c",
                     arrowprops={"arrowstyle": "->", "color": "#63834c"}, fontsize=10)
    forward.text(0, -0.31, "Initial support [−1, 1]", ha="center", color="#995810")
    forward.set_title("Where can a compact disturbance reach?", fontsize=12, pad=12)
    forward.set_xlim(-3.6, 3.6)
    forward.set_ylim(-0.43, 2.3)
    forward.set_xticks((-3, -2, -1, 0, 1, 2, 3))
    forward.set_yticks((0, 0.5, 1, 1.5, 2))
    forward.set_xlabel("Position x")
    forward.set_ylabel("Time t")
    for ax in (back, forward):
        ax.grid(alpha=0.16)
    handles, labels = forward.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.075),
               ncol=3, frameon=False, fontsize=10)
    fig.suptitle("Characteristic cones and finite propagation (c = 1)", fontsize=16, y=0.97)
    fig.text(0.5, 0.03, "Synthetic ideal-PDE geometry. Colored bands: f(x) = b(x), g(x) = 0; outer bounds allow other data.",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.23, top=0.82, wspace=0.24)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
