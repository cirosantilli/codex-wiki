"""Linear Rayleigh-Taylor interface growth, not a nonlinear simulation."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 4 * np.pi, 601)
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.6), sharey=True, layout="constrained")
    for ax, amplitude, title in zip(axes, [0.08, 0.40], ["Initial perturbation", "Later linear growth"]):
        eta = amplitude * np.cos(x)
        ax.fill_between(x, eta, 1, color="#b8b5d9")
        ax.fill_between(x, -1, eta, color="#cce7f2")
        ax.plot(x, eta, color="#51477e", lw=2)
        ax.text(np.pi, 0.77, r"Heavy fluid $\rho_h$", ha="center")
        ax.text(np.pi, -0.80, r"Light fluid $\rho_l$", ha="center")
        ax.annotate(r"$g$", xy=(3.5 * np.pi, 0.12), xytext=(3.5 * np.pi, 0.72),
                    ha="center", arrowprops={"arrowstyle": "->", "lw": 1.6})
        ax.set(xlim=(0, 4 * np.pi), ylim=(-1, 1), title=title, xlabel="Horizontal position", xticks=[], yticks=[])
    fig.suptitle(r"Rayleigh-Taylor instability: $\eta\propto e^{\sigma t}\cos(kx)$, $\sigma^2=gk(\rho_h-\rho_l)/(\rho_h+\rho_l)$", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
