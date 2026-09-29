"""Original critical-angle geometry; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes this script's basename.png to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def arrow(ax, start, end, color, style="-", width=2.7):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color=color, lw=width,
                                linestyle=style, mutation_scale=15))


def main():
    n1, n2 = 1.5, 1.0
    critical = np.degrees(np.arcsin(n2 / n1))
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 5.2), dpi=100)
    fig.patch.set_facecolor("white")
    fig.suptitle("Total internal reflection: the critical-angle transition", fontsize=17, y=0.97)
    colors = dict(incident="#285b94", reflected="#a54825", transmitted="#176b4d")
    headings = ["Just below critical", "At the critical angle", "Above critical"]
    angles = [40.0, critical, 50.0]
    for i, (ax, angle, heading) in enumerate(zip(axes, angles, headings)):
        theta = np.radians(angle)
        ax.set_aspect("equal")
        ax.set_xlim(-1.15, 1.15)
        ax.set_ylim(-1.15, 1.15)
        ax.set_facecolor("white")
        ax.axhspan(-1.15, 0, facecolor="#edf3fb", zorder=0)
        ax.axhline(0, color="#4e5965", lw=1.7)
        ax.plot([0, 0], [-1.04, 0.93], "--", color="#88919b", lw=1)
        ax.text(-1.07, 0.99, r"$n_2=1$", fontsize=12)
        ax.text(-1.07, -1.05, r"$n_1=1.5$", fontsize=12)
        start = (-np.sin(theta), -np.cos(theta))
        arrow(ax, start, (0, 0), colors["incident"])
        arrow(ax, (0, 0), (np.sin(theta), -np.cos(theta)), colors["reflected"])
        ax.add_patch(Arc((0, 0), 0.66, 0.66, theta1=270-angle, theta2=270,
                         color=colors["incident"], lw=1.1))
        ax.text(-0.29, -0.49, r"$\theta$", fontsize=13, color=colors["incident"])
        ax.text(0.56, -0.87, "reflected", color=colors["reflected"], fontsize=10, ha="center")
        ax.text(-0.7, -0.87, "incident", color=colors["incident"], fontsize=10, ha="center")
        if i == 0:
            transmitted = np.arcsin(n1 * np.sin(theta) / n2)
            arrow(ax, (0, 0), (1.03*np.sin(transmitted), 1.03*np.cos(transmitted)), colors["transmitted"])
            ax.text(0.49, 0.39, f"refracted\n{np.degrees(transmitted):.2f}°", color=colors["transmitted"],
                    fontsize=11, ha="center")
            detail = "Outgoing normal power is nonzero"
        elif i == 1:
            arrow(ax, (0, 0.018), (1.04, 0.018), colors["transmitted"])
            ax.text(0.58, 0.2, "grazing field", color=colors["transmitted"], fontsize=11, ha="center")
            ax.text(0.53, 0.55, r"$k_{2z}=0$", fontsize=13, color=colors["transmitted"], ha="center")
            detail = "Zero normal power; no decay in z"
        else:
            z = np.linspace(0, 0.85, 180)
            shade = np.ones((len(z), 30, 4))
            shade[:, :, :3] = [0.20, 0.65, 0.49]
            shade[:, :, 3] = 0.25*np.exp(-z[:, None]/0.17)
            ax.imshow(shade, extent=(-1.14, 1.14, 0, 0.85), origin="lower", aspect="equal", zorder=0)
            arrow(ax, (0.09, 0.10), (1.01, 0.10), colors["transmitted"])
            ax.text(0.18, 0.5, "evanescent field\ndecays away from face", fontsize=10.5,
                    color=colors["transmitted"], ha="center")
            ax.text(0.18, 0.84, r"$k_{2z}=i\kappa$", fontsize=13, color=colors["transmitted"], ha="center")
            detail = "Zero normal power; tangential flow"
        ax.set_title(heading + f"\nθ = {angle:.4f}°", fontsize=12, pad=12)
        ax.text(0.5, -0.08, detail, transform=ax.transAxes, fontsize=9.5, ha="center")
        ax.axis("off")
    fig.text(0.5, 0.085, "Arrows show directions, not relative powers. Shading above critical indicates decay, not a measured field.",
             fontsize=10, ha="center")
    fig.text(0.5, 0.038, "Constructed lossless, isotropic, nonmagnetic interface model • angles measured from the surface normal",
             fontsize=10, color="#505963", ha="center")
    fig.subplots_adjust(left=0.035, right=0.99, top=0.82, bottom=0.18, wspace=0.13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
