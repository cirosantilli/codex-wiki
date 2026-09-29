"""Draw one forward citric acid cycle; run from _media with Python 3.14.

Requires matplotlib 3.10.7 and numpy 2.3.5, as in pyproject.toml.
All positions are schematic. Carbon counts exclude the coenzyme A carrier.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(12, 8), facecolor="white")
    ax = fig.add_axes((0.07, 0.13, 0.62, 0.76))
    ax.set(xlim=(-1.65, 8.8), ylim=(-0.5, 8.6))
    ax.axis("off")
    nodes = [
        ("Oxaloacetate", 4, (0, 6.5)),
        ("Citrate", 6, (3.4, 6.5)),
        ("Isocitrate", 6, (6.8, 6.5)),
        (r"$\alpha$-Ketoglutarate", 5, (6.8, 3.7)),
        ("Succinyl-CoA", 4, (6.8, 0.9)),
        ("Succinate", 4, (3.4, 0.9)),
        ("Fumarate", 4, (0, 0.9)),
        ("Malate", 4, (0, 3.7)),
    ]
    for i, (_, _, start) in enumerate(nodes):
        end = nodes[(i + 1) % len(nodes)][2]
        direction = np.array(end) - start
        direction = direction / np.linalg.norm(direction)
        # Elliptical node boxes need more horizontal than vertical clearance.
        gap = 1.12 if abs(direction[0]) > 0 else 0.57
        ax.add_patch(FancyArrowPatch(
            np.array(start) + gap * direction,
            np.array(end) - gap * direction,
            arrowstyle="-|>", mutation_scale=18, lw=2, color="#536472",
        ))
    for name, carbon, (x, y) in nodes:
        ax.text(x, y, f"{name}\n{carbon} C", ha="center", va="center",
                bbox={"boxstyle": "round,pad=0.4", "fc": "#edf5fa", "ec": "#527f9c"})
    ax.annotate("", xy=(1.7, 6.5), xytext=(1.7, 7.85),
                arrowprops={"arrowstyle": "-|>", "lw": 2, "color": "#9c5d18"})
    ax.text(1.7, 8.12, "Acetyl-CoA\n2 C acetyl group", ha="center", color="#825017")
    ax.text(5.1, 5.88, "rearrangement", ha="center", fontsize=10)
    ax.text(7.08, 5.08, "NADH\n+ CO₂", va="center", color="#27644f")
    ax.text(7.08, 2.28, "NADH\n+ CO₂", va="center", color="#27644f")
    ax.text(5.1, 0.02, "GTP (or ATP)", ha="center", color="#825017")
    ax.text(1.7, 0.02, "QH₂ via bound FAD", ha="center", color="#27644f", fontsize=10)
    ax.text(-0.35, 2.3, "+ H₂O", ha="right", va="center", fontsize=11)
    ax.text(-0.35, 5.08, "NADH", ha="right", va="center", color="#27644f")
    ax.text(3.4, 3.8, "4 + 2 − 1 − 1 = 4\nacceptor regenerated",
            ha="center", va="center", fontsize=14, color="#38424b", linespacing=1.6)
    ledger = fig.add_axes((0.76, 0.2, 0.22, 0.62))
    ledger.axis("off")
    ledger.text(0, 1, "Per acetyl group", weight="bold", fontsize=15)
    for y, text in [(0.84, "3 NADH"), (0.71, "1 QH₂"), (0.58, "1 GTP (or ATP)"), (0.45, "2 CO₂")]:
        ledger.text(0, y, text, fontsize=15)
    ledger.text(0, 0.2, "QH₂ is the mobile output.\nOne FADH₂ equivalent\nis an alternative count,\nnot another output.",
                fontsize=11, linespacing=1.5)
    fig.suptitle("Citric acid cycle: carbon and carrier accounting", fontsize=19, y=0.97)
    fig.text(0.5, 0.035, "Original schematic • carbon skeletons, not molecular structures • no rates or ATP-conversion assumptions",
             ha="center", fontsize=11, color="#4d5960")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
