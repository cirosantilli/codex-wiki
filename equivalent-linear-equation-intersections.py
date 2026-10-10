"""Generate equivalent-linear-equation-intersections.png in the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    x = np.linspace(0, 5, 250)
    fig, axes = plt.subplots(1, 3, figsize=(10.6, 4.8), dpi=120,
                             facecolor="white")
    examples = [
        (2 * x + 3, 9, r"$2x+3=9$", r"$L(x)=2x+3$", r"$R(x)=9$"),
        (2 * x, 6, r"$2x=6$", r"$L(x)=2x$", r"$R(x)=6$"),
        (x, 3, r"$x=3$", r"$L(x)=x$", r"$R(x)=3$"),
    ]
    for ax, (left, right, title, lhs, rhs) in zip(axes, examples):
        ax.plot(x, left, color="#2875ad", linewidth=2.4, label=lhs)
        ax.axhline(right, color="#d4652b", linewidth=2.2, label=rhs)
        ax.scatter([3], [right], color="#23815b", s=65, zorder=4)
        ax.axvline(3, color="#23815b", linestyle="--", linewidth=1.1, alpha=0.8)
        ax.set(title=title, xlabel=r"Input $x$", ylabel="Value of each side",
               xlim=(0, 5), ylim=(0, 14), xticks=[0, 1, 2, 3, 4, 5])
        ax.legend(loc="upper left", fontsize=10)
        ax.grid(alpha=0.18)
    fig.suptitle("Different comparisons, the same solution", fontsize=16, y=0.98)
    fig.text(0.385, 0.83, "subtract 3\nfrom both sides", ha="center", fontsize=10)
    fig.text(0.706, 0.83, "divide both\nsides by 2", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.20, top=0.76, wspace=0.34)
    fig.text(0.5, 0.065, "Each reversible step preserves the solution set {3}.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "equivalent-linear-equation-intersections.png",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
