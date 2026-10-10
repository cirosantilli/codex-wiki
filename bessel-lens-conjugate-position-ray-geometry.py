"""Draw ideal Bessel imaging geometry; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes a PNG with this script's basename to the working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def dimension(ax, left, right, y, label, color="#454545"):
    ax.annotate("", (left, y), (right, y),
                arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.2})
    ax.text((left + right) / 2, y + 0.08, label, ha="center", va="bottom",
            color=color, fontsize=11)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(9.2, 6.9), facecolor="white")
    L, f, height = 45.0, 10.0, 0.5
    for ax, x in zip(axes, (15.0, 30.0)):
        v = L - x
        m = -v / x
        image_height = m * height
        assert np.isclose(1 / f, 1 / x + 1 / v)
        ax.axhline(0, color="#858585", lw=1)
        ax.plot([L, L], [-1.2, 1.8], color="#555555", lw=5, alpha=0.3)
        ax.annotate("", (0, height), (0, 0),
                    arrowprops={"arrowstyle": "-|>", "color": "#27773f", "lw": 2.5})
        ax.annotate("", (L, image_height), (L, 0),
                    arrowprops={"arrowstyle": "-|>", "color": "#27773f", "lw": 2.5})
        ax.annotate("", (x, 1.3), (x, -1.3),
                    arrowprops={"arrowstyle": "<->", "color": "#254c85", "lw": 2.3})
        other = L - x
        ax.plot([other, other], [-1.2, 1.3], ls="--", color="#aaaaaa", lw=1.4)
        # Parallel ray and undeviated central ray; coordinates meet at screen tip.
        ax.plot([0, x, L], [height, height, image_height], color="#ce671d", lw=1.8)
        ax.plot([0, x, L], [height, 0, image_height], color="#387da0", lw=1.8)
        for a, b, col in ((x, L, "#ce671d"), (0, L, "#387da0")):
            p = a + (b - a) * 0.55
            q = a + (b - a) * 0.65
            if a == x:
                y1 = height * (1 - (p - x) / f)
                y2 = height * (1 - (q - x) / f)
            else:
                y1, y2 = height * (1 - p / x), height * (1 - q / x)
            ax.annotate("", (q, y2), (p, y1),
                        arrowprops={"arrowstyle": "->", "color": col, "lw": 1.8})
        ax.scatter([x - f, x + f], [0, 0], color="#254c85", s=24, zorder=5)
        for pos, text in ((x - f, "$F$"), (x + f, "$F'$")):
            ax.text(pos, -0.18, text, ha="center", color="#254c85")
        ax.text(0, 0.65, "Fixed object", ha="center", color="#27773f")
        ax.text(L, 1.9, "Fixed screen", ha="center")
        ax.text(x, 1.48, f"Lens at x = {x:g} cm", ha="center", color="#254c85")
        ax.text(other, -1.43, "Alternative setting", ha="center", color="#777777", fontsize=10)
        ax.text(L + 1.2, image_height, f"Image\nm = {m:g}", va="center", color="#27773f")
        dimension(ax, 0, x, -1.88, f"u = {x:g} cm")
        dimension(ax, x, L, -1.88, f"v = {v:g} cm")
        dimension(ax, 15, 30, 2.12, "d = 15 cm", "#777777")
        ax.set_xlim(-4, 53)
        ax.set_ylim(-2.2, 2.55)
        ax.set_xticks([0, 15, 30, 45])
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_color("#bbbbbb")
        ax.set_xlabel("Position along optical axis (cm)")
    fig.suptitle("Bessel displacement: one lens, two conjugate settings", fontsize=16)
    fig.text(0.5, 0.025, "Stipulated model: L = 45 cm, f = 10 cm. Heights enlarged; not measured data.",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=0.04, right=0.98, top=0.90, bottom=0.12, hspace=0.37)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
