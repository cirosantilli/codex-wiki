"""Original functional schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media: python ../optical-tweezers-force-readout.py
The readout is a proposed calibration arrangement, not a historical reconstruction.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 6.0), facecolor="white")
    ax, flow = axes
    blue, red, green = "#2367a2", "#c04738", "#187b58"
    ax.set(xlim=(-2.8, 2.8), ylim=(-2.6, 3.3), aspect="equal")
    ax.axis("off")
    ax.set_title("A. Light changes momentum; the bead recoils", loc="left", pad=15)
    ax.axvline(0, color="0.75", ls="--", lw=1)
    ax.plot(0, 0.75, marker="+", ms=14, color="0.2")
    ax.text(0.12, 0.86, "beam focus", fontsize=10)
    ax.add_patch(Circle((0, -0.25), 0.85, fc="#e3f1f8", ec=blue, lw=2))
    # Trace a representative ray through a lossless sphere using Snell's law.
    # Lengths are arbitrary; the paraxial incident focus lies above the bead.
    center, radius = np.array([0.0, -0.25]), 0.85

    def hit(point, direction):
        offset = point - center
        b = offset @ direction
        disc = b * b - (offset @ offset - radius * radius)
        roots = [-b - np.sqrt(disc), -b + np.sqrt(disc)]
        return point + min(t for t in roots if t > 1e-8) * direction

    def refract(direction, normal, ratio):
        cosine = -normal @ direction
        return ratio * direction + (ratio * cosine - np.sqrt(1 - ratio ** 2 * (1 - cosine ** 2))) * normal

    incoming = np.array([-2.0, 2.9])
    direction = np.array([0.0, 0.75]) - incoming
    direction /= np.linalg.norm(direction)
    entry = hit(incoming, direction)
    inside = refract(direction, (entry - center) / radius, 1.33 / 1.60)
    leaving = hit(entry, inside)
    outgoing = refract(inside, -(leaving - center) / radius, 1.60 / 1.33)
    assert outgoing[1] < direction[1]  # More downward outgoing momentum: upward recoil.
    end = leaving + ((-2.05 - leaving[1]) / outgoing[1]) * outgoing
    for sign in (-1, 1):
        reflect = np.array([sign, 1])
        points = [reflect * p for p in (incoming, entry, leaving, end)]
        ax.plot(*zip(*points), color=blue, lw=2)
        for start, stop in [(points[0], points[0] + 0.5 * (points[1] - points[0])),
                            (points[2], points[3])]:
            ax.annotate("", stop, start, arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    ax.text(-2.55, 2.9, "incoming\nlight", color=blue, va="top")
    ax.text(0, -1.7, "outgoing light\n(more axial)", color=blue, fontsize=10, ha="center")
    ax.annotate("", (0, 0.57), (0, -0.18), arrowprops={"arrowstyle": "->", "lw": 3, "color": green})
    ax.text(1.25, 0.3, "backward\ngradient force", color=green, va="center")
    ax.annotate("", (0, -1.4), (0, -0.88), arrowprops={"arrowstyle": "->", "lw": 3, "color": red})
    ax.text(1.3, -1.1, "forward\nscattering force", color=red, va="center")
    ax.text(0, -2.52, "Ray picture: bead diameter ≫ wavelength\nNet force vanishes at a stable equilibrium", ha="center", fontsize=10)

    flow.set(xlim=(0, 10), ylim=(0, 10))
    flow.axis("off")
    flow.set_title("B. Hold, read position, then calibrate force", loc="left", pad=15)

    def box(x, y, w, h, label, color="0.25"):
        flow.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12", fc="white", ec=color, lw=1.6))
        flow.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=10, color=color)

    def arrow(start, end, color=blue):
        flow.annotate("", end, start, arrowprops={"arrowstyle": "->", "lw": 1.8, "color": color})

    box(1.5, 8.55, 7, 1.1, "Laser → beam expansion / steering")
    box(1.5, 6.8, 7, 1.05, "High-NA objective → bead in liquid")
    arrow((5, 8.4), (5, 8.0))
    box(0.35, 4.6, 4.0, 1.25, "Collected light\n→ quadrant photodiode")
    box(5.65, 4.6, 4.0, 1.25, "Image → camera\ncheck bead / wall height")
    arrow((3.1, 6.65), (2.35, 6.0))
    arrow((6.9, 6.65), (7.65, 6.0))
    box(0.35, 2.4, 4.0, 1.25, "Voltage V − V₀\nposition x = β(V − V₀)", green)
    box(5.65, 2.4, 4.0, 1.25, "Stage: fluid speed u\ndrag ζu = k⟨x⟩", green)
    arrow((2.35, 4.45), (2.35, 3.8), green)
    arrow((7.65, 4.45), (7.65, 3.8), green)
    box(1.5, 0.45, 7, 1.05, "Thermal spectrum / variance + drag check\nexternal force F = k⟨x⟩", red)
    arrow((2.35, 2.25), (3.1, 1.65), red)
    arrow((7.65, 2.25), (6.9, 1.65), red)
    fig.suptitle("Optical tweezers: forces and a proposed calibrated readout", fontsize=16, y=0.99)
    fig.text(0.5, 0.015, "Original functional diagram; paths and sizes are schematic. Panel B is not the 1986 apparatus.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.035, right=0.985, top=0.87, bottom=0.09, wspace=0.16)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
