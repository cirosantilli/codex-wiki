"""Original toy simulation, NOT discovery data or historical abundances.

Python 3.14; numpy 2.3.5; matplotlib 3.10.7. Run from _media.
The C1/C2 boundaries follow UCRL-3172 p. 5. All event populations,
noise, momentum spread and the constant 40 MeV loss are chosen here.
The left panel is an ideal constant-speed flight; the right is a later
local speed, so the panels must not be treated as simultaneous speeds.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

C = 0.299792458  # metres per nanosecond
M_PROTON = 0.93827  # GeV/c^2, deliberately rounded model input
M_PION = 0.13957
LENGTH = 12.0  # m, illustrative
LOSS = 0.040  # GeV, illustrative energy loss after the ideal flight


def beta(momentum, mass):
    return momentum / np.hypot(momentum, mass)


def downstream_beta(momentum, mass):
    energy = np.hypot(momentum, mass) - LOSS
    return np.sqrt(1 - (mass / energy)**2)


def main():
    rng = np.random.default_rng(1955)
    fig, (ax, av) = plt.subplots(1, 2, figsize=(10, 5.2), dpi=120, facecolor="white")
    fig.suptitle("SIMULATION — selected momentum needs independent velocity tests",
                 fontsize=13, weight="bold", y=0.97)
    fig.text(0.5, 0.90, "Chosen events and noise • no historical event data or abundance information",
             ha="center", fontsize=10, color="#4c5968")
    p_grid = np.linspace(1.145, 1.255, 300)
    series = [(M_PROTON, "Antiproton", "#23699a", "o"),
              (M_PION, "Negative pion", "#ba5b17", "^")]
    for mass, label, color, marker in series:
        p = rng.uniform(1.16, 1.24, 38)
        t = LENGTH / (C * beta(p, mass)) + rng.normal(0, 0.30, len(p))
        v = downstream_beta(p, mass) + rng.normal(0, 0.0015, len(p))
        ax.plot(p_grid, LENGTH / (C * beta(p_grid, mass)), color=color, lw=1.5)
        ax.scatter(p, t, s=20, c=color, marker=marker, alpha=0.75, label=label)
        av.plot(p_grid, downstream_beta(p_grid, mass), color=color, lw=1.5)
        av.scatter(p, v, s=20, c=color, marker=marker, alpha=0.75)

    ax.set(xlim=(1.145, 1.255), ylim=(38, 54), xlabel=r"Selected $p$ (GeV/$c$)",
           ylabel="Ideal-flight time (ns)", title="A. Constant speed over 12 m")
    ax.legend(loc="center right", framealpha=1, fontsize=10)
    ax.text(1.151, 52.9, r"$m^2c^4=p^2c^2[(ct/L)^2-1]$", fontsize=10)
    av.axhspan(0.75, 0.78, color="#39865a", alpha=0.17)
    av.axhspan(0.79, 1.015, color="#b93643", alpha=0.055)
    av.axhline(0.79, color="#b93643", ls="--", lw=1.2)
    av.text(1.149, 0.754, "C2 acceptance", color="#236143", fontsize=10)
    av.text(1.149, 0.807, "C1 guard: reject fast particles", color="#a02432", fontsize=9)
    av.scatter([1.17, 1.19, 1.21, 1.23], [0.768, 0.775, 0.762, 0.773],
               marker="x", s=55, color="#ba5b17", linewidths=2, zorder=5)
    av.annotate("Artificial false C2 responses\nfrom scattering: C1 still rejects",
                xy=(1.21, 0.762), xytext=(1.151, 0.86), fontsize=9,
                arrowprops={"arrowstyle": "->", "color": "#ba5b17"}, color="#91400d")
    av.set(xlim=(1.145, 1.255), ylim=(0.735, 1.015), xlabel=r"Upstream selected $p$ (GeV/$c$)",
           ylabel=r"Later local $\beta=v/c$", title="B. Toy 40 MeV loss, then local speed")
    for axis in (ax, av):
        axis.grid(alpha=0.18)
        axis.tick_params(labelsize=10)
        axis.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.04, "Different stages: flight assumes constant speed; later energy loss changes the local speed.",
             ha="center", fontsize=10, color="#4c5968")
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.17, top=0.79, wspace=0.30)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
