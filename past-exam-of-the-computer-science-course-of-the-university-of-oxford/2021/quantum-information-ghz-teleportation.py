"""Original GHZ-assisted teleportation protocol diagram; output is written to CWD.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. No external assets.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(8.6, 4.6), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.83, bottom=0.12)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    fig.suptitle("Three classical bits complete GHZ-assisted teleportation", fontsize=13, y=0.97)
    fig.text(0.5, 0.86, "Previously shared GHZ on A, B, C; unknown |χ⟩ starts at Alice", ha="center", fontsize=11)

    def box(bounds, text, color):
        xx, yy, ww, hh = bounds
        ax.add_patch(FancyBboxPatch((xx, yy), ww, hh, boxstyle="round,pad=0.09", facecolor=color, edgecolor="#555555", linewidth=0.9))
        ax.text(xx + ww / 2, yy + hh / 2, text, ha="center", va="center", fontsize=11, linespacing=1.45)

    box((0.3, 2.65, 4.0, 1.7), "Alice\nCNOT Q → A, then H on Q\nMeasure Q, A in Z basis: s, t", "#e7eef6")
    box((0.3, 0.35, 4.0, 1.55), "Charlie\nMeasure C in X basis: c\n(H then Z-basis readout)", "#e8f0e8")
    box((6.0, 1.55, 3.45, 1.95), "Bob\nApply Xᵗ, then Zˢ⁺ᶜ\nOutput |χ⟩", "#fbefdb")
    ax.text(7.72, 1.05, "Exponent s + c means XOR", fontsize=9, ha="center")
    for start, end, label, yy in [((4.45, 3.55), (5.9, 2.95), "s, t", 3.72), ((4.45, 1.12), (5.9, 2.08), "c", 1.0)]:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13, color="#34495e", linestyle="--", linewidth=1.4))
        ax.text(5.1, yy, label, ha="center", fontsize=11)
    ax.text(5.15, 2.35, "classical\nbits", ha="center", fontsize=9, color="#34495e")
    fig.text(0.5, 0.035, "Before Bob's correction: Xᵗ Zˢ⁺ᶜ |χ⟩, up to global phase. No quantum transmission during the protocol.", ha="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
