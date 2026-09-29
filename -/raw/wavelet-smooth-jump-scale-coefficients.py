"""Original exact scale comparison; Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Run from _media to write the matching PNG there.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    scales = 2.0 ** (-np.arange(0, 11))
    coeffs = [
        ("Haar: smooth x + x²", (scales**1.5 + scales**2.5) / 4,
         "#237aaf", "o", "-"),
        ("Two moments: smooth x + x²", 2 * scales**2.5 / np.sqrt(6),
         "#d36a31", "s", "-"),
        ("Haar: unit jump", np.sqrt(scales) / 4,
         "#237aaf", "o", "--"),
        ("Two moments: unit jump", np.sqrt(scales) / (4 * np.sqrt(6)),
         "#d36a31", "s", "--"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Smooth details shrink faster than a crossing jump", fontsize=16)
    for label, magnitude, color, marker, style in coeffs:
        axes[0].loglog(scales, magnitude, label=label, color=color,
                       marker=marker, linestyle=style, markersize=4, base=2)
        axes[1].loglog(scales, magnitude / np.sqrt(scales), color=color,
                       marker=marker, linestyle=style, markersize=4, base=2)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlabel("Scale a (finer →)")
        ax.set_xlim(1.1, scales[-1] / 1.1)
        ax.set_xticks([1, 1/4, 1/16, 1/64, 1/256, 1/1024],
                     ["1", "1/4", "1/16", "1/64", "1/256", "1/1024"])
        ax.tick_params(axis="x", labelsize=9)
        ax.grid(alpha=.2)
    axes[0].set_title("Unit L² norm analyzing functions")
    axes[0].set_ylabel("Coefficient magnitude |c|")
    axes[0].legend(fontsize=9, loc="lower left", framealpha=1)
    axes[1].set_title("Remove the common √a factor")
    axes[1].set_ylabel("|c| / √a")
    axes[1].text(.04, .07, "Jump curves stay constant;\nsmooth curves keep shrinking.",
                 transform=axes[1].transAxes, fontsize=10)
    fig.supxlabel("Smooth signal: b = 0.  Fixed jump H(x): b = −a/4, so θ = 1/4.",
                   fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
