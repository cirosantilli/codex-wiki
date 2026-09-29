"""Plot three harmonics and their sum; write fourier-frequency-decomposition.png to cwd.

Uses the root pyproject.toml dependencies. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    time = np.linspace(0, 1, 1201)
    frequencies = np.array([1, 3, 5])
    amplitudes = np.array([1, 0.5, 0.25])
    components = amplitudes[:, None] * np.cos(2 * np.pi * frequencies[:, None] * time)
    colors = ["#2266aa", "#ce6a16", "#26845b"]
    fig, axes = plt.subplots(3, 1, figsize=(8.8, 8), layout="constrained",
                             gridspec_kw={"height_ratios": [1.1, 1.1, 1]})
    fig.suptitle("Three harmonics, one waveform", fontsize=18)
    for component, frequency, amplitude, color in zip(components, frequencies, amplitudes, colors):
        axes[0].plot(time, component, color=color, lw=2,
                     label=f"{frequency} cycles/s; amplitude {amplitude:g}")
    axes[0].set_title("The simple oscillations", loc="left")
    axes[0].legend(loc="lower left", ncol=3, fontsize=9)
    axes[0].set_ylim(-1.4, 1.25)
    axes[1].plot(time, components.sum(axis=0), color="#343745", lw=2.5)
    axes[1].set_title(r"Their sum: $f(t)=\cos(2\pi t)+\frac{1}{2}\cos(6\pi t)+\frac{1}{4}\cos(10\pi t)$",
                      loc="left", fontsize=11)
    axes[1].set_ylim(-1.9, 1.9)
    for ax in axes[:2]:
        ax.set(xlim=(0, 1), xlabel="Time (seconds)", ylabel="Value")
        ax.axhline(0, color="#aaaaaa", lw=0.8, zorder=0)
        ax.grid(alpha=0.18)
    axes[2].vlines(frequencies, 0, amplitudes, colors=colors, lw=3)
    axes[2].scatter(frequencies, amplitudes, c=colors, s=50, zorder=3)
    for frequency, amplitude in zip(frequencies, amplitudes):
        axes[2].text(frequency + 0.15, amplitude + 0.03, f"{amplitude:g}")
    axes[2].set(title="The same recipe in frequency coordinates (one-sided amplitudes)",
                xlabel="Frequency (cycles per second)", ylabel="Cosine amplitude",
                xlim=(0, 6), ylim=(0, 1.22), xticks=np.arange(7))
    axes[2].grid(alpha=0.18)
    fig.savefig(Path("fourier-frequency-decomposition.png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
