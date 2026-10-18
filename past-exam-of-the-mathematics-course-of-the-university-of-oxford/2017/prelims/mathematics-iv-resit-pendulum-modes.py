"""Draw Question 4(b)'s modes; run in the mirrored _media directory.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5;
dependencies are declared in the repository's pyproject.toml.
Output is written only to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def draw_mode(ax, signs, title, frequency):
    pivots = np.array([0.0, 2.0])
    shifts = 0.24 * np.array(signs)
    bob_y = -np.sqrt(1 - shifts**2)
    ax.plot([-0.45, 2.45], [0, 0], color="black", lw=2)
    for i, (pivot, shift, y) in enumerate(zip(pivots, shifts, bob_y)):
        ax.plot([pivot, pivot], [0, -1.17], "--", color="0.75", lw=1)
        ax.plot([pivot, pivot + shift], [0, y], color="#234e70", lw=2)
        ax.plot(pivot, 0, "ko", ms=4)
        ax.plot(pivot + shift, y, "o", color="#234e70", ms=13)
        ax.annotate("", xy=(pivot + shift, -1.35), xytext=(pivot, -1.35),
                    arrowprops={"arrowstyle": "->", "lw": 2, "color": "#b84724"})
        ax.text(pivot, -1.55, rf"$x_{i+1}$", ha="center", fontsize=12)
    left, right = pivots + shifts
    spring_x = np.linspace(left + 0.10, right - 0.10, 85)
    phase = np.linspace(0, 12 * np.pi, len(spring_x))
    ax.plot(spring_x, bob_y[0] + 0.045 * np.sin(phase), color="#75613a", lw=1.7)
    ax.set_title(title, fontsize=13, pad=8)
    ax.text(1, -1.88, frequency, ha="center", fontsize=14)
    ax.set(xlim=(-0.5, 2.5), ylim=(-2.05, 0.2), aspect="equal")
    ax.axis("off")


if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5), facecolor="white")
    draw_mode(axes[0], (1, 1), "Together: equal displacements", r"$\omega_+=\sqrt{g/\ell}$")
    draw_mode(axes[1], (1, -1), "Opposite: equal and opposite displacements", r"$\omega_-=\sqrt{g/\ell+2k/m}$")
    fig.tight_layout(pad=1.2)
    fig.savefig(Path.cwd() / "mathematics-iv-resit-pendulum-modes.png", dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
