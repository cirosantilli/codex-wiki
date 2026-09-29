"""Synthetic spatial tones, their sum, and a sampling ambiguity.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 1, 3001)
    low = np.cos(2 * np.pi * 2 * x)
    high = np.cos(2 * np.pi * 8 * x)
    fig, axes = plt.subplots(3, 1, figsize=(8, 7.2), sharex=True,
                             layout="constrained", facecolor="white")
    axes[0].plot(x, low, color="#14699c", lw=2, label=r"$\nu_1=2$ cycles/m; $\lambda_1=0.50$ m")
    axes[0].plot(x, high, color="#bd4f1c", lw=1.5, label=r"$\nu_2=8$ cycles/m; $\lambda_2=0.125$ m")
    axes[0].legend(loc="upper right", fontsize=9)
    axes[0].set_ylabel("Individual tones")
    for ax, pitch, title in [(axes[1], 0.05, "20 samples/m: Nyquist limit 10 cycles/m"),
                              (axes[2], 0.1, "10 samples/m: 8 cycles/m aliases to 2 cycles/m")]:
        samples = np.arange(round(1 / pitch) + 1) * pitch
        values = np.cos(2 * np.pi * 2 * samples) + 0.5 * np.cos(2 * np.pi * 8 * samples)
        ax.plot(x, low + 0.5 * high, color="#555555", lw=1.4, label="Actual two-tone sum")
        ax.scatter(samples, values, color="#14699c", s=24, zorder=4, label="Spatial samples")
        if pitch == 0.1:
            ax.plot(x, 1.5 * low, "--", color="#803ca3", lw=2,
                    label="Indistinguishable single tone: 1.5 cos(4πx)")
        ax.set_title(title + f"; pitch p = {pitch:.2f} m", fontsize=10)
        ax.set_ylabel(r"Sum $u/A$")
        ax.legend(loc="lower left", fontsize=8)
        ax.set_ylim(-1.95, 1.95)
    for ax in axes:
        ax.set_xlim(0, 1)
        ax.set_facecolor("white")
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylim(-1.35, 1.7)
    axes[-1].set_xlabel("Position x (m)")
    fig.suptitle("Two spatial tones: synthetic snapshots and sampling ambiguity", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
