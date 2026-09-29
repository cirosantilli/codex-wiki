"""Original square-root length and quadratic time scales; run from _media. Tested with Python 3.14."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    times = np.linspace(0, 40, 501)
    lengths = np.geomspace(1e-3, 2e-2, 301)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), layout="constrained")
    fig.suptitle("Diffusion length and time are scales, not sharp arrival thresholds", fontsize=14)
    for alpha, color, letter in zip((2e-6, 5e-7), ("#196ca3", "#bf5620"), ("A", "B")):
        label = rf"{letter}: $\alpha$ = {alpha * 1e6:g} mm$^2$/s"
        axes[0].plot(times, np.sqrt(alpha * times) * 1000, color=color, lw=2.5, label=label)
        axes[1].loglog(lengths * 1000, lengths**2 / alpha, color=color, lw=2.5, label=letter)
        axes[0].scatter([10, 40], np.sqrt(alpha * np.array([10, 40])) * 1000, color=color, zorder=3)
        axes[1].scatter([5, 10], np.array([0.005, 0.010]) ** 2 / alpha, color=color, zorder=3)
    axes[0].annotate("4 × time → 2 × length", (19, 8), fontsize=10)
    axes[1].annotate("2 × length → 4 × time", (2, 500), fontsize=10)
    axes[0].set(xlabel="Time t (s)", ylabel=r"Scale $\ell=\sqrt{\alpha t}$ (mm)", title="Square-root growth", xlim=(0, 42), ylim=(0, 10))
    axes[1].set(xlabel="Length L (mm)", ylabel=r"Scale $t_D=L^2/\alpha$ (s)", title="Quadratic growth (logarithmic axes)", xlim=(1, 22), ylim=(0.4, 1200))
    for axis in axes:
        axis.grid(alpha=0.2, which="both")
        axis.legend(loc="lower right", fontsize=9)
    fig.text(0.5, -0.02, "Same k and density; B has four times A's specific heat capacity. Insulated-bar mode decay time is t_D/π².", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
