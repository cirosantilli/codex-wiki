"""Generate heat-pump-bath-calorimetry.png in the current directory.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
The two finite baths and constant powers are a toy model, not measured data.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(11, 7), dpi=110, facecolor="white")
    gs = fig.add_gridspec(2, 2, height_ratios=[0.8, 1.3], left=0.075, right=0.965,
                          top=0.85, bottom=0.18, hspace=0.62, wspace=0.33)
    apparatus = fig.add_subplot(gs[0, :])
    temp = fig.add_subplot(gs[1, 0])
    energy = fig.add_subplot(gs[1, 1])
    cold, hot, work = "#2378aa", "#bd4529", "#8256a3"
    fig.suptitle("Two-bath calorimetry: measure storage, then correct heat leaks", fontsize=15, y=0.97)
    fig.text(0.5, 0.905, "Stipulated constant-rate model over 180 s — no measured data",
             ha="center", fontsize=11, color="#444444")
    apparatus.set(xlim=(0, 12), ylim=(0, 4))
    apparatus.axis("off")

    def box(x, y, w, h, color, text):
        apparatus.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                                         edgecolor=color, facecolor="white", lw=1.5))
        apparatus.text(x + w / 2, y + h / 2, text, color=color, ha="center", va="center")

    box(0.15, 0.55, 3.0, 2.1, cold, "Stirred cold bath\nprobe: $T_c(t)$\n$C_c=4.5$ kJ/K")
    box(4.85, 0.75, 2.3, 1.65, "#444444", "Cyclic machine\nno storage")
    box(8.85, 0.55, 3.0, 2.1, hot, "Stirred hot bath\nprobe: $T_h(t)$\n$C_h=4.5$ kJ/K")
    for start, end, color in [((3.35, 1.65), (4.65, 1.65), cold),
                               ((7.35, 1.65), (8.65, 1.65), hot),
                               ((6.0, 3.6), (6.0, 2.55), work),
                               ((1.65, 0.05), (1.65, 0.38), "#777777"),
                               ((10.35, 0.38), (10.35, 0.05), "#777777")]:
        apparatus.annotate("", end, start, arrowprops={"arrowstyle": "-|>", "lw": 2, "color": color})
    apparatus.text(4.0, 2.2, "$\\dot Q_c$\n100 W", ha="center", color=cold)
    apparatus.text(8.0, 2.2, "$\\dot Q_h$\n150 W", ha="center", color=hot)
    apparatus.text(6.0, 3.85, "Meter: 50 W electrical input", ha="center", color=work)
    apparatus.text(1.65, -0.38, "Room adds 5 W", ha="center", color="#555555", fontsize=10)
    apparatus.text(10.35, -0.38, "15 W lost to room", ha="center", color="#555555", fontsize=10)

    capacity, input_power, cold_power, hot_power = 4500.0, 50.0, 100.0, 150.0
    hot_leak, cold_leak = 15.0, 5.0
    time = np.linspace(0, 180, 181)
    th = 32 + (hot_power - hot_leak) * time / capacity
    tc = 12 - (cold_power - cold_leak) * time / capacity
    temp.plot(time, th, color=hot, lw=2.5, label="Hot: 32.0 → 37.4 °C")
    temp.plot(time, tc, color=cold, lw=2.5, label="Cold: 12.0 → 8.2 °C")
    temp.axhline(22, ls=":", color="#666666", lw=1.5)
    temp.text(8, 23.1, "Room: 22 °C", color="#666666", fontsize=10)
    temp.text(20, 31.0, "Slope +0.030 K/s", color=hot, fontsize=10)
    temp.text(20, 14.0, "Slope −0.0211 K/s", color=cold, fontsize=10)
    temp.set(xlim=(0, 180), ylim=(5, 42), xlabel="Elapsed time (s)", ylabel="Bath temperature (°C)")
    temp.set_title("Finite baths warm and cool", fontsize=12, pad=12)
    temp.set_xticks([0, 60, 120, 180])
    temp.grid(alpha=0.17)
    temp.legend(loc="upper left", frameon=False, fontsize=9.5)

    duration = time[-1]
    raw_h = (hot_power - hot_leak) * duration / 1000
    raw_c = (cold_power - cold_leak) * duration / 1000
    el = input_power * duration / 1000
    positions = np.array([0.0, 1.0, 2.0])
    raw = [raw_c, el, raw_h]
    corrections = [cold_leak * duration / 1000, 0, hot_leak * duration / 1000]
    energy.bar(positions, raw, color=[cold, work, hot], width=0.57)
    energy.bar(positions, corrections, bottom=raw, color="white", edgecolor="#555555",
               hatch="////", width=0.57, label="Bath-leak correction")
    for x, value, correction in zip(positions, raw, corrections):
        energy.text(x, value / 2, f"{value:.1f}", ha="center", va="center", color="white", fontweight="bold")
        if correction:
            energy.text(x + 0.35, value + correction / 2, f"+{correction:.1f}", ha="left", va="center", fontsize=9)
        energy.text(x, value + correction + 0.5, f"{value + correction:.1f} kJ", ha="center", fontsize=10)
    energy.set(xticks=positions, xticklabels=["Cold extraction", "Work input", "Hot delivery"],
               xlim=(-0.55, 2.9), ylim=(0, 32), ylabel="Energy over 180 s (kJ)")
    energy.tick_params(axis="x", labelsize=9.5)
    energy.set_title("Corrected balance: 27 = 18 + 9 kJ", fontsize=12, pad=12)
    energy.grid(axis="y", alpha=0.17)
    energy.set_axisbelow(True)
    energy.legend(loc="upper left", fontsize=9, frameon=False)
    fig.text(0.5, 0.067, "Raw COPs: heating 2.7, cooling 1.9     |     Corrected COPs: heating 3.0, cooling 2.0",
             ha="center", fontsize=11)
    fig.text(0.5, 0.029, "Real machines may also lose heat directly to the room; check the complete energy boundary.",
             ha="center", fontsize=10, color="#444444")
    fig.savefig("heat-pump-bath-calorimetry.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
