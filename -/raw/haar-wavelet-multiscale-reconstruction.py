"""Original four-step Haar projections at three resolutions; PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    edges = np.linspace(0, 1, 5)
    signal = np.array([2., 4., 6., 8.])
    approximations = [np.full(4, 5.), np.array([3., 3., 7., 7.]), signal]
    titles = [r"$P_0f=5\phi$",
              r"$P_1f=5\phi-2\psi$",
              r"$P_2f=P_1f-(\psi_{1,0}+\psi_{1,1})/\sqrt{2}$"]
    colors = ["#bf7135", "#238367", "#246a9b"]
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 4.1), dpi=120, sharey=True)
    fig.patch.set_facecolor("white")
    for level, (ax, values, title, color) in enumerate(
            zip(axes, approximations, titles, colors)):
        ax.stairs(values, edges, color=color, lw=3, label=f"Level {level}")
        ax.stairs(signal, edges, color="#333333", lw=1.4,
                  linestyle="--", label="Original f", zorder=3)
        for left, right, original, approx in zip(
                edges[:-1], edges[1:], signal, values):
            ax.fill_between([left, right], [original, original],
                            [approx, approx], color=color, alpha=.13)
        ax.set(xlim=(0, 1), ylim=(0, 9), xlabel="x", title=title)
        ax.set_xticks([0, .25, .5, .75, 1])
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.12)
        ax.legend(loc="upper left", frameon=False, fontsize=9)
        error = np.sum((signal-values)**2)/4
        ax.text(.5, -.34, rf"Squared $L^2$ error: {error:g}",
                transform=ax.transAxes, ha="center", fontsize=11)
    axes[0].set_ylabel("Function value")
    fig.suptitle("Mean + global contrast + local contrasts = exact reconstruction",
                 fontsize=14)
    fig.subplots_adjust(left=.055, right=.98, top=.74, bottom=.26, wspace=.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
