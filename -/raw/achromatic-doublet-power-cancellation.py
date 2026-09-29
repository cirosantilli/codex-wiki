"""Generate achromatic-doublet-power-cancellation.png in the working directory.

Run from _media with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Original signed-power diagram. Phi_i(q) = Phi_i,d * (1 + q/V_i).
The exactly flat sum belongs only to this first-order synthetic model.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = np.linspace(-.5, .5, 201)
    crown = 10 * (1 + q / 60)
    flint = -5 * (1 + q / 30)
    total = crown + flint
    assert np.allclose(total, 5, atol=2e-15, rtol=0)
    assert np.allclose(crown[[0, -1]], [119 / 12, 121 / 12])
    assert np.allclose(flint[[0, -1]], [-59 / 12, -61 / 12])
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (power, change) = plt.subplots(1, 2, figsize=(10.8, 5.4), dpi=110)
    fig.subplots_adjust(left=.075, right=.975, bottom=.33, top=.77, wspace=.30)
    green, purple, black = "#277b50", "#8e4395", "#222222"
    curves = [(crown, crown - 10, green, "-", "Crown: +10 D, V = 60"),
              (flint, flint + 5, purple, "--", "Flint: −5 D, V = 30"),
              (total, total - 5, black, "-.", "Sum: +5 D")]
    for values, shifts, colour, style, label in curves:
        power.plot(q, values, color=colour, linestyle=style, lw=2.5, label=label)
        change.plot(q, shifts, color=colour, linestyle=style, lw=2.5)
    for axis in (power, change):
        axis.set_xlim(-.53, .53)
        axis.set_xticks([-.5, 0, .5], ["−0.5\nRed", "0\nReference", "+0.5\nBlue"])
        axis.set_xlabel("Synthetic colour coordinate q", labelpad=8)
        axis.grid(alpha=.18)
        axis.axvline(0, color="0.65", lw=.8, linestyle=":")
    power.axhline(0, color="0.6", lw=.8)
    power.set(ylim=(-6.3, 11.5), yticks=[-5, 0, 5, 10],
              ylabel="Signed optical power (D)", title="Element powers add to +5 D")
    power.text(0, 10.6, "Positive element", ha="center", color=green, fontsize=10)
    power.text(0, 5.6, "Flat only in this first-order model", ha="center", fontsize=10)
    power.text(0, -4.4, "Negative element", ha="center", color=purple, fontsize=10)
    change.set(ylim=(-.116, .116), yticks=[-.1, -.05, 0, .05, .1],
               ylabel="Change from reference power (D)",
               title="Magnified: opposite colour changes")
    change.text(-.47, .077, r"Flint slope: $-1/6$ D per q", color=purple, fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    change.text(-.47, -.105, r"Crown slope: $+1/6$ D per q", color=green, fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    change.annotate("Sum change = 0", xy=(.36, 0), xytext=(.03, .029),
                    arrowprops={"arrowstyle": "->", "color": black}, fontsize=10,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    fig.suptitle("Achromatic doublet: cancel colour change, retain focusing power",
                 fontsize=15, y=.965)
    fig.text(.5, .867, r"$\Phi_c(q)=10(1+q/60)$ D,  $\Phi_f(q)=-5(1+q/30)$ D;  $10/60-5/30=0$", ha="center", fontsize=12)
    handles, labels = power.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(.5, .10),
               ncol=3, frameon=False, fontsize=10)
    fig.text(.5, .073, "Toy dispersion, not measured glass. Thin elements in contact in air; total focal length = 0.2 m.",
             ha="center", fontsize=10)
    fig.text(.5, .027, "Real achromats correct two selected wavelengths and can retain secondary spectrum.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
