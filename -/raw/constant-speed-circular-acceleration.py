"""Generate constant-speed-circular-acceleration.png in the working directory.

Uses only the repository's NumPy and Matplotlib dependencies.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: python ../constant-speed-circular-acceleration.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radius, omega = 2.0, 0.5
    theta = np.linspace(0, 2 * np.pi, 401)
    angles = np.arange(4) * np.pi / 2
    positions = radius * np.column_stack((np.cos(angles), np.sin(angles)))
    velocities = radius * omega * np.column_stack((-np.sin(angles), np.cos(angles)))
    accelerations = -omega**2 * positions
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.8), facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.19, top=0.77, wspace=0.25)
    fig.suptitle("Constant speed still allows acceleration", fontsize=19, y=0.97)
    fig.text(0.5, 0.89, r"Counterclockwise: $R=2$ m, $\omega=0.5$ rad/s", ha="center", fontsize=14)
    times = [r"$t=0$ s", r"$t=\pi$ s", r"$t=2\pi$ s", r"$t=3\pi$ s"]
    labels_xy = [(2.28, -0.4), (0.18, 2.35), (-2.8, -0.4), (0.18, -2.65)]
    for ax, vectors, scale, color, title in (
        (axes[0], velocities, 1, "#2368ac", "Velocity: always tangent\nMagnitude 1 m/s"),
        (axes[1], accelerations, 2, "#bf5224", "Acceleration: always inward\nMagnitude 0.5 m/s²"),
    ):
        ax.plot(radius * np.cos(theta), radius * np.sin(theta), color="#9aa4ad", lw=1.6)
        ax.axhline(0, color="#e1e4e8", lw=1, zorder=0)
        ax.axvline(0, color="#e1e4e8", lw=1, zorder=0)
        ax.scatter(*positions.T, color="#333333", s=28, zorder=4)
        ax.scatter(0, 0, color="#777777", s=16)
        for point, vector in zip(positions, vectors):
            ax.annotate("", xy=point + scale * vector, xytext=point,
                        arrowprops={"arrowstyle": "-|>", "lw": 2.6, "color": color,
                                    "mutation_scale": 17})
        for label, xy in zip(times, labels_xy):
            ax.text(*xy, label, fontsize=11)
        ax.set(xlim=(-3.05, 3.05), ylim=(-3.05, 3.05), xlabel="x (m)", ylabel="y (m)")
        ax.set_xticks([-2, 0, 2])
        ax.set_yticks([-2, 0, 2])
        ax.set_aspect("equal")
        ax.set_title(title, color=color, fontsize=13, pad=14)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
    fig.text(0.5, 0.055, "Arrow scales differ between panels; each panel preserves vector directions and relative lengths.",
             ha="center", fontsize=11)
    fig.savefig("constant-speed-circular-acceleration.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
