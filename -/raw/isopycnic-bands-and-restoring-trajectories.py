"""Chosen linear-gradient drift model; run from _media to create the PNG.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
No experimental traces, instrument settings or measured band widths are used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def position(time, target, rate, initial):
    return target + (initial - target) * np.exp(-rate * time)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    colors = {"A": "#1763a6", "B": "#d96a0b", "C": "#7447a5"}
    species = {"A": (0.45, 0.4, 0.1), "B": (0.45, 1.6, 0.95),
               "C": (0.8, 0.8, 0.1)}
    fig = plt.figure(figsize=(10, 5.6), facecolor="white")
    tubes = fig.add_axes((0.08, 0.22, 0.41, 0.57))
    trajectories = fig.add_axes((0.59, 0.22, 0.37, 0.57))
    tubes.set(xlim=(-0.35, 4.2), ylim=(1.12, -0.16))
    tubes.axis("off")
    for center, time, heading in [(0.45, 0, r"$\tau=0$"),
                                  (1.95, 4, r"$\tau=4$"),
                                  (3.45, np.inf, "Limit")]:
        left, width = center - 0.3, 0.6
        tubes.imshow(np.linspace(0, 1, 150)[:, None], cmap="Blues", alpha=0.19,
                     extent=(left, left + width, 1, 0), aspect="auto", vmin=0, vmax=1)
        tubes.add_patch(Rectangle((left, 0), width, 1, fill=False,
                                  edgecolor="#52626f", linewidth=1.6))
        tubes.text(center, -0.10, heading, ha="center", fontsize=12)
        for name, (target, rate, initial) in species.items():
            value = target if np.isinf(time) else position(time, target, rate, initial)
            # Adjacent colored halves expose coincident species without hiding either.
            if time == 0 and name in ("A", "C"):
                offset, band_width = (0 if name == "A" else width / 2), width / 2
            elif np.isinf(time) and name in ("A", "B"):
                offset, band_width = (0 if name == "A" else width / 2), width / 2
            else:
                offset, band_width = 0, width
            tubes.add_patch(Rectangle((left + offset, value - 0.012), band_width,
                                      0.024, color=colors[name], linewidth=0))
        labels = [(0.1, "A + C"), (0.95, "B")] if time == 0 else (
            [(0.45, "A + B"), (0.8, "C")] if np.isinf(time) else
            [(position(time, *species[n]), n) for n in species])
        for value, label in labels:
            tubes.text(left + width + 0.08, value, label, va="center", fontsize=10)
        tubes.text(center, 1.08, "denser", ha="center", color="#52626f", fontsize=10)
    tubes.annotate("", xy=(-0.16, 0.82), xytext=(-0.16, 0.16),
                   arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.4})
    tubes.text(-0.29, 0.49, "outward", rotation=90, ha="center", va="center")
    time = np.linspace(0, 8, 401)
    for name, args in species.items():
        trajectories.plot(time, position(time, *args), color=colors[name], lw=2.5,
                          label=f"{name}: q={args[0]}, λ={args[1]}")
    for target in (0.45, 0.8):
        trajectories.axhline(target, color="#58646e", lw=1, ls="--")
    trajectories.set(xlim=(0, 8), ylim=(1, 0), xlabel=r"Chosen time $\tau$",
                     ylabel=r"Outward position $u$", yticks=[0, 0.45, 0.8, 1])
    trajectories.grid(alpha=0.16)
    trajectories.legend(loc="upper right", fontsize=9, frameon=False)
    fig.suptitle("Isopycnic focusing: matching density sets the destination", y=0.97,
                 fontsize=15)
    fig.text(0.5, 0.86, r"Chosen model: $du/d\tau=\lambda(q-u)$; liquid occupies $0\leq u\leq1$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, "A and B converge from opposite sides. C has a different matching density.\n"
             "Fixed gradient; diffusion omitted; schematic band thickness; no experimental data.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
