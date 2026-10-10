"""Original collision directions and momentum closure; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch, Rectangle
import numpy as np


def arrow(ax, start, end, color, style="-", width=2.4):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15,
                                lw=width, color=color, linestyle=style, zorder=3))


def main():
    e = 70.0
    ep = e / (1 + e / 511.0)
    phi = np.degrees(np.arctan2(ep, e))
    blue, orange, red = "#126f9b", "#a64e16", "#a82d47"
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.4, 6.2),
                                     gridspec_kw={"width_ratios": [1.15, 1]})
    fig.subplots_adjust(left=0.025, right=0.975, top=0.86, bottom=0.16, wspace=0.16)
    fig.patch.set_facecolor("white")
    fig.suptitle("Compton scattering at θ = 90°: direction and momentum", fontsize=15)
    left.set_title("Collision plane (ray lengths schematic)", fontsize=12)
    left.set(xlim=(-3.8, 3.9), ylim=(-3.25, 3.45), aspect="equal")
    left.axis("off")
    arrow(left, (-0.4, 0), (3.65, 0), "#b0b0b0", width=1)
    arrow(left, (0, -2.8), (0, 3.1), "#b0b0b0", width=1)
    left.text(3.68, 0.12, "+x", fontsize=10)
    left.text(0.13, 2.94, "+y", fontsize=10)
    left.add_patch(Rectangle((-3.7, -0.45), 1.1, 0.9, fc="#edf3f6", ec=blue))
    left.text(-3.15, 0, "Photon\nsource", ha="center", va="center", fontsize=10)
    arrow(left, (-2.6, 0), (0, 0), blue)
    left.text(-2.45, 0.28, "Incident photon\nE = 70 keV", color=blue, fontsize=11)
    left.scatter([0], [0], s=90, color="#333333", zorder=5)
    left.text(-0.2, -0.70, "Electron initially at rest", ha="right", fontsize=10)
    arrow(left, (0, 0), (0, 2.6), orange)
    left.text(0.45, 2.0, "Outgoing photon\nE′ = 61.566 keV", color=orange, fontsize=11)
    recoil_end = (2.8, -2.8 * ep / e)
    arrow(left, (0, 0), recoil_end, red)
    left.text(1.05, -2.9, "Recoiling electron\nTₑ = 8.434 keV", color=red, fontsize=11)
    left.add_patch(Arc((0, 0), 1.5, 1.5, theta1=0, theta2=90, color=orange))
    left.text(0.72, 0.7, "θ = 90°", color=orange, fontsize=11)
    left.add_patch(Arc((0, 0), 2.0, 2.0, theta1=-phi, theta2=0, color=red))
    left.text(1.05, -0.53, f"φ = {phi:.2f}°", color=red, fontsize=11)
    right.set_title("Momentum closure (equal axis scales)", fontsize=12)
    right.set(xlim=(-10, 96), ylim=(-80, 29), aspect="equal",
              xlabel="c pₓ (keV)", ylabel="c pᵧ (keV)")
    right.axhline(0, color="#bbbbbb", lw=0.9)
    right.axvline(0, color="#bbbbbb", lw=0.9)
    right.grid(alpha=0.2)
    right.spines[["top", "right"]].set_visible(False)
    arrow(right, (0, 0), (e, 0), blue)
    # The full outgoing momentum is translated to the electron-vector tip.
    arrow(right, (0, 0), (e, -ep), red)
    arrow(right, (e, -ep), (e, 0), orange)
    right.plot([0, e], [-ep, -ep], "--", color="#bbbbbb", lw=1)
    right.text(31, 5, "c p = (70, 0)", color=blue, fontsize=11)
    right.text(73, -34, "c p′", color=orange, fontsize=11)
    right.text(5, 16, "c p′ = (0, 61.566) keV", color=orange, fontsize=10)
    right.text(7, -37, "c pₑ", color=red, fontsize=11)
    right.text(33, -73, "c pₑ = (70, −61.566) keV", color=red, fontsize=10, ha="center")
    fig.supxlabel("E = 70 keV; mₑc² = 511 keV • p = pₑ + p′\n"
                  "Original free-electron model schematic; no experimental data", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
