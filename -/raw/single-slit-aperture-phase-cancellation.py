"""Generate single-slit-aperture-phase-cancellation.png in CWD, opaque white.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Eight midpoint phasors demonstrate the broadside and first-minimum sums;
the continuous aperture integral defines the diffraction envelope.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, width=1.6):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": color, "lw": width,
                            "shrinkA": 0, "shrinkB": 0, "mutation_scale": 10})


def main():
    count = 8
    midpoints = -.5 + (np.arange(count) + .5) / count
    colors = plt.get_cmap("tab10")(np.arange(count))
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 3, figsize=(11.2, 6.4), dpi=110)
    fig.subplots_adjust(left=.06, right=.98, top=.79, bottom=.16, wspace=.38, hspace=.80)
    for row, total_phase in enumerate((0., 2 * np.pi)):
        phasors = np.exp(1j * total_phase * midpoints)
        resultant = phasors.mean()
        assert abs(resultant - (1 if row == 0 else 0)) < 1e-14
        aperture, direction, polygon = axes[row]
        aperture.plot([-.5, .5], [0, 0], color=".6", lw=5, alpha=.3)
        for edge in np.linspace(-.5, .5, count + 1):
            aperture.plot([edge, edge], [-.028, .028], color=".5", lw=.8)
        for j, (position, phasor, color) in enumerate(zip(midpoints, phasors, colors)):
            arrow(aperture, (position, 0),
                  (position + .075 * phasor.real, .075 * phasor.imag), color)
            aperture.text(position, -.105, str(j), ha="center", fontsize=9, color=color)
        aperture.set(xlim=(-.6, .6), ylim=(-.15, .13), xticks=[-.5, 0, .5],
                     yticks=[], xlabel=r"Aperture coordinate $x/a$")
        aperture.set_title("8 equal strips; midpoint samples", fontsize=10)
        aperture.spines[["left", "right", "top"]].set_visible(False)
        # The grey circle is the continuous phase range at the first minimum.
        if row == 1:
            phases = np.linspace(-np.pi, np.pi, 401)
            direction.plot(np.cos(phases), np.sin(phases), color=".72", lw=1.3)
        for phasor, color in zip(phasors, colors):
            arrow(direction, (0, 0), (phasor.real, phasor.imag), color)
        direction.axhline(0, color=".85", lw=.7)
        direction.axvline(0, color=".85", lw=.7)
        direction.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), aspect="equal",
                      xticks=[], yticks=[], xlabel="Real", ylabel="Imaginary")
        direction.set_title("All 8 directions coincide" if row == 0 else "Phases span one full turn", fontsize=10)
        direction.spines[:].set_visible(False)
        vertices = np.r_[0j, np.cumsum(phasors / count)]
        for j, color in enumerate(colors):
            arrow(polygon, (vertices[j].real, vertices[j].imag),
                  (vertices[j + 1].real, vertices[j + 1].imag), color, width=2)
        polygon.scatter([0], [0], color=".2", s=20, zorder=5)
        if row == 0:
            polygon.set(xlim=(-.05, 1.05), ylim=(-.15, .15), aspect="equal")
            polygon.text(.5, -.10, r"$A_8/A(0)=1$", ha="center")
        else:
            polygon.set(xlim=(-.23, .23), ylim=(-.43, .08), aspect="equal")
            polygon.text(0, -.40, r"$A_8/A(0)=0$", ha="center")
            polygon.annotate("Start = end", xy=(0, 0), xytext=(.12, .02),
                             fontsize=9, arrowprops={"arrowstyle": "->", "color": ".35"})
        polygon.set_title("Head-to-tail sum\nEach arrow has length 1/8", fontsize=10)
        polygon.axis("off")
    fig.suptitle("Aperture phase cancellation", fontsize=17, y=.975)
    fig.text(.5, .89, r"Broadside: $\theta=0$, all phases align", ha="center", fontsize=12)
    fig.text(.5, .47, r"First minimum: $a\sin\theta=\lambda$, paired strips differ by $\pi$", ha="center", fontsize=12)
    fig.text(.5, .073, r"$x_j/a=-1/2+(j+1/2)/8$, $j=0,\ldots,7$; finite midpoint sum cancels exactly at the first minimum.",
             ha="center", fontsize=10)
    fig.text(.5, .032, "The continuous slit uses an integral. The circle is its phase range; coloured arrows are 8 samples.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
