"""Draw coordination-game-equilibria.png in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, orange, dark = "#2166a5", "#be4c20", "#202933"
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, (response, payoffs) = plt.subplots(1, 2, figsize=(10.4, 5.3), facecolor="white")

    # x = p and y = q. At ties, include every possible mixture.
    response.plot([0, 0, 1, 1], [0, .4, .4, 1], color=blue,
                  lw=3, label="Row best responses", zorder=3)
    response.plot([0, .6, .6, 1], [0, 0, 1, 1], color=orange,
                  lw=3, linestyle="--", label="Column best responses", zorder=4)
    response.scatter([0, .6, 1], [0, .4, 1], color=dark, s=65, zorder=5)
    for point, text, offset in (
        ((0, 0), "Both choose B", (.09, .12)),
        ((1, 1), "Both choose A", (.55, .87)),
        ((.6, .4), "Mixed equilibrium\n(p, q) = (3/5, 2/5)", (.48, .18)),
    ):
        response.annotate(text, point, xytext=offset, fontsize=10, zorder=6,
                          bbox={"facecolor": "white", "edgecolor": "none", "pad": 2},
                          arrowprops={"arrowstyle": "->", "color": "#64748b"})
    response.set(xlim=(-.04, 1.04), ylim=(-.04, 1.04),
                 xlabel="p: row probability of A", ylabel="q: column probability of A",
                 title="Three intersections = three equilibria")
    response.set_xticks([0, .6, 1], ["0", "3/5", "1"])
    response.set_yticks([0, .4, 1], ["0", "2/5", "1"])
    response.legend(loc="upper center", bbox_to_anchor=(.5, -.19),
                    frameon=False, fontsize=10)

    x = np.arange(3)
    payoffs.bar(x - .18, [3, 2, 1.2], width=.36, color=blue, label="Row player")
    payoffs.bar(x + .18, [2, 3, 1.2], width=.36, color=orange, label="Column player")
    for container in payoffs.containers:
        payoffs.bar_label(container, labels=["6/5" if v == 1.2 else f"{v:g}"
                                            for v in container.datavalues], padding=5)
    payoffs.set_xticks(x, ["Both A", "Both B", "Independent\nmixing"])
    payoffs.set(ylim=(0, 3.7), ylabel="Expected payoff",
                title="Coordination improves both players' payoffs")
    payoffs.legend(loc="upper center", ncol=2, frameon=False, fontsize=10)
    payoffs.set_yticks([0, 1, 2, 3])
    payoffs.text(.5, -.26, "At the mixed equilibrium,\nmeeting probability = 12/25",
                 transform=payoffs.transAxes, ha="center", fontsize=11)
    for ax in (response, payoffs):
        ax.set_facecolor("white")
        ax.grid(axis="y", color="#e5e7eb", lw=.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Coordination: mutual best responses can still waste shared gains", fontsize=15, y=.96)
    fig.text(.5, .035, "Payoff pairs (row, column): (3, 2) at A; (2, 3) at B; (0, 0) if apart.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.075, right=.98, top=.79, bottom=.29, wspace=.38)
    fig.savefig("coordination-game-equilibria.png", dpi=115,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
