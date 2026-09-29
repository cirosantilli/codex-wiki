"""Draw an original conceptual Joule paddle-wheel apparatus and energy balance.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
This is not a reconstruction to scale, and contains no experimental data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle


def draw():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(10, 6.8), dpi=120, facecolor="white")
    ax = fig.add_axes((0, 0, 1, 1), facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.8))
    ax.axis("off")
    ink, blue, orange = "#203447", "#206a9b", "#ad531b"

    def arrow(start, end, color=ink, lw=1.7):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=14, linewidth=lw, color=color))

    def label(text, target, pos, align="left"):
        ax.annotate(text, target, xytext=pos, ha=align, va="center", color=ink,
                    arrowprops={"arrowstyle": "-", "color": ink, "lw": 1},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})

    ax.text(5, 6.43, "Joule's paddle-wheel experiment", ha="center", fontsize=18,
            weight="bold", color=ink)
    ax.text(5, 6.06, "Original explanatory schematic • not to scale • no measured data",
            ha="center", fontsize=10.5, color="#556777")

    # An illustrative pair of weights and external pulleys drive the vertical shaft.
    for x in (1.15, 8.85):
        ax.add_patch(Circle((x, 5.05), 0.27, edgecolor=ink, facecolor="#eeeeee", lw=1.7))
    ax.plot([1.15, 1.15, 4.75, 5.25, 8.85, 8.85],
            [3.75, 5.32, 5.32, 5.32, 5.32, 3.75], color=ink, lw=1.5)
    for x in (0.83, 8.53):
        ax.add_patch(Rectangle((x, 3.10), 0.64, 0.65, facecolor="#e1e5e9", edgecolor=ink, lw=1.5))
        ax.text(x + 0.32, 3.43, "mass", ha="center", va="center", fontsize=10, color=ink)
    arrow((0.52, 3.71), (0.52, 2.67))
    arrow((9.48, 3.71), (9.48, 2.67))
    ax.text(0.39, 3.20, "h", ha="right", fontsize=13, color=ink)
    ax.text(9.61, 3.20, "h", ha="left", fontsize=13, color=ink)
    ax.text(5, 5.68, "Measure mass and fall distance; disconnect drive to rewind",
            ha="center", fontsize=10.5, color=ink)

    # Dashed system boundary includes water, copper vessel, and immersed paddle.
    ax.add_patch(FancyBboxPatch((3.27, 1.89), 3.46, 2.32, boxstyle="round,pad=0.12",
                               edgecolor=blue, facecolor="none", linestyle="--", lw=1.8))
    ax.add_patch(Rectangle((3.52, 2.05), 2.96, 1.95, facecolor="#eef7fc", edgecolor=orange, lw=3))
    ax.plot([3.52, 6.48], [3.74, 3.74], color=blue, lw=1.2)
    ax.text(3.85, 3.47, "water", color=blue)
    ax.plot([5, 5], [2.22, 5.32], color=ink, lw=3)
    ax.plot([5, 5], [4.56, 4.87], color="#bf9164", lw=5)
    for y in (2.62, 3.05):
        ax.add_patch(Rectangle((4.42, y), 1.16, 0.13, facecolor=orange, edgecolor=orange))
        ax.add_patch(Rectangle((3.53, y + 0.19), 0.49, 0.12, facecolor=ink))
        ax.add_patch(Rectangle((5.98, y + 0.19), 0.49, 0.12, facecolor=ink))
    ax.plot([6.13, 6.13], [2.98, 4.68], color="#a3303a", lw=2)
    ax.add_patch(Circle((6.13, 2.96), 0.09, facecolor="#a3303a"))
    label("Thermometer\ninitial / final T", (6.13, 4.48), (7.15, 4.43))
    label("Boxwood segment\nreduces conduction", (5.00, 4.72), (2.87, 4.66), "right")
    label("Stationary vanes\noppose co-rotation", (3.83, 3.30), (2.69, 2.42), "right")
    label("Rotating paddle", (5.33, 2.69), (7.15, 2.51))
    arrow((5.42, 4.50), (5.42, 4.02), blue)
    ax.text(5.71, 4.25, "shaft work", color=blue, fontsize=10)
    arrow((6.61, 3.40), (7.43, 3.40), orange)
    ax.text(7.18, 3.00, "Heat exchange\nwith room", color=orange, ha="left", fontsize=10)
    ax.text(5, 1.62, "Chosen system: water + vessel + immersed paddle", ha="center", color=blue,
            weight="bold", fontsize=11)
    ax.text(5, 1.13,
            r"$NMgh=C_{\rm eff}\Delta T+W_{\rm loss,out}+Q_{\rm room,out}$",
            ha="center", fontsize=16, color=ink)
    ax.text(5, 0.73, "Simplified balance: negligible endpoint motion and elastic storage",
            ha="center", fontsize=10.5, color=ink)
    ax.text(5, 0.31, "Resting controls estimate thermal drift; vessel and paddle also store energy",
            ha="center", fontsize=10.5, color=ink)
    out = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(out, facecolor="white", transparent=False)
    plt.close(fig)
    return out


if __name__ == "__main__":
    print(draw())
