"""Original functional diagram; emits its basename PNG in the working directory.

Experimental functions: Ono et al., Phys. Rev. B 92, 174424 (2015),
Section II, Figures 1 and 2. Layout is original, not a scale reconstruction.
Tested with Python 3.14, matplotlib 3.10.7; no additional dependencies.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 6.6), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.92, bottom=0.035)
    ax.set(xlim=(0, 10), ylim=(0, 7.3), aspect="equal")
    ax.axis("off")
    blue, red, green = "#245b91", "#b03838", "#24704e"

    def arrow(a, b, color=blue, **kwargs):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>",
                                    mutation_scale=15, linewidth=1.8,
                                    color=color, **kwargs))

    fig.suptitle("Barnett rotation magnetometry: drive, shield, detect", fontsize=16)
    ax.add_patch(FancyBboxPatch((0.3, 2.0), 9.3, 4.2,
                               boxstyle="round,pad=0.03", facecolor="white",
                               edgecolor="#727b85", linewidth=2, linestyle="--"))
    ax.text(0.55, 5.91, "Magnetic shielding", color="#525b65")
    ax.add_patch(FancyBboxPatch((3.05, 2.7), 1.25, 2.9,
                               boxstyle="round,pad=0.05", facecolor="#f2f5f8",
                               edgecolor=blue, linewidth=1.5))
    ax.add_patch(Rectangle((3.37, 2.95), 0.6, 2.2, facecolor="#a8c5df",
                           edgecolor=blue, linewidth=1.5))
    ax.plot([3.67, 3.67], [2.4, 5.75], color="#909090", linestyle=":")
    ax.text(0.55, 4.65, "Gd cylinder\n6 mm diameter\n20 mm long", va="center")
    ax.plot([2.0, 3.36], [4.65, 4.45], color="#535353", linewidth=1)
    ax.text(0.55, 3.25, "Nonmagnetic rotor\nZirconia capsule\nPolyimide impeller", va="center")
    ax.plot([2.6, 3.02], [3.25, 3.25], color="#535353", linewidth=1)
    # A straight axial arrow defines positive angular velocity, not gas flow.
    arrow((4.7, 4.55), (4.7, 5.48), blue)
    ax.text(4.9, 5.1, r"$+z,\ +\Omega$", color=blue, va="center")
    arrow((3.67, 4.85), (3.67, 3.35), red)
    ax.text(4.4, 3.5, r"$M_z<0$" + "\n" + r"if $\gamma<0$", color=red)
    ax.plot([3.67, 7.15], [4.05, 4.05], color="#666666", linestyle=":")
    ax.annotate("", xy=(3.67, 4.05), xytext=(7.15, 4.05),
                arrowprops={"arrowstyle": "<->", "color": "#666666"})
    ax.text(5.65, 4.13, "15 mm from axis", ha="center", va="bottom", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.plot(7.15, 4.05, "o", color=green, markersize=5)
    ax.plot([7.15, 7.15], [4.05, 4.45], color=green)
    ax.add_patch(FancyBboxPatch((7.1, 4.45), 2.0, 0.8,
                               boxstyle="round,pad=0.06", facecolor="#eff8f1",
                               edgecolor=green, linewidth=1.5))
    ax.text(8.1, 4.85, "Fluxgate readout", ha="center", color=green)
    arrow((7.15, 3.15), (7.15, 3.95), green)
    ax.text(7.5, 3.25, r"$B_{z,\mathrm{stray}}>0$", color=green, fontsize=11)
    ax.text(5.45, 2.38, "At the equator, stray-field sign opposes M", fontsize=10)
    arrow((3.67, 6.92), (3.67, 5.63), blue)
    ax.text(4.05, 6.78, "Air drive: reverse flow to reverse rotation", va="center")
    ax.text(0.45, 6.68, "Functional schematic\nGeometry simplified", fontsize=10, color="#555555")
    boxes = [(0.35, "Reverse rotation", r"Record $+\Omega,\ 0,\ -\Omega$"),
             (3.6, "Check background", "Repeat with empty capsule"),
             (6.85, "Infer magnetization", "Convert stray field using geometry")]
    for x, title, text in boxes:
        ax.add_patch(FancyBboxPatch((x, 0.65), 2.8, 0.95,
                                   boxstyle="round,pad=0.08", facecolor="white",
                                   edgecolor="#7d8792"))
        ax.text(x+1.4, 1.29, title, ha="center", weight="bold", fontsize=10)
        ax.text(x+1.4, 0.94, text, ha="center", fontsize=8.8)
    ax.text(5, 0.15, "Arrows define signs; no measured trace is drawn.",
            ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
