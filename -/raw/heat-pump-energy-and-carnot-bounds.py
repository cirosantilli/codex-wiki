"""Generate heat-pump-energy-and-carnot-bounds.png in the current directory.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
All values are stipulated budgets or calculated reversible bounds, not data.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, (flow, ax) = plt.subplots(1, 2, figsize=(11, 5.4), dpi=110,
                                  gridspec_kw={"width_ratios": [1.08, 1]})
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.035, right=0.965, top=0.83, bottom=0.15, wspace=0.30)
    fig.suptitle("Moving heat: one budget, two useful outputs", fontsize=16, y=0.97)
    fig.text(0.5, 0.895, "Stipulated cycle at 280 K and 320 K; calculated bounds, not measured performance",
             ha="center", fontsize=10.5, color="#444444")
    cold, hot, work = "#2378aa", "#bd4529", "#8256a3"
    flow.set(xlim=(0, 10), ylim=(0, 10))
    flow.axis("off")
    flow.set_title("Energy per complete cycle", fontsize=12, pad=13)

    def box(x, y, w, h, color, text):
        flow.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                                     linewidth=1.5, edgecolor=color, facecolor="white"))
        flow.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=color)

    box(0.5, 8.05, 8.8, 1.12, hot, "Hot reservoir: 320 K")
    box(0.5, 0.8, 8.8, 1.12, cold, "Cold reservoir: 280 K")
    box(2.3, 4.5, 4.4, 1.25, "#444444", "Cyclic machine\nno energy stored")
    # Shaft widths are exactly proportional to the three energy magnitudes.
    for x, y, dx, dy, magnitude, color in [
        (4.5, 2.12, 0, 2.2, 3, cold),
        (4.5, 5.93, 0, 1.9, 4, hot),
        (9.45, 5.12, -2.5, 0, 1, work),
    ]:
        flow.add_patch(FancyArrow(x, y, dx, dy, width=0.16 * magnitude,
                                 head_width=0.16 * magnitude + 0.30,
                                 head_length=0.37, length_includes_head=True,
                                 color=color))
    flow.text(0.35, 3.15, "$Q_c=3$ kJ\nuseful cooling", color=cold, va="center")
    flow.text(0.35, 6.95, "$Q_h=4$ kJ\nuseful heating", color=hot, va="center")
    flow.text(8.3, 6.12, "$W=1$ kJ\nwork input", color=work, ha="center")
    flow.text(4.9, 0.05, "$4=3+1$ kJ     COP$_{\\rm r}=3$     COP$_{\\rm heat}=4$",
              ha="center", fontsize=11)

    lift = np.linspace(10.0, 80.0, 351)
    cop_r = 280.0 / lift
    cop_h = (280.0 + lift) / lift
    ax.plot(lift, cop_h, color=hot, lw=2.5, label="Heating bound: (280 + ΔT)/ΔT")
    ax.plot(lift, cop_r, color=cold, lw=2.5, label="Cooling bound: 280/ΔT")
    ax.fill_between(lift, cop_r, cop_h, color="#f3dfd5", zorder=0)
    ax.set(xlim=(10, 80), ylim=(0, 32), xlabel="Reservoir temperature lift ΔT (K)",
           ylabel="Coefficient of performance (dimensionless)")
    ax.set_title("Carnot bounds with cold side fixed at 280 K", fontsize=12, pad=13)
    ax.grid(alpha=0.18)
    ax.axvline(40, color="#777777", ls=":", lw=1)
    ax.scatter([40, 40], [8, 7], c=[hot, cold], s=40, zorder=5)
    ax.annotate("Heating: 8", (40, 8), (48, 14), color=hot,
                arrowprops={"arrowstyle": "-", "color": hot})
    ax.annotate("Cooling: 7", (40, 7), (48, 9.5), color=cold,
                arrowprops={"arrowstyle": "-", "color": cold})
    ax.text(43, 20, "Heating − cooling = 1\nLarger lift → lower bounds", fontsize=10)
    ax.legend(loc="upper right", frameon=False, fontsize=9, handlelength=1.8)
    fig.text(0.5, 0.035, "COP above 1 counts heat extracted elsewhere as well as the supplied work.",
             ha="center", fontsize=11)
    fig.savefig("heat-pump-energy-and-carnot-bounds.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
