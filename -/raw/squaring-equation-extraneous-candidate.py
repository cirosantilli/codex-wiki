"""Generate squaring-equation-extraneous-candidate.png in the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    x = np.linspace(0, 5.3, 500)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9), dpi=120,
                             facecolor="white")
    original, squared = axes
    original.plot(x, np.sqrt(x), color="#2875ad", linewidth=2.4,
                  label=r"$\sqrt{x}$")
    original.plot(x, x - 2, color="#d4652b", linewidth=2.3, label=r"$x-2$")
    original.axvspan(0, 2, color="#b54c47", alpha=0.08)
    original.scatter([4], [2], color="#23815b", s=65, zorder=4)
    original.plot([1, 1], [-1, 1], color="#b54c47", linestyle="--", linewidth=1.5)
    original.scatter([1, 1], [-1, 1], color="#b54c47", s=40, zorder=4)
    original.annotate("x = 1 fails:\n1 ≠ −1", (1, 0), xytext=(1.65, -0.9),
                      arrowprops={"arrowstyle": "->", "color": "#b54c47"},
                      fontsize=11, color="#973f3b")
    original.set(title=r"Original: $\sqrt{x}=x-2$", ylim=(-2.25, 4.5))
    squared.plot(x, x, color="#2875ad", linewidth=2.4, label=r"$x$")
    squared.plot(x, (x - 2)**2, color="#d4652b", linewidth=2.3,
                 label=r"$(x-2)^2$")
    squared.axvspan(0, 2, color="#b54c47", alpha=0.08)
    squared.scatter([1], [1], color="#b54c47", s=65, zorder=4)
    squared.scatter([4], [4], color="#23815b", s=65, zorder=4)
    squared.annotate("extra candidate", (1, 1), xytext=(1.7, 2.6),
                     arrowprops={"arrowstyle": "->", "color": "#b54c47"},
                     fontsize=11, color="#973f3b")
    squared.annotate("true solution", (4, 4), xytext=(3.25, 6.5),
                     arrowprops={"arrowstyle": "->", "color": "#23815b"},
                     fontsize=11, color="#23815b")
    squared.set(title=r"Squared: $x=(x-2)^2$", ylim=(-0.4, 9.5))
    for ax in axes:
        ax.set(xlim=(0, 5.3), xlabel=r"Input $x$", ylabel="Value of each side")
        ax.legend(loc="upper left", fontsize=11)
        ax.grid(alpha=0.18)
    fig.suptitle("Squaring can erase the sign restriction", fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.23, top=0.83, wspace=0.26)
    fig.text(0.5, 0.06,
             "Shaded x < 2 cannot satisfy the original equation: x − 2 is negative.\n"
             "Keep x ≥ 2 or check both candidates in the original equation.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.savefig(Path.cwd() / "squaring-equation-extraneous-candidate.png",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
