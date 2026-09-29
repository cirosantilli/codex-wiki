"""Catenary examples, vertical shift and scale; PNG goes to CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1.65, 1.65, 501)
    blue = "#176b9c"
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    ax.plot(x, np.cosh(x), color=blue, lw=2.6, label=r"$y=\cosh x$")
    nodes = np.array([-1., 0., 1.])
    ax.scatter(nodes, np.cosh(nodes), color=blue, s=45, zorder=4)
    ax.scatter([-1, 1], [np.cosh(1)]*2, marker="s", color="#444444",
               s=85, zorder=3, label="Supports at x = ±1")
    for value in nodes:
        text = "(0, 1)" if value == 0 else f"({int(value)}, 1.543)"
        offset = (0, -24) if value == 0 else (0, 13)
        ax.annotate(text, (value, np.cosh(value)), xytext=offset,
                    textcoords="offset points", ha="center", fontsize=11)
    ax.axhline(1, color="0.65", ls=":", lw=1)
    ax.text(-1.58, .18, r"$L_{[-1,1]}=2\sinh1\approx2.350$", fontsize=11)
    ax.set(xlim=(-1.7, 1.7), ylim=(0, 2.95), xlabel="Horizontal position x",
           ylabel="Height y", title="a = 1: lowest point at height 1")
    ax.legend(loc="upper center", fontsize=10, framealpha=1)

    ax = axes[1]
    for a, color in [(.5, "#bf5a15"), (1, blue), (2, "#33844a")]:
        ax.plot(x, a*(np.cosh(x/a)-1), color=color, lw=2.4,
                label=f"a = {a:g}")
    ax.plot(x, x*x/2, color="0.4", ls="--", lw=1.5,
            label=r"Parabola $x^2/2$ (a = 1 locally)")
    ax.scatter(nodes, np.cosh(nodes)-1, color=blue, s=35, zorder=4)
    ax.annotate("(0, 0)", (0, 0), xytext=(15, 12),
                textcoords="offset points", fontsize=11)
    ax.set(xlim=(-1.7, 1.7), ylim=(-.12, 3.0), xlabel="Horizontal position x",
           ylabel="Height above the lowest point",
           title=r"Shifted: $y=a[\cosh(x/a)-1]$")
    ax.legend(loc="upper center", fontsize=9.5, framealpha=1)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="0.5", lw=.8, zorder=0)
        ax.axvline(0, color="0.5", lw=.8, zorder=0)
        ax.grid(alpha=.17)
        ax.set_xticks([-1, 0, 1])
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("A catenary is a scaled hyperbolic cosine", fontsize=15)
    fig.text(.5, .035, "Uniform flexible, inextensible chain under its own weight.  "
             "Larger a = H/(μg) gives less sag over a fixed horizontal span.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.075, right=.98, bottom=.17, top=.83, wspace=.29)
    fig.savefig(Path.cwd() / "hyperbolic-cosine-catenary.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
