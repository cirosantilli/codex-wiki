"""Original conceptual diagram; output is written to the current directory.

Tested with Python 3.14.4 and Matplotlib 3.10.7. No empirical values or source
figures are reproduced. Arrows distinguish measurement routes, not proven
independent memory systems.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(9.4, 3.8), dpi=130, facecolor="white")
    ax.set_facecolor("white")
    centers = [0.09, 0.295, 0.50, 0.705, 0.91]
    labels = ["Early\nexperience", "Memory\nencoding", "Information\nretained", "Information\nretrieved", "Verbal\nreport"]
    width, height, y = 0.16, 0.22, 0.69

    def box(x, y, label, width=width, color="#e4eff7"):
        patch = FancyBboxPatch((x-width/2, y-height/2), width, height,
                              boxstyle="round,pad=0.005,rounding_size=0.02",
                              linewidth=1.4, edgecolor="#35668a", facecolor=color)
        ax.add_patch(patch)
        ax.text(x, y, label, ha="center", va="center", color="#19374d")

    def arrow(start, stop):
        ax.add_patch(FancyArrowPatch(start, stop, arrowstyle="-|>",
                                    linewidth=1.5, mutation_scale=13,
                                    color="#526b7b", shrinkA=4, shrinkB=4))

    for x, label in zip(centers, labels):
        box(x, y, label)
    for left, right in zip(centers, centers[1:]):
        arrow((left+width/2, y), (right-width/2, y))
    box(centers[3], 0.27, "Nonverbal\nresponse", color="#fff0d8")
    box(centers[4], 0.27, "Reported\nevent date", color="#fff0d8")
    arrow((centers[3], y-height/2), (centers[3], 0.27+height/2))
    arrow((centers[4], y-height/2), (centers[4], 0.27+height/2))
    ax.text(0.32, 0.30, "Cue support and response format\nchange what a test can reveal.",
            ha="center", va="center", fontsize=12, color="#19374d")
    ax.text(0.50, 0.045,
            "Conceptual measurement routes · a failed report does not identify where access failed",
            ha="center", va="center", fontsize=10, color="#526b7b")
    ax.set_xlim(-0.015, 1.015)
    ax.set_ylim(-0.01, 1)
    ax.axis("off")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.04, top=0.96)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
