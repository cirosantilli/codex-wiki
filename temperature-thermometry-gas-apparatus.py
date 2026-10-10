"""Original schematic; simplified measurement layout, not measured data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib:
python ../temperature-thermometry-gas-apparatus.py
Tested: Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
The output basename is derived from this script and written to the CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(9.5, 5.6), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 7.1))
    ax.axis("off")
    ax.text(6, 6.86, "Constant-volume gas thermometry: compare two settled states",
            ha="center", va="center", fontsize=15, weight="bold")
    ax.text(6, 6.46, "Original simplified schematic • not an exact NBS instrument • not to scale",
            ha="center", fontsize=10, color="#555555")

    bath = FancyBboxPatch((.45, 2.05), 4.3, 3.7, boxstyle="round,pad=0.08",
                         facecolor="#eaf4fc", edgecolor="#25668c", lw=1.8)
    ax.add_patch(bath)
    ax.text(2.6, 5.38, "Controlled, circulating bath", ha="center", weight="bold")
    bulb = Circle((2.55, 3.65), .72, facecolor="white", edgecolor="#cb6c16", lw=2.8)
    ax.add_patch(bulb)
    ax.text(2.55, 3.65, "Sealed gas\n$T_b$, $V_b$", ha="center", va="center")
    # Three separate bath sensors check the spatial surroundings of the bulb.
    for x, y in [(1.05, 3.7), (4.05, 3.7), (3.65, 2.75)]:
        ax.plot([x, x], [y+.6, y], color="#246a78", lw=3)
        ax.plot(x, y, "o", color="#246a78", ms=6)
    ax.text(2.6, 2.3, "Independent calibrated bath probes", ha="center", fontsize=10)
    ax.annotate("", xy=(1.48, 4.65), xytext=(1.48, 3.05),
                arrowprops={"arrowstyle": "->", "color": "#4384a2", "lw": 1.7})
    ax.annotate("", xy=(3.48, 3.1), xytext=(3.48, 4.65),
                arrowprops={"arrowstyle": "->", "color": "#4384a2", "lw": 1.7})

    ax.plot([2.55, 2.55, 8.4], [4.37, 4.85, 4.85], color="#cb6c16", lw=3)
    ax.text(6.25, 5.32, "Connecting tube\nmeasure $V_j$ and $T_j$", ha="center", fontsize=10)
    for x, label in [(5.1, "$T_1$"), (6.25, "$T_2$"), (7.4, "$T_3$")]:
        ax.plot(x, 4.85, "o", color="#246a78", ms=5)
        ax.text(x, 4.48, label, ha="center", color="#246a78")
    # Filling branch is closed throughout each reference/test comparison.
    ax.plot([6.25, 6.25], [4.85, 3.05], color="#cb6c16", lw=2)
    ax.plot([6.1, 6.4], [3.63, 3.93], color="#333333", lw=2)
    ax.plot([6.1, 6.4], [3.93, 3.63], color="#333333", lw=2)
    ax.text(6.25, 2.55, "Fill / evacuate\nvalve CLOSED", ha="center", va="center", fontsize=10)

    chamber = Rectangle((8.4, 4.13), 1.25, 1.4, facecolor="white", edgecolor="#555555", lw=1.6)
    ax.add_patch(chamber)
    ax.plot([9.03, 9.03], [4.16, 5.5], color="#555555", lw=3)
    ax.plot([9.65, 10.8], [4.85, 4.85], color="#555555", lw=2)
    ax.text(8.98, 3.75, "Diaphragm near null:\npressure transmitted;\ngases kept separate", ha="center", va="top", fontsize=10)
    standard = FancyBboxPatch((10.05, 2.15), 1.6, 1.7, boxstyle="round,pad=0.05",
                             facecolor="#f5f5f5", edgecolor="#555555", lw=1.5)
    ax.add_patch(standard)
    ax.plot([10.8, 10.8], [4.85, 3.9], color="#555555", lw=2)
    ax.text(10.85, 3, "Absolute\npressure\nstandard\n(vacuum ref.)", ha="center", va="center", fontsize=10)

    ax.text(6, 1.6, "Reference $T_0$: record $P_0$   →   Test $T$: record $P$   →   Repeat reference",
            ha="center", fontsize=12, weight="bold")
    ax.text(6, 1.03, "Each pair: fixed total gas inventory • thermalize before reading • correct bulb volume",
            ha="center", fontsize=10)
    ax.text(6, .58, "Correct connecting-tube gas, pressure offsets and nonideality; repeat at several fills",
            ha="center", fontsize=10)
    fig.subplots_adjust(left=.02, right=.985, bottom=.02, top=.99)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
