"""Original Higgs-field teaching diagram; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching opaque PNG in the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, potential) = plt.subplots(1, 2, figsize=(10.8, 5.1), facecolor="white")
    fig.suptitle("One physical radial mode; three angular directions supply vector polarizations", fontsize=14)
    theta = np.linspace(0, 2 * np.pi, 500)
    ax.plot(np.cos(theta), np.sin(theta), color="#247ba0", lw=2)
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8)
    ax.scatter([1], [0], color="black", zorder=5)
    ax.annotate("chosen vacuum", (1, 0), (0.15, -0.5), arrowprops={"arrowstyle": "->"})
    ax.annotate("", (1.55, 0), (1, 0), arrowprops={"arrowstyle": "->", "color": "#be3a34", "lw": 2.5})
    ax.text(1.1, -0.22, r"radial $H$", color="#be3a34")
    ax.annotate("", (1, 0.65), (1, 0), arrowprops={"arrowstyle": "->", "color": "#247ba0", "lw": 2.5})
    ax.text(0.18, 0.8, "angular tangent", color="#247ba0")
    ax.set(xlim=(-1.5, 1.8), ylim=(-1.35, 1.4), aspect="equal", xlabel="real field coordinate / v", ylabel="another real field coordinate / v")
    ax.set_title("Two-coordinate slice of the four real components", fontsize=11)
    ax.text(-1.4, -1.28, "Circle shows one angular direction; full vacuum orbit is 3D.", fontsize=9)
    r = np.linspace(0, 1.75, 600)
    potential.plot(r, 0.25 * (r * r - 1) ** 2, color="#be3a34", lw=2.5)
    potential.scatter([1], [0], color="black", zorder=5)
    potential.annotate(r"curvature $m_H^2=2\lambda v^2$", (1.13, 0.02), (0.25, 0.65), arrowprops={"arrowstyle": "->"})
    potential.set(xlim=(0, 1.75), ylim=(-0.035, 1.12), xlabel=r"radial magnitude $r/v$", ylabel=r"$(V-V_{\min})/(\lambda v^4)$")
    potential.set_title(r"$V=-\mu_h^2 r^2/2+\lambda r^4/4$,  $v^2=\mu_h^2/\lambda$", fontsize=11)
    potential.text(0.08, 0.91, "Gauge directions keep r fixed.\nRadial motion changes the potential.", fontsize=10)
    fig.text(0.5, 0.11, "Same 12 propagating degrees of freedom in the electroweak sector", ha="center", weight="bold")
    fig.text(0.5, 0.058, "4 massless vectors × 2 + 4 real scalars  →  3 massive vectors × 3 + photon × 2 + H × 1", ha="center", fontsize=11)
    fig.subplots_adjust(top=0.82, bottom=0.25, left=0.07, right=0.97, wspace=0.35)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
