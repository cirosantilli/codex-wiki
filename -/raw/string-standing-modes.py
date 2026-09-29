"""Plot the first three fixed-end modes; save the white PNG in the cwd.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(3, 1, figsize=(8.5, 6.2), sharex=True)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.145, top=0.83, hspace=0.55)
    fig.suptitle("Fixed endpoints select standing modes\n"
                 r"$y_n=A_n\sin(n\pi x/L)\cos(\omega_n t)$;  "
                 r"$L=1$ m, $c=100$ m/s", fontsize=13)
    x = np.linspace(0, 1, 1201)
    for n, ax in enumerate(axes, 1):
        shape = np.sin(n * np.pi * x)
        ax.axhline(0, color="#929292", lw=1)
        ax.plot(x, shape, color="#176ca4", lw=2.5, label="one extremum")
        ax.plot(x, -shape, color="#c75a11", lw=2, ls="--", label="opposite extremum")
        nodes = np.arange(n + 1) / n
        ax.scatter(nodes, np.zeros_like(nodes), color="#252525", zorder=4,
                   s=30, label="stationary nodes")
        ax.set(ylim=(-1.3, 1.3), xlim=(-0.025, 1.025), ylabel=r"$y/A_n$")
        ax.set_yticks((-1, 0, 1))
        ax.set_title(rf"$n={n}$:  $\nu_n={50*n}$ Hz,  $\omega_n={100*n}\pi$ rad/s",
                     fontsize=11, loc="left")
        ax.grid(alpha=0.16)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.004),
               ncol=3, fontsize=9, frameon=False)
    axes[-1].set_xlabel(r"Position $x/L$")
    axes[-1].set_xticks((0, 0.25, 0.5, 0.75, 1))
    fig.savefig(Path.cwd() / "string-standing-modes.png", dpi=140, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
