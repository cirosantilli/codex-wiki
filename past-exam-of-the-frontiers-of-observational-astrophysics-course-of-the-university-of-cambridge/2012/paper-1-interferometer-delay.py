"""Original geometry and electronic signal paths for tracking a sky direction."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(8, 4.8), layout="constrained")
    theta = np.deg2rad(28)
    for x in [-3, 3]:
        ax.plot([x-.45, x, x+.45], [.22, 0, .22], color="0.2", lw=2)
        ax.plot([x, x], [0, -.42], color="0.2", lw=2)
        start = np.array([x, .5])+3*np.array([np.sin(theta), np.cos(theta)])
        ax.annotate("", (x, .5), start, arrowprops={"arrowstyle": "->", "color": "tab:blue", "lw": 2})
        ax.text(x, -.72, "Antenna 1" if x < 0 else "Antenna 2\n(earlier arrival)", ha="center", va="top", fontsize=10)
    x = np.linspace(-3.3, 4.8, 2)
    ax.plot(x, 2.6-np.tan(theta)*x, ls="--", color="tab:blue", alpha=.6)
    ax.text(-3.7, 3.1, "Tracked plane wave", color="tab:blue", fontsize=10)
    ax.plot([1.1, 1.1], [2.3, 4.4], color="0.55", ls=":")
    ax.plot([1.1, 2.2], [2.3, 2.3+1.1/np.tan(theta)], color="tab:blue")
    ax.add_patch(Arc((1.1, 2.3), 1.5, 1.5, theta1=62, theta2=90, color="0.3"))
    ax.text(1.32, 3.25, r"$\theta$", fontsize=12)
    ax.annotate("", (-3, -.48), (3, -.48), arrowprops={"arrowstyle": "<->", "color": "0.4"})
    ax.text(0, -.45, r"Baseline $b$", ha="center", va="bottom", bbox={"facecolor": "white", "edgecolor": "none"})
    ax.plot([-3, -3, -.85], [-1.15, -2.4, -2.4], color="tab:orange", lw=2)
    ax.plot([3, 3, .85], [-1.15, -2.4, -2.4], color="tab:orange", lw=2)
    ax.add_patch(Rectangle((1.0, -2.78), 2.35, .7, facecolor="#fff0d6", edgecolor="0.3", zorder=3))
    ax.text(2.175, -2.43, r"Delay $b\sin\theta/c$", ha="center", va="center", zorder=4, fontsize=10)
    ax.add_patch(Rectangle((-.85, -2.8), 1.7, .8, facecolor="#dcecf4", edgecolor="0.3", zorder=3))
    ax.text(0, -2.4, "Correlator", ha="center", va="center", zorder=4)
    ax.text(0, -3.2, "Equal cable paths apart from the inserted tracking delay", ha="center", fontsize=10)
    ax.set(xlim=(-4.2, 5.1), ylim=(-3.55, 4.8),
           title="Geometric lead compensated by an electronic delay")
    ax.axis("off")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
