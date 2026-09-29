"""Generate 2025-subduction-fates.png in the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies are recorded in the repository's top-level pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, ax = plt.subplots(figsize=(11.5, 7.4), dpi=130, facecolor="white")
    ax.set(xlim=(0, 11.5), ylim=(0, 7.4))
    ax.axis("off")
    ax.text(0.25, 7.08, "A subduction zone sorts materials into different pathways",
            fontsize=15, weight="bold", va="center")
    ax.text(0.25, 6.72, "Possible routes; no fixed proportions or universal reaction depths",
            color="#495566", fontsize=10)

    def box(x, y, w, h, label, color, size=10):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                  facecolor=color, edgecolor="#455366", linewidth=1))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=size)

    def arrow(a, b, color="#455366", style="-", rad=0):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12,
                                    connectionstyle=f"arc3,rad={rad}", color=color,
                                    linestyle=style, linewidth=1.5))

    box(0.25, 4.85, 2.0, 1.0, "SEDIMENTS\nPore water, clay,\ncarbonate, organic C", "#fff0c7")
    box(0.25, 3.12, 2.0, 1.0, "OCEANIC CRUST\nAltered basalt,\ndikes and gabbro", "#dae8f8")
    box(0.25, 1.39, 2.0, 1.0, "LITHOSPHERIC MANTLE\nPeridotite; variably\nserpentinized", "#e0edda", size=9.5)
    box(3.12, 5.18, 3.0, 0.91, "Upper-plate solid storage\nAccretion / tectonic underplating\nSome slices later exhumed", "#f3eee2")
    box(3.12, 3.47, 3.0, 1.04, "Burial and reaction\nMetamorphism; crust → eclogite\nHydrous phases may break down", "#edf0f5")
    box(3.12, 1.39, 3.0, 1.05, "Continuing solid slab\nResidual crust + sediment\n+ mostly solid mantle", "#e2e7ee")
    box(7.1, 4.94, 3.95, 1.15, "Fluid and melt transfer\nForearc discharge and storage\nMantle-wedge metasomatism\nFlux melting → arc magmas / gases", "#d9f0f2")
    box(7.1, 2.97, 3.95, 1.09, "Material retained in the mantle\nTransition-zone storage or deeper sinking\nMixing and reaction; some volatile retention", "#e5e4f1", size=9.7)
    box(7.1, 1.13, 3.95, 1.0, "Possible eventual return\nConvection and partial melting\nRecycled components in new basalts", "#f3e3ec")

    arrow((2.33, 5.4), (3.02, 5.58))
    arrow((2.33, 5.05), (3.02, 4.35))
    arrow((2.33, 3.65), (3.02, 3.98))
    arrow((2.33, 1.9), (3.02, 1.9))
    arrow((2.27, 2.45), (3.03, 3.58), color="#14869b", style="--")
    arrow((4.61, 3.37), (4.61, 2.55))
    arrow((6.23, 4.16), (6.97, 5.28), color="#14869b", style="--")
    arrow((6.23, 1.99), (6.97, 3.37))
    arrow((9.07, 2.86), (9.07, 2.24))
    ax.text(4.88, 2.94, "residue", va="center", color="#455366", fontsize=9)
    ax.text(6.66, 4.72, "released\ncomponents", ha="center", va="center",
            fontsize=8.5, color="#11798c")
    ax.text(0.25, 0.63, "Solid paths", weight="bold", color="#455366")
    ax.plot([1.3, 1.83], [0.65, 0.65], color="#455366", lw=1.6)
    ax.text(2.15, 0.63, "Fluid / melt transfer", weight="bold", color="#11798c")
    ax.plot([3.98, 4.51], [0.65, 0.65], color="#14869b", lw=1.6, ls="--")
    ax.text(0.25, 0.20, "Mechanical underplating of rock differs from magmatic underplating of new melt.",
            fontsize=9, color="#495566")
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.01, top=0.99)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=130, facecolor="white", transparent=False,
                metadata={"Software": "codex-wiki figure generator"})
    plt.close(fig)


if __name__ == "__main__":
    main()
