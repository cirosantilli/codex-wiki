"""Original linear gravitational-wave ring distortions; write PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
Proper-frame displacement is (I-h/2) times the fixed TT coordinate vector,
using the +--- background signature. The illustrated amplitude is 0.2.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, 2*np.pi, 361)
    ring = np.array([np.cos(theta), np.sin(theta)])
    particles = np.array([np.cos(theta[::20]), np.sin(theta[::20])])
    amplitude = .2
    tensors = (np.diag([1., -1.]), np.array([[0., 1.], [1., 0.]]))
    colors = ("#1768ab", "#bd6426")
    fig, axes = plt.subplots(2, 3, figsize=(8.7, 5.4), facecolor="white")
    for row, tensor in enumerate(tensors):
        for col, phase in enumerate((1, 0, -1)):
            ax = axes[row, col]
            transform = np.eye(2) - amplitude*phase*tensor/2
            deformed = transform @ ring
            dots = transform @ particles
            ax.plot(*ring, lw=1, ls="--", color="#aeb7bf")
            ax.plot(*deformed, lw=1.5, color=colors[row])
            ax.scatter(*dots, s=13, color=colors[row], zorder=3)
            ax.axhline(0, lw=.5, color="#c9ced3", zorder=0)
            ax.axvline(0, lw=.5, color="#c9ced3", zorder=0)
            ax.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), aspect="equal")
            ax.set_xticks([-1, 0, 1])
            ax.set_yticks([-1, 0, 1])
            mode = "Plus" if row == 0 else "Cross"
            ax.set_title(mode + rf": $\cos\Psi={phase:+d}$", fontsize=10.5)
            ax.spines[["top", "right"]].set_visible(False)
            if row == 1:
                ax.set_xlabel(r"Proper-frame $X/L$")
            if col == 0:
                ax.set_ylabel(r"Proper-frame $Y/L$")
    fig.tight_layout(h_pad=1.1, w_pad=1.2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
