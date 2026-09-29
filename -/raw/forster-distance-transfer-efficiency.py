"""Original FRET model figure; tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes forster-distance-transfer-efficiency.png to the CWD.
The curve is a single-pair model with fixed spectral and orientational properties.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def efficiency(relative_distance):
    return 1.0 / (1.0 + np.asarray(relative_distance) ** 6)


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0.4, 2.3, 900)
    fig, ax = plt.subplots(figsize=(8.2, 5.3), layout="constrained", facecolor="white")
    ax.set_facecolor("white")
    ax.axvspan(4 ** (-1 / 6), 4 ** (1 / 6), color="#e9f4f1", label="20–80% efficiency")
    ax.plot(x, efficiency(x), color="#00796b", lw=3)
    ax.plot([1, 1], [0, 0.5], "--", color="#777777", lw=1)
    ax.plot([0.4, 1], [0.5, 0.5], "--", color="#777777", lw=1)
    for point, label, offset in [
        (0.5, "½ R₀: 98.46%", (15, -23)),
        (1.0, "R₀: 50%", (22, 12)),
        (1.5, "1½ R₀: 8.07%", (12, 22)),
        (2.0, "2 R₀: 1.54%", (-95, 15)),
    ]:
        ax.scatter(point, efficiency(point), color="#00796b", s=40, zorder=4)
        ax.annotate(label, (point, efficiency(point)), xytext=offset, textcoords="offset points", fontsize=11)
    ax.set(xlim=(0.4, 2.3), ylim=(0, 1.05), xlabel="Separation relative to Förster distance, r / R₀", ylabel="Transfer efficiency, E")
    ax.set_title("A steep proximity response near the Förster distance", fontsize=15, pad=14)
    ax.text(1.52, 0.7, r"$E = 1 / [1 + (r/R_0)^6]$", fontsize=15, ha="center")
    ax.legend(loc="center right", frameon=False, fontsize=11)
    ax.grid(alpha=0.2)
    fig.get_layout_engine().set(rect=(0, 0.1, 1, 0.9))
    fig.text(0.5, 0.025, "Single donor–acceptor pair; fixed R₀. Model predictions, not measurements.\nThe dipole approximation is not a model of touching labels at r = 0.", ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
