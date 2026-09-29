"""Passive conductance illustrations; writes basename.png in the CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Illustrative constant steps; no action-potential generation or reset.
Units: mV, ms, pF, nS and pA, so pF/nS = ms and nS*mV = pA.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BLUE = "#23779a"
ORANGE = "#ba5418"
PURPLE = "#7950a1"
GREEN = "#328164"
INK = "#243446"


def voltage(t, ge=0., gi=0., ei=-65., current=0.):
    """Exact constant-coefficient solution, starting at leak rest."""
    capacitance, gl, el, ee, v0 = 200., 10., -65., 0., -65.
    total = gl+ge+gi
    steady = (gl*el+ge*ee+gi*ei+current)/total
    tau = capacitance/total
    return steady+(v0-steady)*np.exp(-t/tau)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(11, 6.8), facecolor="white")
    grid = fig.add_gridspec(2, 2, width_ratios=[1, 1.3], hspace=.49, wspace=.32)
    currents = fig.add_subplot(grid[:, 0])
    responses = fig.add_subplot(grid[0, 1])
    probe = fig.add_subplot(grid[1, 1])
    fig.suptitle("Synaptic conductance: driving force and shunting", fontsize=15, y=.97)
    v = np.linspace(-85., 10., 600)
    for e, color in [(0., BLUE), (-60., PURPLE), (-65., ORANGE), (-75., GREEN)]:
        currents.plot(v, e-v, color=color, lw=2, label=f"E = {e:g} mV")
        currents.plot(e, 0, "o", color=color, ms=5)
    currents.axhline(0, color="#7b8590", lw=.8)
    currents.axvline(-65, color="#8793a0", ls=":", lw=1)
    currents.set(title="A. Current through 1 nS", xlabel="Membrane potential V (mV)",
                 ylabel="Inward-positive current g(E − V) (pA)", xlim=(-85, 10), ylim=(-90, 90))
    currents.legend(loc="upper right", frameon=True, fontsize=9)
    currents.text(-82, 82, "Positive: inward current", fontsize=9, color=INK)
    currents.text(-82, -83, "Negative: outward current", fontsize=9, color=INK)
    currents.annotate("Zero current at E\ncan still mean a shunt", xy=(-65, 0), xytext=(-82, -42),
                      arrowprops={"arrowstyle": "->", "color": INK}, fontsize=9, color=INK)
    currents.grid(alpha=.16)

    t = np.linspace(0, 60, 601)
    curves = [
        (dict(ge=2), BLUE, "-", "Excitatory alone"),
        (dict(ge=2, gi=20), ORANGE, "-", "Excitatory + rest shunt"),
        (dict(gi=20, ei=-60), PURPLE, "--", "Depolarizing alone"),
        (dict(ge=2, gi=20, ei=-60), PURPLE, "-", "Excitatory + depolarizing"),
        (dict(gi=20, ei=-75), GREEN, "-", "Hyperpolarizing alone"),
    ]
    for params, color, style, name in curves:
        responses.plot(t, voltage(t, **params), color=color, ls=style, lw=2, label=name)
    responses.set_title("B. Synaptic conductance steps", loc="left", pad=62)
    responses.axhline(-65, color="#8793a0", ls=":", lw=1)
    responses.set(xlabel="Time after opening (ms)",
                  ylabel="V (mV)", xlim=(0, 60), ylim=(-73, -52))
    responses.legend(loc="lower center", bbox_to_anchor=(.5, 1.14),
                     fontsize=8.3, frameon=False, ncol=2, borderaxespad=0)
    responses.grid(alpha=.16)

    probe.plot(t, voltage(t, current=100), color=BLUE, lw=2, label="100 pA; no shunt")
    probe.plot(t, voltage(t, current=100, gi=20), color=ORANGE, lw=2,
               label="100 pA + rest shunt")
    probe.plot(t, voltage(t, gi=20), color=ORANGE, lw=1.6, ls="--", label="Rest shunt alone")
    probe.set(title="C. Same test current, different voltage response", xlabel="Time after step (ms)",
              ylabel="V (mV)", xlim=(0, 60), ylim=(-66, -54))
    probe.text(59, -55.6, "No shunt: 10 mV steady rise; τ = 20 ms", color=BLUE, ha="right", fontsize=9)
    probe.text(59, -60.8, "With shunt: 3.33 mV steady rise; τ = 6.67 ms", color=ORANGE, ha="right", fontsize=9)
    probe.text(3, -64.65, "Rest shunt alone: no voltage change",
               color=ORANGE, fontsize=9)
    probe.grid(alpha=.16)
    fig.text(.5, .025, "Illustrative passive model: C = 200 pF, leak = 10 nS at −65 mV; "
             "synaptic steps: gₑ = 2 nS at 0 mV, gᵢ = 20 nS • no spike/reset",
             ha="center", color=INK, fontsize=9)
    fig.subplots_adjust(left=.075, right=.98, top=.78, bottom=.12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
