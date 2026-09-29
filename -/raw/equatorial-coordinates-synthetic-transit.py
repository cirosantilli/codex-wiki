"""Synthetic meridian observation and clock calibration, not measured data.

Run from _media. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Altitude comes from the spherical-Earth, unrefracted fixed-direction model.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 6))
    fig.patch.set_facecolor("white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1, .75], width_ratios=[1.2, 1])
    ax, bx, cx = fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[1, 0]), fig.add_subplot(grid[:, 1])
    fig.suptitle("Synthetic meridian observation: angle plus a clock readout", fontsize=15)
    blue, orange, green = "#1966a3", "#be510b", "#22805b"
    theta = np.linspace(4, 8, 401)
    alpha = 6.0
    phi, delta = np.deg2rad([52, 20])
    hour_angle = np.deg2rad(15 * (theta - alpha))
    altitude = np.rad2deg(np.arcsin(np.sin(phi) * np.sin(delta)
                                   + np.cos(phi) * np.cos(delta) * np.cos(hour_angle)))
    ax.plot(theta, altitude, color=blue, lw=2.5)
    ax.axvline(alpha, color="#777777", ls="--", lw=1)
    ax.scatter([alpha], [58], color=blue, zorder=3)
    ax.annotate("Upper crossing\na = 58°, H = 0", (6, 58), (6.3, 55.0),
                arrowprops={"arrowstyle": "->", "color": blue}, fontsize=10)
    ax.set(xlim=(4, 8), ylim=(50, 59.5), ylabel="Geometric altitude (degrees)")
    ax.set_title("Fixed direction: α = 6 h, δ = 20°; site: φ = 52°", fontsize=11)
    ax.tick_params(labelbottom=False)
    ax.grid(alpha=.2)
    bx.plot(theta, theta, color=orange, lw=2, label="local sidereal time Θ")
    bx.axhline(alpha, color=green, lw=2, label="target right ascension α")
    bx.axvline(alpha, color="#777777", ls="--", lw=1)
    bx.set(xlim=(4, 8), ylim=(3.8, 8.3), xlabel="Local sidereal time (hours)", ylabel="Hours")
    bx.set_xticks([4, 5, 6, 7, 8])
    bx.legend(loc="upper left", fontsize=9, frameon=True, facecolor="white")
    bx.grid(alpha=.2)
    bx.text(4.04, 4.08, "H < 0: before", fontsize=9)
    bx.text(7.92, 4.08, "H > 0: after", ha="right", fontsize=9)

    cx.axis("off")
    cx.set(xlim=(0, 1), ylim=(0, 1))
    cx.text(.5, .99, "Two independent readouts", ha="center", va="top", fontsize=12, weight="bold")
    # A schematic focal-plane view; left/right are deliberately not sky cardinal directions.
    cx.plot([.14, .86, .86, .14, .14], [.70, .70, .87, .87, .70], color="#777777")
    cx.plot([.50, .50], [.70, .87], color=blue, lw=2)
    cx.scatter([.22, .50, .78], [.785] * 3, color=green, s=[25, 55, 25])
    cx.annotate("", (.83, .81), (.18, .81), arrowprops={"arrowstyle": "->", "color": green})
    cx.text(.5, .665, "Image crosses the central sighting line\nRecord crossing time and angular circle", ha="center", va="top", fontsize=10)
    cx.text(.04, .53, "Angular example (south of zenith)", fontsize=11, color=blue, weight="bold")
    cx.text(.04, .475, "φ = 52°; signed zenith distance = 32°\nδ = 52° − 32° = 20°", va="top", fontsize=11)
    cx.text(.04, .355, "Clock example (separate synthetic target)", fontsize=10.5, color=orange, weight="bold")
    cx.text(.04, .30, "Reference RA:                 06:00:00\nReference clock readout:  06:00:20\nClock correction:                  −20 s\nTarget clock readout:       06:30:20\nCorrected target RA:        06:30:00", va="top", linespacing=1.6, fontsize=10.5,
            bbox={"boxstyle": "round,pad=.6", "fc": "#f3f5f7", "ec": "none"})
    cx.text(.5, .01, "06:30:00 = 6.5 h = 97.5°", ha="center", fontsize=12, color=orange)
    fig.text(.5, .025, "Analytical illustration, not an observing record. Spherical Earth; no refraction or source motion.\nClock example assumes correct sidereal rate and an independently known reference direction.",
             ha="center", fontsize=9, color="#555555")
    fig.subplots_adjust(left=.085, right=.98, bottom=.17, top=.86, hspace=.15, wspace=.28)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
