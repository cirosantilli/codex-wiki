#!/usr/bin/env python3
"""Draw the free extension for the nested partial-operation tower.

Output paper-23-free-extension.png to cwd.
Tested with Python3.14.4 and Matplotlib3.10.7; see root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 3.2), dpi=100, facecolor="white")
    ax.set(xlim=(-0.65, 8.7), ylim=(-1.3, 1.4))
    ax.axis("off")
    fig.suptitle("Free extension of the next partial operation", fontsize=16, y=0.96)
    for x, label in [(0, r"$a$"), (2, r"$(a,0)$"), (4, r"$(a,1)$"), (6, r"$(a,2)$")]:
        ax.add_patch(Circle((x, 0), 0.28, facecolor="white" if x == 0 else "#eaf3fb",
                            edgecolor="#454b54" if x == 0 else "#1262a3", linewidth=1.7))
        ax.text(x, 0, label, ha="center", va="center", fontsize=13)
    ax.text(0, 0.72, r"Eligible old point: $\alpha_m(a)=a$", ha="left", fontsize=12)
    ax.text(8, 0, r"$\cdots$", ha="center", va="center", fontsize=22)
    for start, end, label, color in [
        (0, 2, r"$\alpha_{m+1}$", "#a34622"),
        (2, 4, r"$\alpha_1$", "#1262a3"),
        (4, 6, r"$\alpha_1$", "#1262a3"),
        (6, 8, r"$\alpha_1$", "#1262a3"),
    ]:
        ax.add_patch(FancyArrowPatch((start + 0.31, 0), (end - 0.31, 0),
                                    arrowstyle="-|>", mutation_scale=17,
                                    color=color, linewidth=1.8))
        ax.text((start + end) / 2, 0.28, label, ha="center", fontsize=14, color=color)
    ax.text(1.85, -0.58, r"New points: only $\alpha_1$ is defined; it shifts the chain.",
            fontsize=12, color="#1262a3")
    ax.text(-0.3, -1.08, r"For $m\geq1$, the new top operation has no fixed points.",
            fontsize=12)
    fig.subplots_adjust(left=0.03, right=0.99, bottom=0.08, top=0.83)
    fig.savefig(Path.cwd() / "paper-23-free-extension.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
