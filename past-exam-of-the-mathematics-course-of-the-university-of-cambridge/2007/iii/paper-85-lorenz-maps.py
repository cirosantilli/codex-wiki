"""Original Lorenz-map and companion sketches; emits basename PNG to caller CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(2, 3, figsize=(10.5, 6.2), facecolor="white", constrained_layout=True)
    for j, mu in enumerate([-.08, 0, .08]):
        ax = axes[0, j]
        neg = np.linspace(-.55, -.0001, 600)
        pos = np.linspace(.0001, .55, 600)
        ax.plot(neg, mu - neg**2, color="#286e9b", lw=2)
        ax.plot(pos, pos**2 - mu, color="#286e9b", lw=2)
        ax.scatter([0], [-mu], color="#286e9b", s=35, zorder=4)
        if mu:
            ax.scatter([0], [mu], facecolors="white", edgecolors="#286e9b", s=35, zorder=4)
        axes[1, j].plot(np.linspace(-.55, .55, 1000), mu - np.linspace(-.55, .55, 1000)**2, color="#c47832", lw=2)
        for row in range(2):
            panel = axes[row, j]
            panel.plot([-.55, .55], [-.55, .55], "--", color="#90979e", lw=1)
            panel.axhline(0, color="#d1d5d9", lw=.8)
            panel.axvline(0, color="#d1d5d9", lw=.8)
            panel.set(xlim=(-.55, .55), ylim=(-.35, .35), xlabel="$x$", ylabel="$f_L(x)$" if row == 0 else "$g(x)$", title=rf"$\mu={mu:g}$")
            panel.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Lorenz discontinuity at zero and the smooth even companion", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
