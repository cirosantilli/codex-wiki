"""Original functional diagram of the induction-ring experiment, not to scale."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(10.5, 5.0), layout="constrained")
    ax.add_patch(Circle((5, 2.6), 1.65, facecolor="#cccccc", edgecolor="#555555", lw=2))
    ax.add_patch(Circle((5, 2.6), .93, facecolor="white", edgecolor="#777777", lw=1.5))
    # The drawing separates the winding groups and the two electrical loops.
    for x, color in [(3.7, "#d55e00"), (6.3, "#0072b2")]:
        u = np.linspace(0, 1, 1000)
        phase = 12 * np.pi * u
        ax.plot(x + .43 * np.sin(phase), 3.25 - 1.35 * u + .075 * (np.cos(phase) - 1),
                color=color, lw=2.2)
    ax.plot([3.7, 1.0, 1.0, 1.0], [3.25, 3.25, 2.72, 2.55], color="#d55e00", lw=2)
    ax.plot([1.0, 1.0, 3.7], [2.1, 1.9, 1.9], color="#d55e00", lw=2)
    # Battery plates in the left vertical return.
    ax.plot([.73, 1.27], [2.55, 2.55], color="#333333", lw=2)
    ax.plot([.85, 1.15], [2.37, 2.37], color="#333333", lw=3)
    ax.plot([1, 1], [2.37, 2.1], color="#d55e00", lw=2)
    # The open contact is drawn on the upper lead.
    ax.plot([1.7, 2.45], [3.25, 3.25], color="white", lw=6)
    ax.plot([1.7, 2.38], [3.25, 3.64], color="#333333", lw=2)
    ax.scatter([1.7, 2.45], [3.25, 3.25], c="#333333", s=22, zorder=5)
    ax.plot([6.3, 9, 9], [3.25, 3.25, 2.99], color="#0072b2", lw=2)
    ax.plot([9, 9, 6.3], [2.21, 1.9, 1.9], color="#0072b2", lw=2)
    ax.add_patch(Circle((9, 2.6), .39, facecolor="white", edgecolor="#333333", lw=2))
    ax.add_patch(FancyArrowPatch((8.82, 2.39), (9.18, 2.81), arrowstyle="->", mutation_scale=14, lw=2))
    ax.text(1.0, 1.25, "Battery and contact", ha="center", fontsize=12)
    ax.text(3.55, 3.73, "Winding group A", ha="center", fontsize=12, color="#9b4400")
    ax.text(6.45, 3.73, "Winding group B", ha="center", fontsize=12, color="#005b8c")
    ax.text(9.0, 1.25, "Galvanometer", ha="center", fontsize=12)
    ax.text(5, 2.63, "Iron ring", ha="center", fontsize=13)
    ax.text(5, 2.15, "Insulated\nwindings", ha="center", va="center", fontsize=10)
    ax.text(5, .45, "Make contact → transient response     Hold → rest     Break contact → opposite response",
            ha="center", fontsize=11)
    ax.set_title("Faraday's induction ring: magnetic coupling between separate circuits", fontsize=15)
    ax.set(xlim=(.15, 10), ylim=(.1, 4.7), aspect="equal")
    ax.axis("off")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
