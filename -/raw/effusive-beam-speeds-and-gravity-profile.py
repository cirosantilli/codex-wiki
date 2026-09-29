"""Original normalized distributions for stipulated beam parameters.

Reservoir: Maxwell speed law. Arrival count: v-weighted effusive law.
Point-launch gravity model: y=C/v**2; include the density Jacobian.
No historical measured data. Output basename.png to the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    mass = 133*1.66053906892e-27
    kb, temperature, distance, gravity = 1.380649e-23, 500., 1.5, 9.81
    a = mass/(2*kb*temperature)
    c = gravity*distance**2/2
    b = a*c
    speed = np.linspace(0, 850, 1400)
    reservoir = 4*a**1.5/np.sqrt(np.pi)*speed**2*np.exp(-a*speed**2)
    arrivals = 2*a**2*speed**3*np.exp(-a*speed**2)
    height = np.linspace(.1, 550, 2000)*1e-6
    height_density = b*b/height**3*np.exp(-b/height)
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.3), dpi=110, facecolor="white")
    fig.suptitle("A particle counter samples flux; a height scan transforms it", fontsize=15)
    ax = axes[0]
    ax.plot(speed, reservoir, lw=2.4, color="#666d73", label="Reservoir particles: f(v)")
    ax.plot(speed, arrivals, lw=2.4, color="#36779d", label="Arrivals per time: v f(v) / ⟨v⟩")
    ax.set(xlabel="Speed (m/s)", ylabel="Speed density (s/m)", title="Effusion favors faster arrivals", xlim=(0, 850))
    ax.legend(fontsize=10)
    ax.grid(alpha=.2)
    ax.text(.43, .44, "Chosen: m = 133 u, T = 500 K\nReservoir mode: 250.0 m/s\nArrival mode: 306.2 m/s", transform=ax.transAxes, fontsize=10, bbox={"facecolor": "white", "alpha": .92, "edgecolor": "none", "pad": 4})
    ax = axes[1]
    ax.plot(height*1e6, height_density*1e-6, lw=2.4, color="#36779d", label="Height density, with Jacobian")
    ax.axvline(b/3*1e6, color="#b34e33", ls="--", label=f"Height-density mode: {b/3*1e6:.1f} μm")
    ax.axvline(2*b/3*1e6, color="#785289", ls=":", label=f"Mapped arrival-speed mode: {2*b/3*1e6:.1f} μm")
    ax.set(xlabel="Downward detector displacement (μm)", ylabel="Height density (1/μm)", title="Equal height bins are unequal speed bins", xlim=(0, 550))
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=.2)
    ax.text(.43, .43, "L = 1.50 m, g = 9.81 m/s²\nPoint launch, zero vertical speed\nCurve extends beyond this window", transform=ax.transAxes, fontsize=10)
    fig.tight_layout(rect=(0, .02, 1, .94), w_pad=2)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
