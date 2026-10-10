"""Original spinless hydrogen Stark model; emit PNG in the working directory.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. No measured spectrum is used.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (levels, lines) = plt.subplots(1, 2, figsize=(10, 4.7),
                                       gridspec_kw={"width_ratios": [1.08, 1]})
    field = np.linspace(0, 1, 101)
    blue, red, gray = "#17669c", "#aa4033", "#475569"
    levels.plot(field, 3 * field, color=red, lw=2.6)
    levels.plot(field, -3 * field, color=blue, lw=2.6)
    levels.plot(field, 0 * field, color=gray, lw=2.6)
    levels.scatter([0], [0], color="black", zorder=5)
    levels.text(.31, 2.45, r"$(2s-2p_0)/\sqrt{2}$", color=red)
    levels.text(.31, -2.75, r"$(2s+2p_0)/\sqrt{2}$", color=blue)
    levels.text(.21, .22, r"$2p_{+1},\ 2p_{-1}$ (two states)", color=gray)
    levels.set(xlim=(-.025, 1.03), ylim=(-3.7, 3.7),
               xlabel=r"Applied field $\mathcal{E}/\mathcal{E}_*$",
               ylabel=r"Level shift $\Delta E/(e a_0\mathcal{E}_*)$",
               title=r"$n=2$: diagonalize the degenerate block")
    levels.grid(alpha=.15)
    # Positions alone: finite field, neglect the ground-state quadratic shift.
    # Equal heights deliberately do not encode populations or line strengths.
    for pos, color, label in [(-3, blue, r"$\pi$"), (0, gray, r"$\sigma^+,\sigma^-$"),
                              (3, red, r"$\pi$")]:
        lines.vlines(pos, 0, 1, color=color, lw=3)
        lines.text(pos, 1.08, label, ha="center", color=color, fontsize=13)
    lines.set(xlim=(-4.4, 4.4), ylim=(-.05, 1.55), xticks=[-3, 0, 3], yticks=[],
              xlabel=r"Frequency offset $h(\nu-\nu_0)/(e a_0\mathcal{E})$",
              title=r"Model $n=2\to 1s$ line positions")
    lines.text(0, 1.36, r"$\pi$: dipole along field; $\sigma$: transverse dipole",
               ha="center", fontsize=10)
    lines.spines[["top", "right", "left"]].set_visible(False)
    levels.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Linear Stark effect: a Coulomb-model prediction", fontsize=15)
    fig.text(.5, .025, "Spin, fine structure and Lamb shift omitted. "
             "Arbitrary field scale; this is not Stark's measured Balmer spectrum.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .07, 1, .93), w_pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
