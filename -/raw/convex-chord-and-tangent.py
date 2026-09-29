"""Render convexity's endpoint and supporting-line inequalities to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-0.3, 3.45, 800)
    assert np.isclose(0.5 * (1**2 + 3**2) - 2**2, 1)
    assert np.allclose(x**2 - (4 * x - 4), (x - 2) ** 2)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, ax = plt.subplots(figsize=(9, 5.4), dpi=120, facecolor="white")
    ax.plot(x, x**2, color="#206a9d", lw=3, label=r"Convex graph: $f(x)=x^2$")
    segment = np.linspace(1, 3, 200)
    ax.plot(segment, 4 * segment - 3, color="#be7521", lw=2.5,
            label=r"Endpoint interpolation: $y=4x-3$")
    ax.plot(x, 4 * x - 4, color="#2f8a68", lw=2, linestyle="--",
            label=r"Supporting tangent at $2$: $y=4x-4$")
    ax.fill_between(segment, segment**2, 4 * segment - 3,
                    color="#be7521", alpha=0.12)
    ax.scatter([1, 3], [1, 9], s=60, color="#be7521", zorder=4)
    ax.scatter([2, 2], [4, 5], s=65, color=["#206a9d", "#be7521"], zorder=4)
    ax.annotate("Mean input = 2\nFunction at mean = 4", xy=(2, 4),
                xytext=(0.05, 3.7), arrowprops={"arrowstyle": "->", "color": "#206a9d"},
                color="#206a9d", fontsize=11)
    ax.annotate("Mean output = 5\nGap = 1", xy=(2, 5), xytext=(2.15, 9.8),
                arrowprops={"arrowstyle": "->", "color": "#9b5e14"},
                color="#9b5e14", fontsize=11)
    ax.set(xlim=(-0.3, 3.45), ylim=(-0.7, 12.2), xlabel="Input x", ylabel="Output y",
           title="A convex graph sits between a chord and a supporting tangent")
    ax.grid(color="#e5e9eb")
    ax.spines[["top", "right"]].set_visible(False)
    fig.legend(*ax.get_legend_handles_labels(), loc="lower center", ncol=1,
               frameon=False, bbox_to_anchor=(0.5, 0.01), fontsize=11)
    fig.subplots_adjust(left=0.085, right=0.98, top=0.9, bottom=0.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
