"""Draw stipulated compartment counts and conceptual transport energy profiles.

Output basename.png in cwd. Tested with Python 3.14, Matplotlib 3.10.7,
and NumPy 2.3.5. Profile heights are unscaled, not experimental barriers.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def profile(x, start, peak, end):
    """Join prescribed endpoints and a peak using smooth cubic segments."""
    t = np.where(x <= 0.5, 2 * x, 2 * x - 1)
    smooth = t * t * (3 - 2 * t)
    return np.where(x <= 0.5, start + (peak - start) * smooth,
                    peak + (end - peak) * smooth)


def main():
    blue, orange, gray = "#236d99", "#bc6419", "#636a72"
    fig = plt.figure(figsize=(10, 7.8), facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=(1, 1.25),
                           left=0.09, right=0.97, bottom=0.13, top=0.88,
                           hspace=0.55, wspace=0.36)
    counts = fig.add_subplot(grid[0, :])
    counts.set(xlim=(0, 1), ylim=(0, 1))
    counts.axis("off")
    counts.add_patch(Rectangle((0.02, 0.02), 0.96, 0.85,
                               facecolor="white", edgecolor=gray, lw=1.4))
    counts.add_patch(Rectangle((0.485, 0.02), 0.03, 0.85,
                               facecolor="#fff0d7", edgecolor=orange, lw=1.2))
    left = [(x, y) for x in (0.085, 0.155, 0.225, 0.295) for y in (0.3, 0.6)]
    right = [(0.82, 0.3), (0.82, 0.6)]
    counts.scatter(*zip(*(left + right)), s=65, color=blue)
    counts.text(0.25, 0.94, "A: 8 tracers", ha="center", fontsize=12, weight="bold")
    counts.text(0.75, 0.94, "B: 2 tracers", ha="center", fontsize=12, weight="bold")
    counts.annotate("", (0.69, 0.60), (0.36, 0.60),
                    arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    counts.text(0.525, 0.70, "Passive: A → B", ha="center", fontsize=11, color=blue)
    counts.annotate("", (0.36, 0.26), (0.69, 0.26),
                    arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
    counts.text(0.525, 0.36, "Active: B → A", ha="center", fontsize=11, color=orange)
    counts.text(0.5, -0.12, "Equal volumes; neutral solute; c(A) / c(B) = 4. Counts are stipulated.",
                ha="center", fontsize=11)
    x = np.linspace(0, 1, 501)
    passive = fig.add_subplot(grid[1, 0])
    active = fig.add_subplot(grid[1, 1])
    passive.plot(x, profile(x, 2, 5.5, 0), color=gray, lw=2.4)
    passive.plot(x, profile(x, 2, 3.4, 0), color=blue, lw=2.4)
    passive.text(0.50, 5.85, "Unassisted route", ha="center", color=gray, fontsize=10)
    passive.text(0.51, 3.77, "Facilitated route", ha="center", color=blue, fontsize=10)
    passive.text(0.80, 4.75, "Same endpoints\nΔμ < 0", ha="center", fontsize=10)
    passive.set_title("Passive: a route, no uphill drive", fontsize=12, pad=12)
    passive.set_xticks([0, 1], ["A: higher μ", "B: lower μ"])
    passive.set_ylabel("Conceptual free energy (unscaled)", fontsize=11)
    active.plot(x, profile(x, 0, 3.8, 2), color=orange, lw=2.4)
    active.text(0.5, 4.2, "Solute alone: Δμ > 0", ha="center", color=orange, fontsize=11)
    active.annotate("", (0.78, 0.1), (0.78, 1.9),
                    arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#356957"})
    active.text(0.50, -1.15, "Couple to a downhill process:\nATP hydrolysis or another gradient", ha="center",
                fontsize=10, color="#356957")
    active.set_title("Active: couple to an energy source", fontsize=12, pad=12)
    active.set_xticks([0, 1], ["B: lower μ", "A: higher μ"])
    for ax in (passive, active):
        ax.set(xlim=(-0.03, 1.03), ylim=(-1.55, 6.6), yticks=[])
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(axis="x", labelsize=10)
        ax.set_xlabel("Route progress (not time)", fontsize=10, labelpad=8)
        for xpos, ypos in ((0, 2 if ax is passive else 0), (1, 0 if ax is passive else 2)):
            ax.plot(xpos, ypos, "o", color="#30353b", ms=4)
    fig.suptitle("Transport: downhill passage or coupled uphill movement", fontsize=15, y=0.975)
    fig.text(0.5, 0.935, "Arrows indicate the neutral-solute net direction under the stated conditions.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Constructed energy sketches: heights, routes and particle counts are not measured biophysical data.",
             ha="center", fontsize=10, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    ratio = len(left) / len(right)
    r, temp, faraday = 8.314462618, 300.0, 96485.33212
    neutral = r * temp * np.log(1 / ratio)
    ion = r * temp * np.log(ratio) + faraday * (-0.060)
    budget = np.log(ratio) - 2.0
    print(f"Wrote {output.name}: 1200 x 936 pixels")
    print(f"Counts: {len(left)} + {len(right)} = 10; ratio = {ratio:g}; ln(4) = {np.log(ratio):.9f}")
    print(f"Neutral A->B at 300 K: {neutral / 1000:.6f} kJ/mol")
    print(f"z=+1, B->A, V(A)-V(B)=-60 mV: {ion / 1000:.6f} kJ/mol")
    print(f"Assumed active cycle budget: ln(4) - 2 = {budget:.9f} RT")


if __name__ == "__main__":
    main()
