"""Synthetic modes of x' = -x - 2*x(t-d); no biological measurements.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; write matching-basename opaque white PNG to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def characteristic_root(delay):
    """Follow the oscillatory branch from its first imaginary-axis crossing."""
    critical = 2 * np.pi / (3 * np.sqrt(3))
    z = 1j * np.sqrt(3)
    for d in np.linspace(critical, delay, 100):
        for _ in range(30):
            step = (z + 1 + 2 * np.exp(-z * d)) / (1 - 2 * d * np.exp(-z * d))
            z -= step
            if abs(step) < 1e-14:
                break
    assert abs(z + 1 + 2 * np.exp(-z * delay)) < 1e-11
    return z


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    critical = 2 * np.pi / (3 * np.sqrt(3))
    fig = plt.figure(figsize=(10, 7), dpi=110)
    grid = fig.add_gridspec(2, 1, height_ratios=(1, 3), hspace=0.24)
    circuit = fig.add_subplot(grid[0])
    circuit.set(xlim=(0, 10), ylim=(0, 3))
    circuit.axis("off")
    circuit.text(5, 2.6, "SYNTHETIC LINEAR MODEL — no biological data", ha="center", weight="bold")
    for px, text in ((2, "Displacement x(t)"), (8, "Return after delay d")):
        circuit.text(px, 1.4, text, ha="center", va="center", bbox={"boxstyle": "round,pad=0.6", "fc": "white", "ec": "#334155"})
    circuit.annotate("", (6.4, 1.7), (3.5, 1.7), arrowprops={"arrowstyle": "->", "color": "#334155"})
    circuit.text(5, 1.9, "+", ha="center")
    circuit.annotate("", (3.5, 0.8), (6.4, 0.8), arrowprops={"arrowstyle": "-[", "color": "#334155"})
    circuit.text(5, 0.10, "Negative return: −2x(t−d); local removal: −x(t)", ha="center")
    ax = fig.add_subplot(grid[1])
    t = np.linspace(0, 12, 2401)
    ax.plot(t, np.exp(-3 * t), color="#475569", lw=2, label="d = 0: exponential decay")
    for d, color, label in ((0.7, "#187c64", "d = 0.7: damped mode"), (critical, "#2468b4", f"d = {critical:.4f}: neutral mode"), (1.5, "#ba4a29", "d = 1.5: growing mode")):
        z = characteristic_root(d)
        ax.plot(t, np.exp(z.real * t) * np.cos(z.imag * t), color=color, lw=2, label=label)
    ax.axhline(0, color="#94a3b8", lw=0.8)
    ax.set(xlabel="Time t (normalized units)", ylabel="Signed displacement x(t)", xlim=(0, 12), ylim=(-2.7, 2.7))
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left", ncol=2, fontsize=10, framealpha=1)
    ax.text(0.99, 0.02, "Each curve uses its own matching exponential-mode history.\nGrowing oscillations are instability, not a bounded limit cycle.", transform=ax.transAxes, ha="right", va="bottom", fontsize=10, bbox={"fc": "white", "ec": "none"})
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.10, top=0.96)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
