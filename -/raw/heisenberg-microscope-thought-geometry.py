"""An original conceptual microscope geometry, not an experimental record.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Ellipse, Polygon
import numpy as np


def main():
    fig, (ax, text) = plt.subplots(1, 2, figsize=(10, 4.9),
                                  gridspec_kw={"width_ratios": [1.2, 1]},
                                  layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-3.6, 3.1), ylim=(-1.35, 4.5))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Polygon([(0, 0), (-1.6, 3), (1.6, 3)],
                         facecolor="#fff0db", edgecolor="none"))
    ax.plot([0, 0], [0, 4.1], color="0.6", ls=":", lw=1)
    ax.add_patch(Ellipse((0, 3), 3.3, 0.28, facecolor="#dceaf6",
                         edgecolor="#2166ac", lw=1.8))
    ax.text(0, 3.38, "Imagined microscope objective", ha="center", fontsize=10)
    for target in [(-1.6, 3), (1.6, 3)]:
        ax.annotate("", xy=target, xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": "#bd4c22", "lw": 1.8})
    ax.annotate("", xy=(0, 2.95), xytext=(0, 0.05),
                arrowprops={"arrowstyle": "->", "color": "#bd4c22", "lw": 1.8})
    ax.text(1.35, 1.4, "Possible outgoing\nphoton directions", fontsize=10)
    ax.add_patch(Arc((0, 0), 1.5, 1.5, theta1=62, theta2=90,
                     color="#333333", lw=1.2))
    ax.text(0.19, 0.88, r"$\alpha$", fontsize=13)
    incident = np.linspace(-3.4, -0.2, 250)
    ax.plot(incident, 0.11*np.sin(12*incident), color="#238b45", lw=1.8)
    ax.annotate("", xy=(-0.16, 0), xytext=(-0.7, 0),
                arrowprops={"arrowstyle": "->", "color": "#238b45"})
    ax.text(-3.3, 0.38, "Incident photon", color="#17642e", fontsize=10)
    ax.plot(0, 0, "o", ms=10, color="#2166ac")
    ax.text(-0.13, -0.42, "Electron", ha="center", fontsize=10)
    ax.annotate("", xy=(2.5, -0.9), xytext=(0.8, -0.9),
                arrowprops={"arrowstyle": "->", "color": "0.2"})
    ax.text(1.65, -0.69, r"transverse $x$", ha="center", fontsize=10)
    ax.text(0, 4, "Collected scattered light", ha="center", fontsize=10)
    text.axis("off")
    paragraphs = [
        (0.91, "THOUGHT EXPERIMENT", 13, "#943b1b"),
        (0.78, "Larger collection half-angle α:", 11, "black"),
        (0.66, "• Finer diffraction resolution", 11, "black"),
        (0.56, r"$\delta x\sim\lambda/\sin\alpha$", 16, "#2166ac"),
        (0.40, "• Wider transverse recoil range", 11, "black"),
        (0.29, r"$\delta p_x\sim(h/\lambda)\sin\alpha$", 16, "#bd4c22"),
        (0.13, r"Product scale: $\delta x\,\delta p_x\sim h$", 13, "black"),
        (0.01, "Heuristic scales; no measured data or sharp variance constant", 9, "0.3"),
    ]
    for y, label, size, color in paragraphs:
        text.text(0, y, label, fontsize=size, color=color, transform=text.transAxes)
    fig.suptitle("Heisenberg’s microscope: resolution and recoil in an imagined geometry",
                 fontsize=13)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
