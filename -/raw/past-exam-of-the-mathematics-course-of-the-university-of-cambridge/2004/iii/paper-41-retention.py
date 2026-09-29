"""Pareto reinsurance variance sketch.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root dependencies).
Writes paper-41-retention.png to caller CWD; caller MPLCONFIGDIR is honored.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7.4, 4.1), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    left = np.linspace(0, 1, 301)
    right = np.linspace(1, 5, 500)
    ax.plot(left, 3 - 3 * left + 2 * left**2, color="#0066a3", lw=2.6,
            label=r"$0\leq M/d\leq1$")
    ax.plot(right, 3 - 1 / right, color="#00866a", lw=2.6, label=r"$M/d\geq1$")
    ax.axhline(3, ls="--", color="#666666", lw=1.1)
    ax.text(4.94, 3.04, r"Asymptote $3$", ha="right", color="#555555")
    ax.plot(0.75, 15 / 8, "o", color="#a63800", ms=6)
    ax.annotate(r"Minimum $(3/4,15/8)$", (0.75, 15 / 8), (1.6, 1.5),
                arrowprops={"arrowstyle": "->", "color": "#a63800"}, color="#a63800")
    ax.plot(1, 2, "o", mfc="white", mec="#0066a3", ms=5)
    ax.annotate(r"Join $(1,2)$", (1, 2), (1.7, 2.05),
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(xlim=(0, 5), ylim=(0, 3.3), xlabel=r"Normalized retention $M/d$",
           ylabel=r"$[\operatorname{Var}(S_I)+\operatorname{Var}(S_R)]/(\lambda d^2)$",
           title="Per-claim excess of loss: shape-three Pareto claims")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.15)
    ax.legend(loc="lower right", frameon=False)
    fig.savefig(Path.cwd() / "paper-41-retention.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
