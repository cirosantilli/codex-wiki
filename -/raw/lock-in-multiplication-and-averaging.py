"""Original lock-in waveforms; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes lock-in-multiplication-and-averaging.png to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    cycles = np.linspace(0, 4, 8001)
    theta = 2 * np.pi * cycles
    wanted = 0.4 * np.cos(theta + np.pi / 3)
    interference = 0.9 * np.cos(3 * theta + np.pi / 5)
    signal = wanted + interference
    px = 2 * signal * np.cos(theta)
    py = -2 * signal * np.sin(theta)
    # Composite trapezoidal integrals of the computed products, divided by time.
    dt = cycles[1] - cycles[0]
    ix = np.r_[0, np.cumsum((px[:-1] + px[1:]) * dt / 2)]
    iy = np.r_[0, np.cumsum((py[:-1] + py[1:]) * dt / 2)]
    use = cycles >= 0.15
    x_running = ix[use] / cycles[use]
    y_running = iy[use] / cycles[use]
    for n in range(1, 5):
        k = np.argmin(abs(cycles - n))
        np.testing.assert_allclose([ix[k] / n, iy[k] / n],
                                   [0.2, 0.2 * np.sqrt(3)], atol=1e-12)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(3, 1, figsize=(9, 7.5), sharex=True,
                             layout="constrained", facecolor="white")
    blue, orange = "#1663a6", "#c45111"
    axes[0].plot(cycles, signal, color="#6a6f75", lw=1.5, label="Input: wanted + third harmonic")
    axes[0].plot(cycles, wanted, color=blue, lw=2, label="Wanted: 0.4 cos(2πt + π/3) V")
    axes[0].set_title("A larger third harmonic cancels after coherent averaging", fontsize=14)
    axes[0].set_ylabel("Input (V)")
    axes[0].legend(loc="upper right", fontsize=9, ncol=2)
    axes[1].plot(cycles, px, color=blue, lw=1.4, label=r"$2s(t)\cos(2\pi t)$")
    axes[1].plot(cycles, py, color=orange, lw=1.4, label=r"$-2s(t)\sin(2\pi t)$")
    axes[1].axhline(0.2, color=blue, ls="--", lw=1)
    axes[1].axhline(0.2 * np.sqrt(3), color=orange, ls="--", lw=1)
    axes[1].set_ylabel("Products (V)")
    axes[1].legend(loc="upper right", fontsize=10, ncol=2)
    axes[2].plot(cycles[use], x_running, color=blue, lw=1.7, label=r"$X(t)$")
    axes[2].plot(cycles[use], y_running, color=orange, lw=1.7, label=r"$Y(t)$")
    axes[2].axhline(0.2, color=blue, ls="--", lw=1)
    axes[2].axhline(0.2 * np.sqrt(3), color=orange, ls="--", lw=1)
    axes[2].scatter(np.arange(1, 5), np.full(4, 0.2), color=blue, zorder=4, s=28)
    axes[2].scatter(np.arange(1, 5), np.full(4, 0.2 * np.sqrt(3)), color=orange, zorder=4, s=28)
    axes[2].set_ylim(-0.5, 0.9)
    axes[2].set_ylabel("Running averages (V)")
    axes[2].set_xlabel("Time / reference period  (reference frequency = 1 Hz)")
    axes[2].legend(loc="upper right", fontsize=10)
    axes[2].text(2.1, 0.71, "At every complete cycle:\nX = 0.200 V, Y = 0.346410 V", fontsize=10)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.set_xlim(0, 4)
    fig.get_layout_engine().set(rect=(0, 0.04, 1, 0.96))
    fig.text(0.5, 0.012, "Constructed waveforms • interference = 0.9 cos(6πt + π/5) V • peak convention",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
