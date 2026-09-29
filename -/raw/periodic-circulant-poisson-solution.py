"""A balanced discrete Poisson problem on a four-node ring; output to CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def draw_ring(ax, values, title, symbol):
    points = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]], dtype=float)
    for n in range(4):
        a, b = points[n], points[(n + 1) % 4]
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#a0a0a0", lw=2, zorder=1)
    for n, ((px, py), value) in enumerate(zip(points, values)):
        color = "#dcebf8" if value > 0 else "#f8e2d5" if value < 0 else "#f0f0f0"
        ax.add_patch(Circle((px, py), 0.22, facecolor=color,
                            edgecolor="#343434", lw=1.5, zorder=2))
        ax.text(px, py, f"{value:g}", ha="center", va="center",
                fontsize=15, zorder=3)
        ax.text(px * 1.32, py * 1.38, f"n = {n}",
                ha="left" if px > 0 else "right" if px < 0 else "center",
                va="center", fontsize=11)
    ax.set_title(title, fontsize=14, pad=8)
    ax.text(0, 0, symbol, ha="center", va="center", fontsize=16)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.65, 1.65)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    n = np.arange(4)
    column = np.array([2.0, -1.0, 0.0, -1.0])
    laplacian = column[(n[:, None] - n[None, :]) % 4]
    forcing = np.array([1.0, 0.0, -1.0, 0.0])
    eigenvalues = np.fft.fft(column)
    rhs = np.fft.fft(forcing)
    spectrum = np.zeros(4, dtype=complex)
    nonzero = np.abs(eigenvalues) > 1e-12
    assert np.allclose(rhs[~nonzero], 0)
    spectrum[nonzero] = rhs[nonzero] / eigenvalues[nonzero]
    solution = np.fft.ifft(spectrum).real
    assert np.allclose(solution, [0.5, 0, -0.5, 0])
    assert np.allclose(laplacian @ solution, forcing)
    assert np.isclose(solution.mean(), 0)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2), dpi=110)
    fig.patch.set_facecolor("white")
    draw_ring(axes[0], forcing, "Forcing: total is zero", "b")
    draw_ring(axes[1], solution, "Solution: mean is zero", "x")
    fig.suptitle("Discrete Poisson balance on a four-node ring", fontsize=16)
    fig.text(0.5, 0.105, r"$2x_n-x_{n-1}-x_{n+1}=b_n$ (indices modulo four)",
             ha="center", fontsize=14)
    fig.text(0.5, 0.045,
             "At n = 0: 2(0.5) − 0 − 0 = 1. "
             "Adding the same constant to every x leaves b unchanged.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.18,
                        top=0.86, wspace=0.05)
    fig.savefig(Path.cwd() / "periodic-circulant-poisson-solution.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
