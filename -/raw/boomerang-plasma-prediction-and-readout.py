"""Prediction/readout diagram; historical facts: astro-ph/0004404, pp. 2–9.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7.
No simulated or digitized experimental spectrum is drawn.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10.8, 6.0), dpi=120, facecolor="white")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    blue, green, ink = "#e7f0fa", "#e8f4ed", "#183344"

    def box(x, y, w, h, text, color, size=10):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.008",
                                   facecolor=color, edgecolor=ink, linewidth=1.1))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=size,
                color=ink, linespacing=1.5)

    def arrow(a, b):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=13,
                                    linewidth=1.3, color=ink))

    ax.text(0.02, .965, "From primordial plasma to a test on the sky", fontsize=17,
            weight="bold", color=ink)
    ax.text(.02, .895, "PREDICTION", fontsize=11, weight="bold", color=ink)
    box(.025, .675, .25, .17, "Atomic rates + expansion\nIonization history\nScattering / last scattering", blue)
    box(.365, .675, .25, .17, "Gravity + photon pressure\nCoupled acoustic evolution\nSound horizon + amplitudes", blue)
    box(.705, .675, .265, .17, "Angular projection\nPredicted sky covariance\n"+r"Model parameters → $C_\ell$", blue)
    arrow((.282, .76), (.355, .76))
    arrow((.622, .76), (.695, .76))
    ax.text(.02, .59, "BOOMERANG: EXPERIMENTAL PATH", fontsize=11,
            weight="bold", color=ink)
    box(.025, .345, .25, .19, "Balloon near 38 km\nRepeated telescope scans\nBolometers at 0.3 K", green)
    box(.365, .345, .25, .19, "Detector signal + pointing\nCalibration + beam response\nTemperature maps", green)
    box(.705, .345, .265, .19, "Maps → angular power\nNoise / beam treatment\nModel comparison", green)
    arrow((.282, .44), (.355, .44))
    arrow((.622, .44), (.695, .44))
    arrow((.838, .665), (.838, .545))
    box(.365, .075, .25, .18, "CONTROLS\nFrequency differences\nTime-split difference map", "#fff1d9")
    arrow((.49, .335), (.49, .265))
    arrow((.623, .165), (.695, .165))
    arrow((.838, .335), (.838, .265))
    box(.705, .075, .265, .18, "PUBLISHED PEAK LOCATION\n"+r"$\ell_{\rm peak}=197\pm6$ ($1\sigma$)"+"\nNo bandpower curve drawn", "#fff1d9", 10)
    ax.text(.025, .185, "Acoustic angle constrains\na ruler-to-distance ratio.\nBaryon abundance also\naffects relative peak heights.",
            fontsize=10, color=ink, va="center", linespacing=1.5)
    fig.subplots_adjust(left=.025, right=.985, top=.98, bottom=.03)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
