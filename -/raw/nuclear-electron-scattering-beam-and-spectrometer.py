"""Functional scattering schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; emits an opaque PNG with this script's basename.
Historical architecture: Hofstadter, Rev. Mod. Phys. 28 (1956), Figs. 14–17.
The two views deliberately separate scattering angle from magnetic bending.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Rectangle


def arrow(ax, start, end, color="#236aaf", **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=14, linewidth=2, color=color,
                                **kwargs))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11.2, 6.2), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[4, 1])
    left = fig.add_subplot(grid[0, 0])
    right = fig.add_subplot(grid[0, 1])
    for ax in (left, right):
        ax.set_aspect("equal")
        ax.axis("off")
    left.set(xlim=(-3.7, 3.8), ylim=(-1.25, 4.1))
    left.set_title("Choose the scattering angle\n(horizontal plane)", pad=14)
    arrow(left, (-3.4, 0), (-0.12, 0))
    left.text(-2.25, 0.22, "Selected electron beam", ha="center")
    left.text(-2.25, -0.4, "Linear accelerator → slits / magnets", ha="center", fontsize=9)
    left.add_patch(Circle((0, 0), 0.13, color="#bf4938"))
    left.text(-0.05, -0.38, "Target", ha="center")
    left.add_patch(Circle((0, 0), 0.63, fill=False, edgecolor="#8d9aa4", linestyle="--"))
    arrow(left, (0.16, 0), (3.1, 0), color="#77838b")
    left.add_patch(Rectangle((2.8, -0.18), 0.12, 0.36, color="#77838b"))
    left.text(2.1, -0.55, "Beam monitor", ha="center")
    theta = np.deg2rad(80)
    end = 3 * np.array([np.cos(theta), np.sin(theta)])
    arrow(left, (0.08*np.cos(theta), 0.08*np.sin(theta)), end)
    left.add_patch(Arc((0, 0), 2.25, 2.25, theta1=0, theta2=80, color="#bf4938"))
    left.text(1.1, 0.73, r"$\theta$", color="#bf4938", fontsize=15)
    left.text(1.15, 2.9, "Entrance slit →", ha="left")
    left.text(-0.35, 1.9, "Scattered\nelectron", ha="right")
    left.text(0.7, 3.7, "Rotate the spectrometer about the target", ha="center", fontsize=10)
    right.set(xlim=(-2.5, 3.4), ylim=(-0.9, 4.1))
    right.set_title("Select the outgoing momentum\n(vertical bending plane)", pad=14)
    right.add_patch(Rectangle((-1.9, 0.65), 3.8, 2.4, facecolor="#e4eef6", edgecolor="#8cacc7"))
    phi = np.linspace(np.pi, 0, 200)
    right.plot(1.5*np.cos(phi), 1+1.5*np.sin(phi), color="#236aaf", linewidth=2.5)
    arrow(right, (-1.5, -0.25), (-1.5, 1.0))
    arrow(right, (1.5, 1.0), (1.5, -0.25))
    arrow(right, (-0.15, 2.49), (0.15, 2.49))
    right.text(0, 1.35, "Magnetic field\nnormal to this view", ha="center")
    right.text(0, 0.82, r"$p'\simeq eBr_b$", ha="center", fontsize=13)
    right.text(0, 3.35, "180° bend ≠ scattering angle", ha="center", color="#bf4938")
    right.text(-1.5, -0.57, "Entrance", ha="center")
    right.text(1.5, -0.57, "Exit slit", ha="center")
    right.text(2.15, 0.12, "To shielded\ncounter", fontsize=10)
    foot = fig.add_subplot(grid[1, :])
    foot.axis("off")
    foot.text(0.5, 0.78, "Scan magnet setting → count / monitor charge → isolate elastic peak → vary θ",
              ha="center", va="center", fontsize=12)
    foot.text(0.5, 0.23, "Functional schematic, not to scale. Views are separate; field and orbit formula are locally idealized.",
              ha="center", va="center", fontsize=10, color="#47545f")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
