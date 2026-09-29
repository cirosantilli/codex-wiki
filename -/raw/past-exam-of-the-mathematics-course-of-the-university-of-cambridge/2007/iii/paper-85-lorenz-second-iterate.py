"""Local second-iterate sketches; emits basename PNG to caller CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.8), facecolor="white", constrained_layout=True)
    for ax, mu in zip(axes, [.96, 1, 1.04]):
        for sign in [-1, 1]:
            x = sign * np.linspace(.00001, .28, 700)
            y = sign * (mu - mu**2 + 2 * mu * x**2 - x**4)
            ax.plot(x, y, color="#286e9b", lw=2)
        ax.scatter([0], [mu - mu**2], color="#286e9b", s=35, zorder=4)
        if mu != 1:
            ax.scatter([0], [-mu + mu**2], facecolors="white", edgecolors="#286e9b", s=35, zorder=4)
        ax.plot([-.28, .28], [-.28, .28], "--", color="#90979e", lw=1)
        ax.axhline(0, color="#d1d5d9", lw=.8)
        ax.axvline(0, color="#d1d5d9", lw=.8)
        ax.set(xlim=(-.28, .28), ylim=(-.2, .2), xlabel="$x$", ylabel="$f_L^2(x)$", title=rf"$\mu={mu:g}$")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Local return branch near zero: two fixed points become one two-cycle\nThe nonzero preimages of zero lie outside the plotted domain", fontsize=13)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
