"""Draw a meridional BIon profile; write an opaque PNG to the caller's cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radius = np.linspace(0.3, 4, 800)
    displacement = 1 / radius
    fig, ax = plt.subplots(figsize=(7.4, 4.4), dpi=120, facecolor="white")
    ax.plot(radius, displacement, color="#3572b0", linewidth=2.4)
    ax.plot(-radius, displacement, color="#3572b0", linewidth=2.4)
    ax.axhline(0, color="#667482", linewidth=1.1, linestyle="--")
    ax.axvspan(-0.3, 0.3, color="#e5e8ed", alpha=1, zorder=0)
    ax.annotate(
        "String charge continues along the spike",
        xy=(0, 4.05), xytext=(1.1, 3.4),
        fontsize=10, color="#64477c",
        arrowprops={"arrowstyle": "->", "color": "#64477c", "lw": 1.4},
    )
    ax.plot([0, 0], [3.3, 4.15], color="#64477c", linewidth=2, linestyle=":")
    ax.text(0, 1.55, "Core omitted", rotation=90, ha="center", va="center", color="#586572")
    ax.text(3.65, 0.1, "Planar-brane asymptote", ha="right", va="bottom", fontsize=9, color="#586572")
    ax.set(
        xlim=(-4, 4), ylim=(-0.1, 4.3),
        xlabel="Signed radial coordinate in the brane plane (units √c)",
        ylabel="Transverse displacement (units √c)",
        title="BIon spike: transverse position X − X∞ = c/r",
    )
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(
        0.5, 0.025,
        "Radial cross-section of a spherically symmetric D3 profile; the shaded cutoff is schematic.",
        ha="center", fontsize=8.3, color="#354254",
    )
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
