"""Equal-volume spheroid geometry; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; the PNG is written to the current working directory.
The surfaces are geometric models, not images of individual nucleons.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(11, 4.4), dpi=120, facecolor="white")
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 65)
    uu, vv = np.meshgrid(u, v)
    cases = [
        ("Prolate", 1.8, "#258d9c", r"$Q_0>0$"),
        ("Spherical", 1.0, "#9ba8b4", r"$Q_0=0$"),
        ("Oblate", 1 / 1.8, "#d78b4c", r"$Q_0<0$"),
    ]
    for index, (title, ratio, color, sign) in enumerate(cases, 1):
        a, c = ratio ** (-1 / 3), ratio ** (2 / 3)
        assert np.isclose(a * a * c, 1)
        ax = fig.add_subplot(1, 3, index, projection="3d")
        x = a * np.sin(vv) * np.cos(uu)
        y = a * np.sin(vv) * np.sin(uu)
        z = c * np.cos(vv)
        ax.plot_surface(x, y, z, color=color, linewidth=0, antialiased=True,
                        alpha=1, shade=True, rcount=65, ccount=100)
        ax.plot([0, 0], [0, 0], [-1.7, 1.7], color="#374151", lw=1, ls="--")
        for angle in [0, np.pi / 2]:
            ax.plot(a * np.sin(v) * np.cos(angle),
                    a * np.sin(v) * np.sin(angle), c * np.cos(v),
                    color="#354958", lw=0.7, alpha=0.6)
        ax.set(xlim=(-1.7, 1.7), ylim=(-1.7, 1.7), zlim=(-1.7, 1.7))
        ax.set_box_aspect((1, 1, 1))
        ax.view_init(elev=16, azim=-64)
        ax.set_axis_off()
        ax.set_title(title + "\n" + sign, pad=-4, fontsize=14)
        ax.text2D(0.5, -0.02, f"a/R = {a:.3f}    c/R = {c:.3f}",
                  transform=ax.transAxes, ha="center", fontsize=11)
    fig.suptitle("Same volume, different intrinsic shapes", fontsize=17, y=0.98)
    fig.text(0.5, 0.065, r"Semiaxes $(a,a,c)$:  $a^2c=R^3$  and  $V=4\pi R^3/3$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.014, "Smooth geometric surfaces; dashed line is the chosen intrinsic z axis.",
             ha="center", fontsize=10, color="#374151")
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.19, top=0.84, wspace=0.03)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False, dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
