"""Plot a stipulated F=1 to F'=0 optical-pumping population model.

Run from _media; output is the generator's basename with a .png suffix.
Python 3.14, matplotlib 3.10.7, numpy 2.3.5. This is not a sodium or
rubidium spectrum. Equal spontaneous branching follows rotational symmetry
of the scalar upper level; only m=-1 absorbs the chosen sigma-plus beam.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


def populations(time, pump, relaxation):
    """Unpolarized initial condition; short-lived upper level eliminated."""
    rate = relaxation + 2 * pump / 3
    bright_star = relaxation / (3 * relaxation + 2 * pump)
    bright = bright_star + (1 / 3 - bright_star) * np.exp(-rate * time)
    dark = (1 - bright) / 2
    return np.array([bright, dark, dark])


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(12, 7), dpi=120, facecolor="white")
    gs = fig.add_gridspec(2, 2, width_ratios=(1.05, 1.2), height_ratios=(1, 0.8),
                          left=0.065, right=0.975, top=0.85, bottom=0.12,
                          wspace=0.32, hspace=0.39)
    level = fig.add_subplot(gs[:, 0])
    pop = fig.add_subplot(gs[0, 1])
    signal = fig.add_subplot(gs[1, 1])
    blue, purple, green = "#1768ac", "#9253a1", "#16734a"
    fig.suptitle("Selective absorption can empty one sublevel into two dark states",
                 fontsize=18, weight="bold", y=0.965)
    fig.text(0.5, 0.905, r"Hypothetical isolated $F=1\to F'=0$ system · all curves start unpolarized",
             ha="center", fontsize=12, color="#505050")

    level.set(xlim=(-0.55, 2.55), ylim=(-0.5, 3.7))
    level.axis("off")
    level.plot([0.76, 1.24], [2.85, 2.85], color="#222222", linewidth=3)
    level.text(1, 3.11, r"$F'=0,\ m'=0$", ha="center", fontsize=14)
    for x, m in enumerate([-1, 0, 1]):
        level.plot([x - 0.23, x + 0.23], [0.45, 0.45], color="#222222", linewidth=3)
        level.text(x, 0.12, rf"$m={m:+d}$" if m else r"$m=0$", ha="center")
        level.text(x, -0.15, "bright" if x == 0 else "dark", ha="center",
                   color=blue if x == 0 else green, weight="bold")
        # A return to the bright level scatters a photon without changing m.
        level.add_patch(FancyArrowPatch((1 + (x - 1) * 0.10, 2.75), (x, 0.53),
                                         arrowstyle="-|>", mutation_scale=16,
                                         linewidth=2, linestyle="--", color=purple))
    level.add_patch(FancyArrowPatch((-0.10, 0.55), (0.78, 2.78),
                                     connectionstyle="arc3,rad=-0.25",
                                     arrowstyle="-|>", mutation_scale=18,
                                     linewidth=2.6, color=blue))
    level.text(-0.40, 1.92, "$\\sigma^+$\nabsorption\nrate $R$", color=blue, fontsize=12)
    level.text(1.94, 2.18, "Spontaneous\nreturn: 1/3\nto each level", color=purple,
               ha="center", fontsize=12)
    level.text(1, 0.89, r"$F=1$", ha="center", fontsize=14,
               bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    level.text(1, 3.60, "Absorption and spontaneous branching", ha="center", weight="bold")
    level.text(1, -0.46, "Relaxation resets all three populations toward 1/3.",
               ha="center", fontsize=11, color="#505050")

    time = np.linspace(0, 1.7, 450)
    pump, relaxation = 6.0, 1.0
    finite = populations(time, pump, relaxation)
    pure = populations(time, pump, 0)
    assert np.all(finite >= 0) and np.all(pure >= 0)
    assert np.allclose(finite.sum(axis=0), 1)
    assert np.allclose(pure.sum(axis=0), 1)
    pop.plot(time, finite[0], color=blue, linewidth=2.5, label=r"$p_-$: bright")
    pop.plot(time, finite[1], color=green, linewidth=2.5, label=r"$p_0=p_+$: each dark")
    pop.plot(time, pure[0], color=blue, linestyle="--", linewidth=1.7)
    pop.plot(time, pure[1], color=green, linestyle="--", linewidth=1.7)
    pop.axhline(1 / 15, color=blue, alpha=0.3, linewidth=1)
    pop.axhline(7 / 15, color=green, alpha=0.3, linewidth=1)
    pop.set(ylim=(-0.005, 0.55), ylabel="Population fraction", xlim=(0, 1.7))
    pop.set_title(r"Solid: $R=6\ \mathrm{s}^{-1},\ \gamma=1\ \mathrm{s}^{-1}$", fontsize=12)
    pop.legend(loc="center right", frameon=False, fontsize=11)
    pop.tick_params(labelbottom=False)
    pop.grid(alpha=0.17)

    signal.plot(time, pump * finite[0], color=purple, linewidth=2.5)
    signal.plot(time, pump * pure[0], color=purple, linestyle="--", linewidth=1.7)
    signal.axhline(0.4, color=purple, alpha=0.3)
    signal.text(1.65, 0.51, r"$Rp_-^*=0.40\ \mathrm{s}^{-1}$", ha="right", color=purple)
    signal.set(xlabel="Time (s)", ylabel=r"Scattering per atom ($\mathrm{s}^{-1}$)",
               xlim=(0, 1.7), ylim=(-0.02, 2.13))
    signal.grid(alpha=0.17)
    fig.text(0.52, 0.035, r"Dashed: same $R$, no relaxation ($\gamma=0$).   Parameters are chosen, not measured.",
             ha="center", fontsize=11, color="#505050")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
