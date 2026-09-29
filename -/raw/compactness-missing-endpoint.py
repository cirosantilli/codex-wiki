"""Draw compactness-missing-endpoint.png in cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def main():
    indices = np.arange(2, 41)
    values = 1 / indices
    assert np.all((0 < values) & (values < 1))
    assert np.all(np.diff(values) < 0)
    assert np.allclose(values[[0, 8, -1]], [0.5, 0.1, 0.025])

    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), facecolor="white")
    for ax, closed, color in zip(axes, [True, False], ["#277b64", "#b74440"]):
        ax.set_facecolor("white")
        ax.axhspan(0, 1, color="#eaf3f6", zorder=0)
        ax.plot(indices, values, "o", ms=4.5, color="#247393", zorder=3)
        for endpoint in [0, 1]:
            ax.axhline(endpoint, color=color, lw=2,
                       linestyle="-" if closed else "--", zorder=2)
            ax.scatter([0], [endpoint], edgecolors=color,
                       facecolors=color if closed else "white", s=80,
                       linewidths=2, zorder=4)
        ax.annotate(r"$x_2=1/2$", xy=(2, 0.5), xytext=(9, 0.67),
                    arrowprops={"arrowstyle": "->", "color": "#247393"},
                    color="#1f5e77")
        ax.annotate(r"$x_{10}=1/10$", xy=(10, 0.1), xytext=(13, 0.33),
                    arrowprops={"arrowstyle": "->", "color": "#247393"},
                    color="#1f5e77")
        ax.text(22, 0.85, "Allowed values", ha="center", color="#546771")
        ax.set(xlim=(-1.5, 42), ylim=(-0.09, 1.12),
               xticks=[2, 10, 20, 30, 40], yticks=[0, 0.25, 0.5, 0.75, 1])
        ax.set_xlabel(r"Sequence index $n$", labelpad=7)
        ax.set_ylabel(r"Value $x_n$", labelpad=6)
        ax.set_title("Closed interval [0, 1]" if closed else "Open interval (0, 1)", pad=13)
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#acb5bb")
        ax.text(0.5, -0.25, "Limit 0 belongs to the interval" if closed
                else "Limit 0 is missing from the interval", transform=ax.transAxes,
                ha="center", color=color, fontsize=12)
    fig.suptitle(r"The same sequence $x_n=1/n$ approaches zero", fontsize=18, y=0.98)
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.27, top=0.80, wspace=0.24)
    fig.text(0.5, 0.025, "All subsequences still approach 0. Hollow boundary markers mean excluded values.",
             ha="center", fontsize=11)
    fig.savefig("compactness-missing-endpoint.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
