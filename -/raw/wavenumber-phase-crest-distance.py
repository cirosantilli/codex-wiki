"""Synthetic monochromatic-wave phase and crest distances.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    wavelength, frequency = 0.4, 5.0
    k, omega = 2 * np.pi / wavelength, 2 * np.pi * frequency
    period = 1 / frequency
    x = np.linspace(0, 1, 2001)
    fig, (wave, phase) = plt.subplots(2, 1, figsize=(8, 6), sharex=True,
                                     layout="constrained", facecolor="white")
    for time, color, label in [(0, "#14699c", r"$t=0$"),
                               (period / 4, "#bd4f1c", r"$t=T/4=0.05$ s")]:
        phi = k * x - omega * time
        wave.plot(x, np.cos(phi), color=color, lw=2, label=label)
        phase.plot(x, phi / (2 * np.pi), color=color, lw=2, label=label)
    wave.scatter([0.4, 0.8], [1, 1], color="#14699c", zorder=5)
    wave.annotate("", (0.8, 1.32), (0.4, 1.32),
                  arrowprops={"arrowstyle": "<->", "color": "#14699c"})
    wave.text(0.6, 1.4, r"$\lambda=0.40$ m (crest to crest)", ha="center")
    wave.annotate("", (0.5, -1.32), (0.4, -1.32),
                  arrowprops={"arrowstyle": "->", "color": "#bd4f1c"})
    wave.text(0.57, -1.41, r"crest advance $\lambda/4=0.10$ m", ha="center", va="top")
    wave.set_ylim(-1.75, 1.75)
    wave.set_ylabel(r"Disturbance $u/A$")
    wave.legend(loc="lower left", fontsize=9)
    phase.scatter([0.4, 0.8], [1, 2], color="#14699c", zorder=5)
    phase.annotate(r"$\Delta\phi=2\pi$ over $\Delta x=\lambda$",
                   xy=(0.8, 2), xytext=(0.38, 2.4), fontsize=10,
                   arrowprops={"arrowstyle": "->", "color": "#14699c"})
    phase.set_ylim(-0.4, 2.8)
    phase.set_ylabel(r"Unwrapped phase $\phi/(2\pi)$")
    phase.set_xlabel("Position x (m)")
    phase.set_xticks(np.arange(0, 1.01, 0.2))
    for ax in (wave, phase):
        ax.set_facecolor("white")
        ax.set_xlim(0, 1)
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Crest spacing and phase slope: synthetic plane wave\n"
                 r"$k=5\pi$ rad/m, $\nu=2.5$ cycles/m, $f=5$ Hz, $v_p=2$ m/s", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
