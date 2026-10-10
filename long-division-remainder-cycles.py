"""Draw exact long-division states; Python 3.14, matplotlib 3.10.7.

Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def division_states(denominator):
    states, digits, seen = [], [], {}
    remainder = 1
    while remainder not in seen and remainder != 0:
        seen[remainder] = len(states)
        states.append(remainder)
        digit, remainder = divmod(10 * remainder, denominator)
        digits.append(digit)
    return states, digits, seen.get(remainder), remainder


def row(ax, denominator, y):
    states, digits, start, repeated = division_states(denominator)
    all_states = states + [repeated]
    xs = [0.8 + 1.15 * j for j in range(len(all_states))]
    for j, (x, remainder) in enumerate(zip(xs, all_states)):
        prefix = j < start
        color = "#95502b" if prefix else "#176b91"
        ax.add_patch(Circle((x, y), 0.30, fc="white", ec=color, lw=2))
        ax.text(x, y, str(remainder), ha="center", va="center", fontsize=16, color=color)
        if j < len(digits):
            ax.add_patch(FancyArrowPatch((x + 0.32, y), (xs[j + 1] - 0.32, y),
                                        arrowstyle="-|>", mutation_scale=15, lw=1.7, color=color))
            ax.text(x + 0.575, y + 0.43, str(digits[j]), ha="center", fontsize=15, color=color)
    ax.plot([xs[-1], xs[-1], xs[start]], [y - 0.32, y - 0.68, y - 0.68],
            lw=1.5, color="#176b91")
    ax.add_patch(FancyArrowPatch((xs[start], y - 0.68), (xs[start], y - 0.32),
                                arrowstyle="-|>", mutation_scale=15, lw=1.5, color="#176b91"))
    ax.text((xs[-1] + xs[start]) / 2, y - 1.15,
            f"Same remainder: repeat the {len(states) - start} blue digit steps",
            ha="center", fontsize=12, color="#176b91")
    return states, digits


def main():
    fig, ax = plt.subplots(figsize=(10.0, 6.0), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-0.2, 10.5), ylim=(-1.65, 5.8))
    ax.axis("off")
    ax.text(5.2, 5.48, "Long division remembers the remainder", ha="center", fontsize=20)
    ax.text(5.2, 4.95, r"$10r_{j-1}=q\,d_j+r_j$: circles = remainders, arrow labels = digits",
            ha="center", fontsize=14)
    ax.text(0.35, 4.15, r"$1/7=0.\overline{142857}$", fontsize=18)
    row(ax, 7, 3.2)
    ax.text(0.35, 1.56, r"$1/28=0.03\overline{571428}$", fontsize=18)
    row(ax, 28, 0.58)
    ax.text(5.2, -1.3, "Orange: two-digit prefix 03.  Blue: the repeating block 571428.",
            ha="center", fontsize=13)
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.035, top=0.98)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
