"""Draw the fixed-charge dielectric model; tested with Python 3.14.

Dependencies: matplotlib 3.10.7 and numpy 2.3.5, as in pyproject.toml.
Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def main():
    epsilon_r = 4.0
    field_fraction = 1.0 / epsilon_r
    polarization_fraction = 1.0 - field_fraction
    assert np.isclose(field_fraction + polarization_fraction, 1.0)
    plt.rcParams.update({"font.size": 11, "savefig.facecolor": "white"})
    fig, (ax, bars) = plt.subplots(
        1, 2, figsize=(10.8, 5.0), dpi=110,
        gridspec_kw={"width_ratios": [1.6, 1]},
    )
    fig.patch.set_facecolor("white")
    fig.suptitle("Polarization at fixed free plate charge", fontsize=16, y=0.96)
    ax.set(xlim=(0, 6.5), ylim=(-0.2, 6.1))
    ax.axis("off")
    ax.text(3.25, 5.55, r"Uniform dielectric: $\epsilon_r=4$", ha="center", fontsize=13)
    ax.add_patch(Rectangle((1.65, 2.1), 3.2, 2.8, fc="#eef4fa", ec="#a5b7c9"))
    for x, sign, color in [(1.2, "+", "#ba4239"), (5.3, "−", "#2866a3")]:
        ax.plot([x, x], [1.9, 5.05], color="#4b515b", lw=7)
        for y in np.linspace(2.25, 4.65, 5):
            sign_x = x - 0.18 if sign == "+" else x + 0.18
            ax.text(sign_x, y, sign, color=color, ha="center", va="center", fontsize=15)
    ax.text(1.2, 1.65, r"$+Q$", ha="center", color="#ba4239")
    ax.text(5.3, 1.65, r"$-Q$", ha="center", color="#2866a3")
    for x, sign, color in [(1.75, "−", "#2866a3"), (4.75, "+", "#ba4239")]:
        for y in np.linspace(2.4, 4.6, 5):
            ax.text(x, y, sign, color=color, ha="center", va="center", fontsize=14)
    for y in [2.85, 3.65, 4.45]:
        for x in [2.4, 3.65]:
            ax.add_patch(Circle((x, y), 0.11, fc="#2866a3", ec="none"))
            ax.add_patch(Circle((x + 0.55, y), 0.11, fc="#ba4239", ec="none"))
            ax.text(x, y, "−", ha="center", va="center", color="white", fontsize=10)
            ax.text(x + 0.55, y, "+", ha="center", va="center", color="white", fontsize=10)
            ax.annotate("", xy=(x + 0.48, y), xytext=(x + 0.13, y),
                        arrowprops={"arrowstyle": "->", "color": "#56616c", "lw": 1.2})
    ax.text(3.25, 2.35, r"Dipole moments and $\mathbf{P}$ point right", ha="center", fontsize=10)
    ax.text(3.25, 5.1, "Bound surface charges oppose plate charges", ha="center", fontsize=10)
    # Field arrows have lengths in the exact ratio 1 : 3/4 : 1/4.
    for y, start, end, label, color in [
        (1.1, 2.25, 5.25, r"$E_{\rm free}$", "#626b77"),
        (0.6, 5.25, 5.25 - 3 * polarization_fraction, r"$E_{\rm pol}$", "#b57b13"),
        (0.1, 2.25, 2.25 + 3 * field_fraction, r"$E$ (total)", "#2866a3"),
    ]:
        ax.text(1.95, y, label, ha="right", va="center")
        ax.annotate("", xy=(end, y), xytext=(start, y),
                    arrowprops={"arrowstyle": "-|>", "lw": 2.2, "color": color,
                                "mutation_scale": 13})
    bars.set_title(r"$D=Q/A$ stays fixed", fontsize=13, pad=15)
    bars.barh([1, 0], [1, field_fraction], color="#2866a3", height=0.36,
              label=r"$\epsilon_0 E$")
    bars.barh([1, 0], [0, polarization_fraction], left=[1, field_fraction],
              color="#d8a13c", height=0.36, label=r"$P$")
    bars.text(0.5, 1, "1", ha="center", va="center", color="white", fontsize=13)
    bars.text(field_fraction / 2, 0, "1/4", ha="center", va="center", color="white", fontsize=11)
    bars.text(field_fraction + polarization_fraction / 2, 0, "3/4", ha="center", va="center", fontsize=13)
    bars.set(yticks=[0, 1], yticklabels=["Dielectric", "Vacuum"], xlim=(0, 1.04),
             ylim=(-0.7, 1.7), xticks=[0, 0.25, 0.5, 0.75, 1],
             xlabel=r"Fraction of $D_{\rm ref}=Q/A$ (dimensionless)")
    bars.grid(axis="x", alpha=0.18)
    bars.set_axisbelow(True)
    bars.spines[["top", "right"]].set_visible(False)
    bars.legend(loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.03))
    fig.text(0.5, 0.075, r"$D=\epsilon_0E+P$; all three terms have units C/m².",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025, "Ideal plates; uniform static scalar response; schematic not to microscopic scale.",
             ha="center", fontsize=10, color="#4b515b")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.22, top=0.84, wspace=0.26)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
