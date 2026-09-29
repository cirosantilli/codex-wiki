"""Qualitative memory dissociation; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write the opaque PNG to the current working directory. No patient scores.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, ax = plt.subplots(figsize=(8.0, 3.45), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.985, top=0.86, bottom=0.19)
    ax.set_xlim(0, 3.45)
    ax.set_ylim(0, 2.4)
    ax.axis("off")
    fig.suptitle("Complementary impairments constrain memory models", fontsize=13, y=0.965)
    ax.text(1.55, 2.2, "Immediate verbal\nretention", ha="center", va="center", fontsize=11)
    ax.text(2.75, 2.2, "New long-term\nexplicit learning", ha="center", va="center", fontsize=11)
    row_labels = ("H.M.-type\nprofile", "K.F.-type\nprofile")
    values = (("Relatively\npreserved", "Impaired"), ("Impaired", "Relatively\npreserved"))
    for i, label in enumerate(row_labels):
        y = 1.13 - i * 0.95
        ax.text(0.44, y + 0.38, label, ha="center", va="center", fontsize=11)
        for j, value in enumerate(values[i]):
            x = 0.99 + 1.2 * j
            color = "#d8ece8" if "preserved" in value else "#f3dfd3"
            ax.add_patch(Rectangle((x, y), 1.12, 0.77, facecolor=color, edgecolor="#555555", linewidth=0.8))
            ax.text(x + 0.56, y + 0.385, value, ha="center", va="center", fontsize=11)
    fig.text(0.5, 0.075, "Qualitative selected-task profiles, not scores. Material, procedure and remaining routes matter.", ha="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
