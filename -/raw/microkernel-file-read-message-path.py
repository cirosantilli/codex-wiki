"""Draw an original cached file-read protocol. Python 3.14; matplotlib 3.10.7.

Run from _media; the PNG is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.3), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.3))
    ax.axis("off")

    def box(x, y, w, h, color, title, detail):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                                   facecolor=color, edgecolor="#374151", linewidth=1.4))
        ax.text(x + w / 2, y + h - .27, title, ha="center", va="top",
                fontsize=13, weight="bold")
        ax.text(x + w / 2, y + h / 2 - .12, detail, ha="center", va="center",
                fontsize=11, linespacing=1.6)

    def arrow(a, b, color):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=16,
                                    linewidth=2, color=color))

    ax.text(5, 6.02, "A cached file read crosses two protection domains", ha="center",
            fontsize=16, weight="bold")
    box(.45, 3.65, 3.55, 1.85, "#edf4ff", "Client: address space A",
        "Private memory + local buffer\nSend authority to endpoint E\nREAD(7, 9, 0, 4)")
    box(6, 3.65, 3.55, 1.85, "#edfaf0", "File service: address space B",
        "Private memory + cached file\nHandle 9 contains LIME + newline\nCheck handle rights and bounds")
    ax.plot([.3, 9.7], [3.3, 3.3], "--", color="#6b7280", linewidth=1.3)
    ax.text(5, 3.4, "Privilege boundary",
            fontsize=10, ha="center", bbox={"facecolor": "white", "edgecolor": "none"})
    box(3.3, 1.15, 3.4, 1.7, "#fff6df", "Microkernel",
        "Endpoint E + reply authority\nCheck authority; transfer payload\nBlock / resume threads")
    arrow((1.1, 3.65), (3.5, 2.4), "#1759a8")
    ax.text(.62, 2.67, "1  Call E\nrequest 7", color="#1759a8", fontsize=11)
    arrow((6.5, 2.4), (8.9, 3.65), "#1759a8")
    ax.text(7.65, 2.67, "2  Deliver\nrequest 7", color="#1759a8", fontsize=11)
    arrow((7.05, 3.65), (5.9, 2.85), "#a54913")
    ax.text(6.5, 3.02, "3  Reply", color="#a54913", fontsize=10)
    arrow((4.1, 2.85), (2.95, 3.65), "#a54913")
    ax.text(2.06, 3.02, "4  Resume", color="#a54913", fontsize=10)
    ax.text(5, .65, "Reply: OK(7, 4, LIME)   |   Request and reply are two logical messages",
            ha="center", fontsize=11, weight="bold")
    ax.text(5, .25, "A pointer in A does not name B's memory. This example uses no shared data page or device I/O.",
            ha="center", fontsize=10)
    fig.subplots_adjust(left=.01, right=.99, bottom=.02, top=.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
