"""Original permanent-dipole energy plot; output PNG basename in cwd.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Dependencies are declared in the repository's top-level pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, 2 * np.pi, 500)
    fig, ax = plt.subplots(figsize=(7.2, 4.4), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.plot(theta, -np.cos(theta), color="#2463a5", lw=2.5)
    ax.axhline(0, color="#aaaaaa", lw=0.8)
    ax.plot([0, np.pi, 2 * np.pi], [-1, 1, -1], "o", color="black", ms=4)
    ax.annotate("Aligned: stable", xy=(0, -1), xytext=(0.50, 0.40),
                fontsize=10, arrowprops={"arrowstyle": "->"})
    ax.annotate("Anti-aligned: unstable", xy=(np.pi, 1),
                xytext=(np.pi, 0.38), ha="center", fontsize=10,
                arrowprops={"arrowstyle": "->"})
    ax.text(4.8, 0.78, r"$U=-mB\cos\theta$", fontsize=12)
    ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                  ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax.set_yticks([-1, 0, 1])
    ax.set(xlabel=r"Angle $\theta$ between $\mathbf{m}$ and $\mathbf{B}$",
           ylabel=r"Potential energy $U/(mB)$",
           title="Magnetic dipole orientation energy",
           xlim=(-0.10, 2 * np.pi + 0.10), ylim=(-1.25, 1.25))
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=145,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
