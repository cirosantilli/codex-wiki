"""Functional DIS readout, not an engineering drawing. Python 3.14; matplotlib 3.10.7.

Run from _media; writes this script's basename with a .png extension to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 6.6), dpi=120, facecolor="white")
    ax = fig.add_axes([0.025, 0.30, 0.95, 0.60])
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    blue, orange, grey = "#176eac", "#b64c10", "#56616a"
    fig.suptitle("From an outgoing electron to proton kinematics", fontsize=17, y=0.97)
    fig.text(0.5, 0.915, "Functional schematic • geometry exaggerated • not to scale", ha="center", color=grey)

    def arrow(start, end, color=blue, **kwargs):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15,
                                    linewidth=2, color=color, **kwargs))

    arrow((0.15, 1.5), (2.65, 1.5))
    ax.text(0.3, 1.85, "Incident electron beam\nknown energy $E$", color=blue)
    ax.add_patch(FancyBboxPatch((2.65, 1.0), 0.65, 1.0, boxstyle="round,pad=0.08",
                               facecolor="#dceff4", edgecolor=blue, linewidth=1.5))
    ax.text(2.98, 0.8, "Liquid hydrogen\nproton target", ha="center", va="top")
    ax.plot([3.3, 5.4], [1.5, 1.5], "--", color="#aeb7bd", lw=1)
    arrow((3.05, 1.6), (5.8, 3.1))
    ax.text(3.65, 3.0, "Scattered electron\n$E'$, $p'$, angle $\\theta$", color=blue)
    ax.add_patch(Arc((3.05, 1.5), 2.6, 2.6, theta1=0, theta2=29, color=grey, lw=1.4))
    ax.text(4.4, 1.85, "$\\theta$", fontsize=16)
    arrow((3.1, 1.35), (5.2, 0.45), color=grey, linestyle="--")
    ax.text(5.25, 0.45, "Hadronic state $X$\nunobserved", color=grey, va="center")
    ax.add_patch(FancyBboxPatch((5.8, 2.6), 1.5, 1.35, boxstyle="round,pad=0.08",
                               facecolor="#fff0e4", edgecolor=orange, linewidth=1.5))
    ax.text(6.55, 4.2, "Magnetic analysis", color=orange, ha="center")
    ax.text(6.55, 3.65, "$B$", color=orange, ha="center", fontsize=15)
    for start_y, end_y in [(3.04, 3.2), (3.1, 3.5), (3.16, 3.8)]:
        arrow((5.9, start_y), (8.1, end_y), connectionstyle="arc3,rad=-0.12", color=orange)
    ax.plot([8.2, 8.2], [2.95, 4.1], color=grey, lw=5)
    ax.text(8.45, 3.55, "Focal-plane\nreadout", va="center")
    ax.text(6.8, 2.05, "Momentum dispersion\nand angle selection", ha="center", color=orange)

    fig.text(0.5, 0.255, "Count electrons in momentum and angle bins", ha="center", fontsize=13, weight="bold")
    fig.text(0.5, 0.205, "Acceptance + normalization + radiative corrections", ha="center")
    fig.text(0.5, 0.145, "$E, E', \\theta \\quad \\longrightarrow \\quad Q^2, x, W^2 \\quad \\longrightarrow \\quad F_1, F_2$",
             ha="center", fontsize=16, color=blue)
    fig.text(0.5, 0.065, "$Q^2=4EE'\\sin^2(\\theta/2)$     $x=Q^2/[2M(E-E')]$     $W^2=M^2+2M(E-E')-Q^2$",
             ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
