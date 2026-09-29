"""Plot original power-family curves and exact Hardy norm contributions.

Output matching PNG in the CWD. Tested with Python 3.14, NumPy 2.3.5
and Matplotlib 3.10.7. No endpoint a=1/2 is evaluated as an L2 function.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained",
                             facecolor="white")
    inner = np.geomspace(1e-4, 1, 500)
    tail = np.geomspace(1, 4, 160)
    colors = ["#2463a4", "#2a8084", "#b64c0b"]
    for a, color in zip([0, .25, .49], colors):
        axes[0].loglog(inner, inner ** -a, color=color, lw=1.8, ls="--")
        axes[0].loglog(inner, inner ** -a / (1 - a), color=color, lw=2.3,
                        label=fr"$a={a:g}$")
        axes[0].loglog(tail, 1 / ((1 - a) * tail), color=color, lw=2.3)
    axes[0].axvline(1, color="#777777", lw=1, ls=":")
    axes[0].set(xlabel=r"$x$ (log scale)", ylabel="Value (log scale)",
                 title=r"$f_a=x^{-a}\mathbf{1}_{(0,1)}$, $0\leq a<1/2$",
                 xlim=(1e-4, 4), ylim=(.2, 220))
    handles, labels = axes[0].get_legend_handles_labels()
    handles += [Line2D([], [], color="#333333", ls="--", label=r"Input $f_a$"),
                Line2D([], [], color="#333333", label=r"Average $Hf_a$")]
    axes[0].legend(handles=handles, loc="upper right", fontsize=10)
    a = np.linspace(0, .4995, 800)
    inner_ratio = 1 / (1 - a) ** 2
    tail_ratio = (1 - 2 * a) / (1 - a) ** 2
    total = inner_ratio + tail_ratio
    axes[1].fill_between(a, 0, inner_ratio, color="#2a8084", alpha=.3,
                         label="Inner contribution")
    axes[1].fill_between(a, inner_ratio, total, color="#e4a33c", alpha=.5,
                         label="Tail contribution")
    axes[1].plot(a, total, color="#333333", lw=2.3,
                 label=r"Total $2/(1-a)$")
    axes[1].axhline(4, color="#b64c0b", ls="--", lw=1.5)
    axes[1].plot([.5], [4], "o", ms=8, mfc="white", mec="#b64c0b", mew=2)
    axes[1].annotate("Limit 4\nEndpoint excluded", xy=(.5, 4),
                     xytext=(.27, 4.34), fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "#b64c0b"})
    axes[1].set(xlabel=r"$a$", ylabel=r"Contribution to $\|Hf_a\|_2^2/\|f_a\|_2^2$",
                 title="Both portions count toward sharpness",
                 xlim=(0, .53), ylim=(0, 4.9))
    axes[1].legend(loc="upper left", fontsize=10)
    axes[1].grid(axis="y", alpha=.16)
    fig.supxlabel("Curves start at x = 0.0001; norm contributions integrate over all (0, infinity).",
                  fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
