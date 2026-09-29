"""Ohmic toy currents; writes an opaque PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
All parameters are stipulated, not empirical. V = inside minus outside;
conventional current is inward-positive. Units: nS * mV = pA.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


BLUE = "#207ea2"
ORANGE = "#bc5b22"
INK = "#263749"


def current(voltage, conductance, reversal):
    """Inward-positive current in pA for mV and nS inputs."""
    return conductance * (reversal - np.asarray(voltage))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (single, pair) = plt.subplots(1, 2, figsize=(11.0, 5.5), facecolor="white")
    fig.subplots_adjust(left=.085, right=.98, top=.75, bottom=.2, wspace=.3)
    fig.suptitle("Reversal means zero NET current; ion movement can continue", y=.97,
                 fontsize=15, color=INK)
    fig.text(.5, .9, "V = inside − outside • conventional current: inward positive, outward negative",
             ha="center", fontsize=11, color=INK)
    v = np.linspace(-115., 60., 701)
    for ax in [single, pair]:
        ax.axhline(0, color="#82909c", lw=.9)
        ax.set(xlabel="Membrane potential V (mV)",
               ylabel="Inward-positive current (pA)")
        ax.grid(alpha=.17)

    single.plot(v, current(v, 10., -80.), color=BLUE, lw=2.4)
    single.set(title="A. One Ohmic pathway: g = 10 nS, E = −80 mV",
               xlim=(-115, -45), ylim=(-400, 400))
    single.set_xticks([-110, -100, -80, -60, -50])
    for probe, label, delta in [(-100., "+200 pA", (5, 8)),
                                (-80., "0 pA", (9, 10)),
                                (-60., "−200 pA", (-62, -22))]:
        y = current(probe, 10., -80.)
        single.plot(probe, y, "o", color=BLUE, ms=6)
        single.annotate(label, (probe, y), xytext=delta, textcoords="offset points",
                        color=BLUE, fontsize=10)
    single.axvline(-80, color=BLUE, ls=":", lw=1)
    single.text(-112, 335, "Positive: net positive charge enters", fontsize=9, color=INK)
    single.text(-112, -355, "Negative: net positive charge leaves", fontsize=9, color=INK)

    balance = (10.*-80. + 2.*50.) / 12.
    pair.plot(v, current(v, 10., -80.), color=ORANGE, lw=2,
              label="K: 10 nS, E = −80 mV")
    pair.plot(v, current(v, 2., 50.), color=BLUE, lw=2,
              label="Na: 2 nS, E = +50 mV")
    pair.plot(v, current(v, 10., -80.) + current(v, 2., 50.),
              color=INK, lw=2.2, ls="--", label="Total: 12 nS, E = −58.3333 mV")
    pair.set(title="B. Two pathways across the same membrane",
             xlim=(-110, 60), ylim=(-1500, 650))
    pair.set_xticks([-100, -80, -60, 0, 50])
    pair.legend(loc="lower left", fontsize=9, frameon=True)
    pair.axvline(balance, color="#82909c", ls=":", lw=1)
    for g, e, color in [(10., -80., ORANGE), (2., 50., BLUE)]:
        pair.plot(balance, current(balance, g, e), "o", color=color, ms=5)
    pair.plot(balance, 0, "o", color=INK, ms=5)
    pair.annotate("At −58.3333 mV:\nNa: +216.6667 pA\nK: −216.6667 pA\nTotal: 0 pA",
                  xy=(balance, 0), xytext=(-10, 390), fontsize=9, color=INK,
                  va="top", arrowprops={"arrowstyle": "->", "color": INK},
                  bbox={"boxstyle": "round,pad=.3", "fc": "white", "ec": "#ccd4dc"})
    fig.text(.5, .07, "Stipulated constant conductances and fixed gradients • "
             "instantaneous passive current balance, not a full resting-voltage model",
             ha="center", fontsize=9.5, color=INK)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
