"""Explain incline force balance and weight decomposition in separate panels.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is static-friction-incline-onset-geometry.png in CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon
import numpy as np


MU_STATIC = 0.4
THETA = np.arctan(MU_STATIC)
UPHILL = np.array([np.cos(THETA), np.sin(THETA)])
OUTWARD = np.array([-np.sin(THETA), np.cos(THETA)])


def arrow(ax, origin, vector, color, label, text_offset, linestyle="-", label_end=True):
    end = origin + vector
    ax.annotate("", end, origin,
                arrowprops={"arrowstyle": "-|>", "lw": 2.3, "color": color,
                            "linestyle": linestyle, "mutation_scale": 16})
    anchor = end if label_end else origin + 0.5 * vector
    ax.text(*(anchor + np.array(text_offset)), label, fontsize=12, color=color,
            ha="center", va="center")


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), dpi=120, facecolor="white")
    blue, green, orange = "#176797", "#278148", "#b25623"
    ax = axes[0]
    ax.set_title("Actual forces on the resting block", fontsize=13, pad=15)
    ax.plot([0, 5.2], [0, 5.2 * np.tan(THETA)], color="#687783", lw=2)
    ax.plot([0, 2], [0, 0], color="#99a3aa", lw=1)
    ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=0,
                     theta2=np.degrees(THETA), color="#394954"))
    ax.text(1.00, 0.18, r"$\theta$", fontsize=14)
    base = 2.55 * UPHILL
    w, h = 0.95, 0.7
    corners = np.array([base-w/2*UPHILL, base+w/2*UPHILL,
                        base+w/2*UPHILL+h*OUTWARD, base-w/2*UPHILL+h*OUTWARD])
    ax.add_patch(Polygon(corners, facecolor="#e3e9ed", edgecolor="#506471", lw=1.3))
    center = base + h/2 * OUTWARD
    scale = 1.85
    arrow(ax, center, scale*np.cos(THETA)*OUTWARD, blue, r"$N$", (-0.2, 0.22))
    arrow(ax, center, scale*np.sin(THETA)*UPHILL, green, r"$f_s$", (0.1, 0.32))
    arrow(ax, center, np.array([0., -scale]), orange, r"$mg$", (0.25, -0.15))
    arrow(ax, np.array([3.9, 0.7]), -0.8*UPHILL, "#5c6470", "", (0, 0))
    ax.text(3.85, 0.14, "Impending slip: downhill", fontsize=10, ha="center")
    ax.text(2.15, -1.00, r"$f_s=mg\sin\theta$,  $N=mg\cos\theta$", ha="center", fontsize=12)
    ax.set(xlim=(-0.25, 5.55), ylim=(-1.45, 3.9))

    ax = axes[1]
    ax.set_title("Decompose weight separately", fontsize=13, pad=15)
    origin = np.array([0., 0.])
    size = 2.8
    downhill = -size*np.sin(THETA)*UPHILL
    inward = -size*np.cos(THETA)*OUTWARD
    weight = np.array([0., -size])
    arrow(ax, origin, downhill, green, r"$mg\sin\theta$", (-0.3, -0.25))
    arrow(ax, downhill, inward, blue, r"$mg\cos\theta$", (-1.0, -0.08), label_end=False)
    arrow(ax, origin, weight, orange, r"$mg$", (-0.3, -0.15), linestyle="--")
    ax.plot([0, inward[0]], [0, inward[1]], color="#597b96", lw=1, ls=":")
    corner = downhill
    tick_size = 0.15
    tick = np.array([corner-tick_size*UPHILL,
                     corner-tick_size*UPHILL-tick_size*OUTWARD,
                     corner-tick_size*OUTWARD])
    ax.plot(tick[:, 0], tick[:, 1], color="#65727e", lw=1)
    ax.add_patch(Arc((0, 0), 1.1, 1.1, theta1=-90,
                     theta2=-90+np.degrees(THETA), color="#394954"))
    ax.text(0.14, -0.8, r"$\theta$", fontsize=14)
    ax.text(1.22, -1.0, "Inward normal", fontsize=10, ha="center", color="#597b96")
    ax.annotate("", (0.85*inward[0], 0.85*inward[1]), (1.2, -1.18),
                arrowprops={"arrowstyle": "-", "lw": 0.8, "color": "#597b96"})
    ax.text(0, -3.50, r"At onset: $\tan\theta_c=\mu_s=0.40$", fontsize=12, ha="center")
    ax.text(0, -3.90, r"$\theta_c\approx21.80^\circ$; a model angle, not a measurement", fontsize=10, ha="center")
    ax.set(xlim=(-2.15, 2.9), ylim=(-4.25, 1.1))
    for ax in axes:
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_facecolor("white")
    fig.suptitle("Incline geometry: demand reaches the static-friction bound", fontsize=15, y=0.98)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.88, wspace=0.12)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
