"""Original circuit for CNOT synthesized using two exchange pulses."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def box(ax, x, y, label, height=0.48, width=0.90, color="#e1ecf5"):
    ax.add_patch(Rectangle((x-width/2, y-height/2), width, height,
                           facecolor=color, edgecolor="0.25", zorder=3))
    ax.text(x, y, label, ha="center", va="center", fontsize=11, zorder=4)


def main():
    fig, ax = plt.subplots(figsize=(9.4, 2.8), layout="constrained")
    for y, label in [(1, "Qubit 1\n(control)"), (0, "Qubit 2\n(target)")]:
        ax.plot([-0.6, 7.3], [y, y], color="0.35", lw=1.5, zorder=1)
        ax.text(-0.85, y, label, ha="right", va="center", fontsize=10)
    box(ax, 0, 0, r"$R_y(-\pi/2)$")
    box(ax, 1.4, 0.5, r"$\sqrt{\mathrm{SWAP}}$", height=1.45, width=1.15, color="#f6e3c4")
    box(ax, 2.8, 1, r"$R_z(\pi)$")
    box(ax, 4.2, 0.5, r"$\sqrt{\mathrm{SWAP}}$", height=1.45, width=1.15, color="#f6e3c4")
    box(ax, 5.6, 1, r"$R_z(\pi/2)$")
    box(ax, 5.6, 0, r"$R_z(-\pi/2)$")
    box(ax, 7.0, 0, r"$R_y(\pi/2)$")
    ax.annotate("Time", xy=(6.8, -0.65), xytext=(0, -0.65), va="center",
                arrowprops={"arrowstyle": "->", "color": "0.4"})
    ax.set(xlim=(-2.1, 7.65), ylim=(-0.9, 1.6),
           title="CNOT from exchange and local rotations (up to a global phase)")
    ax.axis("off")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
