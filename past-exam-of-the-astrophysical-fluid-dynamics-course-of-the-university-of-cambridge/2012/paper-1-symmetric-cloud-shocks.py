"""Center-of-momentum frame of two cold identical colliding gas clouds."""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    gamma = 5 / 3
    compression = (gamma + 1) / (gamma - 1)
    speed_ratio = (gamma - 1) / 2
    assert abs((1 + speed_ratio) / speed_ratio - compression) < 1e-12
    fig, ax = plt.subplots(figsize=(8, 3.6), layout="constrained")
    ax.axvspan(-3, -1, color="#d6e9f5")
    ax.axvspan(-1, 1, color="#f3bf99")
    ax.axvspan(1, 3, color="#d6e9f5")
    ax.axvline(0, color="0.4", ls=":", label="Contact plane")
    for x in [-1, 1]:
        ax.axvline(x, color="#9c3b24", lw=2.5)
    for start, end, label in [(-2.7, -1.5, r"$+V$"), (2.7, 1.5, r"$-V$"),
                              (-1, -1.7, r"$-S$"), (1, 1.7, r"$+S$")]:
        y = 0.3 if abs(start) > 2 else 0.8
        ax.annotate("", (end, y), (start, y), arrowprops={"arrowstyle": "->", "lw": 2})
        ax.text((start + end) / 2, y + 0.08, label, ha="center")
    ax.text(-2.1, -0.35, "Cold upstream\ncloud", ha="center")
    ax.text(2.1, -0.35, "Cold upstream\ncloud", ha="center")
    ax.text(0, -0.25, "Hot compressed gas\nvelocity = 0", ha="center",
            bbox={"facecolor": "#f3bf99", "edgecolor": "none"})
    ax.text(0, -0.77, r"$S=(\gamma-1)V/2=V/3$ for $\gamma=5/3$", ha="center")
    ax.set(xlim=(-3, 3), ylim=(-1, 1.15), xticks=[], yticks=[],
           title="Symmetric cloud collision: two outward-moving shocks")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
