"""Original measurement schematic and synthetic calorimeter readout.

Python 3.14 / matplotlib 3.10.7 / numpy 2.3.5. Run from _media to save the PNG.
The temperature curve solves C dT/dt = P - G(T - T_room), not measured data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.labelsize": 12})
    fig = plt.figure(figsize=(11, 6.1), layout="constrained")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.1, 1])
    ax, trace = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    fig.suptitle("Electrical calorimetry: heater-terminal input and thermal response", fontsize=16)
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.axis("off")
    ink, blue, orange = "#263544", "#17638d", "#bb4e20"

    def wire(xs, ys, color=ink, lw=2):
        ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round")

    def meter(x, y, label, color=ink):
        ax.add_patch(Circle((x, y), .42, facecolor="white", edgecolor=color, lw=2, zorder=4))
        ax.text(x, y, label, ha="center", va="center", fontsize=14, color=color, zorder=5)

    ax.add_patch(Rectangle((.45, 7.15), 1.65, 1.5, facecolor="#f1f3f5", edgecolor=ink, lw=1.5))
    ax.text(1.27, 7.9, "DC\nsupply", ha="center", va="center")
    wire([2.1, 7.6, 7.6, 6.15], [8.15, 8.15, 4.8, 4.8])
    wire([4.75, 3.8, 3.8, 2.1], [4.8, 4.8, 7.35, 7.35])
    meter(4.15, 8.15, "A")
    ax.text(4.15, 8.85, "Heater branch: 1 A", ha="center")
    ax.annotate("", xy=(6.8, 8.15), xytext=(5.6, 8.15), arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
    ax.text(6.2, 8.5, r"$I$", ha="center", color=orange)
    # The blue pair attaches directly at the heater terminals, inside the boundary.
    wire([4.75, 4.75, 5.03], [4.8, 6.35, 6.35], blue, 1.6)
    wire([5.87, 6.15, 6.15], [6.35, 6.35, 4.8], blue, 1.6)
    meter(5.45, 6.35, "V", blue)
    ax.text(5.45, 7.0, "Sense at heater: 5 V", ha="center", color=blue)
    ax.add_patch(Rectangle((3.3, 2.55), 4.85, 3.0, facecolor="#e6f2f8", edgecolor=ink, lw=2))
    ax.add_patch(Rectangle((3.15, 5.45), 5.15, .18, facecolor="#d8dde2", edgecolor=ink))
    ax.add_patch(Rectangle((3.05, 2.3), 5.6, 3.75, fill=False, edgecolor=blue, ls="--", lw=1.3))
    ax.add_patch(Rectangle((4.75, 4.57), 1.4, .46, facecolor="#f7dbc8", edgecolor=orange, lw=2))
    ax.text(5.45, 4.1, r"Immersed resistor: $5\,\Omega$", ha="center", color=orange)
    for x in [4.75, 6.15]:
        ax.plot(x, 4.8, "o", ms=4, color=ink, zorder=6)
    wire([7.0, 7.0], [6.7, 3.35], lw=3)
    ax.plot(7, 3.35, "o", color=orange, ms=7)
    ax.text(8.2, 6.85, "Calibrated\nthermometer", ha="center",
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.0})
    wire([4.15, 4.15], [5.95, 3.05], lw=1.5)
    wire([3.85, 4.45], [3.05, 3.05], lw=2.5)
    ax.text(2.1, 3.2, "Gentle\nstirring", ha="center")
    ax.text(5.65, 2.9, "Water bath", ha="center")
    ax.text(5.65, 1.9, r"Calibrated $C_{\mathrm{eff}}=500$ J/K", ha="center", color=blue)
    ax.annotate("", xy=(9.25, 4.05), xytext=(8.4, 4.05), arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
    ax.text(9.15, 3.0, "Room\nleakage", ha="center", color=orange)
    ax.text(5.1, .75, "Record V, I, temperature and time.\nExclude losses in supply leads outside the vessel.", ha="center", fontsize=11)

    time = np.linspace(0, 360, 721)
    C, G, P, room, start, stop = 500., .5, 5., 20., 60., 180.
    heating_duration = np.clip(time - start, 0, stop - start)
    excess = P / G * (-np.expm1(-G * heating_duration / C))
    excess *= np.exp(-G * np.maximum(time - stop, 0) / C)
    ideal = room + P / C * heating_duration
    trace.axvspan(start, stop, color="#fff0df", label="Heater on: 5 W for 120 s")
    trace.plot(time, ideal, "--", color="#7e8791", lw=2, label="Same input, no leakage")
    trace.plot(time, room + excess, color=blue, lw=2.5, label="Model with room leakage")
    trace.axhline(room, color="#9ba6af", lw=1, ls=":")
    endpoint = room + P / G * (-np.expm1(-G * (stop - start) / C))
    trace.plot(stop, endpoint, "o", color=blue, ms=6)
    trace.annotate("21.1308 °C", (stop, endpoint), xytext=(30, -26), textcoords="offset points", color=blue,
                   arrowprops={"arrowstyle": "-", "color": blue})
    trace.text(.05, .47, "Input: 600 J\nStored: 565.398 J\nLost to room: 34.602 J", transform=trace.transAxes,
               bbox={"boxstyle": "round,pad=0.5", "facecolor": "white", "edgecolor": "#d6dce0"})
    trace.text(28, 20.14, "Baseline", ha="center", fontsize=10)
    trace.text(276, 20.83, "Heater off:\ncooling", ha="center", fontsize=10)
    trace.set(xlabel="Time (s)", ylabel="Assembly temperature (°C)", xlim=(0, 360), ylim=(19.96, 21.52))
    trace.set_title("Synthetic readout; room held at 20 °C", fontsize=12)
    trace.legend(loc="upper left", fontsize=9.5, frameon=False)
    trace.grid(alpha=.15)
    trace.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
