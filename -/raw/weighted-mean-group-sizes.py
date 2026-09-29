"""Synthetic group sizes and their weighted mean; output to the working directory."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.array([60] * 8 + [90] * 2)
    mean = float(values.mean())
    assert mean == 66
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.scatter([60] * 8, np.arange(8) * 0.12 + 0.4, s=100,
               color="#2768a6", label="8 observations at 60", zorder=4)
    ax.scatter([90] * 2, np.arange(2) * 0.12 + 0.4, s=100,
               color="#ba5524", label="2 observations at 90", zorder=4)
    ax.axvline(mean, color="#207745", linewidth=2.4,
               label="Individual mean: 66")
    ax.axvline(75, color="#80519d", linewidth=2, linestyle="--",
               label="Equal-weight mean of group means: 75")
    ax.text(60, 1.43, "8 observations", ha="center", color="#2768a6")
    ax.text(90, 1.43, "2 observations", ha="center", color="#ba5524")
    ax.text(66, 1.18, "66", ha="center", color="#207745", weight="bold")
    ax.text(75, 1.18, "75", ha="center", color="#80519d", weight="bold")
    ax.set(xlim=(54, 96), ylim=(0.25, 1.6), yticks=[],
           xticks=[60, 66, 75, 90], xlabel="Observation value",
           title="Group counts determine the combined individual mean")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2,
              frameon=False, fontsize=10)
    fig.subplots_adjust(bottom=0.28, top=0.88)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
