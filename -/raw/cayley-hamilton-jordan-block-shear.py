"""Show why a repeated eigenvalue does not remove a nilpotent shear; emit to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    nilpotent = np.array([[0.0, 1.0], [0.0, 0.0]])
    identity = np.eye(2)
    matrix = 2 * identity + nilpotent
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=float)
    fig, axes = plt.subplots(2, 2, figsize=(10, 5.8), dpi=120, facecolor="white", layout="constrained")
    for ax, n in zip(axes.flat, [0, 1, 4, 8]):
        transformed = identity + n / 2 * nilpotent
        assert np.allclose(np.linalg.matrix_power(matrix, n) / 2**n, transformed)
        points = square @ transformed.T
        ax.fill(points[:, 0], points[:, 1], color="#b7d6f2", alpha=0.7)
        ax.plot(points[:, 0], points[:, 1], color="#1565a8", lw=2)
        ax.plot(square[:, 0], square[:, 1], "--", color="#777777", lw=1)
        ax.annotate("", xy=(n / 2, 1), xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": "#a44c1c", "lw": 2})
        ax.set(xlim=(-0.3, 5.4), ylim=(-0.2, 1.4), xticks=range(6), yticks=[0, 1], title=f"n = {n}: top edge shifts by {n / 2:g}")
        ax.set_aspect("equal", adjustable="box")
        ax.grid(alpha=0.2)
    fig.suptitle(r"$B=2I+N$, $N^2=0$: normalized powers $B^n/2^n=I+(n/2)N$", fontsize=15)
    fig.supxlabel("Horizontal coordinate; dashed outline is the original unit square")
    fig.supylabel("Vertical coordinate")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
