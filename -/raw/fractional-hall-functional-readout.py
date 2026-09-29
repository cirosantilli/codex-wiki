"""Original functional Hall-bar diagram. Python 3.14, matplotlib 3.10.7.

Run from _media; writes fractional-hall-functional-readout.png to the CWD.
Contact positions and apparatus layout are schematic, not historical dimensions.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle


def arrow(ax, start, end, color="#176b92", width=2):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": width, "color": color})


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 6.4), facecolor="white")
    fig.suptitle("Fractional Hall transport: two independent voltage readouts",
                 fontsize=16, y=0.97)
    ax = fig.add_axes((0.035, 0.34, 0.93, 0.55))
    ax.set(xlim=(0, 12), ylim=(0, 5.5))
    ax.axis("off")
    ax.add_patch(Rectangle((2.1, 1.45), 7.3, 1.8, fc="#eaf3fa", ec="#234c69", lw=2))
    ax.text(5.75, 2.35, "two-dimensional electron gas", ha="center", fontsize=13)
    ax.text(5.75, 1.77, "Hall bar · chosen contacts · not to scale", ha="center", fontsize=10)
    contacts = {"S": (2.1, 2.35), "D": (9.4, 2.35),
                "A": (3.5, 3.25), "B": (7.8, 3.25), "C": (3.5, 1.45)}
    for name, (x, y) in contacts.items():
        ax.add_patch(Circle((x, y), 0.10, color="#234c69", zorder=5))
        dx, dy = (-0.3, 0) if name == "S" else ((0.3, 0) if name == "D" else (0.22, -0.28 if name == "C" else -0.30))
        ax.text(x + dx, y + dy, name, ha="center", va="center", fontsize=11)
    ax.plot([0.5, 2.1], [2.35, 2.35], color="#176b92", lw=2)
    ax.plot([9.4, 11.3], [2.35, 2.35], color="#176b92", lw=2)
    arrow(ax, (0.65, 2.35), (1.8, 2.35))
    arrow(ax, (9.8, 2.35), (11.1, 2.35))
    ax.text(1.15, 2.8, r"drive $I$", ha="center", color="#176b92")
    ax.text(10.4, 2.8, "return", ha="center", color="#176b92")
    ax.plot([3.5, 3.5, 4.85], [3.25, 4.4, 4.4], color="#b45719", lw=1.8)
    ax.plot([7.8, 7.8, 6.6], [3.25, 4.4, 4.4], color="#b45719", lw=1.8)
    ax.add_patch(FancyBboxPatch((4.85, 4.08), 1.75, 0.64, boxstyle="round,pad=0.1", fc="white", ec="#b45719", lw=1.8))
    ax.text(5.725, 4.4, r"$V_{xx}=V_A-V_B$", ha="center", va="center", color="#b45719")
    ax.text(5.725, 5.0, "same-side probes: longitudinal", ha="center", color="#b45719")
    ax.plot([3.5, 3.5, 0.8, 0.8], [3.25, 3.7, 3.7, 1.62], color="#704bb4", lw=1.8)
    ax.plot([3.5, 3.5, 0.8, 0.8], [1.45, 0.6, 0.6, 0.84], color="#704bb4", lw=1.8)
    ax.add_patch(FancyBboxPatch((0.12, 0.92), 1.38, 0.62, boxstyle="round,pad=0.08", fc="white", ec="#704bb4", lw=1.8))
    ax.text(0.81, 1.23, r"$V_H=V_A-V_C$", fontsize=11, ha="center", va="center", color="#704bb4")
    ax.text(2.2, 0.1, "opposite-side probes: transverse", ha="center", color="#704bb4", fontsize=11)
    ax.add_patch(Circle((10.5, 4.0), 0.25, fill=False, ec="#444444", lw=1.5))
    ax.plot(10.5, 4.0, ".", color="#444444", ms=7)
    ax.text(10.5, 4.6, r"$B$ out of plane", ha="center", fontsize=11)
    inset = fig.add_axes((0.07, 0.08, 0.40, 0.21))
    inset.set(xlim=(0, 1), ylim=(0, 1))
    inset.axis("off")
    for bottom, height, color in [(0.6, 0.28, "#f4dfb7"), (0.36, 0.24, "#f8eddb"), (0.05, 0.31, "#eaf3fa")]:
        inset.add_patch(Rectangle((0.03, bottom), 0.94, height, fc=color, ec="#666666"))
    inset.text(0.5, 0.74, "remote dopants", ha="center", fontsize=11)
    inset.text(0.5, 0.47, "undoped spacer", ha="center", fontsize=11)
    inset.plot([0.04, 0.96], [0.27, 0.27], color="#176b92", lw=3)
    inset.text(0.5, 0.12, "electron layer on GaAs side", ha="center", fontsize=10)
    inset.set_title("Layer concept: doping away from electrons", fontsize=11, pad=4)
    fig.text(0.54, 0.23, "Sweep perpendicular magnetic field; compare temperatures.", fontsize=10)
    fig.text(0.54, 0.17, r"Ideal $\nu=1/3$:  $|V_H|/I=3h/e^2$", fontsize=12)
    fig.text(0.54, 0.11, r"Measure $V_{xx}$ separately; a minimum need not be zero.", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
