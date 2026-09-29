"""Compare fixed source concentrations at a common morphogen threshold.

Writes morphogen-source-strength-boundary-shift.png to the current directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The source boundary prescribes concentration, not flux. Numbers are arbitrary.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    ell, threshold = 100.0, 20.0
    x = np.linspace(0.0, 400.0, 1000)
    amplitudes = np.array([100.0, 200.0])
    crossings = ell * np.log(amplitudes / threshold)
    colors = ["#236b96", "#b55f26"]
    fig, ax = plt.subplots(figsize=(8.4, 5.3))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.12, right=0.97, top=0.84, bottom=0.24)
    for amplitude, crossing, color in zip(amplitudes, crossings, colors):
        ax.plot(x, amplitude * np.exp(-x / ell), lw=2.6, color=color,
                label=f"Source concentration {amplitude:.0f}")
        ax.vlines(crossing, 0, threshold, color=color, ls=":", lw=1.5)
        ax.plot(crossing, threshold, "o", color=color, ms=6, zorder=4)
        ax.annotate(f"{crossing:.2f} µm", (crossing, threshold),
                    xytext=(-8, 23) if amplitude == 100 else (15, 23),
                    textcoords="offset points", ha="right" if amplitude == 100 else "left",
                    fontsize=11, color=color,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.axhline(threshold, color="#555555", ls="--", lw=1.2)
    ax.text(393, 24, "Threshold 20", ha="right", fontsize=11, color="#555555")
    arrow_y = 77
    ax.annotate("", (crossings[1], arrow_y), (crossings[0], arrow_y),
                arrowprops={"arrowstyle": "<->", "color": "#333333", "lw": 1.6})
    for crossing in crossings:
        ax.vlines(crossing, 57, 85, color="#777777", lw=0.8)
    ax.text(np.mean(crossings), 91, "Boundary shift\nℓ ln 2 = 69.31 µm", ha="center", fontsize=11)
    ax.set(xlim=(0, 400), ylim=(0, 210),
           xlabel="Distance from fixed-concentration source x (µm)",
           ylabel="Concentration (arbitrary units)")
    ax.set_yticks([0, 20, 50, 100, 150, 200])
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", frameon=False, fontsize=11)
    ax.grid(alpha=0.14)
    fig.suptitle("Doubling source concentration moves the same threshold", fontsize=15, y=0.96)
    ax.set_title("Same diffusion length ℓ = 100 µm; same threshold = 20", fontsize=12)
    fig.text(0.5, 0.075, "Fixed boundary concentrations 100 and 200, not prescribed fluxes.\nToy values; not measured Bicoid data.",
             ha="center", fontsize=10, linespacing=1.6)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
