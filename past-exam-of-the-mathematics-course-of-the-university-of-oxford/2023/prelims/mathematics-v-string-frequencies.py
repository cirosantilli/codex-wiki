"""Illustrate both string-frequency equations; write the PNG to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def symmetric_root(n, alpha):
    """Bisection on the positive branch (n*pi, n*pi + pi/2)."""
    left, right = n * np.pi + 1e-10, (n + 0.5) * np.pi
    for _ in range(60):
        mid = (left + right) / 2
        if 1 / np.tan(mid) - alpha * mid > 0:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def main():
    pi = np.pi
    alpha = 1.0
    z = np.linspace(0, 4.1 * pi, 6000)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.2), sharex=True,
                             layout="constrained", facecolor="white")
    axes[0].plot(z / pi, np.sin(z), color="#1577b8", linewidth=1.8,
                 label=r"$\sin z$")
    axes[0].axhline(0, color="#777777", linewidth=0.8)
    axes[0].scatter(np.arange(1, 5), np.zeros(4), color="#c53b32",
                    s=32, zorder=5, label=r"Allowed $z=n\pi$, $n\geq1$")
    axes[0].scatter([0], [0], s=32, facecolor="white", edgecolor="#777777",
                    zorder=5)
    axes[0].annotate("Zero is excluded", xy=(0, 0), xytext=(0.15, 0.6),
                     fontsize=9, arrowprops={"arrowstyle": "->"})
    axes[0].set_title("Antisymmetric modes: the central mass is at rest",
                      loc="left")
    axes[0].set_ylim(-1.4, 1.4)
    axes[0].set_ylabel(r"$\sin z$")
    axes[0].legend(loc="lower left", fontsize=9)

    for n in range(5):
        branch = np.linspace(n * pi + 0.007, (n + 1) * pi - 0.007, 1800)
        axes[1].plot(branch / pi, 1 / np.tan(branch), color="#1577b8",
                     linewidth=1.7, label=r"$\cot z$" if n == 0 else None)
        if n > 0:
            axes[1].axvline(n, color="#bbbbbb", linewidth=0.7,
                            linestyle="--")
    axes[1].plot(z / pi, alpha * z, color="#b27710", linewidth=1.7,
                 label=r"$\alpha z$, illustrated with $\alpha=1$")
    roots = np.array([symmetric_root(n, alpha) for n in range(4)])
    axes[1].scatter(roots / pi, alpha * roots, color="#c53b32", s=32,
                    zorder=5, label="One intersection on each positive branch")
    axes[1].axhline(0, color="#777777", linewidth=0.8)
    axes[1].set_ylim(-2, 13)
    axes[1].set_ylabel("Value")
    axes[1].set_title(r"Symmetric modes: $\cot z=\alpha z$, "
                      r"$\alpha=m/(2\rho\ell)$", loc="left")
    axes[1].legend(loc="upper left", fontsize=9)
    axes[1].set_xlabel(r"$z=k\ell$")
    ticks = np.arange(0, 4.5, 0.5)
    axes[1].set_xticks(ticks, ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$",
                              r"$2\pi$", r"$5\pi/2$", r"$3\pi$",
                              r"$7\pi/2$", r"$4\pi$"])
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlim(0, 4.1)
        ax.grid(alpha=0.18)
    fig.savefig("mathematics-v-string-frequencies.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
