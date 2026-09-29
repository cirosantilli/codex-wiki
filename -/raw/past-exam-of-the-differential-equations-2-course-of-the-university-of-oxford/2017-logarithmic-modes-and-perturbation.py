"""Generate 2017-logarithmic-modes-and-perturbation.png in the current directory.

Dependencies: repository pyproject.toml (NumPy, Matplotlib), Python 3.14.
The right panel solves the linear boundary value problem by independent RK4
shooting; all curves and the diagram are original calculations.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def solve_boundary_value(epsilon, steps=1600):
    x = np.linspace(0.0, 1.0, steps + 1)
    states = np.empty((steps + 1, 4))
    states[0] = [2 * np.exp(epsilon), 0, 0, 1]

    def rhs(t, z):
        return np.array([z[1], -(t * z[1] + epsilon * z[0]) / (t + 1),
                         z[3], -(t * z[3] + epsilon * z[2]) / (t + 1)])

    step = 1.0 / steps
    for j, t in enumerate(x[:-1]):
        z = states[j]
        k1 = rhs(t, z)
        k2 = rhs(t + step / 2, z + step * k1 / 2)
        k3 = rhs(t + step / 2, z + step * k2 / 2)
        k4 = rhs(t + step, z + step * k3)
        states[j + 1] = z + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    slope = (3 / np.e - states[-1, 0]) / states[-1, 2]
    return x, states[:, 0] + slope * states[:, 2], slope


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.3), dpi=110, facecolor="white")
    t = np.linspace(0, 1, 801)
    colors = ["#2563eb", "#b45309", "#15803d"]
    for k, color in zip([1, 2, 3], colors):
        axes[0].plot(t, np.sin(k * np.pi * t), lw=2, color=color, label=rf"$k={k}$")
    axes[0].set_xlabel(r"$t=\log x$")
    axes[0].set_ylabel(r"$\widehat y_k(x)/x$")
    axes[0].set_title("Logarithmic coordinates expose sine modes", fontsize=11)
    axes[0].set_xlim(0, 1)
    axes[0].set_ylim(-1.15, 1.15)
    axes[0].axhline(0, color="#64748b", lw=0.7)
    axes[0].legend(ncol=3, fontsize=9, loc="lower center")

    x = np.linspace(0, 1, 801)
    axes[1].plot(x, (x + 2) * np.exp(-x), color="#111827", lw=2.4,
                 label=r"$y_0=(x+2)e^{-x}$")
    for epsilon, color in [(0.05, "#2563eb"), (0.1, "#b45309")]:
        grid, y, _ = solve_boundary_value(epsilon)
        axes[1].plot(grid, y, color=color, lw=1.8, ls="--",
                     label=rf"$\epsilon={epsilon:g}$")
    axes[1].set_title("Small parameter, smoothly changing solution", fontsize=11)
    axes[1].set_xlabel(r"$x$")
    axes[1].set_ylabel(r"$y(x)$")
    axes[1].set_xlim(0, 1)
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.17)
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(pad=1.5, w_pad=2.8)
    fig.savefig("2017-logarithmic-modes-and-perturbation.png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
