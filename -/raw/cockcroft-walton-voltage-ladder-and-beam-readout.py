"""Original functional schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; output is an opaque white PNG in the current directory.
The charge pump is intentionally a block, not a construction circuit.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, xy, width, height, text, color="#eaf2f8", fontsize=11):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.04",
                              facecolor=color, edgecolor="#29475c", linewidth=1.3))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=fontsize)


def arrow(ax, start, end, color="#176a9a"):
    ax.annotate("", end, start, arrowprops=dict(arrowstyle="->", color=color, lw=2))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (a, b) = plt.subplots(2, 1, figsize=(10, 7),
                               gridspec_kw={"height_ratios": [1.1, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Store voltage, accelerate a beam, identify the products", fontsize=16)
    for ax in (a, b):
        ax.set(xlim=(0, 10), ylim=(0, 4))
        ax.axis("off")
    a.text(0, 3.8, "A. Chosen three-stage ideal ladder", fontsize=13, weight="bold")
    box(a, (0.1, 0.65), 1.65, 1.05, "Alternating input\npeak $V_p$")
    box(a, (2.15, 0.35), 2.15, 1.65, "Rectified charge\ntransfer\n(functional block)")
    arrow(a, (1.8, 1.17), (2.1, 1.17))
    levels = [0.45, 1.35, 2.25, 3.15]
    for j, y in enumerate(levels):
        a.plot([5.1, 7.0], [y, y], color="#29475c", lw=1.4)
        a.text(7.15, y, ["0", "$2V_p$", "$4V_p$", "$6V_p$"][j], va="center")
        if j < 3:
            yc = (y + levels[j + 1]) / 2
            a.plot([6.0, 6.0], [y, yc - .1], color="#29475c")
            a.plot([6.0, 6.0], [yc + .1, levels[j + 1]], color="#29475c")
            for offset in (-.1, .1):
                a.plot([5.6, 6.4], [yc + offset] * 2, color="#176a9a", lw=2)
            a.text(6.55, yc, "$C$", va="center")
    for j in range(1, 4):
        arrow(a, (4.35, 1.5), (5.1, levels[j]))
    a.text(8.1, 2.35, "Series storage\nadds voltage", ha="center")
    a.text(8.1, .8, "Load removes charge;\npump replenishes it", ha="center")
    a.text(.1, -.02, "Block diagram only • no component ratings or wiring • not the 1932 stage count", fontsize=10)

    b.text(0, 3.8, "B. Beam and reaction readout", fontsize=13, weight="bold")
    box(b, (.15, 2.2), 1.6, 1, "Positive ions\nat $+V$")
    box(b, (2.45, 2.1), 3.05, 1.2, "Evacuated accelerating tube\n$K_f-K_i=qV$")
    box(b, (6.3, 2.15), 1.55, 1.1, "Lithium\ntarget\nat ground", color="#fff1dc")
    arrow(b, (1.8, 2.7), (2.4, 2.7))
    arrow(b, (5.55, 2.7), (6.25, 2.7))
    b.text(5.87, 3.18, "beam", ha="center", fontsize=10)
    box(b, (6.25, .15), 1.75, .9, "Mica absorber\nor window", color="#f1f0fb")
    box(b, (8.4, .15), 1.35, .9, "ZnS screen\n+ microscope", color="#e9f5e9", fontsize=10)
    arrow(b, (7.1, 2.1), (7.1, 1.1), color="#a63d35")
    b.text(7.3, 1.55, "products", color="#a63d35", fontsize=10)
    arrow(b, (8.05, .6), (8.35, .6), color="#a63d35")
    b.text(.25, 1.3, "One total potential drop sets beam energy.\nAbsorption and flashes test the products.", fontsize=12)
    b.text(.25, .3, "Historical readout functions; geometry simplified.\nBeam blocking supplies a separate control.", fontsize=10)
    fig.subplots_adjust(top=.9, bottom=.07, left=.045, right=.98, hspace=.23)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
