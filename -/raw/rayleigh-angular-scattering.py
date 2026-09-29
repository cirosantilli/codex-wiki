"""Unpolarized Rayleigh beam-angle pattern; opaque PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Angle is measured from the incident propagation direction, not a dipole axis.
Radial coordinate is the relative differential cross-section, with maximum one.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0.0, 2 * np.pi, 1001)
    pattern = (1 + np.cos(theta) ** 2) / 2
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(7.8, 6.6), dpi=100,
                           subplot_kw={"projection": "polar"})
    ax.set_theta_zero_location("E")
    ax.set_theta_direction(1)
    ax.plot(theta, pattern, color="#2166ac", linewidth=2.6)
    ax.fill(theta, pattern, color="#2166ac", alpha=0.12)
    ax.set_ylim(0, 1.1)
    ax.set_rticks([0.5, 1.0])
    ax.set_rlabel_position(35)
    ax.set_thetagrids([0, 45, 90, 135, 180, 225, 270, 315],
                     labels=["0°\nForward", "45°", "90°\nSide", "135°",
                             "180°\nBackward", "225°", "270°\nSide", "315°"])
    ax.tick_params(axis="x", pad=12)
    ax.grid(alpha=0.35)
    ax.scatter([0, np.pi, np.pi / 2, 3 * np.pi / 2], [1, 1, 0.5, 0.5],
               color="#2166ac", s=45, zorder=3)
    ax.annotate("", xy=(0, 0.38), xytext=(0, 0),
                arrowprops={"arrowstyle": "-|>", "lw": 2, "color": "#34495e"})
    ax.scatter([0], [0], color="#34495e", s=25, zorder=4)
    fig.suptitle(r"Unpolarized Rayleigh scattering: $F(\theta)=\frac{1+\cos^2\theta}{2}$",
                 fontsize=16, y=0.96)
    fig.text(0.5, 0.875, "Incident beam propagates to the right; angle measured from that axis",
             ha="center", fontsize=11)
    fig.text(0.5, 0.065, "Radial coordinate: relative scattering per solid angle (maximum = 1)",
             ha="center", fontsize=11)
    fig.text(0.5, 0.03, "One plane through the beam axis; sideways response is half the forward response",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.19, right=0.81, top=0.78, bottom=0.20)
    fig.savefig(Path.cwd() / "rayleigh-angular-scattering.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
