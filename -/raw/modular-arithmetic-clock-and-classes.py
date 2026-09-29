"""Render clock addition and an integer congruence class into the current directory."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def clock_point(residue, radius=1.0):
    angle = np.pi / 2 - 2 * np.pi * np.asarray(residue) / 12
    return radius * np.cos(angle), radius * np.sin(angle)


def main():
    assert (10 + 7) % 12 == 5
    representatives = np.array([-8, -3, 2, 7, 12])
    assert np.all(representatives % 5 == 2)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), color="#a9b7c4", lw=2)
    for residue in range(12):
        x, y = clock_point(residue)
        ax.plot(x, y, "o", color="#607080", ms=5)
        tx, ty = clock_point(residue, 1.18)
        ax.text(tx, ty, str(residue), ha="center", va="center")
    path = np.linspace(10, 17, 300)
    px, py = clock_point(path, 0.86)
    ax.plot(px, py, color="#1a77b9", lw=3)
    for residue in range(11, 18):
        start = clock_point(residue - 0.19, 0.86)
        end = clock_point(residue, 0.86)
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": "#1a77b9", "lw": 2})
    for residue, color in [(10, "#d57816"), (5, "#168556")]:
        x, y = clock_point(residue)
        ax.scatter(x, y, s=140, color=color, edgecolor="white", zorder=5)
    ax.text(0, 0.14, r"$10+7\equiv5\;(\mathrm{mod}\;12)$", ha="center", fontsize=15)
    ax.text(0, -0.14, "Seven clockwise steps", ha="center", fontsize=11)
    ax.text(0, -1.46, "0 is the clock position usually labelled 12", ha="center", fontsize=10)
    ax.set_title("A position survives; complete turns do not", pad=15)
    ax.set_aspect("equal")
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.62, 1.42)
    ax.axis("off")

    ax = axes[1]
    integers = np.arange(-9, 14)
    ax.axhline(0, color="#607080", lw=1.2)
    ax.scatter(integers, np.zeros_like(integers), color="#c4ccd3", s=24, zorder=3)
    ax.scatter(representatives, np.zeros_like(representatives), color="#168556", s=100, zorder=4)
    for residue in representatives:
        ax.text(residue, -0.22, str(residue), ha="center", color="#12683f", fontweight="bold")
    for start, stop in zip(representatives[:-1], representatives[1:]):
        ax.annotate("", xy=(stop, 0.33), xytext=(start, 0.33),
                    arrowprops={"arrowstyle": "<->", "color": "#1a77b9", "lw": 1.6})
        ax.text((start + stop) / 2, 0.45, "+5", ha="center", color="#1a77b9")
    ax.text(2, 1.08, r"$[2]_5=\{2+5k:k\in\mathbb{Z}\}$", ha="center", fontsize=16)
    ax.text(2, -0.78, "Different integers, one congruence class", ha="center")
    ax.text(2, -1.12, "The least nonnegative representative is 2", ha="center", fontsize=11)
    ax.set_title("Modulo five identifies positions five apart", pad=15)
    ax.set_xlim(-9.5, 13.5)
    ax.set_ylim(-1.5, 1.55)
    ax.axis("off")
    fig.subplots_adjust(left=0.04, right=0.98, top=0.88, bottom=0.08, wspace=0.25)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
