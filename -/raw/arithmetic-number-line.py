"""Addition shifts; multiplication scales about zero. PNG goes to cwd."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def number_line(ax, y, label):
    ax.annotate("", xy=(6.3, y), xytext=(-5.3, y),
                arrowprops={"arrowstyle": "<->", "lw": 1, "color": "#74818c"})
    for x in range(-5, 7):
        ax.plot([x, x], [y - 0.05, y + 0.05], color="#74818c", lw=1)
        ax.text(x, y - 0.19, str(x), ha="center", fontsize=9, color="#536371")
    ax.text(-5.2, y + 0.65, label, fontsize=13, color="#273746")


def shift(ax, start, finish, y, label, color, level=0.28):
    ax.annotate("", xy=(finish, y + level), xytext=(start, y + level),
                arrowprops={"arrowstyle": "-|>", "lw": 2.5, "color": color,
                            "mutation_scale": 17})
    ax.text((start + finish) / 2, y + level + 0.13, label, ha="center", fontsize=12, color=color)
    ax.scatter([start, finish], [y, y], s=30, color=color, zorder=3)


def main():
    assert 2 + 3 == 5 and 2 - 3 == -1
    scale = -1.5
    assert scale * 2 == -3 and scale * -2 == 3
    fig, ax = plt.subplots(figsize=(10.8, 5.8), dpi=120)
    blue, orange = "#176997", "#b55d20"
    number_line(ax, 3.3, "Addition: start at 2, then add 3")
    shift(ax, 0, 2, 3.3, "+2", blue)
    shift(ax, 2, 5, 3.3, "+3", orange)
    ax.text(5.55, 3.55, "2 + 3 = 5", ha="center", fontsize=12)
    number_line(ax, 1.85, "Subtraction: start at 2, then add −3")
    shift(ax, 0, 2, 1.85, "+2", blue, level=0.22)
    shift(ax, 2, -1, 1.85, "−3", orange, level=0.5)
    ax.text(5.55, 2.1, "2 − 3 = −1", ha="center", fontsize=12)
    number_line(ax, 0.15, "Multiplication: input x maps to −3x/2")
    number_line(ax, -1.0, "")
    ax.text(-5.2, 0.40, "input", color="#536371", fontsize=10)
    ax.text(-5.2, -0.75, "output", color="#536371", fontsize=10)
    for x, color in [(-2, blue), (2, orange)]:
        output = scale * x
        ax.scatter(x, 0.15, s=45, color=color, zorder=4)
        ax.scatter(output, -1, s=45, color=color, zorder=4)
        ax.annotate("", xy=(output, -0.95), xytext=(x, 0.1),
                    arrowprops={"arrowstyle": "-|>", "lw": 2, "color": color,
                                "mutation_scale": 17})
        ax.text(x, 0.40, str(x), ha="center", color=color, fontsize=13)
        ax.text(output, -1.40, f"{output:g}", ha="center", color=color, fontsize=13)
    ax.text(5.5, -0.45, "2 → −3\n−2 → 3", ha="center", fontsize=12)
    ax.set_xlim(-5.8, 6.8)
    ax.set_ylim(-1.7, 4.6)
    ax.axis("off")
    fig.suptitle("A shift adds the same amount; a scale multiplies every input",
                 fontsize=15, y=0.97)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.9, bottom=0.04)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
