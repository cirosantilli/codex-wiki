"""Exact illustrative LIF responses, never empirical voltage recordings.

Python 3.14 / matplotlib 3.10.7 / numpy 2.3.5.
Run from _media; output PNG uses this script's basename in the current directory.
Units below: ms, mV, pA. The factor .1 converts 100 MOhm * pA to mV.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

REST = -65.0
THRESHOLD = -50.0
TAU = 20.0
RESISTANCE = .1  # mV/pA
REFRACTORY = 2.0
PROTOCOLS = [
    ("One input", [(10.0, 50.0, 100.0)]),
    ("Two coincident inputs", [(10.0, 50.0, 100.0), (10.0, 50.0, 100.0)]),
    ("Two separated inputs", [(10.0, 50.0, 100.0), (70.0, 110.0, 100.0)]),
]


def segments(pulses, end=130.0):
    """Compute exact constant-current segments and exact threshold events."""
    boundaries = sorted({0., end} | {t for start, stop, _ in pulses for t in (start, stop)})
    result, spikes, holds = [], [], []
    voltage, refractory_end = REST, -np.inf
    for start, stop in zip(boundaries[:-1], boundaries[1:]):
        current = sum(i for a, b, i in pulses if a <= start < b)
        time = start
        while time < stop - 1e-12:
            if time < refractory_end:
                until = min(stop, refractory_end)
                result.append((time, until, REST, REST, current, True))
                time, voltage = until, REST
                continue
            equilibrium = REST + RESISTANCE * current
            latency = np.inf
            if equilibrium > THRESHOLD:
                latency = TAU * np.log((equilibrium - voltage) / (equilibrium - THRESHOLD))
            until = min(stop, time + latency)
            result.append((time, until, voltage, equilibrium, current, False))
            voltage = equilibrium + (voltage - equilibrium) * np.exp(-(until - time) / TAU)
            if time + latency <= stop:
                spikes.append(until)
                holds.append((until, until + REFRACTORY))
                voltage = REST
                refractory_end = until + REFRACTORY
            time = until
    return result, np.asarray(spikes), holds


def main():
    colors = ["#28628a", "#b3541b", "#287a61"]
    fig, axs = plt.subplots(2, 3, figsize=(10.5, 5.5), sharex=True, sharey="row",
                            gridspec_kw={"height_ratios": [1, 2]})
    fig.set_facecolor("white")
    for col, ((title, pulses), color) in enumerate(zip(PROTOCOLS, colors)):
        upper, lower = axs[:, col]
        grid = np.linspace(0, 130, 2601)
        currents = sum(np.where((grid >= a) & (grid < b), i, 0) for a, b, i in pulses)
        upper.plot(grid, currents, color=color, lw=2)
        upper.set_title(title, fontsize=12, pad=9)
        charge = sum((b - a) * i for a, b, i in pulses) / 1000
        upper.text(.98, .83, f"Total charge: {charge:g} pC", transform=upper.transAxes,
                   ha="right", fontsize=10)
        parts, spikes, holds = segments(pulses)
        for start, stop, initial, equilibrium, _, held in parts:
            t = np.linspace(start, stop, max(2, int((stop - start) * 15)))
            v = np.full_like(t, REST) if held else equilibrium + (initial - equilibrium) * np.exp(-(t - start) / TAU)
            lower.plot(t, v, color=color, lw=2)
        for spike in spikes:
            lower.plot([spike, spike], [THRESHOLD, REST], color=color, lw=1, ls=":")
            lower.plot([spike, spike], [-48.2, -46.5], color=color, lw=2.5)
        for start, stop in holds:
            lower.axvspan(start, stop, color=color, alpha=.12)
        lower.axhline(THRESHOLD, color="#777777", lw=1, ls="--")
        lower.text(.03, .93, f"{len(spikes)} spike event" + ("s" if len(spikes) != 1 else ""),
                   transform=lower.transAxes, fontsize=11, color=color)
        lower.set(xlim=(0, 130), ylim=(-67, -45), xlabel="Time (ms)", xticks=[0, 40, 80, 120])
        upper.set(ylim=(-10, 255), yticks=[0, 100, 200])
        for ax in (upper, lower):
            ax.spines[["top", "right"]].set_visible(False)
            ax.grid(axis="y", color="#eeeeee")
        if col == 1:
            lower.annotate("Threshold event\nat 37.726 ms", xy=(spikes[0], -47),
                           xytext=(62, -54), fontsize=9, arrowprops={"arrowstyle": "->", "color": color})
            lower.text(77, -64.2, "Reset + 2 ms hold", fontsize=9, color=color)
        else:
            peak = max(eq + (v - eq) * np.exp(-(b - a) / TAU) for a, b, v, eq, _, held in parts if not held)
            lower.text(.98, .11, f"Peak: {peak:.4f} mV", transform=lower.transAxes, ha="right", fontsize=9)
    axs[0, 0].set_ylabel("Input current (pA)")
    axs[1, 0].set_ylabel("Membrane potential (mV)")
    axs[1, 2].text(125, -49.6, "Threshold", ha="right", va="bottom", fontsize=9, color="#666666")
    fig.suptitle("Input timing changes spike output", fontsize=17, y=.975)
    fig.text(.5, .895, "Synthetic exact model • no experimental data • ticks are events, not spike waveforms",
             ha="center", fontsize=10)
    fig.text(.5, .025, "R = 100 MΩ    C = 200 pF    τ = 20 ms    Rest/reset = −65 mV    Threshold = −50 mV",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.085, right=.985, top=.79, bottom=.16, wspace=.15, hspace=.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
