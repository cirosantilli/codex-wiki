"""Original slit propagation geometry; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes fresnel-slit-phase-geometry.png in the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    fig, (ax, phase) = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=100,
                                   gridspec_kw={"width_ratios": [1.35, 1]})
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_xlim(-3.3, 6.3)
    ax.set_ylim(-2.6, 2.7)
    ax.axis("off")
    ax.set_title("Source, slit and observation plane", fontsize=13, pad=15)
    ax.add_patch(Rectangle((-3.1, -.32), 1.35, .64, facecolor="#e8edf3",
                           edgecolor="#34445a"))
    ax.text(-2.425, 0, "Collimated\nsource", ha="center", va="center", fontsize=10)
    for y in [-.9, 0, .9]:
        ax.annotate("", xy=(-.15, y), xytext=(-1.6, y),
                    arrowprops={"arrowstyle": "->", "color": "#326ea8"})
    for x in [-1.25, -.7]:
        ax.plot([x, x], [-1.3, 1.3], color="#326ea8", alpha=.5)
    ax.text(-1.2, 1.7, "Plane incident wave", ha="center", fontsize=11)
    ax.plot([0, 0], [-2.0, -.65], color="#34445a", lw=7)
    ax.plot([0, 0], [.65, 2.0], color="#34445a", lw=7)
    ax.plot([5, 5], [-2, 2], color="#34445a", lw=3)
    ax.text(0, 2.2, r"Slit: $\xi$", ha="center", fontsize=11)
    ax.text(5, 2.2, "Screen", ha="center", fontsize=11)
    ax.plot([-.15, 5.8], [0, 0], color="#8c96a2", ls="--", lw=1)
    ax.text(5.9, -.15, r"$z$", fontsize=12)
    ax.scatter([0, 5], [.42, 1.15], color="#ce6426", zorder=5)
    ax.plot([0, 5], [.42, 1.15], color="#ce6426", lw=2)
    ax.text(2.25, 1.0, r"$r=\sqrt{z^2+(x-\xi)^2}$", fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.add_patch(FancyArrowPatch((5.45, 0), (5.45, 1.15), arrowstyle="<->",
                                 mutation_scale=11, color="#ce6426"))
    ax.text(5.62, .55, r"$x$", fontsize=12)
    ax.add_patch(FancyArrowPatch((.35, -.65), (.35, .65), arrowstyle="<->",
                                 mutation_scale=11, color="#34445a"))
    ax.text(.5, -.45, r"$D=2a$", fontsize=11)
    ax.add_patch(FancyArrowPatch((0, -2.2), (5, -2.2), arrowstyle="<->",
                                 mutation_scale=11, color="#34445a"))
    ax.text(2.5, -2.52, "Propagation distance z (drawing not to scale)",
            ha="center", fontsize=10)
    t = np.linspace(-.5, .5, 501)
    D, wavelength = .4e-3, 633e-9
    for z, color in [(.02, "#326ea8"), (2.0, "#ce6426")]:
        number = D**2 / (wavelength * z)
        phase.plot(t, np.pi * number * t**2, lw=2.2, color=color,
                   label=f"z = {z:g} m; edge = {np.pi * number / 4:.3f} rad")
    phase.set_title("Phase curvature across the slit", fontsize=13, pad=15)
    phase.set_xlabel(r"Aperture coordinate $\xi/D$")
    phase.set_ylabel(r"Quadratic phase $\pi\xi^2/(\lambda z)$ (rad)")
    phase.set_xlim(-.5, .5)
    phase.set_ylim(0, 10.6)
    phase.grid(alpha=.2)
    phase.legend(loc="upper center", fontsize=9, frameon=False)
    phase.text(.5, .45, r"$\lambda=633$ nm; $D=0.400$ mm" + "\n"
               + r"Edge phase = $\pi N_D/4$", transform=phase.transAxes,
               ha="center", va="center", fontsize=11)
    fig.subplots_adjust(left=.025, right=.98, bottom=.14, top=.85, wspace=.27)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
