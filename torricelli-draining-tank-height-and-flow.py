"""Original stipulated drainage model; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; emit the matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    A, a, Cd, H, g = 0.1, 1e-4, 0.62, 0.25, 9.81
    T = (A / (Cd * a)) * np.sqrt(2 * H / g)
    Q0 = Cd * a * np.sqrt(2 * g * H)
    t = np.linspace(0, 1.14 * T, 600)
    remaining = np.maximum(1 - t / T, 0)
    h = H * remaining**2
    q = 1000 * Q0 * remaining
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 6.6), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.23, top=0.76, wspace=0.33)
    fig.suptitle("A draining tank slows down as the head falls", fontsize=19, y=0.955)
    fig.text(0.5, 0.89, r"$A=0.100\ {\rm m^2},\ a=10^{-4}\ {\rm m^2},\ C_d=0.620,$"
             r" $H=0.250\ {\rm m},\ g=9.81\ {\rm m\,s^{-2}}$", ha="center", fontsize=13)
    axh, axq = axes
    axh.plot(t, h, lw=3, color="#167cb4")
    axq.fill_between(t, 0, q, color="#d4eee3")
    axq.plot(t, q, lw=3, color="#168566")
    for ax in axes:
        ax.set_xlim(0, 1.14 * T)
        ax.set_xlabel("Time (s)")
        ax.set_xticks([0, T / 2, T], ["0", f"{T / 2:.1f}", f"{T:.1f}"])
        ax.axvline(T, color="#71818d", lw=1.2, ls="--")
        ax.grid(alpha=0.22)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
    axh.set_ylim(-0.007, 0.275)
    axh.set_ylabel("Head above outlet, h (m)")
    axh.set_title(r"$h=H(1-t/T)^2$ up to $T$", fontsize=15, pad=17)
    axh.plot(T / 2, H / 4, "o", color="#167cb4", ms=7)
    axh.annotate(r"At $T/2$: $h=H/4$" + "\n0.0625 m", xy=(T / 2, H / 4),
                 xytext=(0.40 * T, 0.18), arrowprops={"arrowstyle": "->", "color": "#167cb4"},
                 fontsize=12, linespacing=1.5)
    axq.set_ylim(-0.004, 0.152)
    axq.set_ylabel("Discharge, Q (L/s)")
    axq.set_title(r"$Q=Q_0(1-t/T)$ up to $T$", fontsize=15, pad=17)
    axq.plot(T / 2, 500 * Q0, "o", color="#168566", ms=7)
    axq.annotate(r"At $T/2$: $Q=Q_0/2$", xy=(T / 2, 500 * Q0),
                 xytext=(0.35 * T, 0.128), arrowprops={"arrowstyle": "->", "color": "#168566"},
                 fontsize=12)
    axq.text(0.30 * T, 0.025, "Area under curve\n= discharged volume\n= 25.0 L", ha="center",
             va="center", fontsize=12, linespacing=1.4, color="#145c49")
    fig.text(0.5, 0.12, f"Model reaches zero head at T = {T:.1f} s; h and Q remain zero afterwards.",
             ha="center", fontsize=13)
    fig.text(0.5, 0.06, "Synthetic analytic curves — a stipulated constant-coefficient model, not measured data.",
             ha="center", fontsize=11, color="#576570")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
