"""Draw the three exact stopped sequences for r=2, X=2, p=1/2.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Write an opaque white PNG with this script's basename to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.4, 4.6), dpi=100)
    sequences = ("SFFS", "FSFS", "FFSS")
    ax.add_patch(FancyBboxPatch((3.56, -0.42), 0.88, 3.00,
                               boxstyle="round,pad=0.04", facecolor="#fff1d9",
                               edgecolor="#b76c00", linewidth=1.8))
    for row, sequence in enumerate(sequences):
        y = 2 - row
        for trial, outcome in enumerate(sequence, 1):
            color = "#19705b" if outcome == "S" else "#496e9c"
            ax.scatter(trial, y, s=1100, facecolor=color, edgecolor="white", zorder=3)
            ax.text(trial, y, outcome, ha="center", va="center", color="white",
                    fontsize=17, weight="bold", zorder=4)
        ax.text(0.30, y, sequence, ha="right", va="center", weight="bold")
        ax.text(4.80, y, "Probability 1/16", va="center")
    for trial in range(1, 5):
        ax.text(trial, 2.96, f"Trial {trial}", ha="center", fontsize=12)
    ax.text(2, -0.78, "First three trials: one S and two F", ha="center", fontsize=11)
    ax.text(4, -0.78, "Second S: stop", ha="center", fontsize=11, color="#8d5300")
    ax.set(xlim=(-0.65, 6.5), ylim=(-1.03, 3.3))
    ax.axis("off")
    fig.suptitle("Two failures before the second success", fontsize=16, weight="bold", y=0.97)
    fig.text(0.5, 0.025, "S = success, F = failure; p = 1/2.  Total N = X + r = 4 trials; P(X = 2) = 3/16.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.055, right=0.985, bottom=0.13, top=0.88)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
