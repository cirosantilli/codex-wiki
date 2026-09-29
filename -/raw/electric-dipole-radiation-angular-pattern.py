"""Draw electric-dipole-radiation-angular-pattern.png in the current directory.

Calculated small-dipole radiation-zone pattern; no experimental data.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    blue, orange = "#1766a6", "#bc5710"
    theta = np.linspace(0, 2 * np.pi, 1001)
    pattern = np.sin(theta) ** 2
    fig = plt.figure(figsize=(10.4, 5.2), facecolor="white")
    fig.suptitle("Electric dipole radiation: direction changes received power", fontsize=17, y=0.97)
    fig.text(0.5, 0.89, r"Radiation-zone model: normalized power per solid angle $=\sin^2\theta$",
             ha="center", fontsize=13)

    polar = fig.add_axes((0.05, 0.23, 0.39, 0.53), projection="polar", facecolor="white")
    polar.set_theta_zero_location("N")
    polar.set_theta_direction(-1)
    polar.plot(theta, pattern, color=blue, lw=2.7)
    polar.fill(theta, pattern, color=blue, alpha=0.12)
    polar.set_ylim(0, 1.12)
    polar.set_rticks([0.5, 1.0], labels=["0.5", "1"])
    polar.set_rlabel_position(60)
    polar.set_thetagrids([0, 45, 90, 135, 180, 225, 270, 315])
    for angle in [0, np.pi]:
        polar.plot([angle, angle], [0, 1.1], "--", color=orange, lw=1.6)
    fig.text(0.24, 0.105, "Dipole axis: dashed vertical line\nCurve radius means power, not distance",
             ha="center", fontsize=11, linespacing=1.5)

    angular = fig.add_axes((0.56, 0.23, 0.40, 0.51), facecolor="white")
    degrees = np.linspace(0, 180, 501)
    angular.plot(degrees, np.sin(np.deg2rad(degrees)) ** 2, color=blue, lw=2.7)
    angular.scatter([0, 30, 90, 180], [0, 0.25, 1, 0], color=orange, s=34, zorder=3)
    angular.annotate("30°: one quarter", (30, 0.25), xytext=(52, 0.17), fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": orange})
    angular.annotate("Maximum across axis", (90, 1), xytext=(90, 1.13), ha="center", fontsize=11)
    angular.set(xlim=(-4, 184), ylim=(-0.05, 1.23), xlabel=r"Angle $\theta$ from dipole axis (degrees)",
                ylabel="Normalized power per solid angle")
    angular.set_xticks([0, 30, 60, 90, 120, 150, 180])
    angular.set_yticks([0, 0.25, 0.5, 0.75, 1])
    angular.grid(alpha=0.2)
    fig.text(0.75, 0.105, r"Total-power normalization: $(1/P)\,dP/d\Omega=(3/8\pi)\sin^2\theta$",
             ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Calculated curves, not measured data. Rotate the polar pattern about the dipole axis for all directions.",
             ha="center", fontsize=10.5)
    fig.savefig("electric-dipole-radiation-angular-pattern.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
