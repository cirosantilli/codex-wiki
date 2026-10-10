"""Draw a water mass, mole and particle-count map into the current directory.

Original schematic with explicitly chosen approximate composition inputs.
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(10.5, 6.3), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    blue, red, ink = "#236aa0", "#bd4938", "#243241"
    ax.text(.5, .95, "Water: from a weighed sample to particles", ha="center",
            fontsize=20, weight="bold", color=ink)
    ax.text(.5, .885, r"Chosen inputs: $A_r(\mathrm{H})=1.008$, $A_r(\mathrm{O})=15.999$; "
            r"$M\approx18.015\ \mathrm{g\,mol^{-1}}$", ha="center", fontsize=13)

    def box(x, heading, value, detail):
        ax.add_patch(FancyBboxPatch((x, .59), .255, .21,
                     boxstyle="round,pad=0.008", facecolor="#eef5fa", edgecolor=blue))
        ax.text(x+.1275, .755, heading, ha="center", weight="bold", color=blue)
        ax.text(x+.1275, .686, value, ha="center", fontsize=17, color=ink)
        ax.text(x+.1275, .627, detail, ha="center", fontsize=11)

    box(.03, "Sample mass", r"$m=4.50375\ \mathrm{g}$", "illustrative pure water sample")
    box(.373, "Amount of water", r"$n\approx0.250000\ \mathrm{mol}$", "entities: water molecules")
    box(.716, "Molecule count", r"$N\approx1.50553519\times10^{23}$", "count has no mass units")
    for start, end, label in [(.292, .364, r"$\div M$"), (.635, .707, r"$\times N_A$")]:
        ax.annotate("", xy=(end, .696), xytext=(start, .696),
                    arrowprops={"arrowstyle": "->", "lw": 2, "color": blue})
        ax.text((start+end)/2, .735, label, ha="center", fontsize=12)

    # One symbolic molecule illustrates atom accounting, not molecular geometry.
    oxygen = (.14, .415)
    hydrogen = [(.085, .365), (.195, .365)]
    for p in hydrogen:
        ax.plot([oxygen[0], p[0]], [oxygen[1], p[1]], color=ink, lw=3, zorder=1)
    for (x, y), color, symbol, radius in [(oxygen, red, "O", .032),
            (hydrogen[0], blue, "H", .025), (hydrogen[1], blue, "H", .025)]:
        ax.add_patch(Circle((x, y), radius, facecolor=color, edgecolor="white", zorder=2))
        ax.text(x, y, symbol, color="white", ha="center", va="center", weight="bold")
    ax.text(.14, .295, "One molecule (schematic)", ha="center", fontsize=11)
    ax.text(.35, .458, "Keep molecule counts and atom counts distinct", weight="bold", color=ink)
    ax.text(.35, .392, r"Hydrogen atoms: $2N\approx3.01107038\times10^{23}$", color=blue)
    ax.text(.35, .328, r"Oxygen atoms: $N\approx1.50553519\times10^{23}$", color=red)
    ax.text(.5, .217, r"Mean mass per molecule: $M/N_A\approx2.99146\times10^{-26}\ \mathrm{kg}$",
            ha="center", fontsize=15, color=ink)
    ax.plot([.03, .97], [.165, .165], color="#cbd5df")
    ax.text(.5, .115, r"$N_A=6.02214076\times10^{23}\ \mathrm{mol^{-1}}$ is exact.",
            ha="center", fontsize=13)
    ax.text(.5, .055, "Sample results are approximate: isotope composition and input rounding matter.",
            ha="center", fontsize=12, color=ink)
    fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
