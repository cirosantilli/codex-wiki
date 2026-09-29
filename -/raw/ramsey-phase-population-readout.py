"""Draw ideal Ramsey phase-to-population conversion with inverse y pulses.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; writes ramsey-phase-population-readout.png to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10.8, 6.2))
    fig.suptitle("Ideal Ramsey readout: convert relative phase into population",
                 fontsize=15, y=0.965)
    sequence = fig.add_axes([0.03, 0.67, 0.94, 0.22])
    sequence.set(xlim=(0, 1), ylim=(0, 1))
    sequence.axis("off")
    stages = [(0.015, 0.12, "Prepare", r"$|0\rangle$", "#eef1f4"),
              (0.18, 0.15, "First pulse", r"$R_y(\pi/2)$", "#e7dff0"),
              (0.375, 0.20, "Free interval", r"$U_\phi=e^{-i\phi\sigma_z/2}$", "#f7e7cc"),
              (0.62, 0.16, "Analysis pulse", r"$R_y(-\pi/2)$", "#e7dff0"),
              (0.825, 0.16, "Read population", r"$0$ or $1$", "#daedf0")]
    for x, width, heading, formula, color in stages:
        sequence.add_patch(FancyBboxPatch((x, 0.32), width, 0.46,
                          boxstyle="round,pad=0.008,rounding_size=0.025",
                          facecolor=color, edgecolor="#8f9aa5"))
        sequence.text(x + width / 2, 0.63, heading, ha="center", fontsize=10)
        sequence.text(x + width / 2, 0.43, formula, ha="center", fontsize=12)
    for (x, width, *_), (next_x, *_) in zip(stages, stages[1:]):
        sequence.annotate("", xy=(next_x - 0.01, 0.55), xytext=(x + width + 0.01, 0.55),
                          arrowprops={"arrowstyle": "->", "color": "#4c5864", "lw": 1.6})
    sequence.text(0.285, 0.07, r"creates $|+\rangle$", ha="center", fontsize=10)
    sequence.text(0.48, 0.07, r"$P_Z(0)=P_Z(1)=1/2$", ha="center", fontsize=10)
    sequence.text(0.9, 0.07, r"$P(0)\ne P(1)$ in general", ha="center", fontsize=10)
    ax = fig.add_axes([0.085, 0.19, 0.59, 0.40])
    phase = np.linspace(0, 2 * np.pi, 501)
    ax.plot(phase, np.cos(phase / 2) ** 2, color="#7346a5", lw=2.5,
            label=r"$P(0)=\cos^2(\phi/2)$")
    ax.plot(phase, np.sin(phase / 2) ** 2, color="#147c96", lw=2.5,
            label=r"$P(1)=\sin^2(\phi/2)$")
    ax.axhline(0.5, color="#606b75", ls="--", lw=1.6,
               label="Without analysis pulse: both 1/2")
    phi_example = 2 * np.pi / 3
    ax.axvline(phi_example, color="#a1adb8", lw=1, ls=":")
    ax.scatter([phi_example, phi_example], [0.25, 0.75],
               c=["#7346a5", "#147c96"], s=40, zorder=5)
    ax.set(xlim=(0, 2 * np.pi), ylim=(-0.035, 1.035),
           xlabel=r"Relative phase $\phi$ (e.g. $\delta T$ in the rotating frame)",
           ylabel="Probability")
    ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                  ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.grid(alpha=0.18)
    ax.legend(loc="upper left", bbox_to_anchor=(1.03, 1.02), frameon=False, fontsize=10)
    fig.text(0.72, 0.32, r"$\phi=2\pi/3$" + "\n\n$P(0)=1/4$\n$P(1)=3/4$",
             fontsize=13, ha="left", va="center")
    fig.text(0.5, 0.065, "Perfect instantaneous pulses • noiseless free interval • exact model, not measured data",
             ha="center", color="#4c5864", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
