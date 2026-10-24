"""Draw Q5's contour; write the PNG to the current working directory.

Tested with Python 3.14.4, Matplotlib 3.10.7+dfsg1, NumPy 2.3.5.
Dependencies are documented in the repository's root pyproject.toml.
"""

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/metric-2015-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    a, radius = 1.0, 2.4
    pi = 3.141592653589793
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.axhline(0, color="#c5c5c5", linewidth=0.8)
    ax.axvline(0, color="#c5c5c5", linewidth=0.8)
    points = [(-radius, 0), (radius, 0), (radius, pi), (-radius, pi)]
    for start, end in zip(points, points[1:] + points[:1]):
        ax.plot([start[0], end[0]], [start[1], end[1]], color="#286ba6", lw=2)
        p = (0.45 * start[0] + 0.55 * end[0], 0.45 * start[1] + 0.55 * end[1])
        q = (0.55 * start[0] + 0.45 * end[0], 0.55 * start[1] + 0.45 * end[1])
        ax.annotate("", xy=p, xytext=q, arrowprops={"arrowstyle": "-|>", "color": "#286ba6", "lw": 2})
    ax.plot([-radius, radius], [pi / 2, pi / 2], "--", color="#dddddd", lw=1)
    for sign in [-1, 1]:
        ax.plot(sign * a, pi / 2, "o", color="#c54a30", ms=7)
        label = r"$-a+\frac{\pi i}{2}$" if sign < 0 else r"$a+\frac{\pi i}{2}$"
        ax.annotate(label, (sign * a, pi / 2), xytext=(0, 15), textcoords="offset points", ha="center", fontsize=13)
    ax.text(0, -0.48, r"Bottom: $x/D(x)$, left to right", ha="center", fontsize=12)
    ax.text(0, pi + 0.32, r"Top: $(x+\pi i)/D(x)$, right to left", ha="center", fontsize=12)
    ax.text(-radius - 0.13, pi / 2, "vanishes\nas $R$ grows", ha="right", va="center", fontsize=10)
    ax.text(radius + 0.13, pi / 2, "vanishes\nas $R$ grows", ha="left", va="center", fontsize=10)
    for x, label in [(-radius, "$-R$"), (radius, "$R$")]:
        ax.text(x, -0.19, label, ha="center", va="top", fontsize=12)
    ax.text(0.12, pi - 0.22, r"$\pi i$", fontsize=11)
    ax.set_title("A vertical shift cancels the horizontal numerators", fontsize=14, pad=30)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-0.7, pi + 0.8)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.04, top=0.85)
    fig.savefig(Path.cwd() / "metric-2015-residue-contour.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
