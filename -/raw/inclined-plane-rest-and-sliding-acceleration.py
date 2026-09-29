"""Original stipulated incline model; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    g, mu_s, mu_k = 9.8, 0.45, 0.30
    degrees = np.linspace(0, 55, 551)
    theta = np.deg2rad(degrees)
    acceleration = g * (np.sin(theta) - mu_k * np.cos(theta))
    threshold = np.rad2deg(np.arctan(mu_s))
    fig, ax = plt.subplots(figsize=(9, 5.7), dpi=120)
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.axvspan(0, threshold, color="#e5efe5", zorder=0,
               label="Rest permitted by static friction")
    ax.plot(degrees, g * np.sin(theta), color="#d57919", lw=2.3,
            label=r"Frictionless: $a=g\sin\theta$")
    ax.plot(degrees, acceleration, color="#3274b5", lw=2.6,
            label=r"Already sliding downhill: $a=g(\sin\theta-\mu_k\cos\theta)$")
    ax.axhline(0, color="#667085", lw=1)
    ax.axvline(threshold, color="#48704a", ls="--", lw=1.6)
    ax.text(threshold+0.9, 6.4, r"$\theta_c=24.23^\circ$", fontsize=12,
            color="#48704a", va="top")
    for d, text_offset in [(20, (-55, -45)), (30, (35, -38))]:
        t = np.deg2rad(d)
        a = g * (np.sin(t) - mu_k * np.cos(t))
        ax.scatter([d], [a], s=45, color="#3274b5", zorder=5)
        ax.annotate(f"{d}°: a = {a:.3f} m/s²", xy=(d, a),
                    xytext=text_offset, textcoords="offset points", fontsize=11,
                    arrowprops={"arrowstyle": "-", "color": "#3274b5"},
                    bbox={"boxstyle": "round,pad=0.3", "fc": "white", "ec": "#c8d4df"})
    zero = np.rad2deg(np.arctan(mu_k))
    ax.scatter([zero], [0], s=30, color="#222222", zorder=5)
    ax.annotate("Constant downhill speed\nθ = 16.70°", xy=(zero, 0),
                xytext=(1.5, -2.55), fontsize=11,
                arrowprops={"arrowstyle": "-", "color": "#667085"})
    ax.set_xlim(0, 55)
    ax.set_ylim(-3.3, 8.5)
    ax.set_xlabel(r"Incline angle $\theta$ (degrees)", fontsize=12)
    ax.set_ylabel("Signed downhill acceleration (m/s²)", fontsize=12)
    ax.grid(alpha=0.22)
    ax.set_axisbelow(True)
    ax.set_title("Rest and sliding are different states on the same ramp", fontsize=16, pad=18)
    ax.legend(loc="upper left", fontsize=10, framealpha=1)
    fig.text(0.5, 0.025, "Stipulated model: g = 9.8 m/s², μs = 0.45, μk = 0.30. No measured data.",
             ha="center", fontsize=11, color="#475467")
    fig.subplots_adjust(left=0.11, right=0.97, top=0.87, bottom=0.15)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
