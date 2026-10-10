"""Deterministic Q-Q example; write an opaque basename PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path
from statistics import NormalDist

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 19
    p = (np.arange(1, n + 1) - 0.5) / n
    z = np.array([NormalDist().inv_cdf(float(level)) for level in p])
    a = 10 + 2 * z
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=110)
    line = np.linspace(-2.15, 2.15, 301)
    axes[0].plot(line, 10 + 2 * line, color="#b45320", lw=2,
                 label=r"Specified line: $a=10+2z$")
    axes[0].scatter(z, a, s=33, color="#246bce", zorder=3,
                    label="19 constructed values")
    axes[0].set(ylabel=r"Ordered value $a_i$", ylim=(5.5, 14.5))
    axes[0].set_title("Location 10, scale 2", fontsize=13)
    axes[1].plot(line, line, color="#b45320", lw=2,
                 label=r"Identity line: $y=z$")
    axes[1].scatter(z, (a - 10) / 2, s=33, color="#246bce", zorder=3,
                    label="Same 19 values rescaled")
    axes[1].set(ylabel=r"Rescaled value $(a_i-10)/2$", ylim=(-2.15, 2.15))
    axes[1].set_aspect("equal", adjustable="box")
    axes[1].set_title("Remove the specified location and scale", fontsize=13)
    for ax in axes:
        ax.set(xlabel=r"Standard normal reference quantile $z_i$", xlim=(-2.15, 2.15))
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper left", frameon=False, fontsize=9)
    fig.suptitle("A straight Q-Q plot need not follow the identity line",
                 fontsize=15, weight="bold", y=0.97)
    fig.text(0.5, 0.035,
             r"$p_i=(i-1/2)/19$, $z_i=\Phi^{-1}(p_i)$: constructed examples, not random draws.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.17, top=0.80, wspace=0.34)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
