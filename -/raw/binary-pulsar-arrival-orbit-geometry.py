"""Original geometric and functional timing diagram; Python 3.14, NumPy, Matplotlib.

Run from _media to write the matching opaque PNG. Chosen edge-on orbit,
not a reconstruction of PSR B1913+16 or historical observing hardware.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 6.3), facecolor="white")
    ax = fig.add_axes([0.07, 0.32, 0.42, 0.57])
    e, omega = 0.6, np.deg2rad(40)
    E = np.linspace(0, 2 * np.pi, 601)
    X, Y = np.cos(E) - e, np.sqrt(1 - e * e) * np.sin(E)
    sky = np.cos(omega) * X - np.sin(omega) * Y
    away = np.sin(omega) * X + np.cos(omega) * Y
    ax.plot(sky, away, color="#246799", lw=2)
    k = 125
    ax.scatter([0], [0], marker="+", s=100, color="black", zorder=4)
    ax.annotate("binary barycentre", (0, 0), (0.18, 0.10))
    ax.scatter(sky[k], away[k], s=100, color="#d36816", zorder=5)
    ax.annotate("pulsar", (sky[k], away[k]), (sky[k] - 0.47, away[k] + 0.13))
    ax.axhline(0, color="0.6", ls=":", lw=1)
    ax.plot([sky[k], sky[k]], [0, away[k]], color="#d36816", lw=3)
    ax.text(sky[k] - 0.08, away[k] / 2, r"$z_1=c\Delta_R$", ha="right", color="#a24c08")
    for x in (sky[k], 0.85):
        z = away[k] if x == sky[k] else 0
        ax.annotate("", (x, -1.82), (x, z - 0.08),
                    arrowprops={"arrowstyle": "->", "color": "#698d65", "lw": 1.6})
    ax.text(0.76, -1.96, "to distant observer", ha="center", color="#42673f")
    ax.set(xlim=(-1.8, 1.25), ylim=(-2.12, 1.05),
           xlabel=r"sky coordinate / $a_1$", ylabel=r"distance away from observer / $a_1$")
    ax.set_aspect("equal")
    ax.set_title("Chosen edge-on orbit", fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)

    profile = fig.add_axes([0.57, 0.67, 0.38, 0.17])
    t = np.linspace(0, 1, 600)
    pulse = sum(np.exp(-0.5 * ((t - c) / 0.018)**2) for c in (0.17, 0.50, 0.83))
    profile.plot(t, pulse, color="#246799", lw=1.8)
    profile.set(xticks=[], yticks=[], xlabel="arrival time (schematic)", ylabel="signal")
    profile.set_title("A receiver records repeated pulses", fontsize=12)
    profile.spines[["top", "right"]].set_visible(False)
    fig.text(0.59, 0.53, r"$t_n^{\rm arr}\simeq t_0+nP_s+\Delta_R(t_n)$", fontsize=14)
    fig.text(0.59, 0.39, "Extra path length changes arrival time.\n"
             "Its rate changes apparent pulse spacing:\n"
             r"$P_{\rm app}/P_s-1\simeq d\Delta_R/dt=v_\parallel/c$", linespacing=1.6)

    flow = fig.add_axes([0.02, 0.025, 0.96, 0.20])
    flow.set(xlim=(0, 1), ylim=(0, 1)); flow.axis("off")
    labels = ["Channels +\npulse template", "Dispersion +\nclock correction",
              "Solar-system\nbarycentric timing", "Orbit + spin fit\n→ timing residuals"]
    for j, label in enumerate(labels):
        x = 0.01 + j * 0.25
        flow.add_patch(FancyBboxPatch((x, 0.26), 0.225, 0.48,
                       boxstyle="round,pad=0.008", facecolor="#f2f6fa", edgecolor="#607c91"))
        flow.text(x + 0.1125, 0.5, label, ha="center", va="center", fontsize=10.5)
        if j < 3:
            flow.annotate("", (x + 0.248, 0.5), (x + 0.228, 0.5),
                          arrowprops={"arrowstyle": "->", "lw": 1.5})
    fig.suptitle("A binary orbit writes a delay onto a pulse clock", fontsize=15, y=0.98)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
