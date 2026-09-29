"""Population influence curves for two normal location-scale models.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output basename matches this root generator.
"""

from math import erf, sqrt
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k = 1.345
    normalization = erf(k / sqrt(2))
    colors = ["#2166ac", "#b35806", "#1b7837"]
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.3), layout="constrained")
    for ax, mu, sigma in zip(axes, [0.0, 3.0], [1.0, 2.0]):
        x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 801)
        z = (x - mu) / sigma
        ax.plot(x, x - mu, color=colors[0], label="Mean", lw=2.2)
        # The jump has no connecting vertical segment; the derivative at mu is 0.
        for sign in [-1, 1]:
            mask = sign * z > 0
            ax.plot(x[mask], sigma * sqrt(np.pi / 2) * np.sign(z[mask]),
                    color=colors[1], lw=2.2,
                    label="Median" if sign == -1 else None)
        ax.scatter([mu], [0], color=colors[1], s=28, zorder=5)
        ax.plot(x, sigma * np.clip(z, -k, k) / normalization,
                color=colors[2], lw=2.2, label=f"Huber, k = {k}")
        ax.axhline(0, color="#777777", lw=0.7)
        ax.axvline(mu, color="#777777", lw=0.7)
        ax.set(title=rf"$F = N({mu:g}, {sigma:g}^2)$; fixed scale $s={sigma:g}$",
               xlabel="Contamination location x", ylabel="Influence IF(x; T, F)")
        ax.grid(alpha=0.2)
        ax.legend(loc="upper left", fontsize=9)
    fig.suptitle("Normal-location influence: an unbounded mean and bounded alternatives", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
