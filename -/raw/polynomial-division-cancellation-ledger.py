"""Draw the coefficient cancellations in an original polynomial division."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.035, top=0.98)
    ax.set(xlim=(0, 10), ylim=(0, 6.2))
    ax.axis("off")
    blue, orange, ink = "#1765a3", "#be5b0b", "#243746"
    ax.text(5, 5.97, "Cancel one leading term at a time", ha="center", va="center", fontsize=20, color=ink)
    ax.text(5, 5.52, r"$f=2X^3+3X^2-5X+6\qquad g=X^2+X-2$", ha="center", fontsize=16, color=ink)
    columns = [3.25, 4.35, 5.45, 6.55]
    for x, label in zip(columns, [r"$X^3$", r"$X^2$", r"$X$", r"$1$"]):
        ax.text(x, 4.95, label, ha="center", va="center", fontsize=16)
    ax.text(8.55, 4.95, "Quotient added", ha="center", va="center", color=ink)
    rows = [
        (4.45, r"Start: $f$", [2, 3, -5, 6], ink),
        (3.94, r"Subtract $2Xg$", [2, 2, -4, 0], blue),
        (3.30, r"Remainder $h$", [0, 1, -1, 6], ink),
        (2.79, r"Subtract $g$", [0, 1, 1, -2], orange),
        (2.15, r"Final remainder $r$", [0, 0, -2, 8], ink),
    ]
    for y, label, values, color in rows:
        ax.text(0.20, y, label, va="center", color=color)
        for x, value in zip(columns, values):
            ax.text(x, y, rf"${value}$", ha="center", va="center", fontsize=18, color=color if value else "#7d8992")
    for x, top, bottom, color in [(3.25, 4.70, 3.72, blue), (4.35, 3.55, 2.57, orange)]:
        ax.add_patch(Rectangle((x-0.37, bottom), 0.74, top-bottom, facecolor=color, alpha=0.10, edgecolor="none", zorder=-1))
    for y in [3.64, 2.49]:
        ax.plot([2.78, 7.02], [y, y], color="#aeb8c0", lw=1.5)
    for y, term, color in [(4.18, r"$+\,2X$", blue), (3.05, r"$+\,1$", orange)]:
        ax.text(8.55, y, term, ha="center", va="center", color=color, fontsize=19)
    ax.text(8.55, 2.15, r"$q=2X+1$", ha="center", va="center", color=ink, fontsize=18)
    ax.annotate("", xy=(7.25, 2.15), xytext=(7.25, 3.96), arrowprops={"arrowstyle": "->", "color": "#778690", "lw": 1.5})
    ax.text(5, 1.65, r"Stop: $\deg r=1<\deg g=2$", ha="center", color=ink, fontsize=16)
    ax.add_patch(FancyBboxPatch((0.42, 0.25), 9.16, 1.0, boxstyle="round,pad=0.10", facecolor="#f1f5f8", edgecolor="#d3dce3"))
    ax.text(5, 0.90, "Every subtraction preserves the identity", ha="center", color=ink)
    ax.text(5, 0.52, r"$f=gq+r=(X^2+X-2)(2X+1)+(-2X+8)$", ha="center", fontsize=16, color=ink)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
