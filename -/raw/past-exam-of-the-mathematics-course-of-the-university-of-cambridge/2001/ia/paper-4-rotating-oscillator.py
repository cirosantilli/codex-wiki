"""Compare an oscillator's inertial ellipse, rotating astroid and relative speed.

Write paper-4-rotating-oscillator.png to the current working directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    phase = np.linspace(0, 2 * np.pi, 801)
    relative = np.cos(phase)**3 + 1j * np.sin(phase)**3
    inertial = np.cos(2 * phase) + 0.5j * np.sin(2 * phase)
    assert np.allclose(np.exp(1j * phase) * relative, inertial)
    derivative = -3 * np.cos(phase)**2 * np.sin(phase) + 3j * np.sin(phase)**2 * np.cos(phase)
    speed = 1.5 * np.abs(np.sin(2 * phase))
    assert np.allclose(np.abs(derivative), speed)

    fig, axes = plt.subplots(1, 3, figsize=(12, 4.2), layout="constrained", facecolor="white")
    for ax, curve, title, color in [
        (axes[0], relative, "Rotating frame: astroid", "#27659f"),
        (axes[1], inertial, "Inertial frame: ellipse", "#a05b24"),
    ]:
        ax.plot(curve.real, curve.imag, color=color, lw=2.3)
        ax.scatter([1], [0], color=color, zorder=3)
        ax.annotate("initial position", xy=(1, 0), xytext=(0.1, -0.9), arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=9)
        start = 60
        ax.annotate("", xy=(curve[start + 16].real, curve[start + 16].imag), xytext=(curve[start].real, curve[start].imag), arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        ax.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), xlabel=r"$x$", ylabel=r"$y$", title=title)
        ax.set_aspect("equal")
        ax.axhline(0, color="#aaaaaa", lw=0.6)
        ax.axvline(0, color="#aaaaaa", lw=0.6)
        ax.grid(alpha=0.18)

    ax = axes[2]
    ax.plot(phase / np.pi, speed, color="#27659f", lw=2)
    peaks = np.arange(0.25, 2, 0.5)
    ax.scatter(peaks, np.full(peaks.shape, 1.5), color="#bd3030", zorder=3)
    ax.axhline(1.5, color="#bd3030", ls="--", lw=1)
    ax.set(xlim=(0, 2), ylim=(0, 1.75), xlabel=r"$\omega t/\pi$", ylabel=r"$|\dot{\mathbf{x}}|/\omega$", title="Speed in the rotating frame")
    ax.text(0.98, 0.96, r"maximum $3\omega/2$", transform=ax.transAxes, ha="right", va="top", color="#bd3030", fontsize=10)
    ax.grid(alpha=0.22)
    fig.suptitle(r"One physical oscillator, two coordinate frames ($\omega>0$, initial length unit one)", fontsize=12)
    fig.savefig(Path("paper-4-rotating-oscillator.png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
