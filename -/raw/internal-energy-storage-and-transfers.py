"""Draw an original internal-energy schematic; output a PNG in the working directory.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
The numerical labels are a stipulated ideal-gas model, not measurements.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def draw():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(10, 6.2), dpi=120, facecolor="white")
    ax = fig.add_axes((0, 0, 1, 1), facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.2))
    ax.axis("off")
    ink, blue, orange = "#203447", "#206a9b", "#ad531b"

    def box(x, y, w, h, text, color, fill):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.10",
                                   edgecolor=color, facecolor=fill, linewidth=1.5))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=ink,
                linespacing=1.45)

    def arrow(start, end, color):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=17, linewidth=2, color=color))

    ax.text(5, 5.83, "Internal energy: storage and transfer", ha="center",
            fontsize=18, weight="bold", color=ink)
    box(3.16, 3.49, 3.64, 1.52,
        "Inside the chosen system\n" + r"Stored internal energy $U$" +
        "\nMicroscopic kinetic energy\n+ interaction potential energy", blue, "#eef7fc")
    arrow((0.65, 4.25), (3.02, 4.25), orange)
    ax.text(1.80, 4.64, "Heat transfer", ha="center", color=orange, weight="bold")
    ax.text(1.80, 3.83, r"$Q_{\rm in}$", ha="center", color=orange)
    arrow((9.33, 4.25), (6.94, 4.25), blue)
    ax.text(8.17, 4.64, "Work transfer", ha="center", color=blue, weight="bold")
    ax.text(8.17, 3.83, r"$W_{\rm on}$", ha="center", color=blue)
    ax.text(5, 3.12, r"$\Delta U=Q_{\rm in}+W_{\rm on}$", ha="center", fontsize=16, color=ink)
    ax.text(5, 2.69, "Calculated model: 1 mol monatomic ideal gas, rigid volume, 300 → 310 K",
            ha="center", fontsize=11.5, color=ink)
    box(0.59, 1.39, 4.15, 1.00,
        "Thermal route\n" + r"$Q_{\rm in}=124.71$ J,   $W_{\rm on}=0$", orange, "#fff5ed")
    box(5.24, 1.39, 4.15, 1.00,
        "Insulated stirring route\n" + r"$Q_{\rm in}=0$,   $W_{\rm on}=124.71$ J", blue, "#eef7fc")
    ax.text(5, 1.05, "Same equilibrium endpoints: ΔU = 124.71 J in both routes",
            ha="center", color=ink, weight="bold", fontsize=11.5)
    ax.text(5, 0.55, "Accounted for separately: whole-body motion and external elevation",
            ha="center", fontsize=11.5, color=ink)
    ax.text(5, 0.22, "Schematic + stipulated model • R = 8.314 J mol⁻¹ K⁻¹ • no measured data",
            ha="center", fontsize=10, color="#556777")
    out = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(out, facecolor="white", transparent=False)
    plt.close(fig)
    return out


if __name__ == "__main__":
    print(draw())
