"""Chosen finite-time rate-zonal model; run from _media to create the PNG.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The dimensionless arrival time is theoretical, not an operating instruction.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def position(time, rate):
    return 2 - 1.9 * np.exp(-rate * time)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    colors = {"A": "#1763a6", "B": "#d96a0b"}
    rates = {"A": 0.15, "B": 0.6}
    fig = plt.figure(figsize=(10, 5.6), facecolor="white")
    tubes = fig.add_axes((0.08, 0.22, 0.41, 0.57))
    trajectories = fig.add_axes((0.59, 0.22, 0.37, 0.57))
    tubes.set(xlim=(-0.35, 4.2), ylim=(1.12, -0.16))
    tubes.axis("off")
    for center, time in [(0.45, 0), (1.95, 0.5), (3.45, 1)]:
        left, width = center - 0.3, 0.6
        tubes.imshow(np.linspace(0, 1, 150)[:, None], cmap="Blues", alpha=0.19,
                     extent=(left, left + width, 1, 0), aspect="auto", vmin=0, vmax=1)
        tubes.add_patch(Rectangle((left, 0), width, 1, fill=False,
                                  edgecolor="#52626f", linewidth=1.6))
        tubes.text(center, -0.10, rf"$\tau={time:g}$", ha="center", fontsize=12)
        for name, rate in rates.items():
            value = position(time, rate)
            offset = width / 2 if time == 0 and name == "B" else 0
            band_width = width / 2 if time == 0 else width
            tubes.add_patch(Rectangle((left + offset, value - 0.012), band_width,
                                      0.024, color=colors[name], linewidth=0))
            if time != 0:
                tubes.text(left + width + 0.08, value, name, va="center", fontsize=10)
        if time == 0:
            tubes.text(left + width + 0.08, 0.1, "A + B", va="center", fontsize=10)
        tubes.text(center, 1.08, "denser", ha="center", color="#52626f", fontsize=10)
    tubes.annotate("", xy=(-0.16, 0.82), xytext=(-0.16, 0.16),
                   arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.4})
    tubes.text(-0.29, 0.49, "outward", rotation=90, ha="center", va="center")
    for name, rate in rates.items():
        arrival = np.log(1.9) / rate
        time = np.linspace(0, min(1.25, arrival), 251)
        trajectories.plot(time, position(time, rate), color=colors[name], lw=2.5,
                          label=f"{name}: λ={rate}")
    arrival = np.log(1.9) / rates["B"]
    trajectories.axhline(1, color="#52626f", lw=1.2)
    trajectories.axvline(arrival, color=colors["B"], ls="--", lw=1)
    trajectories.plot([arrival], [1], "o", color=colors["B"], ms=6)
    trajectories.text(arrival - 0.025, 0.70, "B reaches boundary\nτ ≈ 1.0698",
                      ha="right", fontsize=10, color=colors["B"])
    trajectories.set(xlim=(0, 1.25), ylim=(1.04, 0), xlabel=r"Chosen time $\tau$",
                     ylabel=r"Outward position $u$", yticks=[0, 0.25, 0.5, 0.75, 1])
    trajectories.grid(alpha=0.16)
    trajectories.legend(loc="upper right", fontsize=10, frameon=False)
    fig.suptitle("Rate-zonal migration: separate before the bands reach the wall", y=0.97,
                 fontsize=15)
    fig.text(0.5, 0.86, r"Chosen model: $du/d\tau=\lambda(2-u)$; matching density at $q=2$ is outside the column",
             ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Equal buoyant density; B has twice A's sphere radius and four times its rate parameter.\n"
             "Fixed gradient; diffusion omitted; schematic band thickness; no experimental data.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
