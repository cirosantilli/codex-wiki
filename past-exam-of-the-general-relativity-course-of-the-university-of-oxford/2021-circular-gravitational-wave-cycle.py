"""Generate the 2021 Q2(c) periodic physical-separation sketch (Python 3.14)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    strain = 0.30
    initial = np.array([[1., 0.], [0., 1.], [-1., 0.], [0., -1.]])
    colors = ["#bf3d32", "#2166ac", "#bf3d32", "#2166ac"]
    phases = np.linspace(0., 2*np.pi, 9)
    fig, axes = plt.subplots(3, 3, figsize=(9, 8.6), facecolor="white")
    for j, (ax, phase) in enumerate(zip(axes.flat, phases)):
        h = strain*np.array([[-np.cos(phase), -np.sin(phase)],
                             [-np.sin(phase), np.cos(phase)]])
        h0 = strain*np.diag([-1., 1.])
        moved = initial + initial @ (h-h0).T/2
        ax.axhline(0, color="0.86", lw=0.7)
        ax.axvline(0, color="0.86", lw=0.7)
        ax.plot(*initial.T, linestyle="none", marker="o", mfc="white",
                mec="0.5", ms=7, zorder=2)
        for p, dest, color in zip(initial, moved, colors):
            ax.annotate("", xy=dest, xytext=p,
                        arrowprops={"arrowstyle": "->", "color": color, "lw": 1.5})
            ax.scatter(*dest, color=color, s=30, zorder=4)
        outline = moved[[0, 1, 2, 3, 0]]
        ax.plot(*outline.T, color="#6a51a3", alpha=.6, lw=1)
        ax.set(xlim=(-1.55, 1.55), ylim=(-1.55, 1.55), aspect="equal",
               xticks=[-1, 0, 1], yticks=[-1, 0, 1])
        ax.set_title(rf"$t/T_{{\rm wave}}={j}/8$", fontsize=12)
        ax.tick_params(labelsize=9)
        if j >= 6:
            ax.set_xlabel(r"$x/a$", fontsize=11)
        if j % 3 == 0:
            ax.set_ylabel(r"$y/a$", fontsize=11)
    fig.suptitle("Four free particles in a circularly polarized gravitational wave", fontsize=14, y=.99)
    fig.text(.5, .025,
             "Open circles: positions at t = 0.  Filled points: periodic response.\n"
             "Strain H = 0.30 exaggerates the first-order motion; initial velocities select bounded motion.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .07, 1, .965))
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=125, facecolor="white", transparent=False,
                metadata={"Software": "codex-wiki figure generator"})
    plt.close(fig)


if __name__ == "__main__":
    main()
