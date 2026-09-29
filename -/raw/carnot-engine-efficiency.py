"""Draw a reversible 600 K / 300 K engine and its temperature-entropy cycle.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
The PNG is written to the current working directory.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np


def main():
    hot, cold, heat_in = 600.0, 300.0, 1000.0
    efficiency = 1.0 - cold / hot
    work = heat_in * efficiency
    heat_out = heat_in - work
    entropy_width = heat_in / hot
    assert np.isclose(heat_in / hot, heat_out / cold)
    assert np.isclose((hot - cold) * entropy_width, work)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10.5, 5.2), dpi=120)
    layout = fig.add_gridspec(1, 2, width_ratios=[1.12, 1], wspace=0.30)
    flow = fig.add_subplot(layout[0, 0])
    cycle = fig.add_subplot(layout[0, 1])
    fig.suptitle("Carnot engine: energy conserved, total entropy unchanged", fontsize=15)
    fig.subplots_adjust(left=0.04, right=0.97, bottom=0.19, top=0.82)
    hot_color, cold_color, work_color = "#b44324", "#226a9e", "#247657"
    flow.set_xlim(0, 10)
    flow.set_ylim(0, 10)
    flow.axis("off")
    flow.set_title("One reversible cycle", pad=16)

    def box(x, y, width, height, label, color, fill):
        flow.add_patch(FancyBboxPatch((x, y), width, height,
                       boxstyle="round,pad=0.08,rounding_size=0.15",
                       facecolor=fill, edgecolor=color, linewidth=1.8))
        flow.text(x + width / 2, y + height / 2, label,
                  ha="center", va="center", color=color)

    def arrow(start, end, color):
        flow.annotate("", xy=end, xytext=start,
                      arrowprops={"arrowstyle": "-|>", "color": color,
                                  "lw": 3, "mutation_scale": 18})

    box(0.8, 8.0, 6.6, 1.4, "Hot reservoir: 600 K", hot_color, "#fff1e9")
    box(1.7, 4.0, 3.7, 1.6, "Reversible engine\n" + r"$\Delta U=\Delta S=0$",
        "#3e4754", "#f3f5f7")
    box(0.8, 0.2, 6.6, 1.4, "Cold reservoir: 300 K", cold_color, "#edf5fc")
    arrow((3.55, 7.95), (3.55, 5.65), hot_color)
    flow.text(3.9, 6.8, rf"$Q_h={heat_in:.0f}$ J", color=hot_color, va="center")
    arrow((3.55, 3.95), (3.55, 1.65), cold_color)
    flow.text(3.9, 2.8, rf"$Q_c={heat_out:.0f}$ J", color=cold_color, va="center")
    arrow((5.5, 4.8), (9.45, 4.8), work_color)
    flow.text(7.45, 5.35, rf"$W={work:.0f}$ J", color=work_color, ha="center")
    flow.text(7.45, 4.0, "Work output", color=work_color, ha="center")

    cycle.set_title("Temperature-entropy cycle", pad=16)
    cycle.add_patch(Rectangle((0, cold), entropy_width, hot - cold,
                             facecolor="#e6f2ec", edgecolor="none"))
    vertices = [(0, hot), (entropy_width, hot), (entropy_width, cold),
                (0, cold), (0, hot)]
    colors = [hot_color, "#545d69", cold_color, "#545d69"]
    labels = ["1", "2", "3", "4"]
    for start, end, color in zip(vertices[:-1], vertices[1:], colors):
        cycle.plot([start[0], end[0]], [start[1], end[1]], color=color, lw=2.2)
        middle = np.array(start) * 0.35 + np.array(end) * 0.65
        before = np.array(start) * 0.65 + np.array(end) * 0.35
        cycle.annotate("", xy=middle, xytext=before,
                       arrowprops={"arrowstyle": "-|>", "lw": 2,
                                   "color": color, "mutation_scale": 15})
    for (x, y), label in zip(vertices[:-1], labels):
        cycle.plot(x, y, "o", color="#39424e", ms=4)
        cycle.annotate(label, (x, y), xytext=(-12 if x == 0 else 7,
                       7 if y == hot else -16), textcoords="offset points")
    cycle.text(entropy_width / 2, 450, "Enclosed area\n" + rf"$W={work:.0f}$ J",
               ha="center", va="center", color=work_color)
    cycle.text(entropy_width / 2, 645, "Heat absorbed", ha="center", color=hot_color)
    cycle.text(entropy_width / 2, 248, "Heat rejected", ha="center", color=cold_color)
    cycle.set_xlim(-0.25, entropy_width + 0.3)
    cycle.set_ylim(205, 695)
    cycle.set_yticks([300, 450, 600])
    cycle.set_xticks([0, entropy_width], ["0", "5/3"])
    cycle.set_xlabel(r"Entropy relative to state 1 (J K$^{-1}$)", labelpad=10)
    cycle.set_ylabel("Temperature (K)")
    cycle.grid(axis="y", alpha=0.18)
    fig.text(0.5, 0.06, r"$\eta_C=1-300/600=50\%$     |     "
             r"$\Delta S_h=-5/3$ J/K,  $\Delta S_c=+5/3$ J/K", ha="center")
    fig.savefig("carnot-engine-efficiency.png", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
