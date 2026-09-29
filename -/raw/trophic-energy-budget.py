"""Plot a production budget with explicitly assumed 10% transfer efficiency.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Write an opaque white same-basename PNG to the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    efficiency = 0.10
    production = 1000 * efficiency ** np.arange(3)
    not_transferred = production[:-1] - production[1:]
    np.testing.assert_allclose(production, [1000, 100, 10])
    np.testing.assert_allclose(not_transferred, [900, 90])

    fig, ax = plt.subplots(figsize=(8.8, 4.9))
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    fig.subplots_adjust(left=0.24, right=0.95, top=0.76, bottom=0.29)
    y = np.array([2, 1, 0])
    ax.barh(y, production, height=0.48,
            color=["#5c8b48", "#367fa3", "#9d6298"], zorder=3)
    for pos, value in zip(y, production):
        ax.text(value + 14, pos, f"{value:g}", va="center",
                fontsize=13, weight="bold", color="#243642")
    ax.set_yticks(y, ["Level 1\nPrimary producers",
                     "Level 2\nPrimary consumers", "Level 3\nSecondary consumers"])
    ax.set_xlim(0, 1100)
    ax.set_ylim(-0.6, 2.6)
    ax.set_xticks(np.arange(0, 1001, 200))
    ax.set_xlabel("Net production (kJ per m² per day) • one linear scale", fontsize=11)
    ax.tick_params(axis="both", labelsize=11)
    ax.grid(axis="x", color="#dce3e8", linewidth=0.8, zorder=0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.text(0.5, 0.94, "An assumed trophic energy budget", ha="center",
             fontsize=16, weight="bold", color="#243642")
    fig.text(0.5, 0.87, "10% transfer at EACH step is assumed, not a universal law",
             ha="center", fontsize=11.5, color="#243642")
    fig.text(0.5, 0.16, "1000 × 0.10 = 100       100 × 0.10 = 10", ha="center",
             fontsize=12, color="#243642")
    fig.text(0.5, 0.095, "Production not transferred along this chain: 900, then 90",
             ha="center", fontsize=11, color="#243642")
    fig.text(0.5, 0.04, "Includes other material routes and heat; these differences are not heat alone",
             ha="center", fontsize=10, color="#243642")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Production: {production.tolist()}; not transferred: {not_transferred.tolist()}")


if __name__ == "__main__":
    main()
