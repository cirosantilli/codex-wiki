"""Illustrate the classical cubic-quartic potential; output PNG to cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def potential(phi, cubic):
    return phi**2 / 2 - cubic * phi**3 / 6 + phi**4 / 24


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.4), layout="constrained")
    field = np.linspace(-0.6, 5.2, 1201)
    cases = [(1.0, "Stable origin", r"$\mu=1$", (-0.4, 6)), (np.sqrt(3), "Degenerate vacua", r"$\mu=\sqrt{3}$", (-0.2, 1.2)), (2.0, "Metastable origin", r"$\mu=2$", (-4, 1.6))]
    for ax, (cubic, title, label, limits) in zip(axes, cases):
        ax.plot(field, potential(field, cubic), color="#2468ad", lw=2)
        ax.axhline(0, color="#a2a6ad", lw=0.8, ls="--")
        ax.set(xlabel=r"Field $\phi$", ylabel=r"Potential $V(\phi)$", title=title + "\n" + label, xlim=(-0.6, 5.2), ylim=limits)
        ax.grid(alpha=0.18)
        if cubic < np.sqrt(3) + 1e-10:
            minima = [0.0] if cubic < np.sqrt(3) - 1e-10 else [0.0, 2 * cubic]
            ax.scatter(minima, [potential(x, cubic) for x in minima], color="#202830", s=30, zorder=4)
        else:
            minimum = (3 * cubic + np.sqrt(9 * cubic**2 - 24)) / 2
            ax.scatter([minimum], [potential(minimum, cubic)], color="#202830", s=30, zorder=4)
            ax.scatter([0], [0], facecolors="white", edgecolors="#d06b23", s=40, linewidths=1.8, zorder=4)
            ax.annotate("False vacuum", (0, 0), xytext=(0.7, 1.0), arrowprops={"arrowstyle": "->", "color": "#d06b23"})
    fig.suptitle(r"Classical scalar potential with $m^2=\lambda=1$", fontsize=12)
    fig.savefig(Path.cwd() / "paper-49-scalar-vacua.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
