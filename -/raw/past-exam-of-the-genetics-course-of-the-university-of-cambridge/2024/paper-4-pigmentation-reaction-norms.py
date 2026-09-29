"""Schematic reaction norms, not measured Drosophila pigmentation data.

Outputs a PNG basename to the working directory; see root pyproject.toml.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    temperature = np.linspace(18, 28, 120)
    intercepts = [60, 50, 40]
    colors = ["#1261a0", "#c05420", "#278251"]
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.9), sharey=True,
                             layout="constrained", facecolor="white")
    panels = [([ -2, -2, -2], "Baseline differences; shared response"),
              ([ -4, -1.5, -.5], "Genotype-specific response")]
    for ax, (slopes, title) in zip(axes, panels):
        for i, (a, b, color) in enumerate(zip(intercepts, slopes, colors), 1):
            values = a + b * (temperature - 22)
            assert np.all((values >= 0) & (values <= 100))
            ax.plot(temperature, values, color=color, lw=2.5, label=f"Genotype {i}")
            ax.scatter([18, 22, 28], a + b * (np.array([18, 22, 28]) - 22),
                       color=color, s=28, zorder=3)
        ax.set(xlabel="Developmental temperature (°C)", title=title,
               xlim=(17.6, 28.4), ylim=(20, 82), xticks=[18, 20, 22, 24, 26, 28])
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.18)
    axes[0].set_ylabel("Illustrative pigmentation score")
    axes[1].legend(frameon=False, loc="upper right")
    fig.suptitle("Reaction norms distinguish baseline colour from plasticity", fontsize=15)
    fig.supxlabel("Illustrative linear responses only — no empirical measurements plotted", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
