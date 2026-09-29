"""Original Ramsey beam/timing model; Python 3.14, matplotlib 3.10.7.

Run from _media; writes the matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (beam, timing) = plt.subplots(
        2, 1, figsize=(11.5, 5.8), gridspec_kw={"height_ratios": [1.25, 1]}
    )
    fig.patch.set_facecolor("white")
    blue, orange, gray = "#1766a5", "#c66313", "#48535c"
    beam.set(xlim=(0, 12), ylim=(-0.45, 3.2))
    beam.axis("off")
    beam.set_title("A beam supplies the timing by moving through space", loc="left", pad=10)
    boxes = [
        (0.1, 1.6, "Source +\napertures", gray, 1.55),
        (2.0, 1.6, "State\nselection", gray, 1.35),
        (4.05, 1.6, "Zone 1", blue, 1.05),
        (8.05, 1.6, "Zone 2", blue, 1.05),
        (9.85, 1.6, "State-sensitive\nreadout", gray, 1.95),
    ]
    beam.add_patch(Rectangle((3.75, 0.60), 5.65, 2.15, facecolor="#f3f6f8", edgecolor="#a7afb5"))
    for x, y, label, color, width in boxes:
        beam.add_patch(Rectangle((x, y - 0.43), width, 0.86, facecolor="white", edgecolor=color, linewidth=1.6))
        beam.text(x + width / 2, y, label, ha="center", va="center", color=color)
    for left, right in [(1.65, 2.0), (3.35, 4.05), (5.1, 8.05), (9.1, 9.85)]:
        beam.add_patch(FancyArrowPatch((left, 1.6), (right, 1.6), arrowstyle="->", mutation_scale=13, color=gray))
    beam.text(6.57, 1.83, "Dark drift", ha="center", color=orange)
    beam.text(6.57, 1.30, r"$H_f=\hbar\delta\sigma_z/2$", ha="center")
    beam.text(6.57, 0.84, "Static field may remain; no transverse drive", ha="center", fontsize=10)
    beam.text(6.57, 2.99, "One coherent oscillator feeds both zones", ha="center", color=blue)
    beam.plot([4.575, 4.575, 8.575, 8.575], [2.05, 2.55, 2.55, 2.05], color=blue, linewidth=1.4)
    beam.annotate("", xy=(8.05, 0.31), xytext=(5.1, 0.31), arrowprops={"arrowstyle": "<->", "color": orange})
    beam.text(6.57, 0.02, r"Edge-to-edge gap $L$", ha="center", va="top", color=orange)
    beam.text(0.1, -0.35, "Functional model; paths and lengths are schematic", fontsize=9, color=gray)

    timing.set_title("The same sequence along one particle's trajectory", loc="left", pad=10)
    timing.set(xlim=(-0.25, 6.8), ylim=(-0.65, 1.55), yticks=[0, 1], yticklabels=["0", r"$\Omega$"], xticks=[0, .5, 5.5, 6], xticklabels=["0", r"$\tau$", r"$\tau+T$", r"$2\tau+T$"])
    timing.plot([0, 0, .5, .5, 5.5, 5.5, 6, 6], [0, 1, 1, 0, 0, 1, 1, 0], color=blue, linewidth=2)
    timing.fill_between([0, .5], 0, 1, color=blue, alpha=.12)
    timing.fill_between([5.5, 6], 0, 1, color=blue, alpha=.12)
    timing.text(.25, 1.13, r"$\varphi_1=0$", ha="center", color=blue)
    timing.text(5.75, 1.13, r"$\varphi_2=\varphi$", ha="center", color=blue)
    timing.text(3, .62, r"Relative phase accumulates: $\delta T$", ha="center", color=orange)
    timing.text(3, .30, r"$\tau=\ell/v$,   $T=L/v$,   $\Omega\tau=\pi/2$ on resonance", ha="center")
    timing.text(3, -.51, "Drive phase is defined relative to the oscillator, which keeps running", ha="center", fontsize=10, color=gray)
    timing.set_ylabel("Transverse drive")
    timing.set_xlabel("Elapsed time")
    timing.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(left=.09, right=.985, top=.93, bottom=.10, hspace=.42)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
