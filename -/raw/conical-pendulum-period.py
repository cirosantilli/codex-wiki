"""Plot ideal predictions for stipulated parameters, never measured data.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
The matching PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    blue, orange, green = "#235d9f", "#c65b16", "#167146"
    length, gravity = 1.0, 9.81
    p0 = 2 * np.pi * np.sqrt(length / gravity)
    degrees = np.linspace(0, 80, 401)
    periods = p0 * np.sqrt(np.cos(np.deg2rad(degrees)))
    sample_degrees = np.array([15.0, 40.0, 60.0])
    sample_drop = length * np.cos(np.deg2rad(sample_degrees))
    sample_period = 2 * np.pi * np.sqrt(sample_drop / gravity)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.8))
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.19, top=0.74, wspace=0.30)
    fig.suptitle("Conical pendulum: period and a testable straight line", fontsize=17, y=0.96)
    fig.text(0.5, 0.87, r"Ideal predictions, not measured data: $\ell=1.00$ m, $g=9.81$ m/s$^2$", ha="center")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.20)
        ax.set_axisbelow(True)

    ax = axes[0]
    ax.set_title("Wider cone, shorter period", fontsize=13, pad=14)
    ax.plot(degrees, periods, color=blue, lw=2.5)
    ax.axhline(p0, color=green, ls="--", lw=1.6)
    ax.plot(0, p0, "o", mfc="white", mec=blue, ms=7, zorder=5)
    ax.scatter(sample_degrees, sample_period, color=orange, s=35, zorder=5)
    ax.text(8, p0 + 0.035, r"Small-angle limit $P_0=2.006$ s", color=green, fontsize=11)
    ax.text(26, 1.15, r"$P=P_0\sqrt{\cos\theta}$", color=blue, fontsize=14)
    ax.annotate("40°: 1.756 s", xy=(40, sample_period[1]), xytext=(47, 1.90), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": orange}, color=orange)
    ax.set(xlim=(-1, 81), ylim=(0.72, 2.17), xlabel=r"Angle from downward vertical $\theta$ (degrees)", ylabel="Revolution period P (s)")
    ax.set_xticks([0, 20, 40, 60, 80])

    ax = axes[1]
    drops = np.linspace(0, length, 401)
    ax.plot(drops, 4 * np.pi**2 * drops / gravity, color=blue, lw=2.5)
    ax.scatter(sample_drop, sample_period**2, color=orange, s=35, zorder=5)
    ax.plot(length, p0**2, "o", mfc="white", mec=blue, ms=7, zorder=5)
    for angle, drop, period in zip(sample_degrees, sample_drop, sample_period):
        ax.annotate(f"{angle:.0f}°", (drop, period**2), xytext=(-9, 9), textcoords="offset points", ha="right", color=orange, fontsize=11)
    ax.text(0.06, 3.3, r"$P^2=\frac{4\pi^2}{g}h$", color=blue, fontsize=16)
    ax.text(0.07, 2.63, "Slope = 4.024 s²/m", color=blue, fontsize=11)
    ax.set_title("Measure height and timing independently", fontsize=13, pad=14)
    ax.set(xlim=(0, 1.06), ylim=(0, 4.5), xlabel=r"Pivot-to-orbit vertical drop $h$ (m)", ylabel="Squared period P² (s²)")
    fig.text(0.5, 0.055, "Orange points: chosen example angles. Open circles: zero-radius limit, not a revolution at rest.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
