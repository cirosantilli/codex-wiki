"""Generate angular-momentum-lever-arm.png in the current working directory.

Use: make _media/angular-momentum-lever-arm.png
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Position is in metres; momentum is in kg m/s. Arrows use separate scales.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    r = np.array([2.0, 0.0, 0.0])
    momenta = np.array([[0.0, 3.0, 0.0], [0.0, -3.0, 0.0], [3.0, 0.0, 0.0]])
    angular = np.cross(r, momenta)
    assert np.allclose(angular[:, 2], [6, -6, 0])
    shifted = np.cross(r - [1.0, 0.0, 0.0], momenta[0])
    assert np.allclose(shifted, [0, 0, 3])
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.7), facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.23, top=0.76, wspace=0.19)
    fig.suptitle("Angular momentum: transverse motion counts, radial motion does not",
                 fontsize=16, y=0.97)
    fig.text(0.5, 0.87, r"Same position: $\mathbf{r}=(2,0,0)$ m.  $L_z=xp_y-yp_x$; $+z$ points out of the page.",
             ha="center", fontsize=12)
    titles = ["Positive: out of the page", "Negative: into the page", "Radial: zero"]
    colors = ["#18775c", "#b04939", "#5b537c"]
    for i, (ax, p, angular_i, title, color) in enumerate(zip(axes, momenta, angular, titles, colors)):
        ax.set(xlim=(-0.35, 4.7), ylim=(-2.55, 2.55), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=12, pad=12, color=color)
        ax.annotate("", (4.6, 0), (-0.25, 0), arrowprops={"arrowstyle": "->", "color": "#bbbbbb"})
        ax.annotate("", (0, 2.4), (0, -2.35), arrowprops={"arrowstyle": "->", "color": "#bbbbbb"})
        ax.text(4.5, -0.33, "x", color="#555555")
        ax.text(-0.25, 2.2, "y", color="#555555")
        if i < 2:
            ax.plot([2, 2], [-2.25, 2.25], ls="--", color="#d4b6a0", lw=1.4, zorder=0)
        ax.annotate("", (1.92, 0), (0, 0),
                    arrowprops={"arrowstyle": "-|>", "lw": 2.5, "color": "#2469a0"})
        ax.text(0.85, -0.38, r"$\mathbf{r}$", color="#2469a0", fontsize=14)
        ax.scatter([0, 2], [0, 0], s=[24, 60], color="#263341", zorder=5)
        ax.text(-0.25, -0.45, "O", color="#263341")
        ax.text(1.95, 0.3, "(2, 0) m", fontsize=10)
        tip = r[:2] + 0.68 * p[:2]
        ax.annotate("", tip, r[:2],
                    arrowprops={"arrowstyle": "-|>", "lw": 2.8, "color": "#c86c21"})
        if i < 2:
            ax.text(2.25, 0.9 if i == 0 else -1.25,
                    r"$\mathbf{p}$" + ("\n+3 y" if i == 0 else "\n−3 y"),
                    color="#a45213", fontsize=12)
            level = -2.15 if i == 0 else 2.05
            ax.annotate("", (2, level), (0, level),
                        arrowprops={"arrowstyle": "<->", "color": "#777777"})
            ax.text(1, level + (-0.35 if i == 0 else 0.22), r"$\ell=2$ m", ha="center", fontsize=11)
        else:
            ax.text(3.0, -0.65, r"$\mathbf{p}=3\,\hat{\mathbf{x}}$", color="#a45213", fontsize=12)
            ax.text(2.5, -1.8, r"$\mathbf{r}\parallel\mathbf{p}$; $\ell=0$", ha="center", fontsize=12)
        ax.text(0.5, -0.15, rf"$L_z={angular_i[2]:+g}$ kg m$^2$/s" if i < 2 else r"$L_z=0$ kg m$^2$/s",
                transform=ax.transAxes, ha="center", fontsize=14, color=color)
    fig.text(0.5, 0.045, "Blue: position. Orange: momentum (drawn to a separate scale). Dashed lines: direction of momentum.",
             ha="center", fontsize=10)
    fig.savefig("angular-momentum-lever-arm.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
