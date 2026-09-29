"""Generate the matching PNG in CWD; tested with Python 3.14.4.

Plan view of an ideal two-face film; force is perpendicular to the rim and in
the film plane. Uses the repository's NumPy and Matplotlib dependencies.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    gamma = .072  # N/m, assumed toy parameter
    length_mm = np.linspace(0, 50, 301)
    one_mN = gamma * length_mm  # N/m times mm gives mN
    two_mN = 2 * one_mN
    assert np.isclose(2 * gamma * .020, .00288)
    assert np.isclose((2 * gamma * .020) * .001, 2.88e-6)
    assert np.allclose(two_mN, 2 * one_mN)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (sketch, ax) = plt.subplots(1, 2, figsize=(10.8, 5.2), dpi=110,
                                    gridspec_kw={"width_ratios": [1.1, 1.2]})
    fig.subplots_adjust(left=.025, right=.98, top=.81, bottom=.24, wspace=.2)
    blue, orange = "#1768ac", "#bb5b12"
    sketch.set_xlim(-.45, 2.9)
    sketch.set_ylim(-.55, 2.15)
    sketch.set_aspect("equal")
    sketch.axis("off")
    sketch.add_patch(Rectangle((0, 0), 1.55, 1.5,
                               facecolor="#e7f2fa", edgecolor="none"))
    sketch.add_patch(Rectangle((1.55, 0), .27, 1.5, facecolor="#fff1db",
                               edgecolor="none"))
    sketch.plot([2.15, 0, 0, 2.15], [0, 0, 1.5, 1.5], color=".35", lw=3)
    sketch.plot([1.55, 1.55], [0, 1.5], color=".15", lw=4)
    sketch.plot([1.82, 1.82], [0, 1.5], color=".5", lw=1.5, linestyle="--")
    sketch.annotate("", xy=(-.25, 1.5), xytext=(-.25, 0),
                    arrowprops={"arrowstyle": "<->", "color": ".2"})
    sketch.text(-.35, .75, r"$\ell$", va="center", ha="right")
    sketch.annotate("", xy=(.6, .75), xytext=(1.55, .75),
                    arrowprops={"arrowstyle": "->", "lw": 2.3, "color": blue})
    sketch.text(.82, .92, r"$2\gamma\ell$ inward", color=blue, ha="center", fontsize=10)
    sketch.annotate("", xy=(2.85, .75), xytext=(1.55, .75),
                    arrowprops={"arrowstyle": "->", "lw": 2.3, "color": orange})
    sketch.text(2.25, .51, "$F$ outward", color=orange, ha="center", fontsize=10)
    sketch.annotate("", xy=(1.82, 1.83), xytext=(1.55, 1.83),
                    arrowprops={"arrowstyle": "->", "color": ".2"})
    sketch.text(1.69, 1.94, "$dx$", ha="center")
    sketch.text(.73, .18, "Two faces overlap\nin plan view", ha="center", fontsize=10)
    sketch.text(1.5, -.35, "Sliding rim moves perpendicular to itself", ha="center", fontsize=10)
    sketch.set_title("Film in a frame: plan view", pad=14)
    ax.plot(length_mm, one_mN, lw=2.5, color=blue, label=r"One interface: $\gamma\ell$")
    ax.plot(length_mm, two_mN, lw=2.5, color=orange, label=r"Two interfaces: $2\gamma\ell$")
    for y, color in [(1.44, blue), (2.88, orange)]:
        ax.scatter([20], [y], color=color, zorder=5)
        ax.annotate(f"{y:.2f} mN", (20, y), xytext=(10, 10),
                    textcoords="offset points", color=color, fontsize=10,
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95, "pad": 2})
    ax.set(xlabel="Rim length ℓ (mm)", ylabel="Holding force F (mN)",
           xlim=(0, 50), ylim=(0, 8), title="Same constant γ; twice the force")
    ax.grid(alpha=.22)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    fig.suptitle("Surface tension counts interfaces, not just rim length", fontsize=15, y=.96)
    fig.text(.5, .12, r"$dA_{total}=2\ell\,dx$     and     $F\,dx=\gamma\,dA_{total}$",
             ha="center", fontsize=12)
    fig.text(.5, .045, "Assumed γ = 0.072 N/m. At ℓ = 20 mm and dx = 1 mm: work = 2.88 μJ.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
