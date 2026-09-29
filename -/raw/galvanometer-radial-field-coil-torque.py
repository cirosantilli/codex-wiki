"""Draw a moving-coil force couple; Python 3.14, matplotlib 3.10.7, NumPy 2.3.5."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Wedge
import numpy as np


def arrow(ax, start, end, color, width=2.0, style="-|>"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                mutation_scale=15, linewidth=width, color=color))


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, notes) = plt.subplots(1, 2, figsize=(9.2, 4.9),
                                  gridspec_kw={"width_ratios": [1.5, 1]})
    blue, red, green = "#2166ac", "#b2182b", "#397343"
    ax.set_aspect("equal")
    ax.set_xlim(-2.35, 2.35)
    ax.set_ylim(-1.95, 2.05)
    ax.axis("off")
    for label, angles, color in [("N", (145, 215), "#f4ddd7"),
                                  ("S", (-35, 35), "#dce8f4")]:
        ax.add_patch(Wedge((0, 0), 1.9, *angles, width=0.63,
                           facecolor=color, edgecolor="#555555", linewidth=1.5))
        ax.text(-1.60 if label == "N" else 1.60, 0, label,
                ha="center", va="center", fontsize=18, weight="bold")
    ax.add_patch(Circle((0, 0), 0.70, facecolor="#ededed",
                        edgecolor="#777777", linewidth=1.4))
    ax.text(0, -0.30, "fixed iron\ncore", ha="center", va="center")
    ax.plot(0, 0, "k.", ms=7)
    alpha = np.deg2rad(20)
    radial = np.array([np.cos(alpha), np.sin(alpha)])
    tangent = np.array([-np.sin(alpha), np.cos(alpha)])
    # Left gap: N -> core; right gap: core -> S. Both local B vectors
    # point along +radial, though one is inward and the other outward.
    for degrees in [-24, 0, 24]:
        e = np.array([np.cos(np.deg2rad(degrees)), np.sin(np.deg2rad(degrees))])
        arrow(ax, -1.23 * e, -0.76 * e, blue, width=1.6)
        arrow(ax, 0.76 * e, 1.23 * e, blue, width=1.6)
    left, right = -1.06 * radial, 1.06 * radial
    ax.plot([left[0], right[0]], [left[1], right[1]], "--",
            color="#7b4b18", linewidth=2.1)
    for position, sign in [(left, -1), (right, 1)]:
        ax.add_patch(Circle(position, 0.095, facecolor="white",
                            edgecolor="#7b4b18", linewidth=2, zorder=5))
        ax.text(*position, "×" if sign == -1 else "•", ha="center", va="center",
                color="#7b4b18", fontsize=14, zorder=6)
        arrow(ax, position + sign * 0.13 * tangent,
              position + sign * 0.90 * tangent, red)
    ax.text(-1.0, -1.38, r"$F=N I\ell B$", color=red, ha="center")
    ax.text(1.04, 1.36, r"$F=N I\ell B$", color=red, ha="center")
    ax.text(-1.98, 1.34, "shaped poles", ha="left", fontsize=10)
    ax.text(0.55, -1.40, "coil-plane projection\n(dashed, not a wire\nthrough the core)",
            ha="center", fontsize=9.5, color="#7b4b18")
    ax.text(-0.30, 1.73, "positive rotation ↺", color=red, ha="center")
    ax.add_patch(FancyArrowPatch((1.46, 0.10), (0.74, 1.27),
                                connectionstyle="arc3,rad=0.24", arrowstyle="-|>",
                                color=red, linewidth=2, mutation_scale=15))
    ax.add_patch(FancyArrowPatch((-0.36, 0.43), (0.41, 0.33),
                                connectionstyle="arc3,rad=-0.6", arrowstyle="-|>",
                                color=green, linewidth=1.8, mutation_scale=13))
    notes.axis("off")
    notes.text(0.02, 0.94, "Top view along the rotation axis", fontsize=12, weight="bold")
    notes.text(0.02, 0.87, "⊙ current out of page\n⊗ current into page\nActive wire length ℓ: along the axis",
               linespacing=1.6, color="#7b4b18", va="top")
    notes.text(0.02, 0.55, "Local gap field B", color=blue, weight="bold")
    notes.text(0.02, 0.47, "Side forces form a couple", color=red, weight="bold")
    notes.text(0.02, 0.39, "Restoring spring torque ↻", color=green, weight="bold")
    notes.text(0.02, 0.29, r"$A=w\ell$" "\n" r"$\tau_{\rm m}=N I\ell B\,w=NIAB$"
               "\n" r"$\tau_{\rm s}=-k\theta$" "\n" r"$\theta=NIAB/k$ at rest", linespacing=1.6, va="top")
    fig.suptitle("Moving coil in a radial working-gap field", fontsize=15)
    fig.text(0.5, 0.025, "Schematic only • reverse I to reverse both forces and deflection • flux return path omitted",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.99, top=0.88, bottom=0.12, wspace=0.08)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
