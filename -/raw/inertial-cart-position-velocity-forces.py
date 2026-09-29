"""Plot exact cart kinematics while two balancing forces are switched off.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes inertial-cart-position-velocity-forces.png to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(3, 1, figsize=(9, 7.5), dpi=120, sharex=True,
                             facecolor="white", gridspec_kw={"height_ratios": [1, 1, 1.35]})
    time = np.linspace(0, 4, 401)
    axes[0].plot(time, 1.5 * time, color="#176a9b", linewidth=2.8)
    axes[0].set(ylabel="Position x (m)", ylim=(-0.4, 6.6), yticks=[0, 3, 6])
    axes[0].text(0.12, 5, "x(t) = 1.5t", color="#176a9b")
    axes[1].plot(time, np.full_like(time, 1.5), color="#176a9b", linewidth=2.8)
    axes[1].set(ylabel="Velocity vₓ (m/s)", ylim=(-0.2, 2.2), yticks=[0, 1.5])
    axes[1].text(0.12, 0.45, "vₓ(t) = +1.5 m/s throughout", color="#176a9b")
    force_ax = axes[2]
    for value, color, label in [(6, "#b3482f", "Rightward device"),
                               (-6, "#725299", "Leftward device")]:
        force_ax.plot([0, 2], [value, value], color=color, linewidth=2.5, label=label)
        force_ax.plot(2, value, marker="o", markersize=7, markerfacecolor="white",
                      markeredgecolor=color, markeredgewidth=1.8, zorder=5)
        force_ax.plot([2, 4], [0, 0], color=color, linewidth=2.5)
    force_ax.plot(time, np.zeros_like(time), color="#267b52", linestyle="--",
                  linewidth=2, label="Net horizontal force", zorder=6)
    force_ax.plot(2, 0, "o", color="#267b52", markersize=7, zorder=7)
    force_ax.set(ylabel="Horizontal force (N)", xlabel="Time t (s)",
                 ylim=(-8.5, 8.5), yticks=[-6, 0, 6], xlim=(0, 4), xticks=[0, 1, 2, 3, 4])
    force_ax.legend(loc="lower right", fontsize=9, framealpha=1)
    for ax in axes:
        ax.axvspan(0, 2, color="#f2ede5", alpha=0.8, zorder=0)
        ax.axvline(2, color="#666666", linestyle=":", linewidth=1.3)
        ax.grid(axis="y", alpha=0.22)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_title("2 kg cart: both balancing horizontal forces switch off at t = 2 s",
                      fontsize=14, pad=25)
    axes[0].text(1, 6.85, "Both devices on", ha="center", fontsize=10)
    axes[0].text(3, 6.85, "Both devices off; no impulse", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.13, right=0.97, top=0.87, bottom=0.1, hspace=0.2)
    fig.text(0.5, 0.025, "Exact model curves, not measured data. Vertical forces remain balanced.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "inertial-cart-position-velocity-forces.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
