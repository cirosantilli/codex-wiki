"""Generate standing-string-normal-modes.png in the current working directory.

Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp.
The parameters describe an ideal model, not a measured musical instrument.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    length, tension, density = 1.0, 1.0, 1.0
    speed = np.sqrt(tension / density)
    position = np.linspace(0, length, 1201)
    snapshots = [(0, "0", "#176ca4", "-"),
                 (1 / 8, "1/8", "#dc951c", "--"),
                 (1 / 4, "1/4", "#40845a", ":"),
                 (1 / 2, "1/2", "#bd446b", "-.")]
    fig, axes = plt.subplots(3, 1, figsize=(8.4, 6.7), sharex=True)
    fig.subplots_adjust(left=0.10, right=0.97, top=0.81, bottom=0.15, hspace=0.57)
    fig.suptitle("First three normal modes of an ideal fixed string\n"
                 r"$L=1$ m, $\tau=1$ N, $\mu=1$ kg/m; $c=1$ m/s",
                 fontsize=13, y=0.98)
    fig.text(0.5, 0.865, r"Snapshots use each mode's OWN period $T_n=1/f_n$; phase $\varphi=0$",
             ha="center", fontsize=10)
    for n, ax in enumerate(axes, start=1):
        frequency = n * speed / (2 * length)
        period = 1 / frequency
        shape = np.sin(n * np.pi * position / length)
        for fraction, label, color, style in snapshots:
            factor = np.cos(2 * np.pi * fraction)
            if fraction == 1 / 4:
                factor = 0.0
            ax.plot(position / length, shape * factor, color=color, ls=style,
                    lw=2.1, label=rf"$t/T_n={label}$")
        nodes = np.arange(n + 1) / n
        ax.scatter(nodes, np.zeros_like(nodes), color="#222222", s=30,
                   zorder=5, label="permanent nodes (ends included)")
        ax.set(xlim=(-0.025, 1.025), ylim=(-1.25, 1.25), ylabel=r"$u_n/A$")
        ax.set_yticks([-1, 0, 1])
        period_label = ["2", "1", "2/3"][n - 1]
        ax.set_title(rf"$n={n}$: $f_n={frequency:g}$ Hz, $T_n={period_label}$ s; "
                     f"{n - 1} interior node{'s' if n != 2 else ''}", loc="left", fontsize=11)
        ax.grid(alpha=0.18)
    axes[-1].set_xlabel(r"Position $x/L$")
    axes[-1].set_xticks([0, 1 / 4, 1 / 2, 3 / 4, 1])
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.006),
               ncol=3, fontsize=9, frameon=False)
    fig.savefig(Path.cwd() / "standing-string-normal-modes.png", dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
