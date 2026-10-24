"""Draw an exact Desargues configuration; Python 3.14, repo plotting dependencies.

Run from the intended image output directory. The affine coordinates are
u = y / (x+y+z), v = z / (x+y+z); no source-paper images are reproduced.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(8.0, 6.0), facecolor="white")
    ax.set_facecolor("white")
    blue, orange, red = "#2563a6", "#c66a16", "#a52e40"
    points = {
        "P": (0, 1 / 3), "Q": (1 / 2, 0), "R": (1 / 2, 1 / 2),
        "P'": (0, 1 / 2), "Q'": (1 / 3, 0), "R'": (1 / 3, 1 / 3),
    }
    for names, color, label in [
        (("P", "Q", "R"), blue, r"$PQR$"),
        (("P'", "Q'", "R'"), orange, r"$P'Q'R'$"),
    ]:
        triangle = np.array([points[n] for n in (*names, names[0])])
        ax.fill(triangle[:, 0], triangle[:, 1], color=color, alpha=0.045)
        ax.plot(triangle[:, 0], triangle[:, 1], color=color, lw=2, label=label)
    for endpoint in [(0, 0.56), (0.57, 0), (0.57, 0.57)]:
        ax.plot([0, endpoint[0]], [0, endpoint[1]], color="#858585",
                ls=(0, (3, 4)), lw=1, zorder=0)
    ax.plot([0.2, 0.2], [-0.035, 0.63], color=red, lw=1.6, ls="--")
    ax.annotate("", xy=(0.2, 0.65), xytext=(0.2, 0.59),
                arrowprops={"arrowstyle": "->", "color": red, "lw": 1.6})
    ax.text(0.215, 0.635, r"$Y=[1:0:-1]$ at infinity", color=red, fontsize=10)
    for name, (u, v) in points.items():
        color = orange if "'" in name else blue
        ax.scatter(u, v, color=color, s=28, zorder=4)
        offsets = {"P": (-19, -3), "P'": (-21, 2), "Q": (5, -15),
                   "Q'": (-8, -18), "R": (7, 0), "R'": (7, -3)}
        ax.annotate(rf"${name}$", (u, v), xytext=offsets[name],
                    textcoords="offset points", color=color, fontsize=12)
    for name, xy, offset in [("X", (0.2, 0.2), (-20, -12)),
                              ("Z", (0.2, 0.4), (-20, 6))]:
        ax.scatter(*xy, color=red, s=37, zorder=5)
        ax.annotate(rf"${name}$", xy, xytext=offset,
                    textcoords="offset points", color=red, fontsize=12)
    ax.scatter(0, 0, color="black", s=34, zorder=5)
    ax.annotate(r"$O$", (0, 0), xytext=(-18, -14), textcoords="offset points",
                fontsize=12)
    ax.text(0.23, 0.55, r"axis $u=1/5$", color=red, fontsize=11)
    ax.text(0.565, 0.21, "$QR$ and $Q'R'$\nmeet at the same\nvertical point at infinity",
            color="#444444", fontsize=10, va="center")
    ax.set_aspect("equal")
    ax.set_xlim(-0.07, 0.87)
    ax.set_ylim(-0.075, 0.69)
    ax.axis("off")
    fig.suptitle("Desargues: one center and one axis", fontsize=15, y=0.97)
    fig.text(0.5, 0.055, r"Affine chart $x+y+z=1$:  $u=y$, $v=z$",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.91, bottom=0.10)
    fig.savefig(Path.cwd() / "2017-desargues-configuration.png", dpi=140,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
