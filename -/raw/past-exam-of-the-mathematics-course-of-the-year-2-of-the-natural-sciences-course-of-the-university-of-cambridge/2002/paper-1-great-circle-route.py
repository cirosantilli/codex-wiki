"""Original great-circle route plot; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Uses the rounded exam coordinates, not modern city coordinates.
Run from the desired output directory; the PNG is written in the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    phi_a, phi_b = np.deg2rad([15, 105])
    a = np.array([np.cos(phi_a), np.sin(phi_a), 1.0])/np.sqrt(2)
    b = np.array([np.cos(phi_b), np.sin(phi_b), 0.0])
    s = np.linspace(0, np.pi/2, 500)
    points = np.cos(s)[:, None]*a + np.sin(s)[:, None]*b
    lon = np.rad2deg(np.arctan2(points[:, 1], points[:, 0]))
    lat = np.rad2deg(np.arcsin(points[:, 2]))
    fig, ax = plt.subplots(figsize=(7.7, 4.4), dpi=120, layout="constrained")
    ax.plot(lon, lat, color="#1674a5", lw=2.4, label=r"$\ell=\arctan[\cos(\phi-15^\circ)]$")
    tick_s = np.linspace(0, np.pi/2, 7)
    ticks = np.cos(tick_s)[:, None]*a + np.sin(tick_s)[:, None]*b
    tick_lon = np.rad2deg(np.arctan2(ticks[:, 1], ticks[:, 0]))
    tick_lat = np.rad2deg(np.arcsin(ticks[:, 2]))
    ax.scatter(tick_lon, tick_lat, s=22, color="#1674a5", zorder=3)
    ax.scatter([15, 105], [45, 0], color="#b35428", s=45, zorder=4)
    ax.annotate("Rome (exam coordinates)", (15, 45), (21, 48), fontsize=10)
    ax.annotate("Singapore\n(exam coordinates)", (105, 0), (73, 9), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "0.3"})
    ax.axhline(0, color="0.5", lw=0.8)
    ax.set(xlim=(10, 110), ylim=(-3, 54), xlabel="Longitude east (degrees)",
           ylabel="Latitude north (degrees)", title="A 90-degree great-circle arc")
    ax.set_xticks(np.arange(15, 106, 15))
    ax.set_yticks(np.arange(0, 46, 15))
    ax.grid(alpha=0.2)
    ax.legend(loc="lower left", fontsize=10)
    ax.text(0.98, 0.95, "Dots are 15 degrees apart\nin spherical distance", ha="right", va="top",
            transform=ax.transAxes, fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
