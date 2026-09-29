"""Original preparation and equilibrium schematic, not data or cooling kinetics.

Run from _media. Tested with Python 3.14 and Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def sample(ax, x, y, interior, screened, label):
    width, height = 1.48, 0.92
    ax.add_patch(Rectangle((x, y), width, height, facecolor="#edf4f7",
                           edgecolor="#4b606c", lw=1.3))
    if screened:
        for edge in (x, x + width - 0.09):
            ax.add_patch(Rectangle((edge, y), 0.09, height,
                                   facecolor="#d97832", edgecolor="none"))
    if interior:
        for yy in (y + 0.24, y + 0.48, y + 0.72):
            ax.add_patch(FancyArrowPatch((x + 0.12, yy), (x + width - 0.12, yy),
                                         arrowstyle="-|>", mutation_scale=12,
                                         lw=1.5, color="#176b9c"))
    else:
        ax.text(x + width / 2, y + height / 2, r"$B_{\rm bulk}\simeq0$",
                ha="center", va="center", fontsize=11)
    ax.text(x + width / 2, y - 0.15, label, ha="center", va="top", fontsize=10)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(10.5, 5.3))
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.14, top=0.84)
    ax.set(xlim=(-1.45, 8.4), ylim=(-0.5, 4.05))
    ax.axis("off")
    columns = (0, 2.35, 4.75, 6.75)
    for x, title in zip(columns, ("1. Start normal", "2. Prepare below transition",
                                  "Meissner equilibrium", "Perfect-conductor model")):
        ax.text(x + 0.74, 3.78, title, ha="center", va="bottom", fontsize=11)
    for y, name in ((2.18, "Field first"), (0.27, "Cool first")):
        ax.text(-1.34, y + 0.62, name, ha="left", va="center", weight="bold")
        field_first = name == "Field first"
        sample(ax, 0, y, field_first, False,
               r"$T>T_c$, field on" if field_first else r"$T>T_c$, field off")
        ax.add_patch(Rectangle((2.35, y), 1.48, 0.92, facecolor="#fff8ec",
                               edgecolor="#a38c65", lw=1.3))
        ax.text(3.09, y + 0.46,
                "Cool while\nholding field fixed" if field_first
                else "Cool with field off;\nthen switch field on",
                ha="center", va="center", fontsize=10)
        sample(ax, 4.75, y, False, True, "Same screened end state")
        sample(ax, 6.75, y, field_first, not field_first,
               "Pre-existing field retained" if field_first else "Zero interior field retained")
        for start, end in ((1.54, 2.29), (3.92, 4.69)):
            ax.add_patch(FancyArrowPatch((start, y + 0.46), (end, y + 0.46),
                                         arrowstyle="-|>", mutation_scale=13,
                                         color="#53636c", lw=1.3))
    fig.suptitle("Cooling and field history: expulsion versus flux memory", fontsize=15, y=0.96)
    fig.text(0.5, 0.04,
             "Both final states: same low temperature and weak applied field. Solid, simply connected, thick sample.\n"
             "Blue: interior field. Orange: screening layer (schematic). Not measured data; no transition kinetics.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
