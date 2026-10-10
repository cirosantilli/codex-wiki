"""Exact fair-die atoms and upper tails; Python 3.14 / NumPy 2.3 / Matplotlib 3.10.

Run from _media. Closed dots include endpoints; white dots exclude them.
All probabilities are analytic model values, rather than measurements.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, orange, grey = "#236a9e", "#bd5b15", "#b5bcc3"
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.2), layout="constrained")
    fig.suptitle("Fair die: an endpoint carries probability 1/6", fontsize=16)
    values = np.arange(1, 7)
    ax = axes[0]
    for value in values:
        color = orange if value >= 4 else grey
        ax.vlines(value, 0, 1 / 6, color=color, linewidth=3)
        ax.plot(value, 1 / 6, "o", color=color, markersize=7)
    ax.axvline(4, color=orange, linestyle=":", linewidth=1.5)
    ax.text(3.5, 0.245, "At threshold 4:\n3 atoms included", ha="center",
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(title="Probability mass", ylabel=r"$P(D=d)$", ylim=(0, 0.31),
           xlim=(0.5, 6.5), xlabel="Die outcome d")
    ax.set_yticks([0, 1 / 6], ["0", "1/6"])

    # The two functions share all plateaus and differ only at integer thresholds.
    for ax, inclusive, color in zip(axes[1:], [True, False], [orange, blue]):
        edges = np.arange(0, 8)
        for left, right in zip(edges[:-1], edges[1:]):
            height = np.count_nonzero(values > left) / 6
            ax.hlines(height, left, right, color=color, linewidth=2.2)
        for value in values:
            upper = np.count_nonzero(values >= value) / 6
            lower = np.count_nonzero(values > value) / 6
            closed, opened = (upper, lower) if inclusive else (lower, upper)
            ax.plot(value, opened, "o", markerfacecolor="white",
                    markeredgecolor=color, markersize=7, markeredgewidth=1.5)
            ax.plot(value, closed, "o", color=color, markersize=7)
        ax.axvline(4, color=color, linestyle=":", linewidth=1.1)
        ax.set(title=r"Inclusive tail $P(D\geq t)$" if inclusive
               else r"Strict tail $P(D>t)$", xlim=(0.5, 6.5),
               ylim=(-0.045, 1.075), xlabel="Threshold t", ylabel="Probability")
        ax.set_yticks([0, 1 / 3, 1 / 2, 1], ["0", "1/3", "1/2", "1"])
        ax.annotate("1/2" if inclusive else "1/3",
                    xy=(4, 1 / 2 if inclusive else 1 / 3), xytext=(4.7, 0.81),
                    arrowprops={"arrowstyle": "->", "color": color}, color=color)
    for ax in axes:
        ax.set_xticks(values)
        ax.grid(axis="y", color="#e6e9ec", linewidth=0.7)
        ax.set_axisbelow(True)
    fig.text(0.5, -0.025, "Exact mathematical model • filled dot: value at the threshold • white dot: excluded endpoint",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
