"""Draw Coulomb force vectors with computed inverse-square lengths.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The output is an opaque white PNG in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def force_on_second(first, second, q1, q2, k=1.0):
    """Use the displacement from the first charge to the second."""
    displacement = np.asarray(second, dtype=float) - np.asarray(first, dtype=float)
    distance = np.linalg.norm(displacement)
    if distance == 0:
        raise ValueError("Distinct point-charge positions are required")
    return k * q1 * q2 * displacement / distance**3


def main():
    separations = np.array([1.0, 2.0, 3.0])
    ratios = separations**-2
    np.testing.assert_allclose(ratios, [1.0, 0.25, 1.0 / 9.0])
    positive, negative, force_color = "#b53d35", "#216baf", "#243d4b"
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.6), dpi=120)
    for ax, q2, heading in zip(
        axes, [1.0, -1.0], ["Like charges: repulsion", "Unlike charges: attraction"]
    ):
        for index, (distance, ratio) in enumerate(zip(separations, ratios)):
            y = 2.0 - index
            left = np.array([0.0, y])
            right = np.array([distance, y])
            force2 = force_on_second(left, right, 1.0, q2)
            force1 = force_on_second(right, left, q2, 1.0)
            np.testing.assert_allclose(force1, -force2)
            np.testing.assert_allclose(np.linalg.norm(force2), ratio)
            ax.plot([0, distance], [y, y], color="#c9d2d8", linewidth=1.2, zorder=1)
            ax.scatter([0, distance], [y, y], s=410,
                       color=[positive, positive if q2 > 0 else negative],
                       edgecolor="white", linewidth=1.4, zorder=5)
            ax.text(0, y, "+q", color="white", ha="center", va="center", fontsize=10, zorder=6)
            ax.text(distance, y, "+q" if q2 > 0 else "−q", color="white",
                    ha="center", va="center", fontsize=10, zorder=6)
            # Offset arrows from the symbols vertically so their tails and full
            # computed lengths remain visible even at the smallest force.
            for charge, force, offset in [(left, force1, 0.28), (right, force2, 0.52)]:
                start = charge + np.array([0, offset])
                ax.plot([charge[0], start[0]], [y + 0.11, start[1]],
                        color="#9baab5", linewidth=0.9, linestyle=":", zorder=1)
                end = start + 1.3 * force
                ax.annotate("", xy=end, xytext=start,
                            arrowprops={"arrowstyle": "->", "color": force_color,
                                        "lw": 2.2, "shrinkA": 0, "shrinkB": 0,
                                        "mutation_scale": 10})
            label = ["1", "1/4 = 0.250", "1/9 ≈ 0.111"][index]
            ax.text(distance / 2, y - 0.24, r"$r=R$" if distance == 1 else rf"$r={int(distance)}R$",
                    ha="center", va="top", fontsize=11)
            ax.text(1.0, y - 0.53, rf"$|F|/F_0$ = {label}", ha="center", fontsize=11)
        ax.set(xlim=(-1.55, 3.9), ylim=(-0.8, 2.95))
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(heading, fontsize=13, pad=10)
    fig.suptitle("Coulomb force: direction from signs, magnitude from distance", fontsize=15, y=0.97)
    fig.text(0.5, 0.105, r"$F_0=kq^2/R^2$     Equal and opposite forces on each pair; one common arrow scale.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.055, r"Displacement from 1 to 2: $\mathbf{r}=\mathbf{r}_2-\mathbf{r}_1$ (rightward here).",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.18, top=0.83, wspace=0.16)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
