"""Plot a first-order Bode gain/phase diagram using angular frequency.

Run from _media; the opaque-white PNG is written by basename to cwd.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    gain, tau = 2.0, 3.0
    corner = 1.0 / tau
    omega = np.geomspace(corner / 100.0, corner * 100.0, 1001)
    response = gain / (1.0 + 1j * omega * tau)
    gain_db = 20.0 * np.log10(np.abs(response))
    phase = np.rad2deg(np.angle(response))
    blue, orange = "#1769aa", "#bd5500"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 1, figsize=(8.0, 6.4), sharex=True,
                             layout="constrained")
    axes[0].semilogx(omega, gain_db, color=blue, linewidth=2.4)
    axes[1].semilogx(omega, phase, color=orange, linewidth=2.4)
    corner_db = 20.0 * np.log10(gain / np.sqrt(2.0))
    low_db = 20.0 * np.log10(gain)
    axes[0].axhline(low_db, color="#666666", linestyle="--", linewidth=1)
    axes[0].text(corner / 60, low_db + 1.0,
                 "Low-frequency gain = 2 (6.02 dB)", fontsize=10)
    axes[0].scatter([corner], [corner_db], color=blue, s=40, zorder=4)
    axes[0].annotate("Corner gain = √2 (3.01 dB)\n3.01 dB below low-frequency gain",
                     xy=(corner, corner_db), xytext=(corner * 2.5, -6),
                     fontsize=10, color=blue,
                     arrowprops={"arrowstyle": "->", "color": blue})
    axes[0].set(ylabel=r"Gain $20\log_{10}|G(i\omega)|$ (dB)", ylim=(-36, 12))
    axes[1].scatter([corner], [-45], color=orange, s=40, zorder=4)
    axes[1].annotate("Corner phase = −45°", xy=(corner, -45),
                     xytext=(corner / 40, -62), fontsize=10, color=orange,
                     arrowprops={"arrowstyle": "->", "color": orange})
    axes[1].set(ylabel="Phase (degrees)", ylim=(-95, 5),
                yticks=[-90, -60, -45, -30, 0],
                xlabel=r"Angular frequency $\omega$ (rad/s), logarithmic scale")
    for ax in axes:
        ax.axvline(corner, color="#666666", linestyle=":", linewidth=1.4)
        ax.grid(which="both", alpha=0.18)
        ax.set_xlim(omega[0], omega[-1])
    fig.suptitle(r"First-order low-pass: $G(i\omega)=2/(1+3i\omega)$", fontsize=14)
    axes[0].set_title("Corner: ωc = 1/3 rad/s; fc = ωc/(2π) = 0.0531 Hz", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
