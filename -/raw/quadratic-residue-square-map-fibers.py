"""Draw the fibers of squaring modulo two odd primes; Python 3.14/matplotlib 3.10."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def chip(ax, x, y, label, color, width=0.105):
    ax.add_patch(FancyBboxPatch(
        (x - width / 2, y - 0.031), width, 0.062,
        boxstyle="round,pad=0.008,rounding_size=0.012",
        facecolor=color, edgecolor="#384957", linewidth=1.1,
    ))
    ax.text(x, y, str(label), ha="center", va="center", fontsize=13)


def draw_panel(ax, p):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(0.5, 0.95, f"Modulo {p}", ha="center", fontsize=18, weight="bold")
    ax.text(0.21, 0.865, "Inputs: x and −x", ha="center", fontsize=12)
    ax.text(0.77, 0.865, "Output: x² mod p", ha="center", fontsize=12)
    colors = ["#dcebf7", "#e6efcd", "#fbe5cb", "#eadff5", "#d9efeb"]
    roots = range(1, (p + 1) // 2)
    spacing = 0.114 if p == 11 else 0.185
    for i, x in enumerate(roots):
        y = 0.775 - i * spacing
        value = x * x % p
        color = colors[i]
        chip(ax, 0.13, y + 0.027, x, color)
        chip(ax, 0.30, y - 0.027, p - x, color)
        chip(ax, 0.77, y, value, color)
        for start in [(0.195, y + 0.027), (0.365, y - 0.027)]:
            ax.add_patch(FancyArrowPatch(
                start, (0.705, y), arrowstyle="-|>",
                mutation_scale=13, linewidth=1.3, color="#435565",
            ))
    ax.plot([0.04, 0.96], [0.24, 0.24], color="#b9c2ca", lw=1)
    squares = sorted({x * x % p for x in range(1, p)})
    nonsquares = sorted(set(range(1, p)) - set(squares))
    ax.text(0.5, 0.195, f"Nonzero squares: {', '.join(map(str, squares))}",
            ha="center", fontsize=11.5, color="#23434b")
    ax.text(0.5, 0.135, f"Empty fibers: {', '.join(map(str, nonsquares))}",
            ha="center", fontsize=11.5)
    ax.text(0.5, 0.065, "Zero separately: 0 → 0 (one input)",
            ha="center", fontsize=11.5)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 6.2), dpi=100, facecolor="white")
    fig.suptitle("Squaring forgets exactly one sign", fontsize=21, weight="bold", y=0.975)
    for ax, prime in zip(axes, (7, 11), strict=True):
        draw_panel(ax, prime)
    fig.text(0.5, 0.027, "Each nonzero square has two roots; each nonsquare has none.",
             ha="center", fontsize=13)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.88, bottom=0.09, wspace=0.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
