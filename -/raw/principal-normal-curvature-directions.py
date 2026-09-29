"""Original Euler normal-curvature graphs; run from _media for the PNG.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
S = -dN; theta is measured from the first indicated principal direction.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    theta = np.linspace(0, np.pi, 721)
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 4.2), layout="constrained",
                             sharex=True, sharey=True)
    fig.suptitle(r"Normal curvature by tangent direction: $S=-dN$" + "\n" +
                 r"$k_n(\theta)=k_1\cos^2\theta+k_2\sin^2\theta$", fontsize=15)
    models = [
        ("Sphere · outward · R = 1", -1, -1, "Any first direction", r"$k_n=-1$", "#28789d"),
        ("Cylinder · outward · R = 1", -1, 0, "First direction: circumferential", r"$k_n=-\cos^2\theta$", "#b27825"),
        ("Saddle · upward · origin", 1, -1, "First direction: x-axis", r"$k_n=\cos(2\theta)$", "#7859a1"),
    ]
    for ax, (name, k1, k2, direction, formula, color) in zip(axes, models):
        values = k1 * np.cos(theta)**2 + k2 * np.sin(theta)**2
        ax.axhline(0, color="#67727e", lw=1)
        ax.axhline((k1 + k2) / 2, color="#ad3940", ls="--", lw=1.5,
                   label="Mean curvature H")
        ax.plot(theta, values, color=color, lw=2.8, label="Normal curvature")
        principal_angles = np.array([0, np.pi / 2, np.pi])
        principal_values = k1 * np.cos(principal_angles)**2 + k2 * np.sin(principal_angles)**2
        ax.scatter(principal_angles, principal_values, s=40, color=color, zorder=5)
        ax.set_title(name + "\n" + formula, fontsize=11.5, pad=10)
        ax.text(0.5, 0.97, direction, transform=ax.transAxes, ha="center",
                va="top", fontsize=9)
        ax.set_xlabel(r"Tangent-plane angle $\theta$")
        ax.set(xlim=(-0.08, np.pi + 0.08), ylim=(-1.22, 1.3))
        ax.set_xticks([0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi],
                      ["0", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
        ax.set_yticks([-1, -0.5, 0, 0.5, 1])
        ax.grid(alpha=0.22)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Signed normal curvature (inverse length)")
    axes[2].scatter([np.pi / 4, 3 * np.pi / 4], [0, 0], marker="o",
                    facecolors="white", edgecolors="#7859a1", s=50, zorder=6)
    axes[2].annotate("Zero normal curvature", (np.pi / 4, 0),
                     xytext=(0.07, -0.34), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "#7859a1"})
    handles, labels = axes[1].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=2,
               frameon=False, fontsize=10)
    output = Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=125, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
