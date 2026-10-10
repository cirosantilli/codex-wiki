"""Toy series RLC predictions, never measured data.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../reactance-frequency-cancellation.py
Writes reactance-frequency-cancellation.png to CWD.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    L, C, R, Rs, Vrms = 10e-3, 1e-6, 100.0, 10.0, 1.0
    f0 = 1 / (2 * np.pi * np.sqrt(L * C))
    f = np.unique(np.r_[np.geomspace(200, 8000, 900), f0])
    w = 2 * np.pi * f
    xl, xc = w * L, -1 / (w * C)
    x = xl + xc
    current = Vrms / np.hypot(R + Rs, x)
    phase = np.degrees(np.arctan2(x, R + Rs))
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig = plt.figure(figsize=(10.4, 7.2), layout="constrained")
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 1])
    top, left, right = fig.add_subplot(gs[0, :]), fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])
    fig.suptitle("Opposite reactances select a frequency\n"
                 "Toy prediction: L = 10 mH, C = 1 μF, RΣ = 100 + 10 = 110 Ω, Vᵣₘₛ = 1.00 V\n"
                 "Ideal calculated curves • no measured data", fontsize=13)
    top.semilogx(f, xl, color="#b7560b", label=r"$X_L=2\pi fL$", linewidth=2)
    top.semilogx(f, xc, color="#2855a5", label=r"$X_C=-1/(2\pi fC)$", linewidth=2)
    top.semilogx(f, x, color="#177352", label=r"$X=X_L+X_C$", linewidth=2.5)
    top.axhline(0, color="0.4", linewidth=0.8)
    top.plot(f0, 0, "o", color="#177352")
    top.annotate("Cancellation\nf₀ = 1.592 kHz", xy=(f0, 0), xytext=(2300, -470),
                 arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=11)
    top.set(ylabel="Signed reactance (Ω)", ylim=(-820, 570))
    top.legend(loc="upper left", ncols=3, fontsize=11)
    left.semilogx(f, 1000 * current, color="#177352", linewidth=2.3)
    left.plot(f0, 1000 * Vrms / (R + Rs), "o", color="#177352")
    left.annotate("9.091 mA", xy=(f0, 1000 * Vrms / (R + Rs)), xytext=(2500, 9.6),
                  arrowprops={"arrowstyle": "->", "color": "0.3"})
    left.set(ylabel="RMS current (mA)", ylim=(0, 11), xlabel="Frequency f (Hz)")
    right.semilogx(f, phase, color="#653c96", linewidth=2.3)
    right.axhline(0, color="0.4", linewidth=0.8)
    right.text(260, -43, "Current leads\nX < 0", color="#2855a5")
    right.text(2700, 21, "Current lags\nX > 0", color="#b7560b")
    right.set(ylabel="Voltage − current phase (degrees)", ylim=(-90, 90),
              yticks=[-90, -45, 0, 45, 90], xlabel="Frequency f (Hz)")
    for ax in (top, left, right):
        ax.axvline(f0, color="0.45", linestyle=":", linewidth=1.2)
        ax.set_xlim(200, 8000)
        ax.set_xticks([200, 500, 1000, 2000, 5000, 8000])
        ax.set_xticklabels(["200", "500", "1000", "2000", "5000", "8000"])
        ax.grid(alpha=0.17)
    fig.savefig(Path.cwd() / "reactance-frequency-cancellation.png", dpi=105,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
