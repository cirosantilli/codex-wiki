"""Original ideal thin-lens construction. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(9.2, 4.8), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.axhline(0, color="0.45", lw=1)
    ax.annotate("", (0, 9), (0, -12), arrowprops={"arrowstyle": "<->", "lw": 2, "color": "#506882"})
    ax.text(0.6, 8, "Converging lens", color="#506882")
    for x, text in [(-8, "$F$"), (8, "$F'$ (8 cm)")]:
        ax.plot(x, 0, "ko", ms=4)
        ax.text(x, 0.6, text, ha="center")
    ax.annotate("", (-12, 5), (-12, 0), arrowprops={"arrowstyle": "-|>", "lw": 2.8, "color": "#28794c"})
    ax.text(-12, 5.7, "Object\n5 cm", ha="center", color="#28794c")
    ax.annotate("", (24, -10), (24, 0), arrowprops={"arrowstyle": "-|>", "lw": 2.8, "color": "#28794c"})
    ax.text(24.7, -8.8, "Real image\n10 cm, inverted", color="#28794c")
    paths = [([-12, 0, 24], [5, 5, -10], "#c06a13"), ([-12, 0, 24], [5, 0, -10], "#406bb4")]
    for xs, ys, color in paths:
        ax.plot(xs, ys, color=color, lw=1.8)
        for a, b in [(0, 1), (1, 2)]:
            dx, dy = xs[b] - xs[a], ys[b] - ys[a]
            start = (xs[a] + 0.45 * dx, ys[a] + 0.45 * dy)
            end = (xs[a] + 0.57 * dx, ys[a] + 0.57 * dy)
            ax.annotate("", end, start, arrowprops={"arrowstyle": "-|>", "color": color, "lw": 1.5})
    for xa, xb, y, label in [(-12, 0, -12, "$u=12$ cm"), (0, 24, -14, "$v=24$ cm")]:
        ax.annotate("", (xb, y), (xa, y), arrowprops={"arrowstyle": "<->", "lw": 1, "color": "0.3"})
        ax.text((xa + xb) / 2, y - 0.65, label, ha="center", va="top")
    ax.set(xlim=(-16, 36), ylim=(-16, 10), xlabel="$x$ (cm)", ylabel="Height (cm)", title="Thin-lens construction: two independent rays meet at (24, −10) cm")
    ax.set_aspect("equal", adjustable="box")
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
