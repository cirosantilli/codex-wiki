"""Draw NST IB 2024 paper 2 Q7 mode patterns; write the PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib (see the root pyproject.toml).
Arrows represent relative angular displacements, not forces or velocities.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.pi / 2 + np.arange(3) * 2 * np.pi / 3
    points = np.column_stack((np.cos(theta), np.sin(theta)))
    tangents = np.column_stack((-np.sin(theta), np.cos(theta)))
    modes = ((1, 1, 1), (1, -1, 0), (1, 1, -2))
    labels = (
        r"$\mathbf{v}_0=(1,1,1)/\sqrt{3}$",
        r"$\mathbf{v}_1=(1,-1,0)/\sqrt{2}$",
        r"$\mathbf{v}_2=(1,1,-2)/\sqrt{6}$",
    )
    frequencies = (
        r"Rigid rotation: $\omega_0=0$",
        r"Vibration: $\omega_1=\sqrt{3k/(4m)}$",
        r"Vibration: $\omega_2=\sqrt{3k/(4m)}$",
    )
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.65), facecolor="white")
    circle = np.linspace(0, 2 * np.pi, 400)
    for ax, mode, label, frequency in zip(axes, modes, labels, frequencies):
        ax.set_facecolor("white")
        ax.plot(np.cos(circle), np.sin(circle), color="#697582", lw=1.4)
        for i, j in ((0, 1), (1, 2), (2, 0)):
            ax.plot(*points[[i, j]].T, color="#bdc5cc", lw=1.3, ls="--")
        ax.scatter(*points.T, s=60, color="#182838", zorder=3)
        for j, (point, tangent, amount) in enumerate(zip(points, tangents, mode)):
            ax.text(*(0.77 * point), str(j + 1), ha="center", va="center", fontsize=11)
            if amount:
                length = 0.55 * amount / np.sqrt(np.dot(mode, mode))
                start, end = point - length * tangent / 2, point + length * tangent / 2
                ax.annotate(
                    "",
                    xy=end,
                    xytext=start,
                    arrowprops=dict(
                        arrowstyle="-|>",
                        color="#1669b2" if amount > 0 else "#cb5c21",
                        lw=2.8,
                        mutation_scale=15,
                        shrinkA=0,
                        shrinkB=0,
                    ),
                )
        ax.set_title(label, fontsize=12, pad=11)
        ax.text(0.5, -0.04, frequency, transform=ax.transAxes, ha="center", fontsize=11)
        ax.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), aspect="equal")
        ax.axis("off")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.86, bottom=0.15, wspace=0.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
