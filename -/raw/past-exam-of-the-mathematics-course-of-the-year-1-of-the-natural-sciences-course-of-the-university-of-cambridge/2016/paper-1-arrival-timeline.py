"""Original Q16 arrival timeline; write the PNG basename to the cwd.

Tested with Python 3.14.4 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    R, r, t = 1, 0.4, 0.15
    fig, ax = plt.subplots(figsize=(10.4, 3.3), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    red, green = "#b94b3c", "#377d58"
    for left, right, color, word in [(0, r, red, "Stop"), (r, R, green, "Pass"), (R, R+r, red, "Stop")]:
        ax.broken_barh([(left, right-left)], (1.05, 0.28), facecolors=color)
        ax.text((left+right)/2, 1.19, word, color="white", ha="center", va="center", fontsize=11)
    intervals = [(t, r, red, r"$\tau_1=0$", r"$(r-t)/R$"), (r, R, green, r"$\tau_1=t+\tau_0-r$", r"$(R-r)/R$"), (R, R+t, red, r"$\tau_1=R$", "$t/R$")]
    for left, right, color, outcome, probability in intervals:
        ax.broken_barh([(left, right-left)], (0.43, 0.23), facecolors=color, alpha=0.23)
        ax.text((left+right)/2, 0.18, outcome, ha="center", fontsize=10)
        ax.text((left+right)/2, -0.16, probability, ha="center", fontsize=11)
    for value in [t, r, R, R+t]:
        ax.axvline(value, ymin=0.25, ymax=0.75, color="#aaaaaa", linewidth=0.8, linestyle="--")
    ax.annotate("A arrives", (t, 1.34), xytext=(t, 1.65), ha="center", fontsize=10, arrowprops={"arrowstyle": "->"})
    ax.annotate("A departs", (r, 1.34), xytext=(r+0.05, 1.65), ha="center", fontsize=10, arrowprops={"arrowstyle": "->"})
    ax.text(0.02, 0.75, "B arrival ranges", fontsize=10)
    ax.set(xlim=(-0.03, 1.43), ylim=(-0.36, 1.88), xlabel="Arrival time", title="A fixed arrival phase and three possible outcomes for B")
    ax.set_xticks([0, t, r, R, R+t, R+r], ["0", "$t$", "$r$", "$R$", "$R+t$", "$R+r$"])
    ax.set_yticks([])
    ax.spines[["top", "left", "right"]].set_visible(False)
    fig.savefig(Path("paper-1-arrival-timeline.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
