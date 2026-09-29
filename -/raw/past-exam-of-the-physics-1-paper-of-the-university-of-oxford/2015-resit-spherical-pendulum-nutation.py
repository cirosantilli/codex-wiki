"""Original conical-pendulum geometry and nutation ratio. Python 3.14,
NumPy 2.3.5, Matplotlib 3.10.7; writes only the same-basename CWD PNG.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Ellipse
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, orange, green, gray = "#126782", "#b55d15", "#287d53", "#596672"
    fig, (sketch, ax) = plt.subplots(1, 2, figsize=(10.8, 5.9), gridspec_kw={"width_ratios": (1, 1.1)})
    angle, length, pivot = np.radians(40), 2.1, np.array([0.0, 1.0])
    bob = pivot + length * np.array([np.sin(angle), -np.cos(angle)])
    sketch.plot([-0.45, 0.45], [1.03, 1.03], color=gray, lw=4)
    sketch.plot([0, 0], [1, -1.4], color=gray, lw=1, ls="--")
    sketch.add_patch(Ellipse((0, bob[1]), 2 * bob[0], 0.43,
                             facecolor="#edf5f8", edgecolor=blue, lw=1.4, ls="--"))
    sketch.plot([0, bob[0]], [1, bob[1]], color=blue, lw=2.4)
    sketch.scatter([0], [1], color=gray, s=35, zorder=5)
    sketch.scatter([bob[0]], [bob[1]], color=blue, s=130, zorder=5)
    sketch.add_patch(Arc(pivot, 1.1, 1.1, theta1=270, theta2=310, color=orange, lw=1.5))
    sketch.text(0.22, 0.31, r"$\theta_0$", color=orange, fontsize=16)
    sketch.text(0.82, 0.36, r"$l$", color=blue, fontsize=17)
    sketch.text(bob[0] + 0.14, bob[1] + 0.06, r"$m$", fontsize=15, color=blue)
    sketch.text(-0.12, -1.46, "Downward vertical", ha="center", color=gray, fontsize=11)
    sketch.annotate("", (bob[0], bob[1] - 0.75), (bob[0], bob[1] - 0.13),
                    arrowprops={"arrowstyle": "->", "color": gray, "lw": 1.5})
    sketch.text(bob[0] + 0.13, bob[1] - 0.52, r"$mg$", color=gray)
    sketch.text(-1.35, bob[1] + 0.32, r"Horizontal orbit: $\dot\phi=\Omega$", color=blue, fontsize=11)
    sketch.text(-0.92, 0.72, "Fixed pivot", color=gray, fontsize=11)
    sketch.set(xlim=(-1.7, 1.95), ylim=(-1.75, 1.4), aspect="equal", title="Steady conical motion (schematic)")
    sketch.set_axis_off()
    theta = np.linspace(0, 90, 900)
    ratio = np.sqrt(1 + 3 * np.cos(np.radians(theta)) ** 2)
    ax.plot(theta, ratio, color=green, lw=2.5)
    ax.scatter([0, 90], [2, 1], facecolors="white", edgecolors=green, s=60, lw=1.5, zorder=4)
    ax.text(7, 1.13, r"$0<\theta_0<90^\circ$", color=green, fontsize=13)
    ax.text(3, 1.60, "Small nonzero cone\nlimit: ratio 2", color=gray, fontsize=10)
    ax.text(55, 1.65, "Nearly horizontal\nlimit: ratio 1", color=gray, fontsize=10)
    ax.set(xlim=(-3, 93), ylim=(0.95, 2.08), xticks=(0, 15, 30, 45, 60, 75, 90),
           yticks=(1, 1.25, 1.5, 1.75, 2), xlabel=r"Steady polar angle $\theta_0$ (degrees)",
           ylabel=r"Frequency ratio $\omega_\theta/|\Omega|$", title="Small polar oscillations at fixed h")
    ax.grid(alpha=0.16)
    fig.suptitle("Spherical pendulum: conical rotation and small nutations", fontsize=17, y=0.97)
    fig.text(0.5, 0.14,
             r"$h=ml^2\sin^2\theta\,\dot\phi$ is conserved; $\dot\phi$ changes during a polar oscillation.",
             ha="center", fontsize=13)
    fig.text(0.5, 0.065,
             r"$\Omega^2=\frac{g}{l\cos\theta_0}$,  $\omega_\theta^2=\Omega^2(1+3\cos^2\theta_0)$;  $\theta=\theta_0+\alpha(t)$.",
             ha="center", fontsize=14)
    fig.text(0.5, 0.018, "Open endpoints show limits of the nontrivial conical family.",
             ha="center", fontsize=10, color=gray)
    fig.subplots_adjust(left=0.035, right=0.975, bottom=0.28, top=0.84, wspace=0.27)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
