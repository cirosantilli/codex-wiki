"""Original electrostatic models; write this script's PNG basename to CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.8, 5.1), layout="constrained")
    fig.get_layout_engine().set(rect=(0, 0.04, 1, 0.90))
    fig.suptitle("Electric potential: field points toward lower potential", fontsize=16, y=0.99)
    ax.set_title("Point charge: spherical equipotentials in section", fontsize=12)
    k, source_charge = 8.99e9, 2e-9
    for radius, color in zip((0.10, 0.20, 0.30), ("#9333a2", "#5266ba", "#307f98")):
        ax.add_patch(Circle((0, 0), radius, fill=False, color=color, lw=1.8))
        ax.text(0.01, radius + 0.007, f"{k * source_charge / radius:.1f} V", color=color)
    ax.scatter([0], [0], s=160, c="#c73f3f", zorder=5)
    ax.text(-0.31, -0.33, r"$Q=+2\,\mathrm{nC}$; zero at infinity", fontsize=11)
    for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        start = 0.22 * np.array([np.cos(angle), np.sin(angle)])
        end = 0.285 * np.array([np.cos(angle), np.sin(angle)])
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": "#19763d", "lw": 1.8})
    ax.text(-0.34, -0.075, r"$\mathbf{E}$ outward", color="#19763d")
    ax.scatter([0.2], [0], c="#202020", s=30, zorder=6)
    ax.annotate(r"$q=-3\,\mathrm{nC}$", xy=(0.2, 0), xytext=(0.13, -0.12),
                arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.annotate("", xy=(0.12, 0), xytext=(0.2, 0),
                arrowprops={"arrowstyle": "->", "color": "#a95616", "lw": 2.3})
    ax.text(0.08, 0.04, "force inward", color="#a95616", fontsize=10)
    ax.set(xlim=(-0.36, 0.36), ylim=(-0.36, 0.36), xlabel="x (m)", ylabel="y (m)")
    ax.set_aspect("equal")

    bx.set_title("Uniform field: plane equipotentials in section", fontsize=12)
    for x in (0, 1, 2, 3, 4):
        bx.plot([x, x], [0.1, 2.8], color="#5266ba", lw=1.8)
        bx.text(x, 2.97, f"{12 - 3 * x:g} V", ha="center", color="#5266ba")
    for y in (0.5, 1.5, 2.5):
        bx.annotate("", xy=(3.9, y), xytext=(0.15, y),
                    arrowprops={"arrowstyle": "->", "color": "#19763d", "lw": 1.8})
    bx.text(2, 2.13, r"$\mathbf{E}=300\,\mathrm{V/m}\,\widehat{\mathbf{x}}$",
            color="#19763d", ha="center")
    bx.scatter([0, 4], [1.5, 1.5], c="#202020", zorder=5)
    bx.text(0.04, 1.22, "A", fontsize=12)
    bx.text(3.83, 1.22, "B", fontsize=12)
    bx.text(2, -0.54, r"A $\to$ B: $\Delta\Phi=-12\,\mathrm{V}$", ha="center")
    bx.text(2, -0.85, r"$q=+2\,\mathrm{nC}$: $\Delta U=-24\,\mathrm{nJ}$", ha="center")
    bx.text(2, -1.16, r"$q=-2\,\mathrm{nC}$: $\Delta U=+24\,\mathrm{nJ}$", ha="center")
    bx.set(xlim=(-0.45, 4.45), ylim=(-1.35, 3.3), xlabel="x (cm)")
    bx.set_yticks([])
    bx.spines[["left", "right", "top"]].set_visible(False)
    fig.text(0.5, 0.003, "Analytic model illustrations; arrows show direction, not measured data", ha="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
