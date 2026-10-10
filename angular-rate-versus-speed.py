"""Generate angular-rate-versus-speed.png in the current working directory.

Use: make _media/angular-rate-versus-speed.png
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Computed nonrelativistic transverse speeds for total proper motion 100 mas/year;
parallaxes use the existing parsec small-angle distance relation.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 13, "savefig.facecolor": "white"})
    conversion, mu_arcsec = 4.74047, 0.100
    distance = np.linspace(0, 110, 301)
    fig, ax = plt.subplots(figsize=(9.5, 5.8), facecolor="white")
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.18, top=0.80)
    fig.suptitle("The same angular rate can mean very different speeds", fontsize=18, y=0.97)
    fig.text(0.5, 0.895, r"Total proper motion fixed at 100 mas/year: $v_\perp = 4.74047\times0.100\times d$ km/s",
             ha="center", fontsize=13)
    ax.plot(distance, conversion * mu_arcsec * distance, lw=2.8, color="#2368ac")
    for d, label_xy, color in ((10, (25, 5.5), "#453778"),
                               (20, (38, 23), "#b85b15"),
                               (100, (64, 46), "#2368ac")):
        speed = conversion * mu_arcsec * d
        p_mas = 1000 / d
        ax.vlines(d, 0, speed, color=color, lw=1.2, ls=":")
        ax.scatter(d, speed, s=85, color=color, edgecolors="white", zorder=4)
        label = f"{d} pc → {speed:.2f} km/s\nParallax: {p_mas:.0f} mas"
        ax.annotate(label, xy=(d, speed), xytext=label_xy, fontsize=12, color=color,
                    va="center", bbox={"facecolor": "white", "edgecolor": "none", "pad": 3},
                    arrowprops={"arrowstyle": "-", "color": color, "lw": 1.2})
    ax.set(xlabel="Distance (pc)", ylabel="Transverse speed (km/s)",
           xlim=(0, 110), ylim=(0, 58), xticks=[0, 10, 20, 40, 60, 80, 100],
           yticks=np.arange(0, 60, 10))
    ax.grid(alpha=0.20)
    ax.set_facecolor("white")
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.045, "Computed examples; only the velocity across the line of sight is shown.",
             ha="center", fontsize=11)
    fig.savefig("angular-rate-versus-speed.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
