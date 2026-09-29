"""Draw eigenvalue-iteration.png in cwd; Python 3.14, NumPy, Matplotlib."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.6), facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.19, top=0.76, wspace=0.43)
    fig.suptitle("Repeated maps separate growth from direction", y=0.97, fontsize=16)
    fig.text(0.5, 0.87, "A = [[2, 1], [1, 2]]    starting vector x₀ = (1, 0)", ha="center", fontsize=12)

    a = np.array([[2.0, 1.0], [1.0, 2.0]])
    states = [np.array([1.0, 0.0])]
    for _ in range(6):
        states.append(a @ states[-1])

    ax = axes[0]
    ax.set_title("Directions after normalization")
    ax.set_aspect("equal")
    ax.set_xlim(-0.1, 1.3)
    ax.set_ylim(-0.85, 1.15)
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks([-0.5, 0, 0.5, 1])
    ax.grid(color="#e3e7eb", lw=0.7)
    ax.axhline(0, color="#a2aab2", lw=0.8)
    ax.axvline(0, color="#a2aab2", lw=0.8)
    ax.plot([0, 1.04], [0, 1.04], ls="--", color="#1765a8", lw=1.4)
    ax.text(0.78, 1.02, r"$E_3$: y = x", color="#1765a8")
    ax.plot([0, 0.74], [0, -0.74], ls="--", color="#9a357a", lw=1.4)
    ax.annotate("Starting in E₁\nstays on y = −x", xy=(0.60, -0.60), xytext=(0.12, -0.82), fontsize=10, color="#9a357a", arrowprops={"arrowstyle": "->", "color": "#9a357a"})
    colors = ["#a65300", "#788d21", "#139e90", "#1765a8"]
    offsets = [(7, -5), (9, 0), (13, -3), (-47, 8)]
    for n, color, offset in zip([0, 1, 2, 5], colors, offsets):
        v = states[n] / np.linalg.norm(states[n])
        ax.annotate("", xy=v, xytext=(0, 0), arrowprops={"arrowstyle": "->", "lw": 2.1, "color": color, "mutation_scale": 15})
        ax.annotate(f"n = {n}", xy=v, xytext=offset, textcoords="offset points", color=color, fontsize=10)
    ax.set_xlabel("x component")
    ax.set_ylabel("y component")

    ax = axes[1]
    ax.set_title("Components in the eigenbasis")
    n = np.arange(7)
    c3 = 3.0**n / 2
    c1 = np.full_like(c3, 0.5)
    ax.semilogy(n, c3, "o-", color="#1765a8", lw=2.2, label=r"$c_3=3^n/2$: growing")
    ax.semilogy(n, c1, "s-", color="#9a357a", lw=2.2, label=r"$c_1=1/2$: unchanged")
    ax.set_ylim(0.23, 1000)
    ax.set_xticks(n)
    ax.set_xlabel("Number of applications n")
    ax.set_ylabel("Coefficient (log scale)")
    ax.grid(color="#e3e7eb", which="major", lw=0.7)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.text(0.97, 0.11, r"$c_1/c_3=3^{-n}$", transform=ax.transAxes, ha="right", fontsize=12)
    fig.text(0.5, 0.035, r"$A^n x_0=c_3(1,1)^T+c_1(1,-1)^T$; normalization removes length, revealing alignment.", ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "eigenvalue-iteration.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
