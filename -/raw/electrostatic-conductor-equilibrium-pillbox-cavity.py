"""Original signed pillbox schematic and exact spherical-cavity model.

Run from _media; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Curves are analytical predictions, never experimental measurements.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    blue, orange = "#1764a0", "#b65013"
    fig, (ax, model) = plt.subplots(1, 2, figsize=(11.8, 5.2),
                                   gridspec_kw={"width_ratios": [1, 1.2]})
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-2.1, 2.1), ylim=(-1.7, 2.4))
    ax.axis("off")
    ax.set_title("A. Signed cap flux at a smooth surface", pad=16)
    ax.add_patch(Rectangle((-2, -1.55), 4, 1.55, fc="#e4e7eb", ec="none"))
    ax.axhline(0, color="#59616b", lw=2)
    ax.add_patch(Rectangle((-.7, -.55), 1.4, 1.1, fill=False,
                           ec=blue, lw=2, ls="--"))
    for x in [-1.6, -.9, -.2, .5, 1.2]:
        ax.text(x, .03, "+", color=orange, fontsize=18, ha="center")
    for x in [-1.5, 0, 1.5]:
        ax.annotate("", (x, 1.7), (x, .25),
                    arrowprops={"arrowstyle": "->", "lw": 2, "color": orange})
    ax.text(-1.95, 2.0, r"Vacuum: $\mathbf{E}_{\rm vac}=(\sigma/\epsilon_0)\mathbf{n}$")
    ax.text(-1.95, -1.27, r"Metal: $\mathbf{E}_{\rm metal}=0$", fontsize=12)
    ax.annotate("", (.85, 1.05), (.85, .55),
                arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.7})
    ax.text(.98, .85, r"$+\mathbf{n}$", color=blue)
    ax.annotate("", (.85, -1.02), (.85, -.55),
                arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.7})
    ax.text(.98, -.86, r"$-\mathbf{n}$", color=blue)
    ax.text(-.62, .66, r"cap area $A$", color=blue)
    ax.text(-1.93, -.45, r"$\sigma>0$", color=orange)
    ax.text(0, -1.65, r"$(E_{{\rm vac},n}-E_{{\rm metal},n})A=\sigma A/\epsilon_0$",
            ha="center", fontsize=12)

    model.set_title("B. Central +q in a spherical enclosure", pad=16)
    model.axvspan(1, 2, color="#e4e7eb", zorder=0)
    for x, y in [(.45, "cavity"), (1.5, "metal"), (2.65, "exterior")]:
        model.text(x, 1.85, y, ha="center", fontsize=11)
    # Plot separate open intervals: do not connect the surface discontinuities.
    for left, right, region in [(.72, 1, "cavity"), (1, 2, "metal"),
                                 (2, 3.35, "exterior")]:
        x = np.linspace(left, right, 160)
        isolated = 1 / x**2 if region != "metal" else np.zeros_like(x)
        grounded = 1 / x**2 if region == "cavity" else np.zeros_like(x)
        model.plot(x, isolated, color=blue, lw=2.8,
                   label="isolated, metal charge 0" if region == "cavity" else None)
        model.plot(x, grounded, color=orange, lw=2.2, ls="--",
                   label="grounded, metal charge −q" if region == "cavity" else None)
    for x, values in [(1, [0, 1]), (2, [0, .25])]:
        for y in values:
            model.plot(x, y, "o", mfc="white", mec=blue, ms=6, mew=1.5)
    model.set(xlim=(.68, 3.35), ylim=(-.09, 2.02), xlabel=r"Radius $r/a$ (outer radius $b=2a$)",
              ylabel=r"Radial field $E_r\,/\,[q/(4\pi\epsilon_0 a^2)]$")
    model.set_xticks([1, 1.5, 2, 2.5, 3])
    model.grid(axis="y", alpha=.2)
    model.legend(loc="upper right", bbox_to_anchor=(1, .88), fontsize=9,
                 framealpha=1, facecolor="white")
    model.text(1.5, .48, "Inner wall normal: −r̂\nInner wall charge: −q",
               ha="center", fontsize=10)
    fig.suptitle("Electrostatic conductor equilibrium: normals and cavities", fontsize=15)
    fig.text(.5, .025, "Original schematic and analytical model • one-sided surface limits • no measured data",
             ha="center", color="#4b5158", fontsize=10)
    fig.subplots_adjust(left=.04, right=.98, bottom=.19, top=.81, wspace=.35)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
