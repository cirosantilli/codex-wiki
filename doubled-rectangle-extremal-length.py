"""Illustrate the flat doubled-rectangle metric; write the PNG to cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    figure, axes = plt.subplots(1, 2, figsize=(10.8, 4.2))
    for index, ax in enumerate(axes):
        ax.fill([0, 2, 2, 0], [0, 0, 1, 1], color="#f5f5fa")
        for xs, ys in [([0, 0], [0, 1]), ([2, 2], [0, 1]), ([0, 2], [0, 0])]:
            ax.plot(xs, ys, "--", color="#746c87", linewidth=2.0)
        ax.plot([0, 2], [1, 1], color="#222222", linewidth=2.5)
        ax.text(1, 1.07, "Outer boundary", ha="center", va="bottom", fontsize=11)
        ax.plot([0, 2], [0.49, 0.49], color="#bd4c20", linewidth=2.7)
        ax.annotate("", (1.05 if index == 0 else 0.95, 0.49), (0.95 if index == 0 else 1.05, 0.49), arrowprops={"arrowstyle": "->", "color": "#bd4c20", "lw": 2.3})
        ax.plot([1.35, 1.35], [0, 1], color="#1666a8", linewidth=2.7)
        ax.annotate("", (1.35, 0.67 if index == 0 else 0.77), (1.35, 0.77 if index == 0 else 0.67), arrowprops={"arrowstyle": "->", "color": "#1666a8", "lw": 2.3})
        ax.plot([0, 2], [0, 0], "o", color="#222222", markersize=5)
        ax.text(0, -0.10, r"$z_1$", ha="center", va="top")
        ax.text(2, -0.10, r"$z_2$", ha="center", va="top")
        ax.set(xlim=(-0.13, 2.13), ylim=(-0.17, 1.2), aspect="equal", title="Upper half-disc" if index == 0 else "Lower half-disc")
        ax.axis("off")
        ax.text(0.08, 0.62, r"Loop: half-length $w$", color="#a03e15", fontsize=11)
        ax.text(1.44, 0.18, r"Crosscut", color="#14598f", fontsize=10)
        ax.text(1.44, 0.09, r"half-length $h$", color="#14598f", fontsize=10)
    figure.suptitle(r"Two rectangles: total area $2wh$", y=0.98, fontsize=15)
    figure.text(0.5, 0.05, "Glue matching dashed sides; the two top sides remain the outer boundary.", ha="center", fontsize=11)
    figure.subplots_adjust(left=0.02, right=0.98, bottom=0.12, top=0.86, wspace=0.11)
    figure.savefig(Path.cwd() / "doubled-rectangle-extremal-length.png", dpi=100)
    plt.close(figure)


if __name__ == "__main__":
    main()
