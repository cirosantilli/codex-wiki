"""Illustrate an original norm-constrained conic program; output to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 13, "axes.titlesize": 15})
    fig, (ax, dual_ax) = plt.subplots(1, 2, figsize=(12, 6), dpi=100)
    fig.patch.set_facecolor("white")
    z = np.linspace(-2.3, 2.3, 501)
    bound = np.hypot(1, z)
    ax.fill_between(z, bound, 3.2, color="#e3f1eb", label="Feasible primal points")
    ax.plot(z, bound, color="#287557", linewidth=2.5, label=r"$t=\sqrt{1+z^2}$")
    ax.axhline(1, color="#4f78a0", linestyle="--", label="Certified lower bound t = 1")
    ax.scatter([0], [1], color="#a43a25", s=90, zorder=5)
    ax.annotate("Minimum (z, t) = (0, 1)", (0, 1), xytext=(-1.9, 0.78), fontsize=12,
                arrowprops={"arrowstyle": "->", "color": "#a43a25"}, color="#8f301f")
    ax.set(xlim=(-2.3, 2.3), ylim=(0.65, 3.2), xlabel=r"$z$", ylabel=r"$t$",
           title=r"Primal slice: $(t,1,z)\in K$")
    ax.legend(loc="upper center", fontsize=11, framealpha=0.96)
    ax.grid(alpha=0.15)
    y1 = np.linspace(-1, 1, 401)
    dual_ax.plot(y1, -y1, color="#4f78a0", linewidth=3, label=r"Dual objective $-y_1$")
    dual_ax.scatter([-1], [1], s=90, color="#a43a25", zorder=5)
    dual_ax.scatter([1], [-1], s=55, color="#4f78a0", zorder=5)
    dual_ax.annotate("Best lower bound = 1\ny = (1, −1, 0)", (-1, 1), xytext=(-0.4, 0.84),
                     color="#8f301f", fontsize=12,
                     arrowprops={"arrowstyle": "->", "color": "#a43a25"})
    dual_ax.text(0.0, -0.72, "Feasibility fixes y₀ = 1, y₂ = 0\nCone membership leaves −1 ≤ y₁ ≤ 1",
                 fontsize=12, ha="center", bbox={"facecolor": "white", "edgecolor": "#cbd3d9", "pad": 8})
    dual_ax.set(xlim=(-1.15, 1.15), ylim=(-1.25, 1.25), xlabel=r"$y_1$",
                ylabel=r"Lower bound $b^Ty=-y_1$", title="Dual slice: maximize the lower bound")
    dual_ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    dual_ax.grid(alpha=0.15)
    fig.suptitle("The same optimality certificate works for a curved constraint", fontsize=18)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.13, top=0.84, wspace=0.25)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
