"""Original oscillator paths and thermal ratios; tested with Python 3.14.

Dependencies are declared in the repository's root pyproject.toml.
The sole generated artifact is a PNG in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.0), layout="constrained")
    fig.set_facecolor("white")
    t = np.linspace(0, 1, 501)
    q = np.linspace(-3.4, 3.4, 601)
    for z, color, label in [
        (0.3, "#2879b9", r"$z=0.3$ (hot)"),
        (2.0, "#bd661a", r"$z=2$"),
        (8.0, "#38814c", r"$z=8$ (cold)"),
    ]:
        path = np.cosh(z * (t - 0.5)) / np.cosh(z / 2)
        ratio = np.exp(-q**2 * np.tanh(z / 2))
        axes[0].plot(t, path, color=color, linewidth=2.3, label=label)
        axes[1].plot(q, ratio, color=color, linewidth=2.3, label=label)
    axes[0].set(
        title="Stationary paths with equal endpoints",
        xlabel=r"Imaginary time $\tau/(\beta\hbar)$",
        ylabel=r"$x_0(\tau)/x$",
        xlim=(0, 1),
        ylim=(0, 1.04),
    )
    axes[1].set(
        title="Diagonal kernel relative to its center",
        xlabel=r"Position $q=x\sqrt{m\omega/\hbar}$",
        ylabel=r"$R=\exp[-q^2\tanh(z/2)]$",
        xlim=(-3.4, 3.4),
        ylim=(0, 1.04),
    )
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(frameon=False, loc="lower left")
    fig.suptitle(r"Thermal harmonic oscillator: $z=\beta\hbar\omega$", fontsize=15)
    fig.savefig(
        Path.cwd() / Path(__file__).with_suffix(".png").name,
        dpi=120,
        facecolor="white",
        transparent=False,
        metadata={"Software": "Matplotlib"},
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
