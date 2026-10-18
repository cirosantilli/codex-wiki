"""Schematic hydrograph for Oxford C5.7 (2023), Question 2(c)(iii).

Run from the destination directory; writes 2023-aquifer-drainage.png.
Dependencies and tested Python version are documented in the root pyproject.toml
and README.md. The curve illustrates asymptotic regimes, not a PDE solution.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    transition = 1.0
    rain_time = np.linspace(0.0, transition, 250)
    dry_time = np.linspace(transition, 3.5, 350)
    rain_flux = 1.0 - np.exp(-3.0 * rain_time)
    dry_flux = rain_flux[-1] / (1.0 + 1.5 * (dry_time - transition)) ** 2

    fig, ax = plt.subplots(figsize=(8.0, 4.2), layout="constrained", facecolor="white")
    ax.set_facecolor("white")
    ax.axhline(1.0, color="0.6", linestyle=":", linewidth=1.2)
    ax.plot(rain_time, rain_flux, color="#1768ac", linewidth=2.5)
    ax.plot(dry_time, dry_flux, color="#bd5825", linewidth=2.5)
    ax.axvline(transition, color="0.35", linestyle="--", linewidth=1.2)
    ax.text(0.48, 1.08, "Rainfall", ha="center", color="#1768ac")
    ax.text(2.25, 1.08, "Drought", ha="center", color="#bd5825")
    ax.text(1.0, 0.04, "$t^*$", transform=ax.get_xaxis_transform(), ha="left", va="bottom")
    ax.annotate(
        r"Early rise: $Q_0\propto t$",
        xy=(0.12, 1.0 - np.exp(-0.36)), xytext=(0.42, 0.32),
        arrowprops={"arrowstyle": "->", "color": "0.25"}, fontsize=10,
    )
    ax.annotate(
        r"Late recession: $Q_0\propto(t-t^*+\mathrm{const.})^{-2}$",
        xy=(2.55, rain_flux[-1] / (1.0 + 1.5 * 1.55) ** 2), xytext=(1.60, 0.53),
        arrowprops={"arrowstyle": "->", "color": "0.25"}, fontsize=10,
    )
    ax.text(3.46, 1.01, "steady recharge $RL$", ha="right", va="bottom", fontsize=9, color="0.4")
    ax.set(xlim=(0.0, 3.5), ylim=(0.0, 1.18), xlabel="$t/t^*$", ylabel="$Q_0/(RL)$")
    ax.set_title("Aquifer drainage response (schematic)", fontsize=13)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig("2023-aquifer-drainage.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
