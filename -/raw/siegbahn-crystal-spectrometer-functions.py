"""Original functional diagram, not a historical apparatus reconstruction.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes the matching PNG in the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyBboxPatch, Rectangle
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 11), ylim=(0, 6.2))
    ax.axis("off")
    blue, red, grey = "#176b9c", "#b44724", "#626b75"
    ax.text(5.5, 5.94, "Crystal spectroscopy: turn an angle into a wavelength",
            ha="center", fontsize=16, weight="bold")
    ax.text(5.5, 5.58, "Functional diagram • arbitrary geometry • no historical dimensions",
            ha="center", fontsize=11, color=grey)
    ax.add_patch(FancyBboxPatch((1.85, 1.55), 8.75, 3.6,
                 boxstyle="round,pad=0.08", facecolor="#f6fafc", edgecolor=grey,
                 linestyle="--", linewidth=1.5))
    ax.text(2.05, 4.86, "Evacuated beam path", fontsize=12, color=blue)
    ax.add_patch(Rectangle((0.18, 2.15), 1.35, 1.05, facecolor="#f6e4da", edgecolor=red))
    ax.text(0.855, 2.68, "X-ray tube\ntarget", ha="center", va="center", fontsize=11)
    cx, cy = 5.65, 2.65
    ax.annotate("", (cx, cy), (1.53, cy), arrowprops=dict(arrowstyle="->", lw=2.4, color=blue))
    for x in (2.6, 3.75):
        for y in (2.13, 2.79):
            ax.add_patch(Rectangle((x, y), 0.12, 0.38, facecolor=grey))
    ax.text(3.22, 1.88, "Collimating slits", ha="center", fontsize=11)
    theta = np.deg2rad(25)
    v = np.array([np.cos(theta), np.sin(theta)])
    normal = np.array([-np.sin(theta), np.cos(theta)])
    center = np.array([cx, cy])
    for shift in (-0.10, 0, 0.10):
        ends = [center - 0.9*v + shift*normal, center + 0.9*v + shift*normal]
        ax.plot(*np.array(ends).T, color=red, lw=2)
    ax.text(6.2, 1.98, "Rotatable crystal\nplane spacing d", ha="center", fontsize=11, color=red)
    out = center + 3*np.array([np.cos(2*theta), np.sin(2*theta)])
    ax.annotate("", out, center, arrowprops=dict(arrowstyle="->", lw=2.4, color=blue))
    ax.plot([cx, cx+1.35], [cy, cy], "--", color=grey, lw=1)
    ax.add_patch(Arc(center, 2.0, 2.0, theta1=0, theta2=25, color=red, lw=1.7))
    ax.text(cx+1.06, cy+0.13, r"$\theta$", color=red, fontsize=14)
    ax.add_patch(Arc(center, 2.7, 2.7, theta1=0, theta2=50, color=blue, lw=1.4))
    ax.text(cx+1.35, cy+0.60, r"$2\theta$", color=blue, fontsize=14)
    ax.add_patch(Rectangle((out[0]-0.45, out[1]-0.22), 0.9, 0.40,
                          facecolor="#dae9e1", edgecolor="#367659"))
    ax.text(8.85, 4.72, "Readout position\nphotographic plate", ha="center", fontsize=11)
    ax.annotate("", out+[0.22, 0.12], (8.1, 4.54), arrowprops=dict(arrowstyle="-", color=grey))
    ax.text(8.85, 3.45, "A scanning ionization\nchamber is an alternative\nreadout, not an extra\nserial optical element.",
            ha="center", va="center", fontsize=10, color="#367659")
    ax.text(2.7, 0.92, "Angle scale + zero checks\nTemperature fixes d", ha="center", fontsize=11)
    ax.text(7.9, 0.92, "Record line positions, then apply\nBragg's law and refraction correction", ha="center", fontsize=11)
    ax.text(5.5, 0.19, r"$n\lambda=2d\sin\theta$   •   $\theta$ is measured from the planes, not their normal",
            ha="center", fontsize=12)
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.015, top=0.985)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
