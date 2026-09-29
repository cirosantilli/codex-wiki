"""Original heat convolution plot. Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-5, 5, 900)
    y = np.linspace(-2, 2, 2401)
    initial_y = np.maximum(1 - np.abs(y) / 2, 0)
    fig, ax = plt.subplots(figsize=(7.2, 4.4), facecolor="white")
    ax.set_facecolor("white")
    ax.plot(x, np.maximum(1 - np.abs(x) / 2, 0), color="#333333", lw=2,
            label="Initial profile")
    for t, color in [(0.1, "#2563a5"), (0.5, "#c4791e"), (2, "#38825b")]:
        kernel = np.exp(-(x[:, None] - y[None, :]) ** 2 / (4 * t)) / np.sqrt(4 * np.pi * t)
        u = np.trapezoid(kernel * initial_y[None, :], y, axis=1)
        ax.plot(x, u, color=color, lw=2, label=f"t = {t:g}")
    ax.set(xlabel="x", ylabel="u(t, x)", xlim=(-5, 5), ylim=(0, 1.05),
           title="Heat flow smooths a triangular profile")
    ax.spines[["right", "top"]].set_visible(False)
    ax.grid(alpha=0.15)
    ax.legend()
    fig.tight_layout()
    fig.savefig(Path.cwd() / "2014-triangular-heat-flow.png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
