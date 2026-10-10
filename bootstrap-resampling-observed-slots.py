"""Draw original resampling examples; emit the matching opaque PNG in CWD."""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    values = (1, 2, 4)
    colors = ("#dcecf9", "#e4efda", "#f7e4ce")
    edges = ("#2675a8", "#567c2c", "#bd741c")
    samples = ((0, 0, 2), (1, 2, 0), (2, 2, 2))
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 5.8)
    ax.axis("off")
    ax.text(5.25, 5.57, "Resample observed slots with replacement", ha="center", fontsize=19, weight="bold")
    ax.text(5.25, 5.15, "Original observations stay fixed: (1, 2, 4)", ha="center", fontsize=13)

    def card(x, y, index):
        ax.add_patch(FancyBboxPatch((x, y), 1.2, .72, boxstyle="round,pad=0.04", facecolor=colors[index], edgecolor=edges[index], lw=1.7))
        ax.text(x+.6, y+.46, str(values[index]), ha="center", va="center", fontsize=20, weight="bold")
        ax.text(x+.6, y+.13, f"slot {index+1}", ha="center", va="center", fontsize=10, color=edges[index])

    ax.text(.2, 4.3, "Source slots", fontsize=12, va="center")
    for i in range(3):
        card(2+i*1.65, 3.95, i)
    ax.text(7.35, 4.3, "Each slot: probability 1/3\non every independent draw", fontsize=12, va="center")
    ax.plot([.2, 10.3], [3.65, 3.65], color="#cccccc", lw=1)
    for r, indices in enumerate(samples):
        y = 2.7-r*.97
        ax.text(.2, y+.36, f"Possible sample {r+1}", fontsize=12, va="center")
        for c, index in enumerate(indices):
            card(3+c*1.5, y, index)
        mean = Fraction(sum(values[i] for i in indices), 3)
        ax.text(8, y+.36, f"mean = {mean}", va="center", fontsize=14)
    ax.text(5.25, .04, "These are three possible sequences, not three new observations or a simulation estimate.", ha="center", va="bottom", fontsize=11)
    fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
