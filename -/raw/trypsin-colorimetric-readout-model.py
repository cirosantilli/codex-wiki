"""Illustrate assay controls and original, explicitly constructed absorbance traces."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle


def main():
    fig = plt.figure(figsize=(9, 6.5), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.5], width_ratios=[1.6, 1.0],
                           left=0.09, right=0.96, bottom=0.10, top=0.88,
                           hspace=0.50, wspace=0.35)
    apparatus = fig.add_subplot(grid[0, :])
    apparatus.set(xlim=(0, 10), ylim=(0, 2.5))
    apparatus.axis("off")
    fig.suptitle("Trypsin assay: product formation becomes an optical signal", fontsize=16)

    for x, label in [(0.2, "405 nm\nlight"), (8.0, "Detector\n→ absorbance")]:
        apparatus.add_patch(FancyBboxPatch((x, 0.55), 1.75, 0.9,
                                          boxstyle="round,pad=0.05", facecolor="#edf1f5",
                                          edgecolor="#496173"))
        apparatus.text(x + 0.875, 1.0, label, ha="center", va="center", fontsize=12)
    apparatus.add_patch(Rectangle((4.0, 0.45), 1.4, 1.35, facecolor="#f8e9a7", edgecolor="#496173"))
    apparatus.text(4.7, 2.17, "Cuvette at 25 °C", fontsize=12, ha="center")
    apparatus.text(4.7, 1.12, "BAPNA\n→ pNA", fontsize=12, ha="center", va="center")
    apparatus.annotate("", xy=(4.0, 1.0), xytext=(2.1, 1.0),
                       arrowprops={"arrowstyle": "->", "color": "#3b73a1", "lw": 2})
    apparatus.annotate("", xy=(7.8, 1.0), xytext=(5.4, 1.0),
                       arrowprops={"arrowstyle": "->", "color": "#3b73a1", "lw": 2})
    apparatus.annotate("", xy=(4.0, 0.18), xytext=(5.4, 0.18),
                       arrowprops={"arrowstyle": "<->", "color": "#496173"})
    apparatus.text(4.7, -0.08, "1 cm geometric light path", fontsize=10, ha="center")
    apparatus.text(0.2, 2.15, "U: trypsin\nI: trypsin + aprotinin\nB: no trypsin", fontsize=11, va="center")

    ax = fig.add_subplot(grid[1, 0])
    t = np.linspace(0, 5, 101)
    initial = 0.02
    rates = {"U": 0.1036, "I": 0.0538, "B": 0.0040}
    colors = {"U": "#246c9b", "I": "#ae6131", "B": "#63686e"}
    for label, rate in rates.items():
        ax.plot(t, initial + rate * t, lw=2.2, color=colors[label],
                linestyle="--" if label == "B" else "-",
                label=f"{label}: slope {rate:.4f} /min")
    ax.set(xlabel="Time (min)", ylabel="Absorbance at 405 nm", xlim=(0, 5), ylim=(0, 0.60))
    ax.set_title("Constructed traces — not measured data", fontsize=11, pad=10)
    ax.legend(loc="upper left", fontsize=9, framealpha=1)
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)

    notes = fig.add_subplot(grid[1, 1])
    notes.axis("off")
    notes.text(0, 0.97, "Subtract the blank", fontsize=14, weight="bold", va="top")
    notes.text(0, 0.80, "U − B = 0.0996 /min\nI − B = 0.0498 /min", fontsize=12, linespacing=1.6, va="top")
    notes.text(0, 0.54, "Corrected ratio = 1/2\nSuppression = 50%", fontsize=12, linespacing=1.6, va="top")
    notes.text(0, 0.28, "Beer–Lambert conversion\n0.0996 / 9.96 = 0.0100\nmM of product per minute\n(for a 1 cm light path)",
               fontsize=11, linespacing=1.45, va="top")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
