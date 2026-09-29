"""Original RC noise-equilibrium comparison; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes this script's basename with a .png extension.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def wire(ax, x, y):
    ax.plot(x, y, color="#333333", linewidth=1.7)


def resistor(ax, x, bottom, top, label):
    wire(ax, [x, x], [bottom, bottom + .22])
    wire(ax, [x, x], [top - .22, top])
    ax.add_patch(Rectangle((x - .13, bottom + .22), .26, top - bottom - .44,
                           facecolor="white", edgecolor="#333333", linewidth=1.7))
    ax.text(x - .23, (top + bottom) / 2, label, ha="right", va="center")


def capacitor(ax, x, bottom, top):
    mid = (top + bottom) / 2
    wire(ax, [x, x], [bottom, mid - .07])
    wire(ax, [x, x], [mid + .07, top])
    for y in [mid - .07, mid + .07]:
        wire(ax, [x - .23, x + .23], [y, y])
    ax.text(x + .32, mid, "C", va="center")


def main():
    k_b, temperature, capacitance = 1.380649e-23, 300, 1e-9
    equilibrium = k_b * temperature / capacitance
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(11.4, 4.9), layout="constrained", facecolor="white")
    grid = fig.add_gridspec(1, 3, width_ratios=[.95, 1.25, 1.3])
    ax = fig.add_subplot(grid[0])
    ax.set(xlim=(-.1, 3.8), ylim=(-.2, 5.3), title="One physical resistor")
    ax.axis("off")
    for base in [2.9, .1]:
        top = base + 1.7
        wire(ax, [.8, 2.6], [top, top])
        wire(ax, [.8, 2.6], [base, base])
        capacitor(ax, 2.6, base, top)
        if base > 1:
            resistor(ax, .8, base, top, "R, T")
            ax.text(2.8, top, r"$v_C$", va="bottom")
        else:
            resistor(ax, .8, base + .75, top, "R")
            wire(ax, [.8, .8], [base, base + .15])
            ax.add_patch(Circle((.8, base + .45), .3, edgecolor="#176a9b",
                                facecolor="white", linewidth=1.7))
            ax.text(.8, base + .45, "~", ha="center", va="center", fontsize=19)
            ax.text(.32, base + .45, r"$e_n$", ha="right", va="center", color="#176a9b")
            ax.text(1.55, -.08, "R here is noiseless", ha="center", fontsize=9)
    ax.text(1.7, 2.38, "↓ equivalent model", ha="center", color=".35")
    ax.text(1.7, 4.87, "Ideal readout across C", ha="center", fontsize=9)
    frequency = np.geomspace(20, 2e6, 1800)
    time = np.linspace(0, 250e-6, 1000)
    spectral = fig.add_subplot(grid[1])
    growth = fig.add_subplot(grid[2])
    for resistance, color in [(1e4, "#176a9b"), (1e5, "#c96616")]:
        tau = resistance * capacitance
        psd = 4 * k_b * temperature * resistance / (1 + (2 * np.pi * frequency * tau) ** 2)
        label = f"R = {resistance / 1000:g} kΩ"
        spectral.loglog(frequency / 1000, psd * 1e18, color=color, linewidth=2.2, label=label)
        growth.plot(time * 1e6, equilibrium * (-np.expm1(-2 * time / tau)) * 1e12,
                    color=color, linewidth=2.2, label=label)
    spectral.set(xlabel="Frequency f (kHz)", ylabel=r"One-sided PSD ($\mathrm{nV^2/Hz}$)",
                 title="Same full spectral area", xlim=(.02, 2000), ylim=(.005, 3000))
    spectral.legend(frameon=False, loc="lower left")
    spectral.text(.04, .57, r"$\int_0^\infty S_C(f)\,df=k_BT/C$", transform=spectral.transAxes,
                  bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    growth.axhline(equilibrium * 1e12, color=".4", linestyle="--", linewidth=1)
    growth.text(120, 4.23, r"$k_BT/C = 4.141947\ \mathrm{\mu V^2}$", fontsize=10, ha="center")
    growth.set(xlabel="Time after connection (µs)", ylabel=r"Mean square voltage ($\mathrm{\mu V^2}$)",
               title="Growth from an exactly discharged C", xlim=(0, 250), ylim=(0, 4.65))
    growth.legend(frameon=False, loc="lower right")
    growth.text(.27, .45, r"$\langle v_C^2(t)\rangle=\frac{k_BT}{C}(1-e^{-2t/RC})$",
                transform=growth.transAxes, fontsize=11)
    fig.suptitle("RC equilibrium noise: resistance changes the pace", fontsize=15)
    fig.supxlabel("T = 300 K, C = 1 nF • analytical ensemble averages • no measured data", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")


if __name__ == "__main__":
    main()
