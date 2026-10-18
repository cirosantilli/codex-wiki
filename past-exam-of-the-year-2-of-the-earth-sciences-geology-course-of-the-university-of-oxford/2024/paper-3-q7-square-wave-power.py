"""Analytic Fourier reconstruction and harmonic powers; PNG in the CWD."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), layout="constrained")
    fig.patch.set_facecolor("white")
    time = np.linspace(0, 8, 8001)
    exact = np.where(time % 4 < 2, 1.0, -1.0)
    axes[0].step(time, exact, where="post", color="black", lw=1.5, label="Exact levels")
    for count, color in [(3, "#b65b15"), (15, "#146eab")]:
        modes = 2 * np.arange(count) + 1
        reconstruction = 4 / np.pi * np.sum(np.sin(np.pi * modes[:, None] * time / 2) / modes[:, None], axis=0)
        axes[0].plot(time, reconstruction, color=color, lw=1.4, label=f"{count} odd harmonics")
    axes[0].set(xlim=(0, 8), ylim=(-1.3, 1.3), xlabel="Time (s)", ylabel="Voltage (V)", title="Smooth partial sums resolve sharp edges")
    axes[0].legend(loc="lower right", fontsize=10)
    modes = np.arange(1, 16, 2)
    powers = 8 / (np.pi**2 * modes**2)
    axes[1].bar(modes / 4, powers, width=0.17, color="#146eab")
    axes[1].text(0.95, 0.65, "Fundamental pair:\n81.1% of total power", fontsize=12)
    axes[1].set(xlim=(0, 4), ylim=(0, 0.9), xlabel="Positive frequency of each ± pair (Hz)", ylabel="Paired mean-square voltage (V²)", title="Power falls as the inverse square of harmonic order")
    for axis in axes:
        axis.grid(alpha=0.18)
        axis.set_axisbelow(True)
    fig.suptitle("A unit square wave: odd Fourier harmonics, zero mean, total mean square 1 V²", fontsize=14)
    fig.savefig(Path.cwd() / "paper-3-q7-square-wave-power.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
