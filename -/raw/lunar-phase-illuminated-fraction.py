"""Original projected-area curve; output PNG basename in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Alpha is the Sun–Moon–observer angle AT THE MOON; this is not a flux curve.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    alpha = np.linspace(0, np.pi, 501)
    k = (1 + np.cos(alpha)) / 2
    fig, ax = plt.subplots(figsize=(8, 4.8), facecolor="white")
    fig.subplots_adjust(left=0.12, right=0.95, bottom=0.31, top=0.82)
    ax.plot(alpha, k, color="#285b85", lw=2.7)
    for a, value, label in [(0, 1, "Full: k = 1"), (np.pi/2, 0.5, "Quarter: k = 1/2"),
                            (np.pi, 0, "New: k = 0")]:
        ax.plot(a, value, "o", color="#a46f08", ms=7)
        ax.annotate(label, (a, value), xytext=(10 if a < np.pi else -10, 12 if value < 1 else -22),
                    textcoords="offset points", ha="left" if a < np.pi else "right", fontsize=11)
    ax.set_xlim(-0.04, np.pi + 0.04)
    ax.set_ylim(-0.06, 1.06)
    ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi],
                  [r"$0$", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xlabel(r"Phase angle $\alpha$ at the Moon (radians)", labelpad=10)
    ax.set_ylabel(r"Illuminated projected disk fraction $k$")
    ax.grid(alpha=0.22)
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Lunar disk geometry: $k=(1+\cos\alpha)/2$", fontsize=16, y=0.96)
    fig.text(0.5, 0.075,
             "Sun–Moon–observer angle: full → quarter → new as α increases.\n"
             "Spherical model with parallel sunlight and distant observer; eclipses excluded.\n"
             "Geometric area fraction, not received flux relative to full Moon.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
