"""Generate signed curvature comparison; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the opaque PNG is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.7), sharey=True)
    models = [
        ("Outward sphere", (-1, -1), r"$\ell=R$", r"$K\ell^2=1$"),
        ("Outward cylinder", (-1, 0), r"$\ell=R$", r"$K\ell^2=0$"),
        ("Catenoid waist", (1, -1), r"$\ell=a$", r"$K\ell^2=-1$"),
    ]
    colors = ["#c44c28", "#2278aa", "#7151a1"]
    for ax, (name, ks, scale, gaussian) in zip(axes, models):
        values = np.array([*ks, np.mean(ks)])
        ax.bar([0, 1, 2], values, color=colors, width=0.52)
        ax.scatter([0, 1, 2], values, c=colors, s=55, zorder=4)
        ax.axhline(0, color="#555555", lw=1)
        for x, value in enumerate(values):
            offset = 0.10 if value >= 0 else -0.16
            ax.text(x, value + offset, f"{value:g}", ha="center", va="center")
        ax.set_xticks([0, 1, 2], [r"$k_1\ell$", r"$k_2\ell$", r"$H\ell$"])
        ax.set_ylim(-1.42, 1.40)
        ax.set_yticks([-1, -0.5, 0, 0.5, 1])
        ax.set_title(name + "\n" + scale, pad=12)
        ax.text(0.5, -0.36, gaussian + "\n" + rf"$2H\ell={2 * values[2]:g}$", transform=ax.transAxes, ha="center")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.15)
        ax.set_axisbelow(True)
    axes[0].set_ylabel("Signed curvature × length scale")
    fig.suptitle(r"$S=-dN$    •    $H=(k_1+k_2)/2$    •    $K=k_1k_2$", y=0.98, fontsize=15)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.73, bottom=0.31, wspace=0.30)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
