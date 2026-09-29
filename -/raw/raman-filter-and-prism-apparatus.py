"""Draw the distinct filter and spectral tests; emit PNG to the working directory.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5 (root pyproject.toml).
Original schematic, not a dimensional reconstruction of the historical apparatus.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Rectangle


def arrow(ax, a, b, color="#3158a5", lw=2):
    ax.annotate("", xy=b, xytext=a,
                arrowprops={"arrowstyle": "->", "color": color, "lw": lw})


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(2, 1, figsize=(10.8, 7.4), dpi=110)
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set(xlim=(0, 12), ylim=(0, 4.2))
        ax.axis("off")
    ax = axes[0]
    ax.set_title("A. Sunlight and complementary filters: a colour-change test", loc="left", weight="bold")
    ax.text(.1, 2.9, "Sunlight", ha="left")
    for x, label in [(1.5, "Telescope\nobjective"), (3.2, "Short-focus\nlens")]:
        ax.add_patch(Ellipse((x, 2.4), .16, .95, facecolor="#e4f0fa", edgecolor="#333333"))
        ax.text(x, 1.35, label, ha="center")
    arrow(ax, (.1, 2.4), (1.3, 2.4))
    arrow(ax, (1.7, 2.4), (3, 2.4))
    ax.add_patch(Rectangle((4, 1.95), .2, .9, facecolor="#6755a6", edgecolor="black"))
    ax.text(4.1, 3.15, "Blue-violet\nfilter", ha="center")
    arrow(ax, (3.4, 2.4), (5.6, 2.4))
    ax.add_patch(Rectangle((5.7, 1.9), 1, 1, facecolor="#e7f4fa", edgecolor="#333333"))
    ax.text(6.2, 3.15, "Purified\nliquid", ha="center")
    arrow(ax, (5.8, 2.4), (6.6, 2.4), "#6755a6")
    arrow(ax, (6.2, 2.1), (6.2, .45), "#31804c")
    ax.add_patch(Rectangle((5.85, 1.05), .7, .17, facecolor="#b6c74a", edgecolor="black"))
    ax.text(7, 1.1, "Yellow-green filter → observer", va="center")
    ax.text(6.2, .12, "Side view", ha="center")
    ax.add_patch(Rectangle((4.65, 1.95), .2, .9, fill=False, edgecolor="#66711e", linestyle="--"))
    ax.text(8.1, 2.9, "Control: put BOTH filters\nin the incident beam.\nThe visible track disappears.", va="top",
            bbox={"facecolor": "#faf9e9", "edgecolor": "#b7b39a", "pad": 7})
    ax.text(.1, -.22, "Move yellow-green filter to the side view: the track reappears.", fontsize=11)

    ax = axes[1]
    ax.set_title("B. Mercury illumination and spectral separation: a later test", loc="left", weight="bold")
    ax.text(.15, 2.95, "Quartz\nmercury arc", ha="left")
    arrow(ax, (.2, 2.4), (1.7, 2.4))
    ax.add_patch(Ellipse((1.85, 2.4), .16, .9, facecolor="#e4f0fa", edgecolor="#333333"))
    ax.text(1.85, 1.45, "Condenser", ha="center")
    ax.add_patch(Rectangle((2.65, 1.95), .2, .9, facecolor="#6755a6", edgecolor="black"))
    ax.text(2.75, 3.15, "Cobalt-glass\nfilter", ha="center")
    ax.add_patch(Rectangle((3.7, 1.95), .9, .9, facecolor="#e7f4fa", edgecolor="#333333"))
    ax.text(4.15, 3.15, "Liquid", ha="center")
    arrow(ax, (2.05, 2.4), (4.4, 2.4))
    arrow(ax, (4.15, 2.05), (4.15, .9), "#31804c")
    arrow(ax, (4.15, .9), (5.7, .9), "#31804c")
    ax.text(4.6, .35, "Collected side light\n(path unfolded)", ha="center")
    ax.add_patch(Rectangle((5.85, .68), .08, .44, facecolor="#333333"))
    ax.text(5.9, 1.55, "Slit", ha="center")
    arrow(ax, (6, .9), (7.55, .9), "#31804c")
    ax.add_patch(Polygon([(7.55, .45), (8.15, .45), (7.85, 1.4)], facecolor="#d9edf4", edgecolor="#333333"))
    ax.text(7.85, 1.8, "Dispersing\nprism", ha="center")
    for y, color in [(1.3, "#6755a6"), (.95, "#207a8c"), (.6, "#31804c")]:
        arrow(ax, (8, .95), (10.25, y), color, 1.7)
        ax.plot([10.4, 10.4], [y-.09, y+.09], color=color, lw=3)
    ax.add_patch(Rectangle((10.2, .35), .45, 1.2, fill=False, edgecolor="#333333"))
    ax.text(10.4, 1.9, "Photographic\nplate", ha="center")
    ax.text(6.1, 3.05, "Compare incident and scattered spectra.\nRemove selected incident lines: their shifted groups vanish.", va="top")
    fig.text(.5, .025, "Original functional schematic; layouts and colours are illustrative, not measured.\n"
             "The prism readout summarizes spectral dispersion, not an exact Hilger optical prescription.",
             ha="center", fontsize=10)
    fig.subplots_adjust(top=.93, bottom=.12, hspace=.35, left=.035, right=.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
