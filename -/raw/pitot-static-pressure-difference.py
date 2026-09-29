"""Original Pitot connection schematic and ideal pressure budget, not data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes only the matching opaque white PNG basename to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    rho, speed, reference_pressure = 1.20, 20.0, 101325.0
    q = rho * speed**2 / 2
    assert q == 240.0
    assert np.isclose(np.sqrt(2 * q / rho), speed)
    fig, (ax, budget) = plt.subplots(1, 2, figsize=(11.2, 5.2), dpi=110,
                                   gridspec_kw={"width_ratios": [1.55, 1]})
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-1, 7.0), ylim=(-2.4, 2.5), aspect="equal")
    ax.axis("off")
    ax.set_title("Separate passages, one pressure difference", pad=14)
    ax.add_patch(FancyBboxPatch((1.2, -.32), 3.65, .64,
                               boxstyle="round,pad=0,rounding_size=0.25",
                               facecolor="#f1f4f7", edgecolor="#39434e", lw=2))
    # The central opening and side ports are separate pressure cavities.
    ax.add_patch(Rectangle((1.14, -.09), .24, .18, facecolor="white",
                           edgecolor="#2374ab", lw=2, zorder=4))
    ax.plot([1.28, 5.3, 5.3, 4.8], [0, 0, -1.3, -1.3],
            color="#2374ab", lw=2.6)
    ax.plot([3.6, 3.6, 5.8, 5.8, 4.8], [.32, .18, .18, -1.85, -1.85],
            color="#d07c20", lw=2.6)
    ax.plot([3.6, 3.6], [-.32, .18], color="#d07c20", lw=2.6)
    ax.scatter([3.6, 3.6], [-.32, .32], s=45, color="#d07c20", zorder=5)
    for y in [-.85, 0, .85]:
        ax.annotate("", xy=(.75, y), xytext=(-.8, y),
                    arrowprops={"arrowstyle": "->", "color": "#555", "lw": 1.7})
    ax.text(-.82, 1.28, r"Incoming flow $U_\infty$", fontsize=11)
    ax.annotate(r"Facing port: $p_{0\infty}$", xy=(1.24, .05), xytext=(.7, 1.95),
                arrowprops={"arrowstyle": "->", "color": "#2374ab"}, color="#2374ab")
    ax.annotate(r"Side ports: $p_\infty$", xy=(3.6, .32), xytext=(3.4, 1.25),
                arrowprops={"arrowstyle": "->", "color": "#d07c20"}, color="#a76112")
    ax.add_patch(FancyBboxPatch((1.5, -2.15), 3.25, 1.1,
                               boxstyle="round,pad=0.08", facecolor="white",
                               edgecolor="#39434e", lw=1.5, zorder=6))
    ax.text(3.12, -1.55, "Differential manometer\nIdeal readout: +240 Pa",
            ha="center", va="center", zorder=7)
    ax.text(4.84, -1.32, "+", color="#2374ab", va="center", fontsize=16)
    ax.text(4.84, -1.86, "−", color="#a76112", va="center", fontsize=16)

    # A local stopping process, not a synthetic spatial streamline profile.
    positions = np.arange(2)
    static_departure = np.array([0.0, q])
    kinetic_density = np.array([q, 0.0])
    assert np.allclose(static_departure + kinetic_density, q)
    budget.bar(positions, static_departure, width=.58, color="#d07c20",
               label=r"Static departure $p-p_\infty$")
    budget.bar(positions, kinetic_density, bottom=static_departure, width=.58,
               color="#2374ab", label=r"Kinetic density $\rho U^2/2$")
    budget.set(xticks=positions, xticklabels=["Reference flow", "Stopped flow"],
               ylabel=r"Energy density / pressure relative to $p_\infty$ (Pa)",
               ylim=(0, 310))
    budget.set_title("Ideal stopping at the same height", pad=14)
    budget.axhline(q, color="#444", lw=1, ls="--")
    for x in positions:
        budget.text(x, 120, "240 Pa", ha="center", va="center", color="white")
    budget.text(.5, 272, r"$p_0 = p_\infty + q_\infty$", ha="center")
    budget.legend(loc="upper center", bbox_to_anchor=(.5, -.15), frameon=False,
                  fontsize=10)
    budget.spines[["top", "right"]].set_visible(False)
    fig.text(.5, .02, "Stipulated: ρ = 1.20 kg/m³, U∞ = 20 m/s, p∞ = 101325 Pa absolute.  Ideal model; not measured data.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.025, right=.98, top=.88, bottom=.29, wspace=.29)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
