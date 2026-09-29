"""Original finite-mode comb, not measured data.

Python 3.14; matplotlib 3.10.7; numpy 2.3.5. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.arange(24, 41)
    amplitudes = np.exp(-.5*((n-32)/3)**2)
    amplitudes /= amplitudes.sum()
    q = np.linspace(-.4, 3.4, 16000)
    field = amplitudes @ np.exp(2j*np.pi*(n[:, None]+.25)*q)
    fig, axes = plt.subplots(2, 1, figsize=(9, 6), dpi=120, facecolor="white")
    ax, spectrum = axes
    ax.plot(q, field.real, color="#2179a5", lw=.75, label=r"Real field $\mathrm{Re}\,E$")
    ax.plot(q, np.abs(field), color="#26313a", lw=1.5, label=r"Envelope $|E|$")
    ax.set(xlim=(-.4, 3.4), ylim=(-1.14, 1.25), xlabel=r"Time $t/T$, with $T=1/f_r$",
           ylabel="Normalized field")
    ax.set_title(r"Equal pulse envelopes; phase advances by $\pi/2$ each period", fontsize=12)
    ax.legend(loc="center", bbox_to_anchor=(.52, .70), fontsize=9)
    for k in range(3):
        ax.annotate("", xy=(k+1, 1.12), xytext=(k, 1.12),
                    arrowprops=dict(arrowstyle="<->", color="#a35c11", lw=1))
    ax.text(1.5, 1.16, r"$T$", ha="center", fontsize=10)
    spectrum.vlines(n+.25, 0, amplitudes, color="#2179a5", lw=2)
    spectrum.plot(n+.25, amplitudes, "o", color="#2179a5", ms=3)
    spectrum.set(xlim=(23.3, 41.2), ylim=(0, .17), xlabel=r"Frequency $f/f_r$",
                 ylabel="Field amplitude")
    spectrum.set_xticks([24.25, 28.25, 32.25, 36.25, 40.25])
    spectrum.set_title(r"Same field: teeth at $f/f_r=n+1/4$, spacing $1$", fontsize=12)
    spectrum.annotate("", xy=(33.25, .151), xytext=(32.25, .151),
                      arrowprops=dict(arrowstyle="<->", color="#a35c11"))
    spectrum.text(32.75, .155, r"$f_r$", ha="center", fontsize=10)
    for axis in axes:
        axis.spines[["top", "right"]].set_visible(False)
        axis.grid(alpha=.16)
    fig.suptitle("One synthetic field, two complementary views", fontsize=15, y=.98)
    fig.text(.5, .015, r"17 Gaussian-weighted modes; $f_0/f_r=1/4$. Dimensionless teaching example.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .04, 1, .94), h_pad=1.7)
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
