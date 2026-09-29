"""Draw matching-pennies-best-responses.png in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, orange = "#2166a5", "#be4c20"
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.8), facecolor="white")
    t = np.linspace(0, 1, 201)
    row, column, response = axes
    row.plot(t, 2 * t - 1, color=blue, lw=2.5, label="Choose H")
    row.plot(t, 1 - 2 * t, color=orange, lw=2.5, linestyle="--", label="Choose T")
    column.plot(t, 1 - 2 * t, color=blue, lw=2.5, label="Choose H")
    column.plot(t, 2 * t - 1, color=orange, lw=2.5, linestyle="--", label="Choose T")
    for ax, variable, title in (
        (row, "q: column probability of H", "Row player: wants to match"),
        (column, "p: row probability of H", "Column player: wants to differ"),
    ):
        ax.set(xlim=(0, 1), ylim=(-1.15, 1.15), xlabel=variable,
               ylabel="Expected payoff of a pure choice", title=title)
        ax.axvline(.5, lw=1, color="#64748b", linestyle=":")
        ax.scatter([.5], [0], color="#202933", s=45, zorder=5)
        ax.annotate("H and T tie", (.5, 0), xytext=(.5, .45),
                    ha="center", arrowprops={"arrowstyle": "->", "color": "#64748b"})
        ax.set_xticks([0, .5, 1], ["0", "1/2", "1"])
        ax.set_yticks([-1, 0, 1])
        ax.legend(loc="lower center", frameon=False, ncol=2, fontsize=10)

    # x = p and y = q. Horizontal/vertical ties include their entire intervals.
    response.plot([0, 0, 1, 1], [0, .5, .5, 1], color=blue,
                  lw=3, label="Row best responses", zorder=3)
    response.plot([0, .5, .5, 1], [1, 1, 0, 0], color=orange,
                  lw=3, linestyle="--", label="Column best responses", zorder=4)
    response.scatter([.5], [.5], color="#202933", s=65, zorder=5)
    response.annotate("Unique equilibrium\n(p, q) = (1/2, 1/2)", (.5, .5),
                      xytext=(.48, .16), ha="center", fontsize=10, zorder=6,
                      bbox={"facecolor": "white", "edgecolor": "none", "pad": 2},
                      arrowprops={"arrowstyle": "->", "color": "#202933"})
    response.set(xlim=(-.04, 1.04), ylim=(-.04, 1.04),
                 xlabel="p: row probability of H", ylabel="q: column probability of H",
                 title="Both players must be best responses")
    response.set_xticks([0, .5, 1], ["0", "1/2", "1"])
    response.set_yticks([0, .5, 1], ["0", "1/2", "1"])
    response.legend(loc="upper center", bbox_to_anchor=(.5, -.22),
                    frameon=False, fontsize=10)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(color="#e5e7eb", lw=.7)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Matching pennies: mixing removes a predictable target", fontsize=16, y=.96)
    fig.text(.5, .035, "Row payoff: +1 for matching, −1 for differing. Column payoff is its negative.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.055, right=.985, top=.79, bottom=.28, wspace=.48)
    fig.savefig("matching-pennies-best-responses.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
