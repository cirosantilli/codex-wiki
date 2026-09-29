"""Plot exact Huber smoothing and optimal splits; write basename.png to cwd.

Illustrative mathematical curves, not measured data. Run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (Debian 3.10.7+dfsg1).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = 1.0
    x = np.linspace(-3.2, 3.2, 1601)
    u = np.sign(x) * np.maximum(np.abs(x) - t, 0)
    v = x - u
    huber = np.where(np.abs(x) <= t, x**2/(2*t), np.abs(x)-t/2)
    assert np.allclose(u + v, x)
    assert np.allclose(np.abs(u) + v**2/(2*t), huber)
    assert np.all(np.abs(v) <= t + 1e-12)
    assert np.all(huber <= np.abs(x) + 1e-12)

    plt.rcParams.update({"font.size": 10.5, "axes.titlesize": 12})
    fig, (ax, splits) = plt.subplots(
        1, 2, figsize=(10.0, 4.5), layout="constrained", facecolor="white"
    )
    blue, orange, green = "#245c91", "#b95b1e", "#287a54"
    ax.axvspan(-t, t, color="#eef4f9", zorder=0)
    ax.plot(x, np.abs(x), color=blue, lw=1.8, ls="--", label=r"Original $|x|$")
    ax.plot(x, huber, color=green, lw=2.8,
            label=r"Moreau envelope $h(x)$")
    ax.scatter([-1, 1], [0.5, 0.5], color=green, s=35, zorder=5)
    ax.annotate(r"Quadratic core $x^2/2$", (0.55, 0.55**2/2),
                xytext=(-2.8, 0.75), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": green},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.annotate(r"Linear tail $|x|-1/2$", (2.6, 2.1), xytext=(0.5, 1.3),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": green},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(xlim=(-3.2, 3.2), ylim=(0, 3.5), xlabel="Required total x",
           ylabel="Cost", title="The corner is replaced by a quadratic core")
    ax.legend(loc="upper center", fontsize=9, framealpha=1)

    splits.axvspan(-t, t, color="#eef4f9", zorder=0)
    splits.plot(x, x, color="#6c747c", ls="--", lw=1.4, label=r"Total $x=u_*+v_*$")
    splits.plot(x, u, color=blue, lw=2.5,
                label=r"Absolute-value contribution $u_*$")
    splits.plot(x, v, color=orange, lw=2.5,
                label=r"Quadratic contribution $v_*$")
    splits.scatter([3, 3], [2, 1], color=[blue, orange], s=40, zorder=5)
    splits.annotate(r"$x=3$: $u_*=2$, $v_*=1$", (3, 2), xytext=(0.05, -2.8),
                    fontsize=10, arrowprops={"arrowstyle": "->", "color": blue},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    splits.set(xlim=(-3.2, 3.2), ylim=(-3.5, 3.5), xlabel="Required total x",
               ylabel="Optimal contribution", title="The quadratic contribution stays clipped")
    splits.legend(loc="upper left", fontsize=9, framealpha=1)
    for panel in (ax, splits):
        panel.set_facecolor("white")
        panel.grid(color="#e4e8eb", lw=0.7)
        panel.set_axisbelow(True)
        panel.axhline(0, color="#afb7bf", lw=0.7, zorder=0)
        for cutoff in (-t, t):
            panel.axvline(cutoff, color="#afb7bf", ls=":", lw=1)
        panel.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Absolute value + quadratic splitting: Huber loss with cutoff t = 1",
                 fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=115,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
