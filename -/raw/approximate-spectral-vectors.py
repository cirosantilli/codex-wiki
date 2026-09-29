"""Write approximate-spectral-vectors.png to cwd; Python 3.14, NumPy, Matplotlib."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def interval(lam, epsilon):
    a, b = max(0.0, lam - epsilon), min(1.0, lam + epsilon)
    length = b - a
    residual = np.sqrt(((b - lam) ** 3 - (a - lam) ** 3) / (3 * length))
    return a, b, length**-0.5, residual


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    colors = ["#1765a8", "#bc570e", "#853795"]
    epsilons = [0.2, 0.1, 0.05]
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 4.7), facecolor="white")
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.23, top=0.77, wspace=0.38)
    fig.suptitle("Concentrate a unit vector to make its spectral residual small", fontsize=15, y=0.96)
    for ax, lam, heading in zip(axes[:2], [0.5, 0.0], ["Interior: λ = 1/2", "Endpoint: λ = 0"]):
        for epsilon, color in zip(epsilons, colors):
            a, b, amplitude, residual = interval(lam, epsilon)
            ax.plot([a, a, b, b], [0, amplitude, amplitude, 0], color=color, lw=2,
                    label=rf"$\varepsilon={epsilon:g}$")
        ax.set_title(heading)
        ax.set_xlim(-0.025, 1.025)
        ax.set_ylim(-0.12, 4.95)
        ax.set_xticks([0, 0.5, 1])
        ax.set_xlabel("x")
        ax.set_ylabel(r"$u_{\lambda,\varepsilon}(x)$")
        ax.text(0.53 if lam == 0 else 0.98, 4.3,
                r"$\int_0^1 |u|^2\,dx=1$", ha="center" if lam == 0 else "right", fontsize=11)
        ax.grid(color="#e7ebef", lw=0.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(loc="upper left", fontsize=10, frameon=False)
    ax = axes[2]
    epsilon_grid = np.linspace(0, 0.22, 200)
    ax.plot(epsilon_grid, epsilon_grid, "--", color="#919ba5", lw=1.5, label=r"Bound $\varepsilon$")
    ax.plot(epsilon_grid, epsilon_grid / np.sqrt(3), color="#3e4954", lw=2,
            label=r"Exact $\varepsilon/\sqrt{3}$")
    for epsilon, color in zip(epsilons, colors):
        ax.scatter([epsilon], [interval(0.5, epsilon)[3]], color=color, s=65, zorder=5)
    ax.set_title("Residual for both panels")
    ax.set_xlabel(r"Interval radius $\varepsilon$")
    ax.set_ylabel(r"$\|(M-\lambda I)u\|_2$")
    ax.set_xlim(0, 0.22)
    ax.set_ylim(0, 0.23)
    ax.set_xticks([0, 0.1, 0.2])
    ax.grid(color="#e7ebef", lw=0.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    fig.text(0.5, 0.09, r"Amplitude = (interval length)$^{-1/2}$; clipping at an endpoint halves the interval length.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.025, "Every vector has norm one, but no nonzero L² eigenvector exists at the limit.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "approximate-spectral-vectors.png", dpi=145, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
