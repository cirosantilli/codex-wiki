"""Deterministic Q-Q curvature examples; write an opaque basename PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from math import pi, sqrt
from pathlib import Path
from statistics import NormalDist

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 19
    p = (np.arange(1, n + 1) - 0.5) / n
    z = np.array([NormalDist().inv_cdf(float(level)) for level in p])
    b = 2 * p - 1
    c = np.sinh(0.7 * z)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=110)
    line = np.linspace(-2.1, 2.1, 301)
    examples = [
        (b, sqrt(2 / pi), "#246bce", r"Uniform quantiles $b_i=2p_i-1$",
         r"$b=\sqrt{2/\pi}\,z$", "Outer quantiles bend inward"),
        (c, 0.7, "#b45320", r"Constructed $c_i=\sinh(0.7z_i)$",
         r"$c=0.7z$", "Outer quantiles bend outward"),
    ]
    for ax, (values, slope, color, label, tangent, title) in zip(axes, examples):
        ax.plot(line, slope * line, color="#626262", ls="--", lw=1.8,
                label="Central tangent: " + tangent)
        ax.scatter(z, values, color=color, s=33, zorder=3, label=label)
        ax.scatter([z[0], z[-1]], [values[0], values[-1]],
                   s=80, facecolors="none", edgecolors=color, zorder=4)
        ax.set(xlabel=r"Standard normal reference quantile $z_i$",
               ylabel="Constructed ordered value", xlim=(-2.1, 2.1), ylim=(-2.05, 2.65))
        ax.set_title(title, fontsize=13)
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper left", frameon=False, fontsize=9)
        ax.annotate(f"{values[-1]:.6f}", (z[-1], values[-1]),
                    xytext=(-65, 13), textcoords="offset points", fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": color}, color=color)
    fig.suptitle("Normal Q-Q plots: compare outer quantiles to the central slope",
                 fontsize=14, weight="bold", y=0.97)
    fig.text(0.5, 0.035,
             r"19 deterministic points per panel; $p_i=(i-1/2)/19$. Dashed lines are not uncertainty bands.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.17, top=0.80, wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
