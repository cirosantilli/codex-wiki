"""Generate heat-engine-efficiency-temperature-model.png in the current directory.

Run from _media with MPLBACKEND=Agg and
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
The lower curve is stipulated at 80% of the reversible bound, not measured.
"""

from fractions import Fraction

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np


def main():
    t_cold = 300
    t_hot = np.linspace(t_cold, 900, 401)
    carnot = 1 - t_cold / t_hot
    model = 0.8 * carnot
    for temperature, expected in [(300, Fraction(0)), (450, Fraction(1, 3)),
                                   (600, Fraction(1, 2)), (900, Fraction(2, 3))]:
        assert 1 - Fraction(t_cold, temperature) == expected
    assert np.all(model <= carnot) and np.all(model >= 0)
    assert np.all(np.diff(carnot) > 0)

    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.2, 5.6), dpi=110, facecolor="white")
    ax.fill_between(t_hot, carnot, 0.8, color="#f6e6e5")
    ax.fill_between(t_hot, 0, carnot, color="#edf3f8")
    ax.plot(t_hot, carnot, color="#204a87", lw=2.5,
            label=r"Reversible bound: $\eta_C=1-300/T_h$")
    ax.plot(t_hot, model, color="#287749", lw=2.3, ls="--",
            label=r"Stipulated model: $\eta=0.8\eta_C$")
    ax.plot([600, 600], [0, 0.5], color="#666666", lw=1.1, ls=":")
    ax.scatter([600, 600], [0.5, 0.4], s=48,
               c=["#204a87", "#287749"], zorder=4)
    ax.annotate("600 K: 50%", (600, 0.5), xytext=(655, 0.48),
                fontsize=11, color="#204a87",
                arrowprops={"arrowstyle": "-", "color": "#204a87"})
    ax.annotate("600 K: 40%", (600, 0.4), xytext=(655, 0.31),
                fontsize=11, color="#287749",
                arrowprops={"arrowstyle": "-", "color": "#287749"})
    ax.text(735, 0.71, "Above bound: forbidden", color="#922f2f",
            ha="center", fontsize=11)
    ax.text(735, 0.15, "Below the bound", color="#35536c", ha="center", fontsize=11)
    ax.set(xlim=(300, 900), ylim=(0, 0.8),
           xlabel=r"Hot-reservoir temperature $T_h$ (K)",
           ylabel=r"Thermal efficiency $\eta$",
           title="Fixed cold reservoir at 300 K")
    ax.set_xticks([300, 450, 600, 750, 900])
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.grid(axis="y", alpha=0.18)
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 1.0), fontsize=10,
              framealpha=1, facecolor="white", edgecolor="#dddddd")
    fig.text(0.5, 0.027,
             "Calculated curves, not data • Cyclic device • Heat exchange only with two fixed reservoirs",
             ha="center", fontsize=9.5)
    fig.subplots_adjust(left=0.12, right=0.965, top=0.89, bottom=0.18)
    fig.savefig("heat-engine-efficiency-temperature-model.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
