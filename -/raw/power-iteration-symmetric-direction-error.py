"""Exact symmetric power iterates; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
    fig, (direction, error) = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained")
    fig.suptitle("Power iteration: a component ratio shrinks by 1/3 per step", fontsize=14)
    A = np.array([[2, 1], [1, 2]], dtype=float)
    u = np.array([1, 1]) / np.sqrt(2)
    v = np.array([1, -1]) / np.sqrt(2)
    k = np.arange(9)
    t = 3.0 ** (-k)
    q = (u[None, :] + t[:, None] * v[None, :]) / np.sqrt(1 + t[:, None] ** 2)
    circle = np.linspace(0, np.pi / 2, 200)
    direction.plot(np.cos(circle), np.sin(circle), color="0.75", lw=1)
    direction.plot([0, 1.02 * u[0]], [0, 1.02 * u[1]], "--", color="#1b7b45", lw=2)
    colors = ["#414487", "#2a788e", "#22a884", "#d08a00"]
    offsets = [(0, -23), (13, -5), (20, 0), (20, 10)]
    for j, color, offset in zip([0, 1, 2, 4], colors, offsets):
        direction.annotate("", xy=q[j], xytext=(0, 0),
                           arrowprops={"arrowstyle": "->", "lw": 2, "color": color})
        direction.annotate(f"k = {j}", xy=q[j], xytext=offset,
                           textcoords="offset points", color=color)
    direction.text(0.03, 1.01, "A = [[2, 1], [1, 2]]\nx₀ = (1, 0)ᵀ", va="top")
    direction.text(0.12, 0.69, "dominant line\ny = x", color="#1b7b45")
    direction.set(xlim=(-0.08, 1.18), ylim=(-0.14, 1.13), xlabel="first coordinate",
                  ylabel="second coordinate", title="Normalized iterate directions")
    direction.set_aspect("equal")
    direction.axhline(0, color="0.75", lw=0.8)
    direction.axvline(0, color="0.75", lw=0.8)
    direction.spines[["top", "right"]].set_visible(False)
    rho = np.einsum("ij,ij->i", q, q @ A.T)
    residual = np.linalg.norm(q @ A.T - rho[:, None] * q, axis=1)
    epsilon = np.abs(q @ v)
    error.semilogy(k, epsilon, "o-", color="#414487", label="direction error: sin θₖ")
    error.semilogy(k, 3 - rho, "s-", color="#d08a00", label="Rayleigh error: 3 − ρₖ")
    error.semilogy(k, residual, "^-", color="#2a788e", label="residual norm: ‖rₖ‖₂")
    error.set(xlabel="iteration k", ylabel="error (log scale)", xticks=k,
              title="Exact errors, computed from the iterates")
    error.grid(which="major", alpha=0.25)
    error.legend(loc="upper right", fontsize=9)
    error.text(0.04, 0.08, "tan θₖ = 3⁻ᵏ\nRayleigh error decays twice as fast", transform=error.transAxes)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
