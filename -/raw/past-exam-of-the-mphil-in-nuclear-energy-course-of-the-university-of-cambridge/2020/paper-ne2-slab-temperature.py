"""Original normalized conduction profiles; Python 3.14, numpy, matplotlib.

Output goes to the current working directory, as required by the media Make rule.
All curves follow the derived analytical solution; no source figure is copied.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def temperature_profile(xi, beta):
    """Return k(T-T0)/(q0*a**2) for equal face temperatures."""
    xi = np.asarray(xi)
    if beta == 0:
        return xi * (1 - xi) / 2
    return (-np.expm1(-beta * xi) + np.expm1(-beta) * xi) / beta**2


def peak_location(beta):
    """Return x_max/a, including the uniform-source limit."""
    if beta == 0:
        return 0.5
    return -np.log(-np.expm1(-beta) / beta) / beta


def main():
    xi = np.linspace(0, 1, 1001)
    fig, ax = plt.subplots(figsize=(6.8, 4.4), layout="constrained")
    fig.set_facecolor("white")
    colors = ["#253858", "#007f91", "#a35012", "#8b3a82"]
    for beta, color in zip((0, 1, 3, 8), colors, strict=True):
        label = r"$\beta=0$ (uniform limit)" if beta == 0 else rf"$\beta={beta}$"
        ax.plot(xi, temperature_profile(xi, beta), color=color, lw=2.1, label=label)
        xm = peak_location(beta)
        ax.scatter(xm, temperature_profile(xm, beta), color=color, s=30, zorder=4)
    ax.set(xlim=(0, 1), ylim=(0, 0.135),
           xlabel=r"Position $\xi=x/a$ from illuminated face",
           ylabel=r"Temperature rise $\theta=k(T-T_0)/(q_0a^2)$",
           title=r"Slab heating with $\beta=\mu a$")
    ax.text(0.98, 0.97, r"Fixed $q_0$, $a$ and $k$; vary $\mu$",
            transform=ax.transAxes, ha="right", va="top", fontsize=9)
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left", bbox_to_anchor=(0.015, 0.88), frameon=False, fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig("paper-ne2-slab-temperature.png", dpi=165, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
