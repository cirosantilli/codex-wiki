"""Uniform interior field of a vacuum parallel-plate capacitor.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5 as in pyproject.toml.
Write the opaque PNG with this script's basename to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    epsilon, area, gap, voltage = 8.854e-12, 0.01, 0.001, 10.0
    capacitance = epsilon * area / gap
    charge = capacitance * voltage
    field = voltage / gap
    np.testing.assert_allclose(
        [capacitance, charge, field], [8.854e-11, 8.854e-10, 1e4], rtol=1e-14
    )
    np.testing.assert_allclose(charge / (epsilon * area), field)

    positive, negative, blue, grey = "#b64827", "#225b96", "#176c84", "#52616c"
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(9.2, 5.2), dpi=120, facecolor="white")
    ax = fig.add_axes((0.04, 0.20, 0.65, 0.64), facecolor="white")
    ax.set(xlim=(-0.7, 6.9), ylim=(-0.55, 3.95))
    ax.axis("off")

    # The gap is enlarged to make the electric field readable.
    ax.add_patch(Rectangle((0.4, 0.7), 5.0, 2.0, fc="#f0f7fa", ec="none"))
    for y, colour, sign in [(2.7, positive, "+"), (0.55, negative, "−")]:
        ax.add_patch(Rectangle((0.4, y), 5.0, 0.15, fc=colour, ec="none"))
        for x in np.linspace(0.7, 5.1, 9):
            ax.text(x, y + 0.075, sign, ha="center", va="center", color="white", fontsize=14)

    for x in np.linspace(0.85, 4.95, 7):
        ax.annotate(
            "", (x, 0.84), (x, 2.56),
            arrowprops={"arrowstyle": "-|>", "lw": 2.0, "color": blue},
        )
    ax.text(2.9, 3.48, r"Positive plate: $+Q$, potential $\phi_+$",
            ha="center", color=positive, fontsize=12)
    ax.text(2.9, 0.12, r"Negative plate: $-Q$, potential $\phi_-$",
            ha="center", color=negative, fontsize=12)
    ax.text(2.9, -0.35, "Plate area A = 0.01 m² (each)", ha="center", color=grey)
    ax.text(2.9, 1.68, r"$\mathbf{E}$", ha="center", va="center", fontsize=19,
            color=blue, bbox={"facecolor": "#f0f7fa", "edgecolor": "none", "pad": 4})

    # Dimension lines refer to the facing surfaces, not plate centres.
    for y in (0.7, 2.7):
        ax.plot([5.45, 5.85], [y, y], color=grey, lw=1)
    ax.annotate("", (5.70, 2.7), (5.70, 0.7),
                arrowprops={"arrowstyle": "<->", "color": grey, "lw": 1.2})
    ax.text(5.94, 1.7, "d = 1 mm", rotation=90, va="center", ha="center", color=grey)

    fig.suptitle("Opposite plate charges create a uniform interior field", fontsize=15, y=0.965)
    fig.text(0.5, 0.88, "Vacuum gap; plates shown edge-on; gap enlarged for clarity",
             ha="center", color=grey, fontsize=11)
    fig.text(0.71, 0.70, "Terminal difference", color=grey, fontsize=11)
    fig.text(0.71, 0.64, r"$V=\phi_+-\phi_-=10\;\mathrm{V}$", fontsize=13)
    fig.text(0.71, 0.52, r"$E\simeq V/d$", color=blue, fontsize=14)
    fig.text(0.71, 0.46, "  = 10,000 V/m", color=blue, fontsize=12)
    fig.text(0.71, 0.34, "C ≈ 88.54 pF", fontsize=12)
    fig.text(0.71, 0.28, "Q ≈ 0.8854 nC", fontsize=12)
    fig.text(0.5, 0.10, "Net device charge = 0; stored field energy ≈ 4.427 nJ",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, "ε₀ ≈ 8.854 × 10⁻¹² F/m. Edge fields neglected; schematic is not to scale.",
             ha="center", color=grey, fontsize=10)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
