"""Oxford A10 (2017), question 3(c): actual first-order particle orbits.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository root pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    k = d = g = 1.0
    a = 0.025
    phase = np.linspace(0, -2 * np.pi, 600)
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 4.6), facecolor="white", sharey=True)
    for ax, c2 in zip(axes, [0.3, 2.0], strict=True):
        b = a * k * c2 / (k * c2 * np.cosh(k * d) - g * np.sinh(k * d))
        x = np.linspace(-0.2, 1.3, 500)
        ax.plot(x, b * np.sin(k * x), color="#176b93", lw=1.6, label="Surface at $t=0$")
        ax.plot(x, -d + a * np.sin(k * x), color="#b4591c", lw=1.6, label="Bed at $t=0$")
        ax.axhline(0, color="0.6", ls="--", lw=0.8)
        ax.axhline(-d, color="0.6", ls="--", lw=0.8)
        for mean_x, mean_y in zip([0.0, 0.33, 0.66, 0.99], [-0.85, -0.6, -0.35, -0.1], strict=True):
            horizontal = b * (g / (k * c2) * np.cosh(k * mean_y) + np.sinh(k * mean_y))
            vertical = b * (g / (k * c2) * np.sinh(k * mean_y) + np.cosh(k * mean_y))
            orbit_x = mean_x + horizontal * np.cos(phase)
            orbit_y = mean_y + vertical * np.sin(phase)
            ax.plot(orbit_x, orbit_y, color="#37474f", lw=1.6)
            ax.plot(mean_x, mean_y, ".", color="0.6", ms=3)
            # Increasing physical time decreases phase for c>0.
            ax.annotate("", xy=(orbit_x[125], orbit_y[125]), xytext=(orbit_x[80], orbit_y[80]),
                        arrowprops={"arrowstyle": "->", "color": "#37474f", "lw": 1.2,
                                    "mutation_scale": 9})
            ax.text(mean_x, mean_y - 0.083, f"$\\bar y={mean_y:g}$", ha="center", fontsize=8)
        regime = "Below resonance" if c2 < g / k * np.tanh(k * d) else "Above resonance"
        ax.set(title=f"{regime}: $c^2={c2:g}$\n$b/a={b/a:.3f}$",
               xlabel="$x$", xlim=(-0.2, 1.3), ylim=(-1.10, 0.13), aspect="equal")
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("$y$")
    axes[1].legend(loc="lower right", fontsize=8, frameon=False)
    fig.suptitle("Bottom-forced particle orbits: $k=d=g=1$, $a=0.025$", fontsize=12)
    fig.tight_layout()
    output = Path.cwd()
    fig.savefig(output / Path(__file__).with_suffix(".png").name, dpi=170,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
