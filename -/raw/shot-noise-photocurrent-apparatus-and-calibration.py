"""Original functional shot-noise apparatus diagram; emit basename.png in CWD.

Python 3.14, matplotlib 3.10.7. Measurement roles follow MIT Department of
Physics, Johnson Noise and Shot Noise (revision 2013), Figs. 1, 6–7, section V.
This is an explanatory arrangement, not a wiring diagram or acquired data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=120, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 6.2))
    ax.axis("off")
    blue, orange, green = "#17659a", "#aa5515", "#26734d"

    def box(x, y, w, h, text, color=blue):
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.06,rounding_size=0.08",
            linewidth=1.5, edgecolor=color, facecolor="white"))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center")

    def arrow(start, end, color=blue, dashed=False):
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=13,
            linewidth=1.6, color=color, linestyle="--" if dashed else "-"))

    ax.text(5.5, 5.92, "Measure the mean and the fluctuations separately",
            ha="center", weight="bold", fontsize=16)
    box(.15, 3.35, 1.35, .95, "Variable\nlamp")
    box(2.2, 3.25, 2.0, 1.15, "Vacuum\nphotodiode\ncollecting bias")
    arrow((1.55, 3.85), (2.12, 3.85), orange)
    ax.text(1.83, 4.17, "light", ha="center", color=orange, fontsize=10)
    box(4.9, 3.25, 2.0, 1.15, "Transimpedance\nfirst stage\n" + r"$V_1=R_F I$")
    arrow((4.28, 3.85), (4.82, 3.85))
    ax.text(4.55, 4.13, r"$i(t)$", ha="center")
    box(8.1, 4.65, 2.55, .65, "DC meter: mean current", green)
    ax.plot([6.95, 7.45, 7.45], [4.0, 4.0, 4.98], color=green, lw=1.6)
    arrow((7.45, 4.98), (8.02, 4.98), green)
    ax.text(7.56, 4.48, r"$I=\langle V_1\rangle/R_F$", color=green, fontsize=10)
    box(7.7, 3.25, 2.95, 1.15, "DC rejection + gain\nthen band-pass filtering\ncalibrate actual response")
    arrow((6.98, 3.6), (7.62, 3.6))
    box(7.7, 1.75, 2.95, .8, "AC readout: square RMS\n" + r"$\sigma_v^2=\langle(v-\langle v\rangle)^2\rangle$")
    arrow((9.17, 3.18), (9.17, 2.63))
    box(.15, 1.7, 3.35, .85, "Calibration sinusoid\nbias off; electronics on", orange)
    ax.plot([3.58, 5.9], [2.12, 2.12], color=orange, lw=1.6, ls="--")
    arrow((5.9, 2.12), (5.9, 3.17), orange, True)
    ax.text(4.65, 2.37, "test port", color=orange, ha="center", fontsize=10)
    ax.text(3.2, 4.68, "anode positive relative\nto emitting cathode",
            ha="center", color=blue, fontsize=10)
    ax.text(.2, 1.15, "Current sweep: change illumination; retain gain and filter settings.",
            fontsize=11)
    ax.text(.2, .73, "Additional dark control: block light; keep detector bias and temperature fixed.",
            fontsize=11)
    ax.text(.2, .25, r"Complete transfer: $K(f)$ in V/A.  Shot contribution: "
            r"$\sigma_v^2=2qI\int_0^\infty|K(f)|^2\,df$.", fontsize=11)
    fig.subplots_adjust(left=.015, right=.99, bottom=.015, top=.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
