"""Illustrate a specified FM phase; emit the matching PNG in the current directory.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0.0, 2.0, 10001)
    fc, fm, deviation = 20.0, 1.0, 5.0
    beta = deviation / fm
    phase = 2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t)
    waveform = np.cos(phase)
    instantaneous_frequency = fc + deviation * np.cos(2 * np.pi * fm * t)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(9.8, 6.4), dpi=110,
                             sharex=True, layout="constrained",
                             gridspec_kw={"height_ratios": [1.45, 1]})
    fig.set_facecolor("white")
    fig.suptitle("Frequency modulation: constant amplitude, changing timing", fontsize=15)
    axes[0].set_title(r"Original model: $f_c=20$ Hz, $f_m=1$ Hz, $\Delta f=5$ Hz, $\beta=5$",
                      fontsize=11)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlim(0, 2)
        ax.set_xticks(np.arange(0, 2.01, 0.25))
        ax.grid(axis="x", color="#e4e7eb", linewidth=0.8)
        for center in (0.0, 1.0, 2.0):
            ax.axvspan(max(0, center - 0.12), min(2, center + 0.12),
                       color="#e2f0fa", zorder=0)
        for center in (0.5, 1.5):
            ax.axvspan(center - 0.12, center + 0.12, color="#fff0db", zorder=0)
    axes[0].plot(t, waveform, color="#205a8c", lw=1.25)
    for bound in (-1, 1):
        axes[0].axhline(bound, color="#59646e", ls="--", lw=1)
    axes[0].set_ylim(-1.45, 1.55)
    axes[0].set_yticks([-1, 0, 1])
    axes[0].set_ylabel(r"Real waveform $s(t)/A$")
    axes[0].text(0.04, 1.15, r"Envelope bounds: $\pm A$", color="#434b53")
    axes[0].text(0.78, 1.15, "closer cycles", color="#205a8c")
    axes[0].text(1.29, 1.15, "wider cycles", color="#91520e")
    axes[1].plot(t, instantaneous_frequency, color="#217865", lw=2.1)
    axes[1].axhline(fc, color="#59646e", ls="--", lw=1)
    axes[1].set_ylim(13.5, 27.7)
    axes[1].set_yticks([15, 20, 25])
    axes[1].set_ylabel(r"$f_i(t)=\phi'(t)/(2\pi)$  [Hz]")
    axes[1].set_xlabel("Time [s]")
    axes[1].text(0.57, 26.1, r"$f_i(t)=20+5\cos(2\pi t)$ Hz", color="#217865")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
