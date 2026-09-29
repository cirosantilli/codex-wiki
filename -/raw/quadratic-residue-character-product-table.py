"""Show how the Legendre character compresses multiplication modulo seven."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    p = 7
    residues = sorted({x * x % p for x in range(1, p)})
    nonresidues = sorted(set(range(1, p)) - set(residues))
    order = residues + nonresidues
    fig = plt.figure(figsize=(10.6, 6.0), dpi=100, facecolor="white")
    grid = fig.add_gridspec(1, 2, width_ratios=(1.35, 1),
                           left=0.035, right=0.97, top=0.80, bottom=0.13, wspace=0.26)
    ax = fig.add_subplot(grid[0, 0])
    ax.set(xlim=(-1.1, 6.1), ylim=(-0.2, 7.1), aspect="equal")
    ax.axis("off")
    fig.suptitle("Multiplication modulo 7 becomes sign multiplication",
                 fontsize=20, weight="bold", y=0.975)
    fig.text(0.5, 0.899, "Q = {1, 2, 4}: sign +1      N = {3, 5, 6}: sign −1",
             ha="center", fontsize=14)
    for i, a in enumerate(order):
        y = 5 - i
        ax.text(-0.38, y + 0.5, str(a), ha="center", va="center", fontsize=14, weight="bold")
        ax.text(i + 0.5, 6.35, str(a), ha="center", va="center", fontsize=14, weight="bold")
        for j, b in enumerate(order):
            value = a * b % p
            square = value in residues
            color = "#deefe2" if square else "#f9e4d2"
            ax.add_patch(Rectangle((j, y), 1, 1, facecolor=color,
                                   edgecolor="white", linewidth=1.2))
            ax.text(j + 0.5, y + 0.66, str(value), ha="center", va="center", fontsize=15)
            ax.text(j + 0.5, y + 0.27, "+1" if square else "−1",
                    ha="center", va="center", fontsize=11, color="#344956")
    for position in (0, 3, 6):
        ax.plot([position, position], [0, 6], color="#485965", lw=1.8)
        ax.plot([0, 6], [position, position], color="#485965", lw=1.8)
    ax.text(2.95, 6.88, "a × b: product above, sign below", ha="center", fontsize=12)
    side = fig.add_subplot(grid[0, 1])
    side.set(xlim=(-0.7, 2.25), ylim=(-1.45, 2.9), aspect="equal")
    side.axis("off")
    side.text(1, 2.75, "Four blocks, two signs", ha="center", fontsize=15, weight="bold")
    for i, row in enumerate(("Q (+1)", "N (−1)")):
        side.text(-0.12, 1.5 - i, row, ha="right", va="center", fontsize=12)
        side.text(i + 0.5, 2.18, row, ha="center", va="center", fontsize=12)
        for j in range(2):
            square = i == j
            side.add_patch(Rectangle((j, 1 - i), 1, 1,
                                     facecolor="#deefe2" if square else "#f9e4d2",
                                     edgecolor="#485965", linewidth=1.2))
            side.text(j + 0.5, 1.5 - i, "Q\n+1" if square else "N\n−1",
                      ha="center", va="center", fontsize=15, linespacing=1.5)
    side.text(0.85, -0.43, "3 × 5 ≡ 1:  (−1)(−1) = +1", ha="center", fontsize=12)
    side.text(0.85, -0.88, "2 × 3 ≡ 6:  (+1)(−1) = −1", ha="center", fontsize=12)
    fig.text(0.5, 0.044, "Zero is separate: multiplying by zero gives product 0 and Legendre symbol 0.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
